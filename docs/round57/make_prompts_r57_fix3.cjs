const fs=require('fs'),path=require('path');
const M='adult athletic man with short dark wavy hair',F='adult athletic woman with brown hair tied in a low ponytail';
const FRAME='ONE single square photograph capturing ONE continuous moment — absolutely no split screen, no collage, no side-by-side or stacked panels, exactly one frame.';
const branded=(scene,who)=>`Use the image generation tool to create exactly one image now. Include the image attached to this prompt as the tool's reference image input. Call the tool with use case "photorealistic-natural" and pass the following prompt text to it VERBATIM, without rewriting or shortening:

BEGIN TOOL PROMPT
Use case: photorealistic-natural. Asset type: ALIVO fitness editorial illustration. The attached photo is a STYLE reference only: create the DIFFERENT exercise described below, never copy its pose. ${FRAME} Neutral gray seamless studio backdrop and floor, soft editorial lighting, natural realistic skin and hair, one ${who} wearing a dark muted forest-green tank top, charcoal shorts and dark athletic shoes. Print exactly one small white wordmark "ALIVO" (letters A L I V O) on the clothing in a clean sans-serif font; absolutely NO text anywhere else in the image — no title, no caption, no words on the backdrop or floor, no branding, no watermark. Exercise: ${scene} Keep the whole athlete, head, hands, feet and all equipment entirely inside the square frame. Realistic anatomy and hand placement, one person only, no mirrors, no gym background clutter, no extra lettering.
END TOOL PROMPT

After the image is generated, reply with only the absolute path of the saved PNG file. Do not edit files, do not review the image, do not generate more than one image.
`;
const scene='BARBELL SIDE BEND. The athlete stands upright with the feet shoulder-width apart, holding a barbell in both hands with an overhand grip in front of the thighs, back straight and core engaged, bending the torso sideways to lower the barbell toward the right knee — captured at the bent position with the torso clearly tilted to one side and the barbell lowered alongside the leg. Front three-quarter view showing the sideways bent torso and the barbell held down near the knee.';
fs.writeFileSync(path.join('prompts57_m','exec_0096.txt'),branded(scene,M));
fs.writeFileSync(path.join('prompts57_f','exec_0096.txt'),branded(scene,F));
console.log('wrote 0096 replacement prompts');
