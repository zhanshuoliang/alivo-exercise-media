# 动态试稿关键帧生成记录

两个素材均以同目录所列的 ALIVO 自研静态图作为风格和虚拟人物参考，通过 OpenAI ImageGen 独立生成九宫格关键帧。以下为最终采用的提示词；生成后取前五个姿态，按相反顺序构成回程，再用 FFmpeg 插帧和 GIF 编码。结果为动态编辑试稿，非动作教学示范。

## 徒手深蹲

参考：`media/bodyweight_squat.png`；关键帧：`bodyweight_squat_keyframes.png`。

> Create a single 3-by-3 sprite sheet with EXACTLY NINE equal square photo cells arranged in a strict 3 columns by 3 rows grid; no gutter, no border, no numbering. This is a set of keyframes for an ALIVO bodyweight squat animation, NOT a sequence diagram. Use image 1 only as the reference for the same fictional athlete, natural skin tone, dark green tank and neutral gray seamless studio background. The same single full-body person appears once in each cell, all with identical locked camera, identical scale, identical face, clothing and lighting. Feet in exactly the same positions on the floor, hands held together at chest. Gradually animate one squat through nine positions, left-to-right top-to-bottom: fully upright, slight dip, half squat, lower squat, bottom squat with thighs near horizontal, lower squat rising, half squat rising, slight dip rising, fully upright. Entire head, arms, feet, shoe soles stay inside every cell. Knees and hips move naturally and bilaterally; heels stay flat. On every tank is a clearly readable small white wordmark spelled exactly 'ALIVO' across the chest, no other letters or text. The same neutral gray floor/backdrop and shadow stay identical. No equipment, no additional person. Natural color studio photography.

## 俯卧撑

参考：`media/push_up.png`；关键帧：`push_up_keyframes.png`。

> Create a single 3-by-3 sprite sheet with EXACTLY NINE equal square photo cells arranged in a strict 3 columns by 3 rows grid; no gutter, no border, no numbering. This is a set of keyframes for an ALIVO standard push-up animation. Use image 1 as the reference for the same fictional athlete, dark green tank, charcoal shorts, black shoes, dark exercise mat and neutral gray studio. The same one full-body person appears once in each cell, all from the SAME locked side-view camera, matching scale and framing. Both hands and toes stay firmly on the same spots on the mat and both elbows bend as the head, shoulders, trunk and hips descend together; body remains straight head-to-heel, knees stay above mat. Nine moments left-to-right top-to-bottom: high plank, slight descent, half descent, almost low, low push-up with chest hovering, almost low rising, half rising, nearly extended, high plank. No cropped heads, hands or shoes. Clothing carries one clearly readable white wordmark exactly 'ALIVO' in each cell, no other writing. Gray studio background and mat identical between cells, natural anatomy, same lighting and no extra objects.
