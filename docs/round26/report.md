# Round 26 — 辅助/史密斯/弹力带/负重批（15 动作 × 4 轨 = 60 张）

日期：2026-11-16。选题原则：辅助类首次覆盖（均可单人呈现）+ 史密斯机续补 + 弹力带收尾补 + 负重双件。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:0011 | assisted hanging knee raise | assisted |
| exercises-dataset:1758 | assisted sit-up | assisted |
| exercises-dataset:0018 | assisted standing triceps extension with towel | assisted |
| exercises-dataset:1259 | behind head chest stretch | assisted |
| exercises-dataset:1713 | assisted prone lying quads stretch | assisted |
| exercises-dataset:0749 | smith bent knee good morning | smith machine |
| exercises-dataset:1434 | smith low bar squat | smith machine |
| exercises-dataset:1361 | smith reverse grip bent over row | smith machine |
| exercises-dataset:1683 | smith machine bicep curl | smith machine |
| exercises-dataset:0768 | smith single leg split squat | smith machine |
| exercises-dataset:0968 | band alternating biceps curl | band |
| exercises-dataset:0978 | band front raise | band |
| exercises-dataset:1022 | band standing rear delt row | band |
| exercises-dataset:0853 | weighted standing curl | weighted |
| exercises-dataset:0856 | weighted svend press | weighted |

选题备注：assisted 桶仅选可单人呈现的动作（凳缘压脚/毛巾自拉/自拉伸），未引入第二人；`0530`、`0656` 延续排除（近重复/重复条目）。

## 产出（60/60 过审，4 轨返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端，绑定数 510 → 525
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` ×15 / `media-open/<base>_female.png` ×15：纯提示词独立生成（无参考图），无字标
- manifest：478 → **508**；`media/` 690 → **720** PNG

## 返工与插曲

- `1361` 男带标、`0968`/`1022` 女带标、`1713` 开源男版：imagegen 连接错误，重试后出图通过
- `1758` 开源男版：任务静默超时（重连失败无 PNG 路径），收集器误把诊断目录清单里的他任务图当作产出；重发后正确出图通过
- 收集器缺陷记录：失败日志内含 `generated_images` 目录转储，"取最后 .png 路径"策略会拾取他任务产物。本轮已全靠目检兜底，后续收集应只认本任务会话目录

## App 端格式迁移适配

本轮接入时主仓工作区正进行 PNG→WebP 打包迁移（未提交）。Round 26 绑定按新规格写入：`resize 1024px + lossy WebP quality 82`，`localPath` 用 `.webp`，`sha256` 记打包后哈希，并追加 `PROVENANCE.csv` 行（原始 PNG sha + 打包 sha + 字节数）。`media/` 与 `media-open/` 媒体库仍存 PNG 母版，不受影响。

## 审核记录

60 张逐张目检：动作/器械/姿态/解剖/字标（带标轨恰一处 ALIVO 小字标；开源轨无任何文字商标）全部合规。0011 开源男版多出悬吊辅助带，贴合 assisted 语义，判过。

## 验证

- 双端 `exercise_metadata.json` 一致，media 记录 510 → 525
- 双端 `exercise_media/` 各 525 webp，15 张新文件逐字节一致
- `PROVENANCE.csv` 510 → 525 行；双端 NOTICE 追加 Round 26 分节（15+15 / 30 条 SHA-256）
- Flutter 测试 5/5；Node 文件级回归仅 3 项已知失败（coach-postgres/sync-postgres 需 SSH 参数；terrain-preview 预存 hash 不符）
- 审查页重建（1352 记录），r26 四版本字段全部就位
