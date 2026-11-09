#!/usr/bin/env python3
"""Build a standalone HTML catalog review page from catalog/*.json.

Usage: python tools/build_catalog_page.py [--out PATH]
Default output: catalog-review.html at the repository root (images resolve to media/).
"""
import argparse
import hashlib
import html
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = ROOT / "catalog"

PART_LABELS = {
    "upper arms": "上肢（手臂）", "upper legs": "下肢（大腿）", "back": "背部", "waist": "腰腹核心",
    "chest": "胸部", "shoulders": "肩部", "lower legs": "小腿", "lower arms": "前臂", "cardio": "有氧/全身",
    "neck": "颈部（并入背部）",
}
EQ_LABELS = {
    "body weight": "自重", "dumbbell": "哑铃", "cable": "绳索", "barbell": "杠铃", "ez barbell": "曲杠",
    "olympic barbell": "奥杆", "trap bar": "六角杠", "kettlebell": "壶铃", "landmine": "地雷杆",
    "leverage machine": "固定器械", "smith machine": "史密斯架", "assisted": "辅助器械",
    "sled machine": "雪橇器械", "stability ball": "瑜伽球", "bosu ball": "波速球", "medicine ball": "药球",
    "band": "弹力带", "resistance band": "阻力带", "rope": "绳索/跳绳", "roller": "泡沫轴/滚轮",
    "wheel roller": "健腹轮", "hammer": "大锤", "tire": "轮胎", "weighted": "负重（未细分）",
    "upper body ergometer": "上肢功率车", "stationary bike": "健身车", "skierg machine": "滑雪测功仪",
    "elliptical machine": "椭圆机", "stepmill machine": "台阶机",
}
MEASURE_LABELS = {"reps": "计数", "duration": "计时", "unknown": "待维护"}
KIND_LABELS = {"repetition": "", "hold": "保持", "continuous": "持续", "duration": "", "blocked": "已阻塞"}
TRACK_LABELS = {
    ("external", "machine"): "器械负重（按器械示值）", ("external", "single"): "单侧负重",
    ("external", "total"): "双侧合计负重", ("bodyweight", "total"): "自重/徒手",
    ("assistance", "total"): "辅助重量（越少越难）",
}

AERO_WORD = re.compile(
    r"(跑步机|健身车|单车|椭圆机|台阶机|跳绳|游泳|划船机|步行机|登山机|treadmill|elliptical|rower|"
    r"jump rope|ski\s*erg|skiing|boxing|kickboxing|跳箱|登山跑|波比)", re.I)
MIX_WORD = re.compile(
    r"(战绳|山羊|开合跳|高抬腿|冲刺|burpee|skater|bear\s*crawl|battle\s*rope|sprint|剪刀跳|星形跳|轮跑步|"
    r"深蹲跳|踏步|跳跃|lunge\s*jump)", re.I)
SIDE_WORD = re.compile(r"(单边|单侧|单臂|交替|换边|换臂|一侧|每侧|左右)")


def load_catalog():
    items = []
    for fname, prefix in [("exercises_zh.json", "exercises-dataset:"), ("exercises_extra.json", "alivo:"),
                          ("exercises_reviewed.json", "free-exercise-db:")]:
        for row in json.loads((CAT / fname).read_text(encoding="utf-8")):
            row = dict(row)
            row["id"] = prefix + row["id"]
            row["source"] = fname
            items.append(row)
    return items


def load_measures():
    data = json.loads((CAT / "exercise_measures.json").read_text(encoding="utf-8"))
    return {e["catalogId"]: e for e in data["entries"]}


def load_metadata():
    data = json.loads((CAT / "exercise_metadata.json").read_text(encoding="utf-8"))
    return {o["catalogId"]: o for o in data.get("overrides", [])}


def load_media():
    media = {}
    for row in json.loads((CAT / "exercise_metadata.json").read_text(encoding="utf-8")).get("media", []):
        media[row["catalogId"]] = row
    return media


