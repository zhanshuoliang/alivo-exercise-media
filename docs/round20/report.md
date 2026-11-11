# Round 20 — 器械/弹力带批（15 动作 × 4 轨 = 60 张）

日期：2026-11-11。选题原则：继续补未绑定的器械类——雪橇机、药球、瑜伽球、EZ 杠、弹力带系列。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:1425 | sled 45 degrees one leg press | sled machine |
| exercises-dataset:0742 | sled forward angled calf raise | sled machine |
| exercises-dataset:2334 | sled lying calf press | sled machine |
| exercises-dataset:0663 | push-up medicine ball | medicine ball |
| exercises-dataset:1305 | medicine ball chest push single response | medicine ball |
| exercises-dataset:1334 | exercise ball back extension with hands behind head | stability ball |
| exercises-dataset:1417 | exercise ball one legged diagonal kick hamstring curl | stability ball |
| exercises-dataset:1744 | exercise ball dip | stability ball |
| exercises-dataset:2328 | narrow push-up on exercise ball | stability ball |
| exercises-dataset:0446 | ez barbell close-grip curl | EZ barbell |
| exercises-dataset:1458 | ez barbell seated curls | EZ barbell |
| exercises-dataset:2432 | ez-bar close-grip bench press | EZ barbell |
| exercises-dataset:0993 | band reverse fly | band |
| exercises-dataset:0979 | band horizontal Pallof press | band |
| exercises-dataset:1018 | band shrug | band |

## 产出（60/60 过审；1 轨返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端，绑定数 421 → 436
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` + `<base>_female.png` ×30：纯提示词独立生成（无参考图），CC-BY-4.0，`media-open/manifest.json` 300 → 330

## 审核要点

- 雪橇机三件：单腿 45° 腿举（单腿蹬板另腿收起）、腿举机上提踵（前脚掌压板跖屈）、仰卧小腿蹬板（仰卧前掌压板）。
- 药球两件：双手持球俯卧撑中程；站姿胸前推出（臂直前送瞬间）。
- 瑜伽球四件：俯卧球上手抱头背伸展（脚抵墙）、臀桥位单腿压球对角踢、背后撑球边臂屈伸、窄距球上俯卧撑。
- EZ 杠三件：站姿窄握弯举顶峰、坐姿窄握弯举、平凳窄握卧推锁定。
- 弹力带三件：反向飞鸟（锚点在身前/侧，水平外展）、水平 Pallof 推（侧向锚点抗旋转前推）、耸肩（带踩脚下提肩顶峰）。
- **返工**：`medicine_ball_chest_push` 开源男版初版错出成 EZ 杠卧推，重出后为站姿胸前推，通过。
- 生成插曲：首批 8 任务遇网络错误（imagegen 连接失败两次），重试后全部出图；本机 codex hooks（SessionStart/PreToolUse 等）报错为既有噪音，不影响生成。

## 归档

- `plan_round20.json` / `batch_round20.json`：目标、文件名、绑定清单。
- `prompts/male/`、`prompts/female/`、`prompts/open_male/`、`prompts/open_female/`：四轨逐图完整提示词（各 15 份）。

## 回归

- Flutter 媒体测试 5/5；Node 文件级回归仅 3 项已知失败（`coach-postgres`、`sync-postgres` 需 SSH host 参数的手动集成测试；`terrain-preview` 预存 manifest hash 不符，与媒体无关）。
