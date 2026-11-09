'use strict';
// Generates exec prompt files for each plan item. Usage: node make_prompts.cjs
const fs=require('node:fs'),path=require('node:path');
const dir=__dirname;
const plan=JSON.parse(fs.readFileSync(path.join(dir,'plan_round7.json'),'utf8'));
const SHARED='Use case: photorealistic-natural. Asset type: ALIVO fitness editorial illustration. The attached photo is a STYLE reference only: create the DIFFERENT exercise described below, never copy its pose. Square photograph, neutral gray seamless studio backdrop and floor, soft editorial lighting, natural realistic skin and hair, one adult athletic person wearing a dark muted forest-green tank top, charcoal shorts and dark athletic shoes. Print exactly one small white wordmark "ALIVO" (letters A L I V O) on the clothing in a clean sans-serif font; no other text, branding or watermark. One person, one coherent exercise moment, full body and all exercise equipment visible, realistic anatomy, hands and feet. Exercise: ';
for(const p of plan){
 const key=p.filename.replace('.png','');
 const txt='Use the image generation tool to create exactly one image now. Include the image attached to this prompt as the tool\'s reference image input. Call the tool with use case "photorealistic-natural" and pass the following prompt text to it VERBATIM, without rewriting or shortening:\n\nBEGIN TOOL PROMPT\n'+SHARED+p.exercise+'\nEND TOOL PROMPT\n\nAfter the image is generated, reply with only the absolute path of the saved PNG file. Do not edit files, do not review the image, do not generate more than one image.\n';
 fs.writeFileSync(path.join(dir,'prompts','exec_'+key+'.txt'),txt);
 console.log(key);
}
console.log('wrote',plan.length,'prompts');
