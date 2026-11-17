# Round 61 — branded-only edition (2026-11-17)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：12 个 exercises-dataset 记录（未绑定池经归一化撞名 + 语义排雷 + 步骤核查后选定）。
- 生成：24 张 PNG（男版 12 + 女版 12），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0689 | seated_leg_raise | 凳上坐姿直腿举 |
| exercises-dataset:1364 | standing_pelvic_tilt | 站姿骨盆倾斜 |
| exercises-dataset:0685 | run | 原地跑 |
| exercises-dataset:0696 | self_assisted_inverse_leg_curl_on_floor | 地板自辅助反向腿弯举 |
| exercises-dataset:3132 | potty_squat_with_support | 扶撑深蹲 |
| exercises-dataset:0401 | dumbbell_seated_palms_up_wrist_curl | 坐姿哑铃正握腕弯举 |
| exercises-dataset:2414 | barbell_standing_concentration_curl | 站姿杠铃集中弯举（站姿、无肘支撑，与全部坐姿集中弯举变体可区分） |
| exercises-dataset:0473 | hanging_pike | 悬垂屈体举腿 |
| exercises-dataset:0490 | incline_close_grip_push_up | 上斜窄距俯卧撑 |
| exercises-dataset:1321 | cable_rope_elevated_seated_row | 高位坐姿绳索划船 |
| exercises-dataset:0199 | cable_pushdown_straight_arm_v_2 | 直臂绳索下压 v2 |
| exercises-dataset:1255 | barbell_decline_pullover | 下斜杠铃直臂拉 |

## 审核

24/24 逐张视觉审核通过。`2414` 初筛时曾标记"疑重复"，复核步骤（站姿、一手握杠铃、另一手撑大腿、肘无支撑）与已绑坐姿集中弯举家族（0297/1682/0976/1770/1631/0403）明确不同，确认为独立可绑记录，保留入选。

## 校验

- 双端 `exercise_metadata.json`：1047 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1047 WebP 各，RIFF/WEBP 魔数全过。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：12/12 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
