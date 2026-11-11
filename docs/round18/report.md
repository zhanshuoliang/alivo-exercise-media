# Round 18 — 器械补全第二批（15 动作 × 4 轨 = 60 张）

日期：2026-11-10。选题原则：继续补未配图器械类别——壶铃进阶动作、雪橇机小腿、药球爆发、EZ 杠臂部、弹力带坐姿、负重自重、滚轮核心。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:0548 | kettlebell sumo high pull | kettlebell |
| exercises-dataset:0552 | kettlebell two arm clean | kettlebell |
| exercises-dataset:0529 | kettlebell double snatch | kettlebell |
| exercises-dataset:1383 | hack calf raise | sled machine |
| exercises-dataset:1391 | sled calf press on leg press | sled machine |
| exercises-dataset:1701 | medicine ball close grip push up | medicine ball |
| exercises-dataset:1303 | medicine ball chest push from 3 point stance | medicine ball |
| exercises-dataset:1750 | medicine ball supine chest throw | medicine ball |
| exercises-dataset:1627 | ez barbell close grip preacher curl | ez barbell |
| exercises-dataset:1682 | ez bar seated close grip concentration curl | ez barbell |
| exercises-dataset:2186 | ez barbell decline triceps extension | ez barbell |
| exercises-dataset:3122 | resistance band seated shoulder press | resistance band |
| exercises-dataset:3144 | resistance band seated straight back row | resistance band |
| exercises-dataset:3286 | weighted muscle up | weighted |
| exercises-dataset:2206 | roller reverse crunch | roller |

## 产出（60/60 一次过审）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端（HarmonyOS `entry/` + Flutter `mobile/`），绑定数 393 → 408
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` + `<base>_female.png` ×30：纯提示词独立生成（无参考图），CC-BY-4.0，`media-open/manifest.json` 240 → 270

## 审核要点

- 壶铃相扑高拉：宽站距、肘高于肩拉至颏下；双抓举双臂过头锁定。
- 哈克机提踵：肩垫承托、踏板边沿踮脚；腿举提踵前脚掌压板跖屈。
- 药球：窄距俯卧撑双手持球；三点位单手控球；仰卧胸前抛抓取脱手瞬间。
- EZ 杠三件：牧师凳斜面垫支撑窄握、坐姿集中弯举肘抵大腿内侧、下斜凳腿部滚轴固定过头臂屈伸。
- 弹力带坐姿两件：肩推带压脚下双臂过头、直背划船带绕脚掌收肘。
- 负重双力臂：杠上支撑位 + 负重腰带链条杠片。
- 滚轮反向卷腹：仰卧双臂过头，小腿夹泡沫轴卷骨盆。
- 带标轨字标合规；开源轨四张全图零文字零标志。

## 归档

- `plan_round18.json` / `batch_round18.json`：目标、文件名、绑定清单。
- `prompts18_m/`、`prompts18_f/`、`prompts18_open_m/`、`prompts18_open_f/`：四轨逐图完整提示词（各 15 份）。

## 验证

- 双端 `exercise_media/` 各 410 文件，新增 15 张逐字节相同；`exercise_metadata.json` 绑定 393 → 408。
- `media/` 484 张 PNG、`media-open/` 270 张；双 NOTICE 各记 30 条 SHA-256。
- Node 回归：与 Round 17 相同的 3 项预存/手动集成失败（`coach-postgres`、`sync-postgres` 需 SSH host 参数；`terrain-preview` 预存 manifest hash 不符），其余全过；Flutter 媒体测试 5/5。
