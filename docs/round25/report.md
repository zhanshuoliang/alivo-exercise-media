# Round 25 — 壶铃收尾 + 史密斯/弹力带/杠杆机批（15 动作 × 4 轨 = 60 张）

日期：2026-11-16。选题原则：壶铃器械桶收尾（剩余 4 个可用目标）+ 史密斯机续补 + 弹力带抗阻补全 + 杠杆机首次覆盖。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:0519 | kettlebell alternating press on floor | kettlebell |
| exercises-dataset:0526 | kettlebell double alternating hang clean | kettlebell |
| exercises-dataset:0539 | kettlebell one arm military press to the side | kettlebell |
| exercises-dataset:0543 | kettlebell pirate supper legs | kettlebell |
| exercises-dataset:0747 | smith behind neck press | smith machine |
| exercises-dataset:0760 | smith leg press | smith machine |
| exercises-dataset:0761 | smith narrow row | smith machine |
| exercises-dataset:0762 | smith rear delt row | smith machine |
| exercises-dataset:3142 | smith sumo squat | smith machine |
| exercises-dataset:0975 | band close-grip push-up | band |
| exercises-dataset:1003 | band squat row | band |
| exercises-dataset:1009 | band stiff leg deadlift | band |
| exercises-dataset:1015 | band vertical pallof press | band |
| exercises-dataset:0606 | lever t-bar row | leverage machine |
| exercises-dataset:2289 | lever calf press | leverage machine |

选题备注：壶铃桶剩余 5 个候选中 `0530`（double windmill）与已入库 `0517`（advanced windmill）姿态过近，本轮入库其余 4 个后壶铃桶收尾；`0656`/`extra-007`/`extra-012` 等重复或已完成项延续排除。

## 产出（60/60 一次过审，无返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端，绑定数 495 → 510
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` + `<base>_female.png` ×30：纯提示词独立生成（无参考图），CC-BY-4.0，`media-open/manifest.json` 448 → 478

## 审核要点

- 壶铃四件（器械桶收尾）：交替地板推（仰卧一臂锁定一臂肩位交替相位）、双交替悬垂翻（双铃一收位一悬垂的交替中程）、单臂军事推（站姿单臂过头锁定）、pirate supper legs 单臂翻（铃收肩位+肘贴身+对侧臂后摆微屈髋）。
- 史密斯五件：颈后推（站姿杆于颈后中程推举）、腿举（仰卧地面双脚掌推导杆向上近全伸展）、窄距划船（俯身窄握拉杆至腹部）、后束划船（宽握拉至上胸、肘外张高位）、相扑蹲（宽站距脚尖外展深蹲位、杆于上背）。
- 弹力带四件：窄距俯卧撑（弹力带绕背上肢推撑位）、深蹲划船（低位锚点深蹲位划船收肘）、直腿硬拉（踩带直腿屈髋提拉）、垂直 Pallof 推（侧向锚点双手过头锁定推）。
- 杠杆机两件（首次覆盖）：T 杆划船（斜板托胸、双手握杠杆臂划船）、坐姿提踵（负重压片机前掌压台跖屈顶点）。
- 全 60 张均为单帧编辑插图，无拼图/多画面；带标轨单一 ALIVO 字标，开源轨完全无标识。
- 生成插曲：首批 8 个任务遇 imagegen 连接错误未出图（`0761` 男带标、`0975` 男带标、`1009` 女带标、`0519/0543/0761` 开源男、`0539/0762` 开源女），重试后全部出图并通过审核。

## 归档

- `plan_round25.json` / `batch_round25.json`：目标、文件名、绑定清单（15 条，无冲突）。
- `prompts_m/`、`prompts_f/`、`prompts_open_m/`、`prompts_open_f/`：四轨逐图完整提示词（各 15 份）。

## 回归

- Flutter 媒体测试 5/5；Node 文件级回归仅 3 项已知失败（`coach-postgres`、`sync-postgres` 需 SSH host 参数的手动集成测试；`terrain-preview` 预存 manifest hash 不符，与媒体无关）。
