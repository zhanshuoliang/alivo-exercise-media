# 第十轮媒体扩充报告（2026-11-10）

## 概要

- **双版本授权自本轮确立**：
  - `media/`：带 ALIVO 字标版，`ALIVO-editorial` 许可，可自由使用，App 两端生产绑定。
  - `media-open/`：无字标开源版，`CC-BY-4.0` 许可，作者 `Paul Leung`，使用须署名；独立发行物，不进 App bundle、不写 `exercise_metadata.json`。
- 本轮目标 30 项（plan.json），带标版全部绑定（总数 213→243），同批无标版全部过审入 `media-open/`（首批 30 张）。
- 新绑定记录 `author: Paul Leung`；旧 213 条 `author: ALIVO` 历史不改写。

## 带标版接入（主仓库 `9d25a98`）

30 张一次全部接入，清单 `bindings.json`，审计脚本 `audit_round10.cjs`：

- 审计：total=243、priorPreserved=213、newCount=30、两端字节相同、metadata/NOTICE 一致、SHA-256 全部有效、新文件与审核稿一致。
- Node 回归 774/774，Flutter 媒体测试 5/5。
- 基线 `media-baseline-213.json`。

## 无标版生成（`media-open/`）

- 提示词模板：与带标版相同的场景/服装/光照描述，但服装改为“plain/纯色”，并显式禁止一切文字、字母、字标、标志、水印（`prompts/exec_*.txt`）。
- **不使用带标参考图**（纯提示词生成），避免参考图上的 ALIVO 字标泄漏到画面。
- 30/30 首稿过审（flutter_kicks、sissy_squat 首次连接失败后重试成功）。
- `media-open/manifest.json`：30 条 catalogId + file + author + license + licenseUrl + SHA-256 + reviewedAt。
- `media-open/NOTICE.md`：许可与署名说明 + 逐文件 SHA-256 表。

## 本轮 30 项目标

0028 barbell clean and press；3305 barbell thruster；0067 barbell one-arm snatch；3888 dumbbell one-arm snatch；0542 kettlebell one-arm snatch；0537 kettlebell one-arm clean and jerk；0544 kettlebell pistol squat；1471 inchworm；3419 L-sit on floor；2459 tire flip；0680 rope climb；3662 cobra push-up；1468 crab toe touch；0459 flutter kicks；1014 band V-up；0826 parallel-bar leg raise；0859 wrist roller；0038 barbell drag curl；0454 EZ-bar spider curl；0354 dumbbell kickback；1489 sissy squat；1705 BOSU squat；2141 elliptical；2142 SkiErg；3666 incline treadmill；2311 stepmill；0798 stationary bike；1302 medicine-ball chest pass；0020 balance board；3219 scissor jump。

## 待办

- 旧 213 条带标图的无标版需分轮补齐（media-open 逐轮增长）。
- 审查页如需 media-open 预览可后续加开关。
