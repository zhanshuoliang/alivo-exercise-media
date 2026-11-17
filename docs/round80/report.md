# Round 80 — branded-only edition, final round (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨收官批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：最后 4 个可绑 exercises-dataset 记录（卷腹、三凳臂屈伸、单凳屈膝臂屈伸、单凳直腿臂屈伸）。三条凳臂屈伸同文记录以凳数/腿位区分各自独立 slug 绑定。
- 生成：8 张 PNG（男版 4 + 女版 4），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 收官盘点：本轮后 1352 目录中全部可绑记录绑定完毕（1321 条）。永久未绑定：10 条双人辅助拉伸（`0010`/`1708`/`1709`/`1710`/`0012`/`0013`/`0016`/`1714`/`1716`/`1712`）、`3562` 黑名单、19 条 curation 排除的同文/v.2/v.3 副本（`0077`/`1371`/`0119`/`0121`/`0125`/`1731`/`1657`/`0304`/`0309`/`0312`/`0317`/`0360`/`2292`/`0395`/`0420`/`0432`/`0497`/`0656`/`1394`）。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:3016 | curl_up | 卷腹起身（手抱头 45°） |
| exercises-dataset:1753 | three_bench_dip | 三凳臂屈伸（手一凳+脚搭二凳） |
| exercises-dataset:0814 | triceps_dip | 单凳臂屈伸（屈膝脚掌着地） |
| exercises-dataset:0812 | triceps_dip_bench_leg | 单凳臂屈伸（双腿伸直跟着地） |

## 审核

8/8 逐张视觉审核通过。重点核对：`3016` 手抱头躯干卷至 45°（与 `3203` 半程同幅度、slug 独立；与 `0001` 全程相位一致但为独立记录各绑各图）；`1753` 双手撑一凳双脚搭二凳身体悬空（与 `0813` 双凳/`0814`/`0812` 凳数腿位区分）；`0814` 单凳屈膝脚掌着地背贴凳下放（与 `0812` 直腿腿位区分）；`0812` 双腿伸直仅跟着地（与 `0814` 屈膝腿位区分）。

## 校验

- 双端 `exercise_metadata.json`：1321 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1321 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定；本轮 4 条均不在 curation 排除清单。
- 媒体仓：`media/` 2312 PNG（2304 + 8）；`catalog-review.html` 1352 记录含本轮 4/4。
- 回归：`tests/regression.cjs` 777/777；Flutter exercise-media 测试全过。
