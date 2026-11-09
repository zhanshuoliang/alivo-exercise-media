'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const repo = 'D:\\codex-temp\\alivo';
const roots = [path.join(repo,'entry/src/main/resources/rawfile'),path.join(repo,'mobile/alivo_app/assets/catalog')];
const currentDate = new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Shanghai' }).format(new Date());
const manifest = JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const apply = process.argv.includes('--apply');
const extras = manifest.extras || [], bindings = manifest.bindings || [];
assert.ok(bindings.length > 0);
const read = file => fs.readFileSync(file,'utf8');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
function appendObjects(text,objects,indent,lastMarker){
 if(!objects.length)return text;
 const at=text.lastIndexOf(lastMarker);assert.ok(at>=0,'missing array marker');
 const eol=text.includes('\r\n')?'\r\n':'\n';
 const rows=objects.map(x=>JSON.stringify(x,null,2).split('\n').map(line=>' '.repeat(indent)+line).join(eol)).join(','+eol);
 return text.slice(0,at).trimEnd()+','+eol+rows+text.slice(at);
}
function insertMeasures(text,objects){
 if(!objects.length)return text;
 const eol=text.includes('\r\n')?'\r\n':'\n';
 const marker=eol+'    {'+eol+'      "catalogId": "free-exercise-db:';
 const at=text.indexOf(marker);assert.ok(at>=0,'reviewed measure marker missing');
 const prefix=text.slice(0,at);assert.ok(prefix.endsWith(','));
 const rows=objects.map(x=>JSON.stringify(x,null,2).split('\n').map(line=>'    '+line).join(eol)).join(','+eol);
 return prefix+eol+rows+','+text.slice(at);
}
const pair = (file, same = true, parse = true) => {
 const paths = roots.map(r=>path.join(r,file)), contents=paths.map(read);
 if(same) assert.equal(contents[0],contents[1],'platform mismatch: '+file);
 return {paths,contents,parsed:parse ? contents.map(JSON.parse) : undefined};
};
const metadata=pair('exercise_metadata.json'), notice=pair('exercise_media/NOTICE.md',true,false),
      extraPair=pair('exercises_extra.json',false), measures=pair('exercise_measures.json');
const base=JSON.parse(read(path.join(roots[0],'exercises_zh.json')));
const reviewed=JSON.parse(read(path.join(roots[0],'exercises_reviewed.json')));
const ids=new Set([...base.map(x=>'exercises-dataset:'+x.id),...extraPair.parsed[0].map(x=>'alivo:'+x.id),...reviewed.map(x=>'free-exercise-db:'+x.id)]);
const currentCount=ids.size;
assert.equal(currentCount,base.length+extraPair.parsed[0].length+reviewed.length);
const meta=structuredClone(metadata.parsed[0]);
const manifestMeasures=structuredClone(measures.parsed[0]);
for(const extra of extras){
 assert.match(extra.id,/^extra-[0-9]{3}$/); assert.ok(!ids.has('alivo:'+extra.id));
 assert.ok(extra.name && extra.nz && extra.eq && Array.isArray(extra.st) && extra.st.length>1);
 assert.ok(bindings.some(x=>x.catalogId==='alivo:'+extra.id));
 ids.add('alivo:'+extra.id);
}
const usedIds=new Set(meta.media.map(x=>x.catalogId)),usedPaths=new Set(meta.media.map(x=>x.localPath)),
      usedHashes=new Set(meta.media.map(x=>x.sha256)), records=[], images=[];
