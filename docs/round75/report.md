# Round 75 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（杠铃侧向/前向分腿蹲、坐姿反握腕弯举、坐姿单腿提踵、坐姿/站姿牧师凳弯举、站姿集中弯举、跪姿肘撑球弯举、坐姿单臂锤式弯举、坐姿交替前平举/交替推、上斜推、仰卧单臂屈伸、球靠墙膝夹网球提踵、站姿触脚尖）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 缓办：`0422`（slug 与同文副本 `1680` 冲突，留待独立 slug 处理）、`0474`/`0140`/`0139`/`0634`/`0735`/`0812`/`0814`/`1753`/`1386`/`2318` 等近亲同文族维持缓办；`3562` 黑名单永不绑定；10 条双人辅助拉伸持续缓办。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0097 | barbell_side_split_squat_v_2 | 杠铃侧向分腿蹲 v2 |
| exercises-dataset:2810 | barbell_split_squat_v_2 | 杠铃前向分腿蹲 v2 |
| exercises-dataset:0385 | dumbbell_reverse_wrist_curl | 坐姿反握腕弯举 |
| exercises-dataset:0400 | dumbbell_seated_one_leg_calf_raise | 坐姿单腿哑铃提踵 |
| exercises-dataset:0402 | dumbbell_seated_preacher_curl | 坐姿牧师凳单臂弯举 |
| exercises-dataset:0428 | dumbbell_standing_preacher_curl | 站姿牧师凳弯举 |
| exercises-dataset:0421 | dumbbell_standing_one_arm_concentration_curl | 站姿单臂集中弯举 |
| exercises-dataset:0387 | dumbbell_seated_alternate_front_raise | 坐姿交替前平举 |
| exercises-dataset:0388 | dumbbell_seated_alternate_press | 坐姿交替推举 |
| exercises-dataset:0325 | dumbbell_incline_raise | 上斜哑铃推举 |
| exercises-dataset:1660 | dumbbell_kneeling_bicep_curl_exercise_ball | 跪姿肘撑球弯举 |
| exercises-dataset:1669 | dumbbell_one_arm_seated_hammer_curl | 坐姿单臂锤式弯举 |
| exercises-dataset:1735 | dumbbell_lying_single_extension | 仰卧单臂屈伸 |
| exercises-dataset:3240 | exercise_ball_on_the_wall_calf_raise_tennis_ball_between_knees | 球靠墙膝夹网球提踵 |
| exercises-dataset:3231 | two_toe_touch_male | 站姿触脚尖（male 变体） |

## 审核

30/30 逐张视觉审核通过。重点核对：`0097` 侧跨深蹲一腿伸直（与 `2810` 前跨弓步方向区分）；`2810` 前弓步底躯干直立；`0385` 前臂搁腿掌心朝下（与已绑 `0126` 掌心朝上/`0367` 凳上版支撑区分）；`0400` 掌踏块+哑铃置腿+另腿前伸（与 `1397` 站姿/`0409` 台阶版体位区分）；`0402` 坐姿上臂压垫单臂弯起（与 `0428` 站姿/`1663` 锤式握区分）；`0428` 站姿上臂靠垫双臂弯起（与 `0402` 坐姿/`1640` 绳索版器械区分）；`0421` 微俯空手撑腿单臂集中弯起（与 `0089` 窄距双肘/`0428` 牧师凳支撑区分）；`0387` 坐姿一臂前平举一臂垂侧（与 `0388` 肩上推举行程区分）；`0388` 坐姿一臂过顶一臂置肩交替（与 `0387` 前平举高度/ `0325` 上斜凳角度区分）；`0325` 45°上斜凳双臂过顶（与 `0388` 直坐凳角度区分）；`1660` 跪地双肘撑球掌心朝上（与 `1659` 坐球/`0402` 牧师凳支撑面区分）；`1669` 坐姿肘抵大腿内侧中立握（与 `0421` 站姿集中弯举体位区分）；`1735` 平躺凳单哑铃落前额（与 `1729` 交替屈伸/`0389` 坐姿版体位区分）；`3240` 球夹背墙+膝间网球+哑铃垂侧提踵（与 `0409` 台阶/`1397` 站姿版支撑区分）；`3231` 站姿平背前屈手触脚尖（与 `0865` 仰卧举腿/`2312` 肘触膝体位区分）。

## 校验

- 双端 `exercise_metadata.json`：1257 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1257 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定；本轮 15 条均不在 curation 排除清单。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
