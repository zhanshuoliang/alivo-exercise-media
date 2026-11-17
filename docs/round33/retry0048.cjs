const fs=require('fs'),path=require('path');
for(const[tr,stage]of[['m','stage33_m'],['f','stage33_f']]){
  const log=fs.readFileSync('logs33_'+tr+'/exec_0048_retry.log','utf8');
  const m=[...log.matchAll(/([A-Za-z]:[\\/][^\s'"]+\.png)/g)].map(x=>x[1]);
  const src=m[m.length-1];
  const dst=path.join(stage,'barbell_incline_reverse_grip_press_'+(tr=='m'?'male':'female')+'.png');
  fs.copyFileSync(src,dst);
  console.log(tr,src,'->',fs.existsSync(dst)?'ok':'FAIL');
}
