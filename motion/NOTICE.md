# ALIVO 动态编辑试稿

本目录两个 GIF 为 ALIVO 自研的动作效果试稿，授权标识为 `ALIVO-editorial`。它们基于同仓库的 ALIVO 自研静态图作为风格参考，使用 OpenAI ImageGen 新生成九宫格关键帧，再选取前五个姿态、按相反顺序构成回程并通过 FFmpeg 运动插值与 GIF 编码。它们不是实拍视频。ALIVO 编辑插图，非动作教学示范。

- `bodyweight_squat_preview.gif`：`alivo:extra-022`；风格参考 `media/bodyweight_squat.png`；关键帧母版 `sources/bodyweight_squat_keyframes.png`。
- `push_up_preview.gif`：`exercises-dataset:0662`；风格参考 `media/push_up.png`；关键帧母版 `sources/push_up_keyframes.png`。

以上文件的 SHA-256、尺寸与循环时长记录在 `manifest.json`。预览资源独立于生产动作库的图片与 `exercise_metadata.json`，尚未作为应用的动作媒体绑定。
