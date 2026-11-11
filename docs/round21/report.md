# Round 21 — 瑜伽球/壶铃批（15 动作 × 4 轨 = 60 张）

日期：2026-11-11。选题原则：继续补未绑定的核心训练 + 壶铃/药球/BOSU/雪橇收尾件。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:0014 | assisted motion russian twist | assisted / medicine ball |
| exercises-dataset:1304 | medicine ball chest push multiple response | medicine ball |
| exercises-dataset:0653 | push-up on BOSU ball | bosu ball |
| exercises-dataset:1335 | exercise ball back extension with knees off ground | stability ball |
| exercises-dataset:1336 | exercise ball back extension with rotation | stability ball |
| exercises-dataset:1343 | exercise ball prone leg raise | stability ball |
| exercises-dataset:1707 | prone twist on stability ball | stability ball |
| exercises-dataset:0650 | pull-in on stability ball | stability ball |
| exercises-dataset:0524 | kettlebell bent press | kettlebell |
| exercises-dataset:0535 | kettlebell hang clean | kettlebell |
| exercises-dataset:0538 | kettlebell one arm jerk | kettlebell |
| exercises-dataset:0546 | kettlebell seated press | kettlebell |
| exercises-dataset:1438 | kettlebell seated two arm military press | kettlebell |
| exercises-dataset:1392 | sled one-leg calf press on leg press | sled machine |
| exercises-dataset:1338 | exercise ball hug | stability ball |

## 产出（60/60 一次过审，无返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端，绑定数 436 → 451
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` + `<base>_female.png` ×30：纯提示词独立生成（无参考图），CC-BY-4.0，`media-open/manifest.json` 330 → 360

## 审核要点

- 核心/球上六件：药球俄罗斯转体（坐姿后倾持球转体）、球上背伸展膝离地（脚抵墙成直线）、旋转背伸展（顶点转体髋稳定）、球上俯卧抬腿（手撑地直腿后抬）、俯卧扭转（球上旋转顶点）、坐姿拉膝（手撑球侧收膝）。
- 抱球后仰：坐姿持球贴胸后仰保持核心张力。
- 壶铃五件：俯身推举（过头持铃+对侧屈旋转）、悬垂翻（髋膝伸展翻收至肩）、单臂挺举（屈膝助力推至锁定）、坐姿单臂推举、坐姿双臂军事推举（双铃过头锁定）。
- BOSU 俯卧撑：平台朝上抓外沿俯卧撑中程。
- 雪橇单腿提踵：腿举机单前掌压板跖屈位。
- 全 60 张均为单帧编辑插图，无拼图/多画面；带标轨单一 ALIVO 字标，开源轨完全无标识。

## 归档

- `plan_round21.json` / `batch_round21.json`：目标、文件名、绑定清单。
- `prompts/male/`、`prompts/female/`、`prompts/open_male/`、`prompts/open_female/`：四轨逐图完整提示词（各 15 份）。

## 回归

- Flutter 媒体测试 5/5；Node 文件级回归仅 3 项已知失败（`coach-postgres`、`sync-postgres` 需 SSH host 参数的手动集成测试；`terrain-preview` 预存 manifest hash 不符，与媒体无关）。
