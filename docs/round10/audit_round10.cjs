'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const roots=['D:/codex-temp/alivo/entry/src/main/resources/rawfile','D:/codex-temp/alivo/mobile/alivo_app/assets/catalog'];
const get=(r,p)=>fs.readFileSync(path.join(r,p));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const meta=roots.map(r=>get(r,'exercise_metadata.json')),notice=roots.map(r=>get(r,'exercise_media/NOTICE.md')),measures=roots.map(r=>get(r,'exercise_measures.json'));
assert.ok(meta[0].equals(meta[1]),'exercise_metadata.json differs between platforms');
assert.ok(notice[0].equals(notice[1]),'NOTICE.md differs between platforms');
assert.ok(measures[0].equals(measures[1]),'exercise_measures.json differs between platforms');
const current=JSON.parse(meta[0]).media;
const baseline=JSON.parse(fs.readFileSync('D:/codex-temp/alivo-selfmade-generated-round7/media-baseline-213.json','utf8'));
assert.equal(baseline.length,213);
const old=new Map(baseline.map(x=>[x.catalogId,x]));
const wanted=JSON.parse(fs.readFileSync(path.join(__dirname,'targets_round10.json'),'utf8'));
const target=new Map(wanted.map(x=>[x.catalogId,x]));
const ids=new Set(),paths=new Set(),hashes=new Set(),added=[];
for(const m of current){
 assert.equal(m.license,'ALIVO-editorial');
 assert.match(m.localPath,/^exercise_media\/[a-z0-9_-]+\.(png|jpg)$/);
 assert.ok(!ids.has(m.catalogId),'duplicate catalogId '+m.catalogId);
 assert.ok(!paths.has(m.localPath),'duplicate path '+m.localPath);
 assert.ok(!hashes.has(m.sha256),'duplicate sha256 '+m.catalogId);
 ids.add(m.catalogId);paths.add(m.localPath);hashes.add(m.sha256);
 const bytes=roots.map(r=>get(r,m.localPath));
 assert.ok(bytes[0].equals(bytes[1]),'platform bytes differ '+m.localPath);
 assert.equal(sha(bytes[0]),m.sha256,'sha mismatch '+m.localPath);
 assert.ok(notice[0].toString('utf8').includes(m.sha256),'NOTICE missing sha '+m.catalogId);
 if(old.has(m.catalogId)){assert.deepEqual(m,old.get(m.catalogId),'old record changed: '+m.catalogId);}
 else {
  const c=target.get(m.catalogId);assert.ok(c,'unexpected new binding '+m.catalogId);
  assert.equal(m.localPath,'exercise_media/'+c.filename);
  const reviewed=path.join(__dirname,'new',c.filename);
  assert.ok(fs.existsSync(reviewed),'reviewed file missing '+c.filename);
  assert.ok(bytes[0].equals(fs.readFileSync(reviewed)),'asset does not match reviewed file '+c.filename);
  added.push({catalogId:m.catalogId,localPath:m.localPath,sha256:m.sha256});
 }
}
for(const id of old.keys()) assert.ok(ids.has(id),'baseline record removed: '+id);
const missing=wanted.filter(x=>!ids.has(x.catalogId)).map(x=>x.catalogId+':'+x.filename);
console.log(JSON.stringify({total:current.length,priorPreserved:old.size,newCount:added.length,platformBytesEqual:true,metadataAndNoticeEqual:true,noticeAndShaValid:true,newFilesMatchReviewed:true,records:added,missing},null,2));
