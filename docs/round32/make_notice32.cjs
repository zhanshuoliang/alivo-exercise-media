'use strict';
const fs=require('fs'),crypto=require('crypto');
const MR='D:/codex-temp/alivo-exercise-media';
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const batch=require('./batch_round32.json');
const rows=batch.bindings.map(x=>({catalogId:x.catalogId,base:x.filename.replace('_male.png','')}));
const date='2026-11-17';
// 1) manifest (idempotent — skip files already present)
const mf=JSON.parse(fs.readFileSync(MR+'/media-open/manifest.json','utf8'));
const items=mf.items||mf;
const have=new Set(items.map(x=>x.file));
let added=0;
rows.forEach(r=>{
  ['male','female'].forEach(sex=>{
    const fn=r.base+'_'+sex+'.png';
    if(have.has(fn))return;
    items.push({catalogId:r.catalogId,file:fn,author:'Paul Leung',license:'CC-BY-4.0',
      licenseUrl:'https://creativecommons.org/licenses/by/4.0/',
      sha256:sha(MR+'/media-open/'+fn),reviewedAt:date,
      changes:'原创开源编辑插图，纯色服装无品牌字标（AI 辅助生成，人工审核）'});
    added++;
  });
});
if(mf.items)mf.items=items;
fs.writeFileSync(MR+'/media-open/manifest.json',JSON.stringify(mf,null,2)+'\n');
console.log('manifest +'+added,'total',items.length);
// 2) media/NOTICE.md (idempotent — skip if heading exists)
const maleRows=rows.map(r=>'- `'+r.base+'_male.png` — `'+r.catalogId+'`; SHA-256 `'+sha(MR+'/media/'+r.base+'_male.png')+'`.').join('\n');
const femaleRows=rows.map(r=>'- `'+r.base+'_female.png` — `'+r.catalogId+'`; SHA-256 `'+sha(MR+'/media/'+r.base+'_female.png')+'`.').join('\n');
const branded='\n\n## Round 32 — dual-athlete edition ('+date+')\n\nKai（男）/ Liv（女）双角色同动作四轨批次的带标轨。男版已绑定入 App 目录数据（exercise_metadata.json）；女版为同动作的性别变体资产，仅入媒体库备用，未绑定。\n\n### Male edition（已绑定 App）\n\n'+maleRows+'\n\n### Female edition（性别变体，未绑定）\n\n'+femaleRows+'\n';
const noticePath=MR+'/media/NOTICE.md';
if(!fs.readFileSync(noticePath,'utf8').includes('## Round 32')) fs.appendFileSync(noticePath,branded);
// 3) media-open/NOTICE.md
const openRows=rows.map(r=>['male','female'].map(sex=>'- `'+r.base+'_'+sex+'.png` — `'+r.catalogId+'`; SHA-256 `'+sha(MR+'/media-open/'+r.base+'_'+sex+'.png')+'`.').join('\n')).join('\n');
const open='\n\n## Round 32 — dual-athlete open edition ('+date+')\n\nKai/Liv 双角色同动作四轨批次的开源轨（男/女各 15 张），纯提示词独立生成，无参考图。\n\n'+openRows+'\n';
const openPath=MR+'/media-open/NOTICE.md';
if(!fs.readFileSync(openPath,'utf8').includes('## Round 32')) fs.appendFileSync(openPath,open);
console.log('NOTICE sections appended (dedup-checked)');
