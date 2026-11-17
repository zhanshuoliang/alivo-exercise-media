# Round 66 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（深蹲站姿/杠位与弯举握距变体、球上绳索组合、自重核心）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:1435 | barbell_low_bar_squat | 低杠深蹲 |
| exercises-dataset:1436 | barbell_high_bar_squat | 高杠深蹲 |
| exercises-dataset:0063 | barbell_narrow_stance_squat | 窄距深蹲 |
| exercises-dataset:0124 | barbell_wide_squat | 宽距深蹲 |
| exercises-dataset:0099 | barbell_single_leg_split_squat | 杠铃分腿蹲 |
| exercises-dataset:0107 | barbell_standing_front_raise_over_head | 站姿前平举过头 |
| exercises-dataset:0106 | barbell_standing_close_grip_curl | 窄握弯举 |
| exercises-dataset:0113 | barbell_standing_wide_grip_curl | 宽握弯举 |
| exercises-dataset:0589 | lever_one_arm_bent_over_row | 器械单臂俯身划船 |
| exercises-dataset:1264 | cable_one_arm_incline_fly_on_exercise_ball | 球上绳索单臂斜板飞鸟 |
| exercises-dataset:1266 | cable_one_arm_incline_press_on_exercise_ball | 球上绳索单臂斜板推举 |
| exercises-dataset:2399 | cable_seated_twist | 绳索坐姿转体 |
| exercises-dataset:0223 | cable_side_crunch | 绳索站姿侧卷腹 |
| exercises-dataset:2429 | frog_crunch | 蛙式卷腹 |
| exercises-dataset:0260 | cocoons | 蚕茧卷腹 |

## 审核

30/30 逐张视觉审核通过。重点核对：`1435` 杠置三角后束低位躯干前倾 vs `1436` 杠置斜方高位躯干直立（杠位差异明确）；`0063` 双脚并拢 vs `0124` 宽站距脚尖外八；`0099` 杠置背上前后分腿（与已绑哑铃版 `0410` 器械区分）；`0107` 杠完全举过头顶；`0106` 双手并拢 vs `0113` 双手近杠端宽距；`0589` 俯身单臂拉杠杆器械另手扶架；`1264`/`1266` 坐球背靠斜凳单臂绳索（与已绑哑铃球上版器械区分）；`2399` 坐姿双臂前伸躯干旋转；`0223` 低滑轮侧向屈曲；`2429` 脚掌相对蛙式腿位；`0260` 抱膝团身紧凑球位。

## 校验

- 双端 `exercise_metadata.json`：1122 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1122 WebP 各，RIFF/WEBP 魔数全过。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