def classify_energy(item, meas):
    """Heuristic three-way split; always flagged as inferred so the reviewer confirms."""
    if meas["measure"] == "duration" and meas["kind"] == "continuous":
        return "aerobic", "规则：计量为持续型计时"
    text = " ".join([item.get("nz", ""), item.get("name", ""), " ".join(item.get("st", [])),
                     item.get("eq", ""), item.get("cat", "")])
    if AERO_WORD.search(text):
        return "aerobic", "关键词：有氧器械/持续动作"
    if MIX_WORD.search(text):
        return "mixed", "关键词：高强度间歇/复合动作"
    if meas["measure"] == "duration" and meas["kind"] in ("duration",):
        return "mixed", "规则：自编计时动作"
    return "strength", "默认：力量/柔韧性（待复核）"


def timing_suggestion(meas, energy):
    """Mirror of proposal A: only a suggestion, never enforced."""
    if meas["measure"] != "duration":
        return None
    evidence = meas.get("evidence", "")
    if re.search(r"尽可能|只要能|所需的时间|所需时间", evidence):
        return {"mode": "free", "seconds": None, "basis": evidence[:60]}
    m = re.search(r"(\d{1,3})\s*[-–~至]\s*(\d{1,3})\s*秒|(\d{1,3})\s*秒", evidence)
    if m:
        lo = int(m.group(1) or m.group(3))
        hi = int(m.group(2) or m.group(3))
        return {"mode": "fixed", "seconds": lo, "basis": evidence[:60], "range": [lo, hi]}
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "catalog-review.html"))
    args = ap.parse_args()

    items, measures, meta, media = load_catalog(), load_measures(), load_metadata(), load_media()
    records = []
    for it in items:
        cid = it["id"]
        meas = measures.get(cid, {"measure": "unknown", "kind": "blocked", "evidence": ""})
        ov = meta.get(cid, {})
        energy, energy_basis = classify_energy(it, meas)
        track = ov.get("trackingSuggestion") or {}
        mrow = media.get(cid)
        records.append({
            "id": cid, "name": it.get("nz") or it.get("name", ""), "en": it.get("name", ""),
            "part": it.get("part") or "", "cat": it.get("cat") or "", "eq": it.get("eq") or "",
            "tg": it.get("tg") or "", "sm": it.get("sm") or [], "st": it.get("st") or [],
            "measure": meas["measure"], "kind": meas["kind"], "evidence": meas.get("evidence", ""),
            "measureVersion": meas.get("version"),
            "meta": {"reviewStatus": ov.get("reviewStatus", ""), "variant": ov.get("variant", ""),
                     "defaultMeasure": ov.get("defaultMeasure", ""),
                     "allowedMeasures": ov.get("allowedMeasures", []),
                     "track": {k: track.get(k) for k in ("loadType", "weightBasis", "repsBasis", "defaultSide") if k in track},
                     "recordingNotes": ov.get("recordingNotes", []), "standardName": ov.get("standardName", "")},
            "energy": energy, "energyBasis": energy_basis,
            "timing": timing_suggestion(meas, energy),
            "media": {"file": mrow["localPath"].split("/", 1)[1] if mrow else "",
                      "license": mrow["license"] if mrow else "", "sha256": mrow["sha256"] if mrow else ""},
            "source": it["source"],
        })
    payload = {
        "generatedAt": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "total": len(records),
        "stats": dict(Counter(r["energy"] for r in records)),
        "records": records,
    }
    labels = json.dumps(label_maps(), ensure_ascii=False)
    esc = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<" + chr(92) + "/")
    page = TEMPLATE.replace("__DATA__", esc(payload)).replace("__LABELS__", esc(label_maps()))
    Path(args.out).write_text(page, encoding="utf-8")
    print(f"wrote {args.out}: {len(records)} records, energy={payload['stats']}, bytes={len(page.encode('utf-8'))}")


