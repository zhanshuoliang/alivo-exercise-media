'use strict';
const fs=require('fs'),crypto=require('crypto');
const MR='D:/codex-temp/alivo-exercise-media';
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const batch=require('./batch_round34.json');
const rows=batch.bindings.map(x=>({catalogId:x.catalogId,base:x.filename.replace('_male.png','')}));
const date='2026-11-17';
// media/NOTICE.md only — Round 34 is branded-track-only; no media-open additions this round.
const maleRows=rows.map(r=>'- `'+r.base+'_male.png` — `'+r.catalogId+'`; SHA-256 `'+sha(MR+'/media/'+r.base+'_male.png')+'`.').join('\n');
const femaleRows=rows.map(r=>'- `'+r.base+'_female.png` — `'+r.catalogId+'`; SHA-256 `'+sha(MR+'/media/'+r.base+'_female.png')+'`.').join('\n');
const branded='\n\n## Round 34 — branded-only edition ('+date+')\n\nKai（男）/ Liv（女）双角色带标轨批次（开源轨本轮暂停，后续独立补生成）。男版已绑定入 App 目录数据（exercise_metadata.json）；女版为同动作的性别变体资产，仅入媒体库备用，未绑定。\n\n### Male edition（已绑定 App）\n\n'+maleRows+'\n\n### Female edition（性别变体，未绑定）\n\n'+femaleRows+'\n';
const noticePath=MR+'/media/NOTICE.md';
if(!fs.readFileSync(noticePath,'utf8').includes('## Round 34')) fs.appendFileSync(noticePath,branded);
console.log('NOTICE Round 34 section appended (dedup-checked),',rows.length,'rows x2');
