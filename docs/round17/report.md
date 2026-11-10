# Round 17 — 未覆盖器械补全批（15 动作 × 4 轨 = 60 张）

日期：2026-11-10。选题原则：补齐此前完全未配图或基本未配图的器械类别——EZ 杠、负重（负重片变体）、雪橇机（腿举/哈克深蹲）、resistance band 坐姿系列、BOSU 球、泡沫轴、大锤、奥林匹克杠。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:1749 | ez bar standing french press | ez barbell |
| exercises-dataset:1344 | ez bar reverse grip bent over row | ez barbell |
| exercises-dataset:0451 | ez barbell reverse grip curl | ez barbell |
| exercises-dataset:0445 | ez barbell anti gravity press | ez barbell |
| exercises-dataset:0830 | weighted bench dip | weighted |
| exercises-dataset:0834 | weighted front raise | weighted |
| exercises-dataset:0835 | weighted hyperextension (on stability ball) | weighted |
| exercises-dataset:1463 | sled 45° leg press (side pov) | sled machine |
| exercises-dataset:0741 | sled closer hack squat | sled machine |
| exercises-dataset:3123 | resistance band seated biceps curl | resistance band |
| exercises-dataset:3124 | resistance band seated chest press | resistance band |
| exercises-dataset:1307 | push up on bosu ball | bosu ball |
| exercises-dataset:2204 | roller body saw | roller |
| exercises-dataset:1496 | sledge hammer | hammer |
| exercises-dataset:0636 | olympic barbell hammer curl | olympic barbell |

## 产出（60/60 一次过审）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端（HarmonyOS `entry/` + Flutter `mobile/`），绑定数 378 → 393
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` + `<base>_female.png` ×30：纯提示词独立生成（无参考图），CC-BY-4.0，`media-open/manifest.json` 210 → 240

## 文档与校验

- 提示词归档：`prompts_m/`、`prompts_f/`（含 -i 风格参考指令）、`prompts_open_m/`、`prompts_open_f/`（纯提示词）
- `plan_round17.json`（15 条 catalogId↔base 映射）、`batch_round17.json`（add_bindings 输入）
- `media/NOTICE.md`、`media-open/NOTICE.md` 各追加 Round 17 分节，30 条 SHA-256
- 回归：Node 全量 840 通过 / 2 失败（`coach-postgres` 需 SSH host 参数、`terrain-preview` 预存 manifest hash 不符，均与本批无关）；Flutter `exercise_media_test.dart` 5/5
