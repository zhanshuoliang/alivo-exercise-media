# Round 22 — 壶铃/雪橇/球上收尾批（15 动作 × 4 轨 = 60 张）

日期：2026-11-11。选题原则：继续补未绑定的壶铃进阶动作 + 雪橇机/稳定球/药球/EZ 杠/负重收尾件。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:1332 | exercise ball alternating arm ups | stability ball |
| exercises-dataset:1416 | exercise ball one leg prone lower body rotation | stability ball |
| exercises-dataset:0656 | push-up (on stability ball) | stability ball |
| exercises-dataset:0738 | sled 45° calf press | sled machine |
| exercises-dataset:0744 | sled lying squat | sled machine |
| exercises-dataset:1312 | medicine ball chest push with run release | medicine ball |
| exercises-dataset:0517 | kettlebell advanced windmill | kettlebell |
| exercises-dataset:0523 | kettlebell Arnold press | kettlebell |
| exercises-dataset:0528 | kettlebell double push press | kettlebell |
| exercises-dataset:0553 | kettlebell two arm military press | kettlebell |
| exercises-dataset:0536 | kettlebell lunge pass through | kettlebell |
| exercises-dataset:1747 | EZ bar French press on exercise ball | ez barbell + stability ball |
| exercises-dataset:1628 | EZ barbell spider curl | ez barbell |
| exercises-dataset:0846 | weighted russian twist | weighted |
| exercises-dataset:0852 | weighted squat | weighted |

## 产出（60/60 一次过审，无返工）

- `media/<base>_male.png` ×14：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端，绑定数 451 → 465
- `media/<base>_female.png` ×14：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` + `<base>_female.png` ×28：纯提示词独立生成（无参考图），CC-BY-4.0，`media-open/manifest.json` 360 → 388
- 例外：`exercises-dataset:0656`（push-up on stability ball）生成后发现与 `exercises-dataset:0655` 为**内容完全重复的目录条目**（同名同步骤，仅 im/gf 文件名不同），且 0655 已绑定 `push_up_on_stability_ball_male.png` 并入 `media/`。0656 的 4 张生成图**不入库**，App 端不做绑定——避免重复资产与文件名冲突。

## 审核要点

- 稳定球两件：交替前举（仰卧球上双臂交替举起）、单腿俯卧旋转（球上俯卧单腿后抬带髋旋转）。
- 雪橇两件：45° 腿举提踵（前脚掌压板边沿跖屈）、仰卧腿举深蹲（仰卧蹬板屈收位）。
- 药球胸前推跑释：站姿胸前推出脱手瞬间+前冲步态。
- 壶铃五件：高翻 windmill（单臂过头锁定+侧屈对侧手触腿、目视壶铃）、阿诺德推（旋转中程掌心外翻）、双挺举（屈膝助力双铃过头锁定）、双臂军事推（双腿伸直严格无助力）、弓步穿越（前腿屈膝壶铃从腿下换手穿越）。
- EZ 杠两件：球上坐姿法式推（坐姿稳定球+EZ 杠过头臂屈伸）、蜘蛛弯举（胸抵斜板、手臂下垂持 EZ 杠）。
- 负重两件：俄转（坐姿后仰杠片转至体侧触地）、深蹲（抱杠片于胸前底部深度位）。
- 全 60 张均为单帧编辑插图，无拼图/多画面；带标轨单一 ALIVO 字标，开源轨完全无标识。

## 归档

- `plan_round22.json` / `batch_round22.json`：目标、文件名、绑定清单（batch 已移除 0656 重复条目，实际绑定 14 条）。
- `prompts/male/`、`prompts/female/`、`prompts/open_male/`、`prompts/open_female/`：四轨逐图完整提示词（各 15 份，含 0656 提示词备查）。

## 回归

- Flutter 媒体测试 5/5；Node 文件级回归仅 3 项已知失败（`coach-postgres`、`sync-postgres` 需 SSH host 参数的手动集成测试；`terrain-preview` 预存 manifest hash 不符，与媒体无关）。
