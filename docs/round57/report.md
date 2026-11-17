# Round 57 — 带标轨批次报告（2026-11-17）

## 概况

- 目标：1352 条带标绑定中的第 57 批，15 个动作 × 男女双轨 = 30 张带标 PNG。
- 进度：**975 → 990 / 1352**。
- 开源轨本轮继续暂停（独立后续阶段），media-open 维持 688 项。

## 选题与排雷

哑铃 ×5、绳索 ×4、杠铃 ×2、自重 ×4，全部对照已绑 975 条做过近重复筛查：

| catalogId | 动作 | 桶 |
|---|---|---|
| exercises-dataset:1674 | dumbbell prone incline hammer curl | dumbbell |
| exercises-dataset:1680 | dumbbell standing one arm curl over incline bench | dumbbell |
| exercises-dataset:0369 | dumbbell over bench wrist curl | dumbbell |
| exercises-dataset:1441 | dumbbell over bench one arm reverse wrist curl | dumbbell |
| exercises-dataset:0366 | dumbbell over bench one arm neutral wrist curl | dumbbell |
| exercises-dataset:1263 | cable one arm fly on exercise ball | cable |
| exercises-dataset:0213 | cable seated high row (v-bar) | cable |
| exercises-dataset:0234 | cable standing row (v-bar) | cable |
| exercises-dataset:1637 | cable overhead curl on exercise ball | cable |
| exercises-dataset:0058 | barbell lying lifting (on hip) | barbell |
| exercises-dataset:0096 | barbell side bent v. 2 | barbell |
| exercises-dataset:3019 | bench pull-ups | bodyweight |
| exercises-dataset:1275 | drop push up | bodyweight |
| exercises-dataset:3582 | lunge with jump | bodyweight |
| exercises-dataset:1466 | twist hip lift | bodyweight |

候选 `0338`（dumbbell lying elbow press）在排雷阶段被剔除：与已绑哑铃仰卧三头伸展近重复。

## 生成与审核

- 首轮 30/30 全部出图，无缺失、无疑似文件。
- 视觉审核两项返工：
  - `3562` 双轨：首版双脚在地面，与 `0058` 呈现几乎一致；按"双脚踩在凳面做臀桥"重写提示词后重发通过。
  - `1466` 双轨：首版为普通臀桥无可见扭转且与已绑 `1422` 骨盆桥近似；加强扭转语义（双膝同侧倒）后重发通过。
- 其余 13 组一次过审。

## 换绑（3562 → 0096）

首轮接入后主仓回归套件判定 `exercises-dataset:3562` 失败：`tests/regression.cjs` 显式断言该目录身份**必须保持未绑定**（"the conflicting hip-thrust catalog identity remains unbound"——它是 `alivo:extra-015` 杠铃臀推与已绑 `3523` 的冲突重复身份）。处理：

- 摘除 `3562` 在两端 `exercise_metadata.json`、`NOTICE.md`、`PROVENANCE.csv` 与 `exercise_media_test.dart` 的全部绑定记录，删除两个 webp；
- 媒体仓删除其双轨 PNG 并修正 Round 57 NOTICE 段；
- 以 `0096`（barbell side bent v. 2）替补，双轨生成一次过审，接入后回到 990/1352，回归全过。

## 接入结果

- 男版 15 张转 1024px WebP q82，写入 HarmonyOS `entry/src/main/resources/rawfile/exercise_media/` 与 Flutter `mobile/alivo_app/assets/catalog/exercise_media/`。
- 两端 `exercise_metadata.json`、`NOTICE.md`、`PROVENANCE.csv` 同步追加，SHA-256 已记录；双端逐字节一致（990 webp 零差异）。
- 女版 15 张仅入媒体仓 `media/`（未绑定 App）。
- `media/` 目录累计 1650 张 PNG。
- `catalog-review.html` 已重建（1352 条），本轮 15 条全部标记为已绑定；`3562` 保持未绑定。

## 验证

- 双端记录数：990 / 990，元数据、NOTICE、PROVENANCE 逐字节一致。
- Flutter 媒体测试与主仓回归套件见本轮提交前执行记录。
