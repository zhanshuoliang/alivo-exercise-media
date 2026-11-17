# Round 47 — branded-only edition (2026-11-17)

第 47 批自研动作图，延续带标轨（男/女双版），开源轨仍暂停。15 动作 × 2 = 30 张一次成片审核；`1624` 反握卧推首轮提示词把反握方向写反（输出为普通卧推），修正提示词重发后过审。

## 选取（哑铃 ×5 / 绳索 ×3 / 杠铃 ×3 / 自重 ×4）

| catalogId | slug | 审核 |
|---|---|---|
| exercises-dataset:0437 | dumbbell_upright_row | 2/2 过 |
| exercises-dataset:0382 | dumbbell_revers_grip_biceps_curl | 2/2 过 |
| exercises-dataset:1624 | dumbbell_reverse_bench_press | 重发后 2/2 过 |
| exercises-dataset:0364 | dumbbell_one_arm_wrist_curl | 2/2 过 |
| exercises-dataset:0343 | dumbbell_lying_one_arm_press | 2/2 过 |
| exercises-dataset:0222 | cable_side_bend | 2/2 过 |
| exercises-dataset:1638 | cable_pulldown_bicep_curl | 2/2 过 |
| exercises-dataset:1728 | cable_two_arm_tricep_kickback | 2/2 过 |
| exercises-dataset:0103 | barbell_standing_ab_rollerout | 2/2 过 |
| exercises-dataset:0092 | barbell_seated_overhead_triceps_extension | 2/2 过 |
| exercises-dataset:0094 | barbell_seated_twist | 2/2 过 |
| exercises-dataset:3212 | basic_toe_touch_male | 2/2 过 |
| exercises-dataset:2329 | spine_twist | 2/2 过 |
| exercises-dataset:3669 | standing_archer | 2/2 过 |
| exercises-dataset:1472 | forward_jump | 2/2 过 |

## 返工记录

- `1624`：初版提示词误写 "palms facing toward the feet"（卧推语境下为正握），出图为普通卧推＝已绑近重复。更正为 "palms facing toward the FACE, thumbs toward the feet" 重发，过审。

## 接入

- 男带标 15 张 → 1024px WebP q82/m4，绑定 App 双端：825 → **840**
- 女带标 15 张入 `media/` 备用未绑定；`media/` PNG 总数 **1350**
- `media/NOTICE.md` Round 47 分节 + SHA-256 ×30
- 双端 metadata/NOTICE/PROVENANCE 逐字节一致，无重复 ID/path/hash，webp diff 0
- Flutter `exercise_media_test.dart` 5/5；Node 回归 777/777
