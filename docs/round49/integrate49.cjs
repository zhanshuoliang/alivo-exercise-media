'use strict';
// Round 40 integration — post-WebP-migration variant of add_bindings.cjs.
// Packages each staged male-branded PNG as 1024px lossy WebP q82 (method 4),
// appends metadata/NOTICE/PROVENANCE/test entries in both app bundles.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');
const assert = require('node:assert/strict');
const repo = 'D:\\codex-temp\\alivo';
const roots = [path.join(repo,'entry/src/main/resources/rawfile'),path.join(repo,'mobile/alivo_app/assets/catalog')];
const currentDate = new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Shanghai' }).format(new Date());
const manifest = JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const apply = process.argv.includes('--apply');
const bindings = manifest.bindings || [];
assert.ok(bindings.length > 0);
const read = file => fs.readFileSync(file,'utf8');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const pair = (file, same = true, parse = true) => {
 const paths = roots.map(r=>path.join(r,file)), contents=paths.map(read);
 if(same) assert.equal(contents[0],contents[1],'platform mismatch: '+file);
 return {paths,contents,parsed:parse ? contents.map(JSON.parse) : undefined};
};
const metadata=pair('exercise_metadata.json'), notice=pair('exercise_media/NOTICE.md',true,false),
      provenance=pair('exercise_media/PROVENANCE.csv',true,false);
const base=JSON.parse(read(path.join(roots[0],'exercises_zh.json')));
const extraCat=JSON.parse(read(path.join(roots[0],'exercises_extra.json')));
const reviewed=JSON.parse(read(path.join(roots[0],'exercises_reviewed.json')));
const ids=new Set([...base.map(x=>'exercises-dataset:'+x.id),...extraCat.map(x=>'alivo:'+x.id),...reviewed.map(x=>'free-exercise-db:'+x.id)]);
const meta=structuredClone(metadata.parsed[0]);
const usedIds=new Set(meta.media.map(x=>x.catalogId)),usedPaths=new Set(meta.media.map(x=>x.localPath)),
      usedHashes=new Set(meta.media.map(x=>x.sha256)), records=[], images=[], provRows=[];
const tmpDir=path.join(__dirname,'tmp_webp49'); fs.mkdirSync(tmpDir,{recursive:true});
for(const b of bindings){
 assert.ok(ids.has(b.catalogId),'unknown: '+b.catalogId); assert.ok(!usedIds.has(b.catalogId),'already bound: '+b.catalogId);
 assert.match(b.filename,/^[a-z0-9_-]+\.png$/); assert.equal(b.folder,'new');
 const base=b.filename.replace(/\.png$/,''), webpName=base+'.webp';
 const pngPath=path.join(__dirname,'new',b.filename), pngBytes=fs.readFileSync(pngPath);
 assert.equal(pngBytes.subarray(0,8).toString('hex'),'89504e470d0a1a0a');
 const pngSha=sha(pngBytes);
 // package: resize to 1024px + lossy WebP q82 method 4 (matches app migration)
 const tmpOut=path.join(tmpDir,webpName);
 execFileSync('python',['-c',
  "import sys;from PIL import Image;img=Image.open(sys.argv[1]).convert('RGB');"
  +"img=img.resize((1024,1024),Image.LANCZOS);img.save(sys.argv[2],'WEBP',quality=82,method=4)",
  pngPath,tmpOut]);
 const webpBytes=fs.readFileSync(tmpOut), webpSha=sha(webpBytes);
 const localPath='exercise_media/'+webpName;
 assert.ok(!usedPaths.has(localPath));assert.ok(!usedHashes.has(webpSha));
 const destinations=roots.map(r=>path.join(r,localPath)); for(const dest of destinations) assert.ok(!fs.existsSync(dest),'target exists: '+dest);
 records.push({catalogId:b.catalogId,sourceRecordId:'alivo:editorial:'+b.filename,localPath,
  sourceUrl:'https://openai.com/policies/terms-of-use/',author:'Paul Leung',license:'ALIVO-editorial',
  licenseUrl:'https://openai.com/policies/terms-of-use/',
  changes:'ALIVO 原创彩色编辑插图，服装带 ALIVO 品牌字标; resized to 1024px and encoded as lossy WebP quality 82',
  sha256:webpSha,reviewedAt:currentDate});
 images.push({destinations,bytes:webpBytes});
 provRows.push([b.catalogId,'exercise_media/'+b.filename,pngSha,localPath,webpSha,webpBytes.length].join(','));
 meta.media.push(records[records.length-1]);
 usedIds.add(b.catalogId);usedPaths.add(localPath);usedHashes.add(webpSha);
}
// metadata append (mirror add_objects indent=4, before final "  ]")
function appendObjects(text,objects,indent,lastMarker){
 if(!objects.length)return text;
 const at=text.lastIndexOf(lastMarker);assert.ok(at>=0,'missing array marker');
 const eol=text.includes('\r\n')?'\r\n':'\n';
 const rows=objects.map(x=>JSON.stringify(x,null,2).split('\n').map(line=>' '.repeat(indent)+line).join(eol)).join(','+eol);
 return text.slice(0,at).trimEnd()+','+eol+rows+text.slice(at);
}
const metaText=appendObjects(metadata.contents[0],records,4,'\n  ]');
assert.deepEqual(JSON.parse(metaText),meta);
// notice
let newNotice=notice.contents[0];
const heading='## ALIVO editorial gap-fill illustrations generated '+currentDate;
if(!newNotice.includes(heading)) newNotice=newNotice.trimEnd()+'\n\n'+heading+'\n\nGenerated specifically for ALIVO with OpenAI ImageGen. Editorial illustrations are not instructional demonstrations.\n';
newNotice=newNotice.trimEnd()+'\n'+records.map(r=>'- `'+r.localPath+'` — `'+r.catalogId+'`; SHA-256 `'+r.sha256+'`.').join('\n')+'\n';
// provenance
const newProv=provenance.contents[0].trimEnd()+'\n'+provRows.join('\n')+'\n';
// flutter test file
const mediaFile=path.join(repo,'mobile/alivo_app/test/exercise_media_test.dart'),oldMedia=read(mediaFile);
const marker="      'exercises-dataset:0691': 'seated_side_crunch_male.webp',";
assert.equal(oldMedia.split(marker).length,2);
for(const r of records) assert.ok(!oldMedia.includes("'"+r.catalogId+"':"),r.catalogId);
const additions=records.map(r=>"      '"+r.catalogId+"': '"+path.basename(r.localPath)+"',").join('\n');
const newMedia=oldMedia.replace(marker,marker+'\n'+additions);
// report / write
console.log('records:',records.length);
for(const r of records) console.log(' +',r.catalogId,r.localPath,r.sha256.slice(0,12));
if(apply){
 for(const [i,p] of metadata.paths.entries()) fs.writeFileSync(p,[metaText,metaText][i]);
 for(const p of notice.paths) fs.writeFileSync(p,newNotice);
 for(const p of provenance.paths) fs.writeFileSync(p,newProv);
 for(const img of images) for(const dest of img.destinations) fs.writeFileSync(dest,img.bytes);
 fs.writeFileSync(mediaFile,newMedia);
 console.log('APPLIED — wrote',images.length,'webp x2 + metadata + NOTICE + PROVENANCE + test');
}else console.log('DRY RUN (pass --apply to write)');
