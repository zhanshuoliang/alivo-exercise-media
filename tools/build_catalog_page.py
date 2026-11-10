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

from motion_samples import load_motion_samples

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


def load_open_media():
    """media-open/manifest.json -> catalogId to unbranded CC-BY edition file."""
    p = ROOT / "media-open" / "manifest.json"
    if not p.exists():
        return {}
    data = json.loads(p.read_text(encoding="utf-8"))
    return {item["catalogId"]: item for item in data.get("items", [])}


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

    items, measures, meta, media, open_media = (
        load_catalog(), load_measures(), load_metadata(), load_media(), load_open_media())
    motion = load_motion_samples()
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
                      "license": mrow["license"] if mrow else "", "sha256": mrow["sha256"] if mrow else "",
                      "open": open_media.get(cid, {}).get("file", "")},
            "source": it["source"],
        })
    payload = {
        "generatedAt": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "total": len(records),
        "stats": dict(Counter(r["energy"] for r in records)),
        "records": records,
        "motionSamples": {item["catalogId"]: item["file"] for item in motion},
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
header{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--line);padding:10px 16px 8px}
h1{font-size:15px;margin:0;white-space:nowrap}
svg.ic{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;flex:none}
select,input[type=search],button{font:inherit}
button{cursor:pointer;border:1px solid var(--line);border-radius:6px;background:#fff;padding:5px 8px}
.top{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:8px;min-width:0}
.brand .mark{width:24px;height:24px;border-radius:6px;background:var(--acc);color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.brand .mark svg{width:15px;height:15px}
.count{color:var(--mut);font-size:12px;font-weight:400;white-space:nowrap}
.search{margin-left:auto;position:relative;flex:0 1 240px;min-width:160px}
.search svg{position:absolute;left:9px;top:50%;transform:translateY(-50%);color:var(--mut)}
.search input{width:100%;padding:6px 10px 6px 30px;border:1px solid var(--line);border-radius:999px;background:#fff}
.filters{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-top:10px}
.fsec{font-size:11px;color:var(--mut);font-weight:600;letter-spacing:.06em;margin:0 3px 0 0;white-space:nowrap}
.fsec+.fsec{margin-left:10px;padding-left:10px;border-left:1px solid var(--line)}
.fld{display:inline-flex;align-items:center;gap:5px;border:1px solid var(--line);border-radius:999px;padding:0 8px 0 9px;background:#fff;height:30px}
.fld svg{color:var(--acc)}
.fld span{font-size:11px;color:var(--mut);white-space:nowrap}
.fld select{border:none;background:transparent;font-size:12px;max-width:120px;outline:none;padding:0;color:var(--ink)}
.chips{display:flex;gap:6px;flex-wrap:wrap}.chip{padding:3px 10px;border-radius:999px;border:1px solid var(--line);background:#fff;cursor:pointer;font-size:12px}
.chip.on{background:var(--acc);color:#fff;border-color:var(--acc)}
.chipsrow{display:flex;align-items:center;gap:12px;margin-top:8px;flex-wrap:wrap}
.chipsrow .note{margin:0}
.main{display:grid;grid-template-columns:300px 1fr;gap:14px;padding:14px 16px;max-width:1500px;margin:0 auto}
@media(max-width:900px){.main{grid-template-columns:1fr}}
.list{max-height:calc(100vh - 170px);overflow:auto;border:1px solid var(--line);border-radius:8px;background:var(--card)}
.row{display:grid;grid-template-columns:52px 1fr auto;gap:8px;padding:6px 8px;border-bottom:1px solid var(--line);cursor:pointer;align-items:center}
.row:hover{background:#f1f3f1}.row.sel{background:#e6efe9}.row img{width:52px;height:52px;object-fit:cover;border-radius:4px;background:#ddd;transition:transform .25s ease}.row:hover img{transform:scale(1.15)}
.detail img{transition:transform .4s ease;transform-origin:50% 40%}
.detail img.zoomed{transform:scale(1.9);cursor:zoom-out}
.detail .imgwrap{position:relative;overflow:hidden;border-radius:6px;background:#ddd;width:260px}
.detail .imgwrap .hint{position:absolute;left:8px;bottom:8px;background:rgba(0,0,0,.55);color:#fff;font-size:11px;padding:2px 7px;border-radius:4px;pointer-events:none}
.detail .imgctrl{margin-top:6px;display:flex;flex-wrap:wrap;gap:6px}
.detail .imgctrl button{font-size:12px;padding:3px 10px}
.detail .imgctrl button.on{background:var(--acc);color:#fff;border-color:var(--acc)}
.segwrap{display:flex;margin-top:8px;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.seg{flex:1;padding:7px 4px;border:none;background:#fff;font-size:12px;line-height:1.35;text-align:center;cursor:pointer}
.seg+.seg{border-left:1px solid var(--line)}
.seg small{display:block;color:var(--mut);font-size:10px}
.seg.on{background:var(--acc);color:#fff}.seg.on small{color:#d8e8e0}
.verdict{margin-top:8px;padding:8px 10px;border:1px solid var(--line);border-radius:8px;display:flex;gap:8px;align-items:center;flex-wrap:wrap;background:#fafaf8}
.verdict .lbl{font-size:12px;color:var(--mut);flex:1 1 100%}
.verdict button{flex:1;padding:9px 6px;border-radius:8px;font-weight:600;font-size:13px}
button.ok{background:#e6f2ec;color:#1d5c44;border:1px solid #bcd9cc}button.ok.on{background:#1d5c44;color:#fff}
button.no{background:#fbeeee;color:var(--warn);border:1px solid #e5bcbc}button.no.on{background:var(--warn);color:#fff}
.grid.duo2{grid-template-columns:minmax(0,560px) 1fr}
@media(max-width:1150px){.grid.duo2{grid-template-columns:1fr}}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.duocol .imgwrap{width:100%;position:relative;overflow:hidden;border-radius:6px;background:#ddd}
.duocol img{width:100%;height:auto;display:block}
.duocol .verdict{margin-top:6px;padding:6px 8px}
.duocol .verdict button{font-size:12px;padding:7px 4px}
.duocol .verdict .lbl{font-size:11px}
.noimg{padding:56px 16px;text-align:center;border:1px dashed var(--line);border-radius:8px;color:var(--mut)}
.wantrow{margin-top:8px}
#wantImg.on{background:var(--acc);color:#fff;border-color:var(--acc)}
.revchip{display:inline-block;margin-left:10px;padding:2px 10px;border-radius:999px;background:#eef4f1;color:#1d5c44;font-size:12px}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-left:4px;vertical-align:middle}
.dot.ok{background:#1d5c44}.dot.no{background:var(--warn)}
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
 <div class="top">
  <div class="brand">
   <span class="mark"><svg class="ic" viewBox="0 0 24 24"><path d="M2 12h20M6 8v8M18 8v8M4 10v4M20 10v4"/></svg></span>
   <h1>ALIVO 动作库审查</h1>
   <span class="count" id="count"></span><span class="revchip" id="revProg" hidden></span>
  </div>
  <div class="search"><svg class="ic" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg><input type="search" id="q" placeholder="搜索名称 / 英文 / 肌群 / 别名"></div>
 </div>
 <div class="filters">
  <span class="fsec">筛选</span>
  <label class="fld"><svg class="ic" viewBox="0 0 24 24"><circle cx="12" cy="7" r="3.5"/><path d="M5 21c0-4 3-7 7-7s7 3 7 7"/></svg><span>部位</span><select id="part"></select></label>
  <label class="fld"><svg class="ic" viewBox="0 0 24 24"><path d="M2 12h20M6 8v8M18 8v8M4 10v4M20 10v4"/></svg><span>器械</span><select id="eq"></select></label>
  <label class="fld"><svg class="ic" viewBox="0 0 24 24"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg><span>类别</span><select id="energy"><option value="">全部</option><option value="aerobic">有氧</option><option value="mixed">混合</option><option value="strength">力量</option></select></label>
  <label class="fld"><svg class="ic" viewBox="0 0 24 24"><path d="M4 9h16M4 15h16M10 3 8 21M16 3l-2 18"/></svg><span>计量</span><select id="measure"><option value="">全部</option><option value="reps">计数</option><option value="duration">计时</option><option value="unknown">待维护</option></select></label>
  <label class="fld"><svg class="ic" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg><span>计时</span><select id="timing"><option value="">全部</option><option value="free">正计时</option><option value="fixed">倒计时</option><option value="none">无建议</option></select></label>
  <span class="fsec">审核</span>
  <label class="fld"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m4 18 5-5 4 4 3-3 4 4"/></svg><span>配图</span><select id="media"><option value="">全部</option><option value="yes">有图</option><option value="no">无图</option><option value="open">有开源版</option><option value="noopen">无开源版</option><option value="want">已标记需配图</option></select></label>
  <label class="fld"><svg class="ic" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/></svg><span>审核</span><select id="review"><option value="">全部</option><option value="reviewed">已审核</option><option value="pending">未审核</option></select></label>
  <label class="fld"><svg class="ic" viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 7.9-1"/></svg><span>开源版</span><select id="mrev"><option value="">全部</option><option value="pending">未审</option><option value="approved">已通过</option><option value="rejected">需重新生成</option></select></label>
  <label class="fld"><svg class="ic" viewBox="0 0 24 24"><path d="m12 3 8 8-8 10L4 11z"/></svg><span>置信</span><select id="conf"><option value="">全部</option><option value="high">高</option><option value="medium">中</option><option value="low">低</option></select></label>
  <button id="reset">重置</button>
 </div>
 <div class="chipsrow"><div class="chips" id="chips"></div><div class="note">类别为规则推断待复核 · <a href="motion-preview.html">动作 GIF 样例 →</a></div></div>
</header>
<div class="main">
 <div class="list" id="list"></div>
 <div class="detail" id="detail"><p class="note">← 选择左侧动作查看详情</p></div>
</div>
<div class="export"><button id="subIssue" title="把全部复核决定打包成 GitHub Issue">提交审核到 GitHub（0）</button><button id="expJson">导出我的复核修改</button><button id="impJson">导入复核修改</button><input type="file" id="impFile" accept=".json" hidden></div>
<script>
const DATA=__DATA__;
const ENERGY={aerobic:'有氧（持续）',mixed:'混合 / 高强度间歇',strength:'力量 / 柔韧（默认）'};
const PART={};DATA.records.forEach(r=>{PART[r.part||'(未标注)']=1});
const EQ={};DATA.records.forEach(r=>{EQ[r.eq||'(未标注)']=1});
const LBL=__LABELS__;

const st={q:'',part:'',eq:'',energy:'',measure:'',timing:'',media:'',review:'',conf:'',mrev:'',energyOv:{}};
const store=JSON.parse(localStorage.getItem('alivoReview')||'{}');
if(store.overrides)Object.assign(st.energyOv,store.overrides);
const mRev=JSON.parse(localStorage.getItem('alivoMediaReview')||'{}');
function saveMRev(){localStorage.setItem('alivoMediaReview',JSON.stringify(mRev));updSubBtn()}
function mRevCount(){return Object.keys(mRev).length}
function updSubBtn(){document.getElementById('subIssue').textContent='提交审核到 GitHub（'+mRevCount()+'）';
 const opens=DATA.records.filter(r=>r.media.open);
 const ap=opens.filter(r=>mRev[r.id+':open']&&mRev[r.id+':open'].status==='approved').length;
 const rj=opens.filter(r=>mRev[r.id+':open']&&mRev[r.id+':open'].status==='rejected').length;
 const el=document.getElementById('revProg');
 const wc=Object.values(mRev).filter(d=>d.version==='request').length;
 if(opens.length||wc){el.hidden=false;el.textContent='开源版审核：通过 '+ap+' · 拒绝 '+rj+' · 未审 '+(opens.length-ap-rj)+' / '+opens.length+(wc?' · 已标记需配图 '+wc:'')}}
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
  if(st.media==='yes'&&!r.media.file)return false;
  if(st.media==='no'&&r.media.file)return false;
  if(st.media==='open'&&!r.media.open)return false;
  if(st.media==='noopen'&&r.media.open)return false;
  if(st.media==='want'&&!mRev[r.id+':request'])return false;
  if(st.review){const s=r.meta.reviewStatus==='reviewed'?'reviewed':'pending';if(s!==st.review)return false}
  if(st.mrev){if(!r.media.open)return false;const d=mRev[r.id+':open'];const s=d?d.status:'pending';if(s!==st.mrev)return false}
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
   '<div style="text-align:right"><span class="badge '+energyOf(r)+'">'+ENERGY[energyOf(r)].split('（')[0]+'</span><br><span class="badge '+(r.meta.reviewStatus==='reviewed'?'reviewed':'pending')+'">'+(r.meta.reviewStatus==='reviewed'?'已审':'未审')+'</span> '+(r.media.file?'<span class="badge">图</span>':(mRev[r.id+':request']?'<span class="badge mixed">需图</span>':''))+(r.media.open?'<span class="badge aerobic">开源</span>'+(mRev[r.id+':open']?'<span class="dot '+(mRev[r.id+':open'].status==='approved'?'ok':'no')+'"></span>':''):'')+'</div>';
  d.onclick=()=>{cur=r.id;renderList();renderDetail(r)};l.appendChild(d)}
 if(rows.length>400){const p=document.createElement('div');p.className='note';p.style.padding='8px';p.textContent='仅显示前 400 条，请用筛选缩小范围';l.appendChild(p)}
 renderChips();
}
function renderList(){/* re-render only selection highlight cheaply */document.querySelectorAll('.row').forEach((el,i)=>{if(rows[i])el.classList.toggle('sel',rows[i].id===cur)})}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function renderDetail(r){
 const e=energyOf(r),conf=confOf(r),t=r.timing;
 const motionFile=DATA.motionSamples[r.id]||'';
 const track=r.meta.track||{},tk=Object.entries(track).filter(([k,v])=>v).map(([k,v])=>({'loadType':'负重类型','weightBasis':'重量口径','repsBasis':'次数口径','defaultSide':'默认侧别'}[k]||k)+'：'+({'external':'外部负重','bodyweight':'自重','assistance':'辅助','machine':'器械示值','single':'单侧','total':'合计','per-side':'单侧','bilateral':'双侧','alternating':'交替','unknown':'未知'}[v]||v)).join('；');
 document.getElementById('detail').innerHTML=
 '<h2>'+esc(r.name)+' <span class="badge '+e+'">'+ENERGY[e]+'</span> <span class="badge '+(r.meta.reviewStatus==='reviewed'?'reviewed':'pending')+'">'+(r.meta.reviewStatus==='reviewed'?'已审核':'未审核')+'</span> <span class="badge '+conf+'">类别置信 '+conf+'</span></h2>'+
 '<div class="en">'+esc(r.en)+' · <code>'+esc(r.id)+'</code> · 来源 '+esc(r.source)+'</div>'+
 (r.energy===e?'':'<div class="warnbox">规则原判：'+ENERGY[r.energy]+'（'+esc(r.energyBasis)+'）。已被你改为：'+ENERGY[e]+'。</div>')+
 '<div class="grid'+(r.media.open?' duo2':'')+'"><div>'+(
 r.media.open?
  '<div class="duo">'+
   '<div class="duocol"><div class="imgwrap"><img id="dImg_branded" alt="'+esc(r.name)+'（带标版）" src="media/'+encodeURIComponent(r.media.file)+'"><div class="hint">带标版 · 点击放大</div></div><div class="verdict"><span class="lbl" id="mrevLabel_branded"></span><button id="mOk_branded" class="ok">✓ 通过</button><button id="mNo_branded" class="no">✗ 重新生成</button></div><div class="note" style="margin-top:4px">ALIVO-editorial · 可自由使用</div></div>'+
   '<div class="duocol"><div class="imgwrap"><img id="dImg_open" alt="'+esc(r.name)+'（无标开源版）" src="media-open/'+encodeURIComponent(r.media.open)+'"><div class="hint">无标开源版 · 点击放大</div></div><div class="verdict"><span class="lbl" id="mrevLabel_open"></span><button id="mOk_open" class="ok">✓ 通过</button><button id="mNo_open" class="no">✗ 重新生成</button></div><div class="note" style="margin-top:4px">CC-BY-4.0 · Paul Leung · 使用须署名</div></div>'+
  '</div>'+(motionFile?'<div class="imgctrl"><button id="btnGif" type="button" aria-pressed="false">动作 GIF 样例</button></div><div class="note">ALIVO 编辑插图，非动作教学示范（动态试稿）</div>':'')
 :r.media.file?
  '<div class="imgwrap"><img id="dImg" alt="'+esc(r.name)+'的插图" src="media/'+encodeURIComponent(r.media.file)+'"><div class="hint">可放大检视</div></div>'+
  '<div class="imgctrl"><button id="btnKb">动态检视</button><button id="btnZoom">放大细节</button>'+(motionFile?'<button id="btnGif" type="button" aria-pressed="false">动作 GIF 样例</button>':'')+'</div>'+
  '<div class="verdict"><span class="lbl" id="mrevLabel_branded"></span><button id="mOk_branded" class="ok">✓ 通过</button><button id="mNo_branded" class="no">✗ 需重新生成</button></div>'+
  (motionFile?'<div class="note">ALIVO 编辑插图，非动作教学示范（动态试稿）</div>':'')
 :'<div class="noimg">无 ALIVO 插图</div><div class="verdict wantrow"><span class="lbl" id="wantLabel"></span><button id="wantImg">＋ 标记需要配图</button></div>')+'</div><div>'+
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
 const verRefresh=[];
 const mSetV=(v,s)=>{const k=r.id+':'+v;if(mRev[k]&&mRev[k].status===s)delete mRev[k];else mRev[k]={status:s,version:v,catalogId:r.id,ts:new Date().toISOString()};saveMRev();verRefresh.forEach(f=>f());render()};
 ['branded','open'].forEach(v=>{
  const ok=document.getElementById('mOk_'+v),no=document.getElementById('mNo_'+v),lb=document.getElementById('mrevLabel_'+v);
  if(!ok)return;
  const show=()=>{const d=mRev[r.id+':'+v];
   lb.textContent=(v==='open'?'无标开源版':'带标版')+'：'+(d?(d.status==='approved'?'✓ 已通过 '+d.ts.slice(0,10):'✗ 需重新生成 '+d.ts.slice(0,10)):'未审');
   ok.classList.toggle('on',!!d&&d.status==='approved');no.classList.toggle('on',!!d&&d.status==='rejected')};
  ok.onclick=()=>mSetV(v,'approved');no.onclick=()=>mSetV(v,'rejected');verRefresh.push(show);show()});
 ['dImg_branded','dImg_open'].forEach(id=>{const img=document.getElementById(id);if(img){
  img.style.cursor='zoom-in';
  img.onclick=()=>{img.classList.toggle('zoomed');img.style.cursor=img.classList.contains('zoomed')?'zoom-out':'zoom-in'};
  img.onmousemove=e=>{if(img.classList.contains('zoomed')){const b=img.getBoundingClientRect();img.style.transformOrigin=((e.clientX-b.left)/b.width*100)+'% '+((e.clientY-b.top)/b.height*100)+'%'}}}});
 const w=document.getElementById('wantImg');
 if(w){const wl=document.getElementById('wantLabel');
  const ws=()=>{const d=mRev[r.id+':request'];wl.textContent=d?'已标记需要配图（'+d.ts.slice(0,10)+'）':'未标记';w.classList.toggle('on',!!d)};
  w.onclick=()=>{const k=r.id+':request';if(mRev[k])delete mRev[k];else mRev[k]={status:'requested',version:'request',catalogId:r.id,ts:new Date().toISOString()};saveMRev();ws();render()};ws()}
 const di=document.getElementById('dImg')||document.getElementById('dImg_branded');
 const kb=document.getElementById('btnKb'),zm=document.getElementById('btnZoom');
 if(di&&kb){
  kb.onclick=()=>{di.classList.toggle('kb');kb.classList.toggle('on');kb.textContent=di.classList.contains('kb')?'停止检视':'动态检视'};
  zm.onclick=()=>{di.classList.toggle('zoomed');zm.classList.toggle('on');zm.textContent=di.classList.contains('zoomed')?'还原':'放大细节'};
  di.onclick=()=>{if(di.classList.contains('zoomed')){di.classList.remove('zoomed');zm.classList.remove('on');zm.textContent='放大细节'}};
  di.onmousemove=e=>{if(di.classList.contains('zoomed')){const b=di.getBoundingClientRect();di.style.transformOrigin=((e.clientX-b.left)/b.width*100)+'% '+((e.clientY-b.top)/b.height*100)+'%'}};
 }
 const gif=document.getElementById('btnGif'),hint=document.querySelector('.detail .hint');
 if(gif&&di){let playing=false;
  gif.onclick=()=>{playing=!playing;di.classList.remove('kb','zoomed');if(kb){kb.classList.remove('on');zm.classList.remove('on');kb.textContent='动态检视';zm.textContent='放大细节'}
   gif.classList.toggle('on',playing);gif.setAttribute('aria-pressed',String(playing));gif.textContent=playing?'返回静态插图':'动作 GIF 样例';
   if(hint)hint.textContent=playing?'动态试稿 · 非动作教学':'可放大检视';di.alt=r.name+(playing?'的动态试稿':'的插图');
   di.onerror=()=>{if(playing){playing=false;di.onerror=null;di.src='media/'+encodeURIComponent(r.media.file);gif.classList.remove('on');gif.setAttribute('aria-pressed','false');gif.textContent='动作 GIF 样例';if(hint)hint.textContent='GIF 加载失败';}};
   di.src=(playing?'motion/'+encodeURIComponent(motionFile):'media/'+encodeURIComponent(r.media.file));
  };
 }
 document.getElementById('eOv').onchange=ev=>{const v=ev.target.value;if(v)st.energyOv[r.id]=v;else delete st.energyOv[r.id];save();renderDetail(r);render()};
 document.getElementById('eClr').onclick=()=>{delete st.energyOv[r.id];save();renderDetail(r);render()};
}
['q','part','eq','energy','measure','timing','media','review','conf','mrev'].forEach(id=>{document.getElementById(id).oninput=e=>{st[id]=e.target.value;render()}});
document.getElementById('reset').onclick=()=>{Object.keys(st).forEach(k=>{if(typeof st[k]==='string')st[k]=''});localStorage.removeItem('alivoReview');document.querySelectorAll('header select,input').forEach(el=>{if(el.tagName==='SELECT')el.selectedIndex=0;else el.value=''});render()};
function out(){return{note:'ALIVO 动作库复核结果；energy 为 aerobic/mixed/strength，合并到 exercise_measures.json 或 exercise_metadata.json 前需维护者确认；mediaReview 为逐图审核决定（version: branded|open, status: approved|rejected）；imageRequests 为无图动作的配图优先级请求',overrides:Object.entries(st.energyOv).map(([id,energy])=>({catalogId:id,energy})),mediaReview:Object.values(mRev).filter(d=>d.version==='branded'||d.version==='open'),imageRequests:Object.values(mRev).filter(d=>d.version==='request')}}
document.getElementById('subIssue').onclick=()=>{
 const payload=out();const body='<!-- alivo-review-payload\n'+JSON.stringify(payload)+'\n-->\n\n复核决定：'+payload.mediaReview.length+' 条媒体审核 + '+payload.overrides.length+' 条类别修正 + '+payload.imageRequests.length+' 条配图请求，请见上方 JSON。';
 const url='https://github.com/zhanshuoliang/alivo-exercise-media/issues/new?title='+encodeURIComponent('媒体与类别复核 '+new Date().toISOString().slice(0,10))+'&body='+encodeURIComponent(body);
 window.open(url,'_blank')};
document.getElementById('expJson').onclick=()=>{const b=new Blob([JSON.stringify(out(),null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='alivo-catalog-review-'+new Date().toISOString().slice(0,10)+'.json';a.click()};
document.getElementById('impJson').onclick=()=>document.getElementById('impFile').click();
document.getElementById('impFile').onchange=async e=>{const f=e.target.files[0];if(!f)return;try{const j=JSON.parse(await f.text());(j.overrides||[]).forEach(o=>{if(o.catalogId&&o.energy)st.energyOv[o.catalogId]=o.energy});save();render();if(cur)renderDetail(DATA.records.find(r=>r.id===cur))}catch(err){alert('导入失败：'+err.message)}};
// enrich rows with labels
{const L=LBL;DATA.records.forEach(r=>{r.partLabel=L.part[r.part]||r.part;r.eqLabel=L.eq[r.eq]||r.eq;r.measureLabel=L.measure[r.measure]})}
// init selects
const partCnt={},eqCnt={};DATA.records.forEach(r=>{partCnt[r.part]=(partCnt[r.part]||0)+1;eqCnt[r.eq]=(eqCnt[r.eq]||0)+1});
document.getElementById('part').innerHTML='<option value="">全部</option>'+Object.entries(partCnt).sort((a,b)=>b[1]-a[1]).map(([k,v])=>'<option value="'+esc(k)+'">'+esc(LBL.part[k]||k)+'（'+v+'）</option>').join('');
document.getElementById('eq').innerHTML='<option value="">全部</option>'+Object.entries(eqCnt).sort((a,b)=>b[1]-a[1]).map(([k,v])=>'<option value="'+esc(k)+'">'+esc(LBL.eq[k]||k)+'（'+v+'）</option>').join('');
updSubBtn();
render();if(DATA.records.length)renderDetail(DATA.records[0]);
</script>
</body></html>"""


def label_maps():
    part = {k: PART_LABELS.get(k, k) for k in PART_LABELS}
    return {"part": part, "eq": EQ_LABELS, "measure": MEASURE_LABELS}


if __name__ == "__main__":
    main()
