# Round 33 — branded-only 批次报告

日期：2026-11-17
规模：15 个动作 × 2 轨（男带标 + 女带标）= 30 张
策略变更：本轮起暂停开源轨生成，专注带标绑定；开源版缺口待后续独立补生成。

## 选题

未绑定池 728 条（排除 8 个已知问题 ID）。器械配比：绳索 ×5 + 杠杆机 ×5 + 杠铃 ×3 + 哑铃 ×2。

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:0158 | cable decline fly | cable |
| exercises-dataset:0169 | cable incline bench press | cable |
| exercises-dataset:1318 | cable incline bench row | cable |
| exercises-dataset:0168 | cable hip adduction | cable |
| exercises-dataset:0152 | cable concentration extension on knee | cable |
| exercises-dataset:2285 | lever pullover | leverage machine |
| exercises-dataset:0583 | lever kneeling twist | leverage machine |
| exercises-dataset:0593 | lever reverse hyperextension | leverage machine |
| exercises-dataset:1452 | lever seated crunch | leverage machine |
| exercises-dataset:2286 | lever hip extension v. 2 | leverage machine |
| exercises-dataset:0048 | barbell incline reverse-grip press | barbell |
| exercises-dataset:0049 | barbell incline row | barbell |
| exercises-dataset:1370 | barbell floor calf raise | barbell |
| exercises-dataset:1437 | dumbbell finger curls | dumbbell |
| exercises-dataset:1732 | dumbbell forward lunge triceps extension | dumbbell |

排除备忘：`0591`（≈已绑 1451）、`2736`（≈0579）、`1722`（≈0194）、`0024`（≈0029/0042）、`0034`（≈1316）、`0036`（≈0033）。

## 生成

- 带标轨沿用参考图风格锚定：男 `media/handstand_male.png`、女 `media/handstand_female.png`（风格参考，不复制姿势）。
- 单波 30 任务一次跑完，30/30 日志路径齐全，零网络错误。
- 收集：`collect33.cjs` → `stage33_m/`、`stage33_f/`，30/30 无缺失无可疑。

## 审核

逐组视觉审查 15 组 × 2 轨：**30/30 过审，1 组重发**。

- `0048` barbell incline reverse-grip press：首版两轨误画成正握（overhand），与 reverse-grip 不符。提示词强化为 SUPINATED underhand（掌心朝上托杆）后重发，两轨均正确（掌心朝上、手指杆下包绕）。重试日志 `logs33_* /exec_0048_retry.log`。

## 入库

- `media/` +30（男带标母版 15 + 女带标 15）→ 累计 **930 PNG**
- `media/NOTICE.md` Round 33 分节（幂等追加，含 SHA-256）
- 男带标 15 张已按迁移规格打包（1024px WebP q82/m4）绑定 App 双端：绑定数 **615 → 630**
- `media-open/` 本轮无新增（开源轨暂停）

## 回归

- Node `tests/regression.cjs`：见主仓日志
- Flutter `test/exercise_media_test.dart`：见主仓日志
- 双端 WebP 逐字节一致 15/15，无重复 catalogId/localPath/sha256
