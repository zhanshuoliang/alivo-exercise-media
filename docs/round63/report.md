# Round 63 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（未绑定池经归一化撞名 + 语义排雷 + 步骤核查后选定）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0084 | barbell_rollerout | 跪姿杠铃前滚 |
| exercises-dataset:0170 | cable_incline_fly_on_stability_ball | 球上斜板绳索飞鸟 |
| exercises-dataset:1325 | cable_wide_grip_rear_pulldown_behind_neck | 颈后宽握下拉 |
| exercises-dataset:0197 | cable_pulldown_pro_lat_bar | 标准背阔下拉 |
| exercises-dataset:0226 | cable_standing_crunch | 背向站姿卷腹 |
| exercises-dataset:1724 | cable_rope_high_pulley_overhead_tricep_extension | 背向高位绳索过顶臂屈伸 |
| exercises-dataset:1775 | side_plank_hip_adduction | 侧平板髋内收 |
| exercises-dataset:1278 | dumbbell_incline_fly_on_exercise_ball | 球上斜板哑铃飞鸟 |
| exercises-dataset:1280 | dumbbell_incline_one_arm_fly_on_exercise_ball | 球上单臂斜板飞鸟 |
| exercises-dataset:1283 | dumbbell_incline_press_on_exercise_ball | 球上斜板推举 |
| exercises-dataset:1293 | dumbbell_press_on_exercise_ball | 球上平板推举 |
| exercises-dataset:1618 | dumbbell_incline_hammer_press_on_exercise_ball | 球上锤式推举 |
| exercises-dataset:1292 | dumbbell_one_leg_fly_on_exercise_ball | 单腿球上飞鸟 |
| exercises-dataset:2796 | dumbbell_step_up_lunge | 台阶上步弓步 |
| exercises-dataset:0414 | dumbbell_standing_alternate_overhead_press | 站姿交替过顶推 |

## 审核

30/30 逐张视觉审核通过。重点核对：`1325` 杆落颈后（后视角）与 `0197` 杆拉胸前（前视角）明确区分；`0226`/`1724` 背向站姿；`1293` 球上平板（中背支撑、膝 90°）与 `1283` 球上斜板（上背支撑、髋桥起）体姿可区分；`1618` 中性对握与 `1283` 正握可区分。

## 校验

- 双端 `exercise_metadata.json`：1077 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1077 WebP 各，RIFF/WEBP 魔数全过。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
