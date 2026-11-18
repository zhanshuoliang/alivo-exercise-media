# Round 82 — branded-only edition, gap-fill round (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨补绑批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：用户指定补绑 12 条此前策略性留白记录——10 条辅助动作（`0010`/`0012`/`0013`/`0016`/`1708`/`1709`/`1710`/`1712`/`1714`/`1716`）、黑名单 `3562` 杠铃臀桥、`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`。
- 语义处理：10 条辅助记录按 zh 步骤均为自辅助（阻力带锚踝 / 毛巾拉脚 / 凳侧搭腿 / 瑜伽球坐撑），保持单人构图规范，无需双人破例。`3562` 杠铃臀桥与已绑 `3523` 自重版（`glute_bridge_two_legs_on_bench`）以新 slug `barbell_glute_bridge_two_legs_on_bench` + 画面中可见杠铃区分。`Kettlebell_Halo_With_Overhead_Extension` 与已绑 `Kettlebell_Halo`（胸前持铃）以双臂过顶伸展持铃区分。
- 生成：24 张 PNG（男版 12 + 女版 12），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0010 | assisted_hanging_knee_raise_throwdown | 悬垂举腿向下甩出 |
| exercises-dataset:0012 | assisted_lying_leg_raise_lateral_throwdown | 仰卧举腿侧向下放（手垫臀下） |
| exercises-dataset:0013 | assisted_lying_leg_raise_throwdown | 仰卧举腿直向下放（手垫臀下） |
| exercises-dataset:0016 | assisted_prone_hamstring | 俯卧腘绳肌弯举（阻力带锚踝） |
| exercises-dataset:1708 | assisted_lying_calves_stretch | 仰卧毛巾套脚小腿拉伸 |
| exercises-dataset:1709 | assisted_lying_glutes_stretch | 仰卧 4 字臀肌拉伸（双腿离地抱腿） |
| exercises-dataset:1710 | assisted_lying_gluteus_piriformis_stretch | 仰卧梨状肌拉伸（对侧踩地变体） |
| exercises-dataset:1712 | assisted_side_lying_adductor_stretch | 侧卧上腿搭凳内收肌拉伸 |
| exercises-dataset:1714 | assisted_prone_rectus_femoris_stretch | 俯卧反手拉踝股直肌拉伸 |
| exercises-dataset:1716 | assisted_seated_pec_stretch_ball | 坐瑜伽球双臂后展胸大肌拉伸 |
| exercises-dataset:3562 | barbell_glute_bridge_two_legs_on_bench | 杠铃臀桥（上背撑凳+杠铃置髋） |
| free-exercise-db:Kettlebell_Halo_With_Overhead_Extension | kettlebell_halo_with_overhead_extension | 壶铃绕头接过顶伸展 |

## 审核

24/24 逐张视觉审核通过。重点核对：辅助类 10 张均单人自辅助构图（无第二人入镜）；`3562` 杠铃清晰可见置髋前、上背撑凳髋顶起，与 `3523` 自重版姿态区分；壶铃过顶伸展持铃，与 `Kettlebell_Halo` 胸前持铃区分；`1709`/`1710` 同族 4 字拉伸以支撑腿离地/踩地姿态区分。

## 校验

- 双端 `exercise_metadata.json`：1333 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1333 WebP 各，SHA-256 与记录一致。
- 回归夹具同步更新：原 `3562`「永不绑定」断言改为新绑定断言；`Kettlebell_Halo_With_Overhead_Extension` 分支断言改为新 WebP 路径；「遗留无媒体」夹具改用 curation 排除记录 `exercises-dataset:1371`（im+gf 字段俱全且无其他回归引用）。
- 媒体仓：`media/` 2336 PNG（2312 + 24）；`catalog-review.html` 1352 记录含本轮 12/12。
- 回归：`tests/regression.cjs` 777/777；Flutter exercise-media 测试全过。
