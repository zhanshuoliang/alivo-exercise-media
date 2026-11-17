const fs=require('fs'),path=require('path');
const plan=require('./plan_round47.json');
const tracks={m:'stage47_m',f:'stage47_f',};
const logs={m:'logs47_m',f:'logs47_f',};
const suffix={m:'_male.png',f:'_female.png',open_m:'_male.png',open_f:'_female.png'};
const lineRe=/^([A-Za-z]:[\\/][^\s"'`]*\.png)\s*$/i;
const anyRe=/([A-Za-z]:[\\/][^\s"'`]*generated_images[^\s"'`]*\.png)/g;
const MAX_AGE_MS=90*60*1000;
let copied=0,missing=[],suspect=[];
for(const[tr,stage]of Object.entries(tracks)){
  fs.mkdirSync(stage,{recursive:true});
  for(const p of plan){
    const eid=p.catalogId.split(':')[1];
    const log=path.join(logs[tr],`${eid}.log`);
    const txt=fs.existsSync(log)?fs.readFileSync(log,'utf8'):'';
    // Preferred: last line that is ONLY a png path (the instructed reply format)
    const lines=txt.split(/\r?\n/);
    let src=null,via='reply-line';
    for(let i=lines.length-1;i>=0;i--){
      const lm=lines[i].trim().match(lineRe);
      if(lm){src=lm[1];break;}
    }
    // Fallback: last generated_images png mention, but require fresh mtime
    if(!src){
      const m=[...txt.matchAll(anyRe)];
      if(m.length){src=m[m.length-1][1];via='log-scan';}
    }
    if(src&&fs.existsSync(src)){
      const age=Date.now()-fs.statSync(src).mtimeMs;
      if(via==='log-scan'&&age>MAX_AGE_MS){missing.push(log+' (stale '+src+')');}
      else{
        fs.copyFileSync(src,path.join(stage,p.base+suffix[tr]));
        copied++;
        if(via==='log-scan')suspect.push(p.catalogId+' '+tr+' via log-scan '+src);
      }
    }else missing.push(log+(src?' (src missing '+src+')':' (no png path)'));
  }
}
console.log('copied',copied,'missing',missing.length,'suspect',suspect.length);
missing.forEach(x=>console.log('MISS',x));
suspect.forEach(x=>console.log('SUSPECT',x));
