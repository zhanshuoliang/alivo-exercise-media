# Round 23 — 史密斯机首发批（15 动作 × 4 轨 = 60 张）

日期：2026-11-12。选题原则：首次覆盖 smith machine 器械桶 + 壶铃划船/推举补全 + EZ 杠与雪橇/负重收尾件。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:0766 | smith shoulder press | smith machine |
| exercises-dataset:0767 | smith shrug | smith machine |
| exercises-dataset:3281 | smith full squat | smith machine |
| exercises-dataset:1360 | smith one arm row | smith machine |
| exercises-dataset:1393 | smith one leg floor calf raise | smith machine |
| exercises-dataset:0518 | kettlebell alternating hang clean | kettlebell |
| exercises-dataset:0527 | kettlebell double jerk | kettlebell |
| exercises-dataset:1345 | kettlebell two arm row | kettlebell |
| exercises-dataset:0522 | kettlebell alternating row | kettlebell |
| exercises-dataset:0540 | kettlebell one arm push press | kettlebell |
| exercises-dataset:0453 | ez barbell seated triceps extension | ez barbell |
| exercises-dataset:2741 | ez-barbell standing wide grip biceps curl | ez barbell |
| exercises-dataset:0452 | ez barbell reverse grip preacher curl | ez barbell |
| exercises-dataset:1464 | sled 45° leg press back pov | sled machine |
| exercises-dataset:0847 | weighted seated bicep curl on stability ball | weighted (catalog bucket: medicine ball) |

## 产出（60/60 一次过审，无返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端，绑定数 465 → 480
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` + `<base>_female.png` ×30：纯提示词独立生成（无参考图），CC-BY-4.0，`media-open/manifest.json` 388 → 418

## 审核要点

- 史密斯机五件（器械桶首次覆盖）：坐姿肩推（导轨内坐姿杆推过头）、站姿耸肩（双臂直持杆耸肩）、全蹲（杆扛斜方肌深蹲底部）、单臂划船（俯身单臂从低位杆划船）、坐姿单腿提踵（杆压膝上、前掌踩杠片垫高跖屈——四轨均以双腿同步踩片呈现，动作主体识别无误，特此注明）。
- 壶铃五件：交替悬垂翻（单臂收位持铃于肩，交替半程定格）、双挺举（屈膝助力双铃过头锁定）、双臂划船（俯身双壶铃收肘）、交替划船（一侧收肘一侧悬垂，交替相位清晰）、单臂借力推（单臂过头锁定+屈膝助力、对侧臂后摆平衡）。
- EZ 杠三件：坐姿过头臂屈伸（EZ 曲杆落头后肘屈）、站姿宽握弯举（宽握曲杆中程）、反握牧师凳弯举（斜面垫+反握曲杆，掌心朝下清晰）。
- 雪橇一件：45° 腿举背视角（挂片斜蹬机+双腿蹬伸，背视角按目录名呈现）。
- 负重一件：坐姿稳定球弯举（坐于瑜伽球、双手持药球弯举中程——目录 equipment 桶标注 medicine ball，按目录解读以药球负重呈现）。
- 全 60 张均为单帧编辑插图，无拼图/多画面；带标轨单一 ALIVO 字标，开源轨完全无标识。

## 归档

- `plan_round23.json` / `batch_round23.json`：目标、文件名、绑定清单（15 条，无重复条目冲突）。
- `prompts_m/`、`prompts_f/`、`prompts_open_m/`、`prompts_open_f/`：四轨逐图完整提示词（各 15 份）。

## 回归

- Flutter 媒体测试 5/5；Node 文件级回归仅 3 项已知失败（`coach-postgres`、`sync-postgres` 需 SSH host 参数的手动集成测试；`terrain-preview` 预存 manifest hash 不符，与媒体无关）。