TEMPLATE = r"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ALIVO 动作库审查</title>
<style>
:root{--bg:#f6f6f4;--card:#fff;--line:#e3e1dc;--ink:#1c1c1a;--mut:#7a7873;--acc:#2f5d50;--acc2:#b3541e;--warn:#9c2b2b}
*{box-sizing:border-box}body{margin:0;font:14px/1.55 -apple-system,"Segoe UI","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--ink)}
header{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--line);padding:10px 16px}
h1{font-size:16px;margin:0 0 8px}.bar{display:flex;flex-wrap:wrap;gap:6px 12px;align-items:center}
select,input[type=search],button{font:inherit;padding:5px 8px;border:1px solid var(--line);border-radius:6px;background:#fff}
button{cursor:pointer}.chips{display:flex;gap:6px;flex-wrap:wrap}.chip{padding:3px 10px;border-radius:999px;border:1px solid var(--line);background:#fff;cursor:pointer;font-size:12px}
.chip.on{background:var(--acc);color:#fff;border-color:var(--acc)}
.main{display:grid;grid-template-columns:300px 1fr;gap:14px;padding:14px 16px;max-width:1500px;margin:0 auto}
@media(max-width:900px){.main{grid-template-columns:1fr}}
.list{max-height:calc(100vh - 170px);overflow:auto;border:1px solid var(--line);border-radius:8px;background:var(--card)}
.row{display:grid;grid-template-columns:52px 1fr auto;gap:8px;padding:6px 8px;border-bottom:1px solid var(--line);cursor:pointer;align-items:center}
.row:hover{background:#f1f3f1}.row.sel{background:#e6efe9}.row img{width:52px;height:52px;object-fit:cover;border-radius:4px;background:#ddd;transition:transform .25s ease}.row:hover img{transform:scale(1.15)}
.detail img{transition:transform .4s ease;transform-origin:50% 40%}
.detail img.zoomed{transform:scale(1.9);cursor:zoom-out}
.detail .imgwrap{position:relative;overflow:hidden;border-radius:6px;background:#ddd;width:260px}
.detail .imgwrap .hint{position:absolute;left:8px;bottom:8px;background:rgba(0,0,0,.55);color:#fff;font-size:11px;padding:2px 7px;border-radius:4px;pointer-events:none}
.detail .imgctrl{margin-top:6px;display:flex;gap:6px}
.detail .imgctrl button{font-size:12px;padding:3px 10px}
.detail .imgctrl button.on{background:var(--acc);color:#fff;border-color:var(--acc)}
@keyframes kenburns{0%{transform:scale(1) translate(0,0)}50%{transform:scale(1.18) translate(-2%,2%)}100%{transform:scale(1) translate(0,0)}}
.detail img.kb{animation:kenburns 9s ease-in-out infinite}
.row .n{font-weight:600}.row .s{font-size:12px;color:var(--mut)}.badge{font-size:11px;padding:1px 6px;border-radius:4px;background:#eee;white-space:nowrap}
.badge.aerobic{background:#dcefe6;color:#1d5c44}.badge.mixed{background:#f6e3c8;color:#8a4a10}.badge.strength{background:#eee;color:#555}
.badge.reviewed{background:#dcefe6;color:#1d5c44}.badge.pending{background:#f6e3c8;color:#8a4a10}.badge.low{background:#f3d7d7;color:var(--warn)}
.detail{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:14px 16px}
.detail h2{margin:0 0 2px;font-size:18px}.detail .en{color:var(--mut);margin-bottom:8px}
.grid{display:grid;grid-template-columns:260px 1fr;gap:16px}@media(max-width:700px){.grid{grid-template-columns:1fr}}
.detail img{width:260px;height:260px;object-fit:cover;border-radius:6px;background:#ddd}
.kv{display:grid;grid-template-columns:90px 1fr;gap:4px 10px;font-size:13px}.kv b{color:var(--mut);font-weight:500}
ol.steps{margin:6px 0;padding-left:20px}ol.steps li{margin:2px 0}
table{border-collapse:collapse;width:100%;font-size:13px}td,th{border-bottom:1px solid var(--line);padding:4px 6px;text-align:left;vertical-align:top}
.note{color:var(--mut);font-size:12px}.warnbox{background:#fbeeee;border:1px solid #e5bcbc;color:var(--warn);padding:8px 10px;border-radius:6px;margin:8px 0}
.export{position:fixed;right:16px;bottom:16px;display:flex;gap:8px}
.export button{background:var(--acc);color:#fff;border:none;padding:8px 12px;border-radius:8px}
.count{color:var(--mut);font-size:12px}
</style>
</head>
<body>
<header>
 <h1>ALIVO 动作库审查 <span class="count" id="count"></span></h1>
 <div class="bar">
  <input type="search" id="q" placeholder="搜索名称 / 英文 / 目标肌群 / 别名" style="width:220px">
  <label>部位 <select id="part"><option value="">全部</option></select></label>
  <label>器械 <select id="eq"><option value="">全部</option></select></label>
  <label>类别 <select id="energy"><option value="">全部</option>
    <option value="aerobic">有氧（持续）</option><option value="mixed">混合 / 高强度间歇</option><option value="strength">力量 / 柔韧（默认，待复核）</option></select></label>
  <label>计量 <select id="measure"><option value="">全部</option><option value="reps">计数</option><option value="duration">计时</option><option value="unknown">待维护</option></select></label>
  <label>计时建议 <select id="timing"><option value="">全部</option><option value="free">正计时</option><option value="fixed">倒计时</option><option value="none">无建议</option></select></label>
  <label>配图 <select id="media"><option value="">全部</option><option value="yes">有 ALIVO 插图</option><option value="no">无图</option></select></label>
  <label>审核 <select id="review"><option value="">全部</option><option value="reviewed">已审核</option><option value="pending">未审核</option></select></label>
  <label>置信 <select id="conf"><option value="">全部</option><option value="high">高</option><option value="medium">中</option><option value="low">低</option></select></label>
  <button id="reset">重置</button>
 </div>
 <div class="chips" id="chips"></div>
 <div class="note">类别为规则推断（见每行依据），“力量/柔韧”为默认值请重点复核；本地修改存于浏览器 localStorage，导出 JSON 后可合并回 exercise_measures / metadata。</div>
</header>
<div class="main">
 <div class="list" id="list"></div>
 <div class="detail" id="detail"><p class="note">← 选择左侧动作查看详情</p></div>
</div>
<div class="export"><button id="expJson">导出我的复核修改</button><button id="impJson">导入复核修改</button><input type="file" id="impFile" accept=".json" hidden></div>
<script>
const DATA=__DATA__;
const ENERGY={aerobic:'有氧（持续）',mixed:'混合 / 高强度间歇',strength:'力量 / 柔韧（默认）'};
const PART={};DATA.records.forEach(r=>{PART[r.part||'(未标注)']=1});
const EQ={};DATA.records.forEach(r=>{EQ[r.eq||'(未标注)']=1});
const LBL=__LABELS__;

const st={q:'',part:'',eq:'',energy:'',measure:'',timing:'',media:'',review:'',conf:'',energyOv:{}};
const store=JSON.parse(localStorage.getItem('alivoReview')||'{}');
if(store.overrides)Object.assign(st.energyOv,store.overrides);
let cur=null,rows=[];
function energyOf(r){return st.energyOv[r.id]||r.energy}
function confOf(r){const e=energyOf(r);return r.energy==='strength'? 'low' : (r.energy===e?'high':'medium')}
function timingOf(r){return r.timing?(r.timing.mode==='free'?'free':'fixed'):'none'}
function save(){localStorage.setItem('alivoReview',JSON.stringify({overrides:st.energyOv}))}
function filtered(){
 const q=st.q.trim().toLowerCase();
 return DATA.records.filter(r=>{
  if(st.part&&r.part!==st.part)return false;if(st.eq&&r.eq!==st.eq)return false;
  if(st.energy&&energyOf(r)!==st.energy)return false;if(st.measure&&r.measure!==st.measure)return false;
  if(st.timing&&timingOf(r)!==st.timing)return false;
  if(st.media&&(st.media==='yes')!==(!!r.media.file))return false;
  if(st.review){const s=r.meta.reviewStatus==='reviewed'?'reviewed':'pending';if(s!==st.review)return false}
  if(st.conf&&confOf(r)!==st.conf)return false;
  if(q){const hay=(r.id+' '+r.name+' '+r.en+' '+(r.meta.standardName||'')+' '+r.tg+' '+r.sm.join(' ')+' '+(r.meta.variant||'')).toLowerCase();if(!hay.includes(q))return false}
  return true}).sort((a,b)=>a.name.localeCompare(b.name,'zh'));
}
function chipSet(){const c={aerobic:0,mixed:0,strength:0};DATA.records.forEach(r=>c[energyOf(r)]++);return c}
function renderChips(){const c=chipSet();const el=document.getElementById('chips');el.innerHTML='';
 [['', '全部 '+DATA.total],['aerobic','有氧 '+c.aerobic],['mixed','混合 '+c.mixed],['strength','力量(默认) '+c.strength]].forEach(([v,t])=>{
  const b=document.createElement('button');b.className='chip'+(st.energy===v?' on':'');b.textContent=t;
  b.onclick=()=>{st.energy=v;document.getElementById('energy').value=v;render()};el.appendChild(b)})}
function render(){
 rows=filtered();document.getElementById('count').textContent='显示 '+rows.length+' / '+DATA.total;
 const l=document.getElementById('list');l.innerHTML='';
 for(const r of rows.slice(0,400)){const d=document.createElement('div');d.className='row'+(cur===r.id?' sel':'');
  d.innerHTML='<img loading="lazy" src="'+(r.media.file?'media/'+encodeURIComponent(r.media.file):'')+'" onerror="this.style.visibility=\'hidden\'">'+
   '<div><div class="n">'+esc(r.name)+'</div><div class="s">'+esc(r.eqLabel||'')+' · '+esc(r.partLabel||'')+' · '+esc(r.measure==='reps'?'计数':r.measure==='duration'?'计时':'待维护')+'</div></div>'+
   '<div style="text-align:right"><span class="badge '+energyOf(r)+'">'+ENERGY[energyOf(r)].split('（')[0]+'</span><br><span class="badge '+(r.meta.reviewStatus==='reviewed'?'reviewed':'pending')+'">'+(r.meta.reviewStatus==='reviewed'?'已审':'未审')+'</span> '+(r.media.file?'<span class="badge">图</span>':'')+'</div>';
  d.onclick=()=>{cur=r.id;renderList();renderDetail(r)};l.appendChild(d)}
 if(rows.length>400){const p=document.createElement('div');p.className='note';p.style.padding='8px';p.textContent='仅显示前 400 条，请用筛选缩小范围';l.appendChild(p)}
 renderChips();
}
function renderList(){/* re-render only selection highlight cheaply */document.querySelectorAll('.row').forEach((el,i)=>{if(rows[i])el.classList.toggle('sel',rows[i].id===cur)})}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function renderDetail(r){
 const e=energyOf(r),conf=confOf(r),t=r.timing;
 const track=r.meta.track||{},tk=Object.entries(track).filter(([k,v])=>v).map(([k,v])=>({'loadType':'负重类型','weightBasis':'重量口径','repsBasis':'次数口径','defaultSide':'默认侧别'}[k]||k)+'：'+({'external':'外部负重','bodyweight':'自重','assistance':'辅助','machine':'器械示值','single':'单侧','total':'合计','per-side':'单侧','bilateral':'双侧','alternating':'交替','unknown':'未知'}[v]||v)).join('；');
 document.getElementById('detail').innerHTML=
 '<h2>'+esc(r.name)+' <span class="badge '+e+'">'+ENERGY[e]+'</span> <span class="badge '+(r.meta.reviewStatus==='reviewed'?'reviewed':'pending')+'">'+(r.meta.reviewStatus==='reviewed'?'已审核':'未审核')+'</span> <span class="badge '+conf+'">类别置信 '+conf+'</span></h2>'+
 '<div class="en">'+esc(r.en)+' · <code>'+esc(r.id)+'</code> · 来源 '+esc(r.source)+'</div>'+
 (r.energy===e?'':'<div class="warnbox">规则原判：'+ENERGY[r.energy]+'（'+esc(r.energyBasis)+'）。已被你改为：'+ENERGY[e]+'。</div>')+
 '<div class="grid"><div>'+(r.media.file?'<div class="imgwrap"><img id="dImg" src="media/'+encodeURIComponent(r.media.file)+'"><div class="hint">可放大检视</div></div><div class="imgctrl"><button id="btnKb">动态检视</button><button id="btnZoom">放大细节</button></div>':'<div class="note" style="padding:40px;text-align:center">无 ALIVO 插图</div>')+'</div><div>'+
 '<div class="kv"><b>类别依据</b><span>'+esc(r.energyBasis)+(r.energy!==e?' → 人工改为 '+ENERGY[e]:'')+'</span>'+
 '<b>部位</b><span>'+esc(r.partLabel||r.part)+'</span><b>器械</b><span>'+esc(r.eqLabel||r.eq)+'</span>'+
 '<b>目标肌群</b><span>'+esc(r.tg)+(r.sm.length?'；协同：'+esc(r.sm.join('、')):'')+'</span>'+
 '<b>计量</b><span>'+({reps:'计数',duration:'计时',unknown:'待维护'}[r.measure]||r.measure)+' / '+({hold:'保持',continuous:'持续',repetition:'重复',duration:'',blocked:'已阻塞'}[r.kind]||r.kind)+'（依据：'+esc(r.evidence||'—')+'）</span>'+
 '<b>计时建议(提案A)</b><span>'+(t?(t.mode==='free'?'正计时（尽可能长）':('倒计时 '+t.seconds+' 秒'+(t.range?'（原文 '+t.range[0]+'–'+t.range[1]+' 秒）':'')))+' <span class="note">依据：'+esc(t.basis)+'</span>':'无（计数动作或无明确依据）')+'</span>'+
 '<b>负重/次数口径</b><span>'+esc(tk||'未维护')+'</span>'+
 (r.meta.recordingNotes.length?'<b>记录说明</b><span>'+r.meta.recordingNotes.map(esc).join('<br>')+'</span>':'')+
 (r.meta.standardName?'<b>标准名</b><span>'+esc(r.meta.standardName)+'</span>':'')+'</div>'+
 '<div style="margin-top:10px"><b>动作类别修正</b> <select id="eOv"><option value="">（跟随规则：'+ENERGY[r.energy]+'）</option>'+
 ['aerobic','mixed','strength'].map(v=>'<option value="'+v+'"'+(e===v&&r.energy!==e?' selected':'')+'>'+ENERGY[v]+'</option>').join('')+'</select> <button id="eClr">清除修正</button></div>'+
 '<ol class="steps">'+r.st.map(s=>'<li>'+esc(s)+'</li>').join('')+'</ol>'+
 (r.media.file?'<div class="note">图片：'+esc(r.media.file)+' · '+esc(r.media.license)+' · sha256 '+esc(r.media.sha256.slice(0,12))+'…</div>':'')+
 '</div></div>';
 const di=document.getElementById('dImg');
 if(di){
  const kb=document.getElementById('btnKb'),zm=document.getElementById('btnZoom');
  kb.onclick=()=>{di.classList.toggle('kb');kb.classList.toggle('on');kb.textContent=di.classList.contains('kb')?'停止检视':'动态检视'};
  zm.onclick=()=>{di.classList.toggle('zoomed');zm.classList.toggle('on');zm.textContent=di.classList.contains('zoomed')?'还原':'放大细节'};
  di.onclick=()=>{if(di.classList.contains('zoomed')){di.classList.remove('zoomed');zm.classList.remove('on');zm.textContent='放大细节'}};
  di.onmousemove=e=>{if(di.classList.contains('zoomed')){const b=di.getBoundingClientRect();di.style.transformOrigin=((e.clientX-b.left)/b.width*100)+'% '+((e.clientY-b.top)/b.height*100)+'%'}};
 }
 document.getElementById('eOv').onchange=ev=>{const v=ev.target.value;if(v)st.energyOv[r.id]=v;else delete st.energyOv[r.id];save();renderDetail(r);render()};
 document.getElementById('eClr').onclick=()=>{delete st.energyOv[r.id];save();renderDetail(r);render()};
}
['q','part','eq','energy','measure','timing','media','review','conf'].forEach(id=>{document.getElementById(id).oninput=e=>{st[id]=e.target.value;render()}});
document.getElementById('reset').onclick=()=>{Object.keys(st).forEach(k=>{if(typeof st[k]==='string')st[k]=''});localStorage.removeItem('alivoReview');document.querySelectorAll('header select,input').forEach(el=>{if(el.tagName==='SELECT')el.selectedIndex=0;else el.value=''});render()};
function out(){return{note:'ALIVO 动作库类别复核结果；energy 为 aerobic/mixed/strength，合并到 exercise_measures.json 或 exercise_metadata.json 前需维护者确认',overrides:Object.entries(st.energyOv).map(([id,energy])=>({catalogId:id,energy}))}}
document.getElementById('expJson').onclick=()=>{const b=new Blob([JSON.stringify(out(),null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='alivo-catalog-review-'+new Date().toISOString().slice(0,10)+'.json';a.click()};
document.getElementById('impJson').onclick=()=>document.getElementById('impFile').click();
document.getElementById('impFile').onchange=async e=>{const f=e.target.files[0];if(!f)return;try{const j=JSON.parse(await f.text());(j.overrides||[]).forEach(o=>{if(o.catalogId&&o.energy)st.energyOv[o.catalogId]=o.energy});save();render();if(cur)renderDetail(DATA.records.find(r=>r.id===cur))}catch(err){alert('导入失败：'+err.message)}};
// enrich rows with labels
{const L=LBL;DATA.records.forEach(r=>{r.partLabel=L.part[r.part]||r.part;r.eqLabel=L.eq[r.eq]||r.eq;r.measureLabel=L.measure[r.measure]})}
// init selects
const partCnt={},eqCnt={};DATA.records.forEach(r=>{partCnt[r.part]=(partCnt[r.part]||0)+1;eqCnt[r.eq]=(eqCnt[r.eq]||0)+1});
document.getElementById('part').innerHTML='<option value="">全部</option>'+Object.entries(partCnt).sort((a,b)=>b[1]-a[1]).map(([k,v])=>'<option value="'+esc(k)+'">'+esc(LBL.part[k]||k)+'（'+v+'）</option>').join('');
document.getElementById('eq').innerHTML='<option value="">全部</option>'+Object.entries(eqCnt).sort((a,b)=>b[1]-a[1]).map(([k,v])=>'<option value="'+esc(k)+'">'+esc(LBL.eq[k]||k)+'（'+v+'）</option>').join('');
render();if(DATA.records.length)renderDetail(DATA.records[0]);
</script>
</body></html>"""


def label_maps():
    part = {k: PART_LABELS.get(k, k) for k in PART_LABELS}
    return {"part": part, "eq": EQ_LABELS, "measure": MEASURE_LABELS}


if __name__ == "__main__":
    main()
