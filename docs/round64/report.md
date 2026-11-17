# Round 64 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（未绑定池经归一化撞名 + 语义排雷 + 步骤核查后选定）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0034 | barbell_decline_bent_arm_pullover | 下斜弯臂杠铃套头拉 |
| exercises-dataset:0036 | barbell_decline_wide_grip_press | 下斜宽握杠铃推 |
| exercises-dataset:0177 | cable_lateral_pulldown_with_rope_attachment | 绳索背阔下拉 |
| exercises-dataset:1287 | dumbbell_one_arm_decline_chest_press | 下斜单臂哑铃推胸 |
| exercises-dataset:1289 | dumbbell_one_arm_incline_chest_press | 上斜单臂哑铃推胸 |
| exercises-dataset:1282 | dumbbell_incline_one_arm_press_on_exercise_ball | 球上单臂斜板推举 |
| exercises-dataset:1621 | dumbbell_one_arm_hammer_press_on_exercise_ball | 球上单臂锤式推举 |
| exercises-dataset:1290 | dumbbell_one_arm_press_on_exercise_ball | 球上单臂坐姿推举 |
| exercises-dataset:1286 | dumbbell_one_arm_chest_fly_on_exercise_ball | 球上单臂飞鸟 |
| exercises-dataset:1331 | dumbbell_reverse_grip_incline_bench_two_arm_row | 上斜反握双臂划船 |
| exercises-dataset:1330 | dumbbell_reverse_grip_incline_bench_one_arm_row | 上斜反握单臂划船 |
| exercises-dataset:0635 | oblique_crunches_floor | 地板斜卷腹 |
| exercises-dataset:0491 | incline_leg_hip_raise | 上斜凳直腿髋举 |
| exercises-dataset:0727 | single_leg_calf_raise_on_a_dumbbell | 踩哑铃单腿提踵 |
| exercises-dataset:3211 | kneeling_push_up | 跪姿俯卧撑 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0034` 头低凳弯臂落杠头后与 `0036` 头低凳宽握推举明确区分；`1282` 球上斜板（上背支撑髋桥起）、`1621`/`1290` 球上直坐（锤式中性握 vs 正握）与 `1286` 球上飞鸟（单臂展开）姿态各异；`1331`/`1330` 胸贴上斜凳反握划船单双臂区分；`3211` 膝触地小腿翘起与标准俯卧撑可区分；`0727` 前掌踩哑铃提踵顶点明确。

## 校验

- 双端 `exercise_metadata.json`：1092 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1092 WebP 各，RIFF/WEBP 魔数全过。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