for(const b of bindings){
 assert.ok(ids.has(b.catalogId),'unknown: '+b.catalogId); assert.ok(!usedIds.has(b.catalogId),'already bound: '+b.catalogId);
 assert.match(b.filename,/^[a-z0-9_-]+\.png$/); assert.equal(b.folder,'new');
 const localPath='exercise_media/'+b.filename, bytes=fs.readFileSync(path.join(__dirname,'new',b.filename));
 assert.equal(bytes.subarray(0,8).toString('hex'),'89504e470d0a1a0a');
 const hash=sha(bytes);
 assert.ok(!usedPaths.has(localPath));assert.ok(!usedHashes.has(hash));
 const destinations=roots.map(r=>path.join(r,localPath)); for(const dest of destinations) assert.ok(!fs.existsSync(dest),'target exists: '+dest);
 const r={catalogId:b.catalogId,sourceRecordId:'alivo:editorial:'+b.filename,localPath,
  sourceUrl:'https://openai.com/policies/terms-of-use/',author:'ALIVO',license:'ALIVO-editorial',
  licenseUrl:'https://openai.com/policies/terms-of-use/',changes:'ALIVO 原创彩色编辑插图，服装带 ALIVO 品牌字标',
  sha256:hash,reviewedAt:currentDate};
 records.push(r);images.push({destinations,bytes});meta.media.push(r);
 usedIds.add(b.catalogId);usedPaths.add(localPath);usedHashes.add(hash);
}
let newNotice=notice.contents[0];
const heading='## ALIVO editorial gap-fill illustrations generated '+currentDate;
if(!newNotice.includes(heading)) newNotice=newNotice.trimEnd()+'\n\n'+heading+'\n\nGenerated specifically for ALIVO with OpenAI ImageGen. Editorial illustrations are not instructional demonstrations.\n';
newNotice=newNotice.trimEnd()+'\n'+records.map(r=>'- '+String.fromCharCode(96)+r.localPath+String.fromCharCode(96)+' — '+String.fromCharCode(96)+r.catalogId+String.fromCharCode(96)+'; SHA-256 '+String.fromCharCode(96)+r.sha256+String.fromCharCode(96)+'.').join('\n')+'\n';
const writes=[];
const setPair=(p,contents)=>{for(let i=0;i<2;i++) writes.push([p.paths[i],p.contents[i],contents[i]]);};
const metaText=appendObjects(metadata.contents[0],records,4,'\n  ]');
assert.deepEqual(JSON.parse(metaText),meta);
setPair(metadata,[metaText,metaText]); setPair(notice,[newNotice,newNotice]);
if(extras.length){
 const extraDocs=extraPair.parsed.map((arr,i)=>arr.concat(extras.map(x=>i===0?{...x,im:'',gf:''}:x)));
 const extraTexts=extraPair.contents.map((text,i)=>appendObjects(text,extraDocs[i].slice(extraPair.parsed[i].length),2,'\n]'));
for(let i=0;i<2;i++)assert.deepEqual(JSON.parse(extraTexts[i]),extraDocs[i]);
setPair(extraPair,extraTexts);
 const newMeasures=extras.map(x=>({catalogId:'alivo:'+x.id,measure:'reps',kind:'repetition',
   evidence:'项目自编动作，按完成重复次数记录。',annotatedAt:'2026-11-08',version:1}));
 const insertAt=manifestMeasures.entries.findIndex(x=>x.catalogId.startsWith('free-exercise-db:'));
 assert.ok(insertAt>=0);
 manifestMeasures.entries.splice(insertAt,0,...newMeasures);
 const measureText=insertMeasures(measures.contents[0],newMeasures);
assert.deepEqual(JSON.parse(measureText),manifestMeasures);
setPair(measures,[measureText,measureText]);
 const policyFile=path.join(repo,'tools/build-exercise-measures.cjs'), oldPolicy=read(policyFile);
 const policyMarker='const repeatEvidence =', newIds=extras.map(x=>'alivo:'+x.id);
 let policy=oldPolicy;
 const existing=/const authoredRound5Repetitions = new Set\((\[[^\]]*\])\);/.exec(policy);
 if(existing){
  const prior=JSON.parse(existing[1]);
  for(const id of newIds)assert.ok(!prior.includes(id),'policy duplicate: '+id);
  policy=policy.replace(existing[0],'const authoredRound5Repetitions = new Set('+JSON.stringify(prior.concat(newIds))+');');
 }else{
  assert.equal(policy.split(policyMarker).length,2);
  const newSet='const authoredRound5Repetitions = new Set('+JSON.stringify(newIds)+');\n';
  policy=policy.replace(policyMarker,newSet+policyMarker);
  const branch='} else if (authoredRepetitions.has(catalogId)) {';
  assert.equal(policy.split(branch).length,2);
  policy=policy.replace(branch,'} else if (authoredRepetitions.has(catalogId) || authoredRound5Repetitions.has(catalogId)) {');
  const date="annotatedAt: authoredRepetitions.has(catalogId) ? '2026-11-07' : (maintained && maintained.reviewedAt > '2026-10-10' ? maintained.reviewedAt : '2026-10-10')";
  assert.equal(policy.split(date).length,2);
  policy=policy.replace(date,"annotatedAt: authoredRound5Repetitions.has(catalogId) ? '2026-11-08' : (authoredRepetitions.has(catalogId) ? '2026-11-07' : (maintained && maintained.reviewedAt > '2026-10-10' ? maintained.reviewedAt : '2026-10-10'))");
 }
 writes.push([policyFile,oldPolicy,policy]);
}
const mediaFile=path.join(repo,'mobile/alivo_app/test/exercise_media_test.dart'),oldMedia=read(mediaFile);
const marker="      'alivo:extra-016': 'bulgarian_split_squat.png',";
assert.equal(oldMedia.split(marker).length,2);
for(const r of records) assert.ok(!oldMedia.includes("'"+r.catalogId+"':"),r.catalogId);
const additions=records.map(r=>"      '"+r.catalogId+"': '"+path.basename(r.localPath)+"',").join('\n');
writes.push([mediaFile,oldMedia,oldMedia.replace(marker,marker+'\n'+additions)]);
const regressionFile=path.join(repo,'tests/regression.cjs'),oldRegression=read(regressionFile);
let regression=(extras.length || records.some(r=>r.catalogId==='free-exercise-db:Pallof_Press')) ? oldRegression.replace(/\r\n/g,'\n') : oldRegression;
if(records.some(r=>r.catalogId==='free-exercise-db:Pallof_Press')){
 const old="    assert.equal(item.media, undefined);\n  }\n  assert.equal(store.search(h.ctx, '壶铃光环'";
 const replacement="    if (id === 'Pallof_Press') {\n      assert.equal(item.media.localPath, 'exercise_media/pallof_press.png');\n      assert.equal(item.media.license, 'ALIVO-editorial');\n    } else { assert.equal(item.media, undefined); }\n  }\n  assert.equal(store.search(h.ctx, '壶铃光环'";
 assert.equal(regression.split(old).length,2);
 regression=regression.replace(old,replacement);
}
if(extras.length){
 const nex=currentCount+extras.length;
 const exact=(text,from,to,expected)=>{
  assert.equal(text.split(from).length-1,expected,'unexpected count for '+from);
  return text.split(from).join(to);
 };
 const countChanges=[
  ['catalog maintenance gives '+currentCount+' stable IDs','catalog maintenance gives '+nex+' stable IDs',1],
  ['high-frequency tracking maintenance preserves '+currentCount+' identities','high-frequency tracking maintenance preserves '+nex+' identities',1],
  ['assert.equal(all.length, '+currentCount+');','assert.equal(all.length, '+nex+');',4],
  ['assert.equal(config.entries.length, '+currentCount+');','assert.equal(config.entries.length, '+nex+');',1],
  ['assert.equal(fallback.length, '+currentCount+');','assert.equal(fallback.length, '+nex+');',1]
 ];
 for(const [from,to,count] of countChanges)regression=exact(regression,from,to,count);
 const prevReps=measures.parsed[0].entries.filter(x=>x.measure==='reps').length,nextReps=prevReps+extras.length;
 for(const prefix of ["all.filter(x => measure(x) === 'reps').length, ","config.entries.filter(x => x.measure === 'reps').length, "])
  regression=exact(regression,prefix+prevReps,prefix+nextReps,1);
 const domainFile=path.join(repo,'mobile/alivo_app/test/domain_test.dart'),domain=read(domainFile);
 let newDomain=domain;
 for(const prefix of ['expect(catalog.items.length, ','expect(catalog.items.map((e) => e.id).toSet().length, '])
  newDomain=exact(newDomain,prefix+currentCount+');',prefix+nex+');',1);
 writes.push([domainFile,domain,newDomain]);
 const testMarker="test('bench hip thrust and rear-foot-elevated split squat stay distinct from conflicting variants', () => {";
 assert.equal(regression.split(testMarker).length,2);
 const checks=extras.map(x=>{
  const record=records.find(r=>r.catalogId==='alivo:'+x.id);
  return "  { const x = store.findById(h.ctx, '"+record.catalogId+"'); assert.equal(x.nz, "+JSON.stringify(x.nz)+"); assert.equal(x.eq, "+JSON.stringify(x.eq)+"); assert.equal(model.catalogExerciseMeasure(x), 'reps'); assert.equal(x.media.localPath, '"+record.localPath+"'); assert.equal(x.media.license, 'ALIVO-editorial'); assert.equal(model.exerciseImageUrl(x), ''); assert.equal(model.exerciseGifUrl(x), ''); }";
 }).join('\n');
 const extraTest="test('new authored actions have independent identities and editorial media', () => {\n  const h = harness(), store = new (h.load('services/ExerciseCatalogStore').ExerciseCatalogStore)(), model = h.load('models/ExerciseCatalogItem');\n"+checks+"\n});\n\n";
 regression=regression.replace(testMarker,extraTest+testMarker);
}
if(regression!==oldRegression) writes.push([regressionFile,oldRegression,regression]);
for(const [p,old] of writes) assert.equal(read(p),old,'changed since read: '+p);
if(apply){
 const done=[];
 try{
  for(const {destinations,bytes} of images) for(const p of destinations){fs.writeFileSync(p,bytes,{flag:'wx'});done.push([p,null]);}
  for(const [p,old,value] of writes){fs.writeFileSync(p,value,'utf8');done.push([p,old]);}
 } catch(e) {
  for(const [p,old] of done.reverse()) try{if(old===null) fs.unlinkSync(p);else fs.writeFileSync(p,old,'utf8');}catch(restore){process.stderr.write('ROLLBACK FAILED '+p+' '+restore.message+'\n');}
  throw e;
 }
}
console.log(JSON.stringify({applied:apply,extras:extras.map(x=>x.id),records:records.map(({catalogId,localPath,sha256})=>({catalogId,localPath,sha256}))},null,2));
