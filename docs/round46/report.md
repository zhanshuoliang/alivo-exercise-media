# Round 46 — branded-only edition (2026-11-17)

连续第八轮 **30/30 一次过审，零返工**。带标轨批次（开源轨暂停，688 不变）。

## 批次（15 动作 × 男/女双轨 = 30 张）

| catalogId | 动作 | 器械 | 审核 |
|---|---|---|---|
| exercises-dataset:3541 | dumbbell incline y-raise | dumbbell | 2/2 pass |
| exercises-dataset:1658 | dumbbell lunge with bicep curl | dumbbell | 2/2 pass |
| exercises-dataset:2470 | dumbbell lying on floor rear delt raise | dumbbell | 2/2 pass |
| exercises-dataset:0358 | dumbbell one arm reverse wrist curl | dumbbell | 2/2 pass |
| exercises-dataset:1414 | dumbbell one arm reverse preacher curl | dumbbell | 2/2 pass |
| exercises-dataset:1476 | one leg squat (pistol) | body weight | 2/2 pass |
| exercises-dataset:1366 | upward facing dog | body weight | 2/2 pass |
| exercises-dataset:3012 | scapula dips | body weight | 2/2 pass |
| exercises-dataset:0699 | shoulder tap push-up | body weight | 2/2 pass |
| exercises-dataset:0220 | cable shrug | cable | 2/2 pass |
| exercises-dataset:2464 | cable thibaudeau kayak row | cable | 2/2 pass |
| exercises-dataset:0874 | cable standing crunch (rope) | cable | 2/2 pass |
| exercises-dataset:0100 | barbell skier | barbell | 2/2 pass |
| exercises-dataset:0087 | barbell seated bradford/rocky press | barbell | 2/2 pass |
| exercises-dataset:0786 | squat jerk | barbell | 2/2 pass |

器械分布：dumbbell ×5 / body weight ×4 / cable ×3 / barbell ×3。

## 候选筛选备注

- 小桶（leverage/smith/band/ball/weighted/kettlebell/assisted）本轮扫尽：余项全部 v2/v3 近重复、已绑定变体或搁置双人项，无新增可用。
- 排除的近重复：`0340` lying hammer press（≈ neutral grip bench press 已绑）、`0260` cocoons（≈ crunch floor 已绑）、`1545` zercher（已绑）、`0110` reverse curl（已绑）、`3562` glute bridge（已绑）、`0115` stiff-leg good morning（已绑变体）。
- `0339` lying femoral 步骤语义含糊（哑铃放下腹部拉向臀）→ 跳过。
- 差异化补入：pistol squat、上犬式、肩胛臂屈伸、拍肩俯卧撑、皮艇划船、Bradford 前后推、下蹲挺、滑雪者。

## 接入

- 男带标绑定 App 双端：810 → **825**（61.0%），15 张 WebP 1024px q82/m4，HarmonyOS 与 Flutter 逐字节一致
- metadata / NOTICE / PROVENANCE / exercise_media_test.dart 双端同步，无重复 ID/path/hash
- 男母版 + 女带标入库：`media/` **1320** PNG
- `media/NOTICE.md` Round 46 分节（男绑定 + 女备用各 15 行，含 PNG SHA-256）

## 回归

- Node 回归 777/777；Flutter exercise-media tests 5/5
- catalog-review.html 重建，1,352 条全量渲染，15/15 新绑定记录就位
