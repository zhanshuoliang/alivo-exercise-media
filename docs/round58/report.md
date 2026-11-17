# Round 58 — branded-only edition（2026-11-17）

## 结果

- 选题 15 个 catalog 记录（哑铃×6、绳索×2、杠铃×1、自重×6），全部为此前未绑定且无归一化/语义撞名。
- 每题生成 Kai（男）/ Liv（女）双轨带标 PNG，共 30 张，全部一次过审、零返工。
- 男版 15 张转 1024px WebP q82 绑定入 App 双端目录；女版 15 张入 `media/` 备用、未绑定。
- 开源轨本轮暂停（沿用第 33 轮起的带标优先策略），`media-open/` 维持 688 项不变。

## 绑定清单（男版 → App）

| catalogId | slug |
|---|---|
| exercises-dataset:0349 | dumbbell_lying_supination |
| exercises-dataset:2705 | dumbbell_lying_pronation_on_floor |
| exercises-dataset:1415 | dumbbell_one_arm_seated_neutral_wrist_curl |
| exercises-dataset:1670 | dumbbell_one_arm_standing_curl |
| exercises-dataset:2805 | dumbbell_single_leg_deadlift_with_stepbox_support |
| exercises-dataset:0403 | dumbbell_seated_revers_grip_concentration_curl |
| exercises-dataset:1267 | cable_one_arm_press_on_exercise_ball |
| exercises-dataset:1268 | cable_press_on_exercise_ball |
| exercises-dataset:0110 | barbell_standing_reverse_grip_curl |
| exercises-dataset:0467 | gorilla_chin |
| exercises-dataset:1774 | side_bridge_hip_abduction |
| exercises-dataset:0642 | outside_leg_kick_push_up |
| exercises-dataset:1421 | modified_push_up_to_lower_arms |
| exercises-dataset:1687 | posterior_step_to_overhead_reach |
| exercises-dataset:3552 | quick_feet_v_2 |

## 审核记录

- 30/30 一次过审：语义动作、构图、解剖、ALIVO 字标、无多余文字均合格。
- 重点复核项：0110 反握（拳眼朝上清晰）、0467 猩猩引体（脚间夹铃）、1774 侧桥外展（上腿高抬）、1421 落臂平板、3552 快速踏步动态。
- `exercises-dataset:3562` 继续按回归黑名单保持未绑定，本轮未触碰。

## 验证

- 两端 `exercise_metadata.json` 均为 1005 条、逐字节一致；NOTICE/PROVENANCE 一致；webp 双端零差异；无重复 catalogId/localPath。
- `media/` 入库后 1680 张 PNG（+30）。
- 回归测试与 Flutter 媒体测试随主仓提交前跑通（结果见主仓提交说明）。
