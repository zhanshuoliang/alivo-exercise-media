# Round 45 — branded-only edition (2026-11-17)

连续第七轮 **30/30 一次过审，零返工**。带标轨批次（开源轨暂停，688 不变）。

## 批次（15 动作 × 男/女双轨 = 30 张）

| catalogId | 动作 | 器械 | 审核 |
|---|---|---|---|
| exercises-dataset:0329 | dumbbell incline shrug | dumbbell | 2/2 pass |
| exercises-dataset:3542 | dumbbell incline T-raise | dumbbell | 2/2 pass |
| exercises-dataset:0332 | dumbbell iron cross | dumbbell | 2/2 pass |
| exercises-dataset:0335 | dumbbell lateral to front raise | dumbbell | 2/2 pass |
| exercises-dataset:1328 | dumbbell lying rear delt row | dumbbell | 2/2 pass |
| exercises-dataset:0624 | march sit (wall) | body weight | 2/2 pass |
| exercises-dataset:0555 | kick out sit | body weight | 2/2 pass |
| exercises-dataset:3288 | korean dips | body weight | 2/2 pass |
| exercises-dataset:3011 | incline scapula push-up | body weight | 2/2 pass |
| exercises-dataset:1636 | cable overhead curl | cable | 2/2 pass |
| exercises-dataset:0206 | cable reverse curl | cable | 2/2 pass |
| exercises-dataset:1723 | cable one-arm tricep pushdown | cable | 2/2 pass |
| exercises-dataset:0776 | snatch pull | barbell | 2/2 pass |
| exercises-dataset:0248 | cambered bar lying row | barbell | 2/2 pass |
| exercises-dataset:0035 | barbell decline close grip to skull press | barbell | 2/2 pass |

器械分布：dumbbell ×5 / body weight ×4 / cable ×3 / barbell ×3。

## 接入

- 男带标绑定 App 双端：795 → **810**（59.9%），15 张 WebP 1024px q82/m4，HarmonyOS 与 Flutter 逐字节一致
- metadata / NOTICE / PROVENANCE / exercise_media_test.dart 双端同步，无重复 ID/path/hash
- 男母版 + 女带标入库：`media/` **1290** PNG
- `media/NOTICE.md` Round 45 分节（男绑定 + 女备用各 15 行，含 PNG SHA-256）

## 候选筛选备注

- 杠铃桶接近饱和，挑选语义差异化动作：snatch pull（宽握爆发拉）、cambered bar lying row（弯杆俯卧划船）、decline close-grip skull press（下斜窄握颅骨推）
- 自重补入差异化动作：靠墙踏步坐、踢出坐、韩式臂屈伸（身后单杠支撑）、上斜肩胛俯卧撑

## 回归

- Node 回归 777/777；Flutter exercise-media tests 5/5
- catalog-review.html 重建，1,352 条全量渲染，15/15 新绑定记录就位
