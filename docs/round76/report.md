# Round 76 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（站姿哑铃侧平举、站姿双臂弯举、坐姿双臂前平举/侧平举、坐姿交替锤式、球上交替弯举/交替锤式、站姿单臂锤式、单臂 Zottman 牧师凳、球上坐姿套头拉、站姿俯身双臂三头屈伸、站姿交替后摆、哑铃支撑深蹲、半蹲、俯卧撑转跑）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 缓办：`3201`/`0668`/`0350`/`0418`/`1380`/`1381`/`0139`/`0140`/`0474`/`0634`/`0735`/`0812`/`0814`/`1753`/`0816`/`3156`/`3162`/`1737`/`0394`/`0398`/`0377`/`0380`/`2318`/`1386`/`0316`/`0328`/`0221`/`0422`（同文副本或近亲，留待独立 slug 处理）；`3562` 黑名单永不绑定；10 条双人辅助拉伸持续缓办。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0376 | dumbbell_raise | 站姿哑铃侧平举 |
| exercises-dataset:0416 | dumbbell_standing_biceps_curl | 站姿双臂哑铃弯举 |
| exercises-dataset:0392 | dumbbell_seated_front_raise | 坐姿双臂前平举 |
| exercises-dataset:0396 | dumbbell_seated_lateral_raise | 坐姿哑铃侧平举 |
| exercises-dataset:1648 | dumbbell_alternate_seated_hammer_curl | 坐姿交替锤式弯举 |
| exercises-dataset:1650 | dumbbell_alternating_seated_bicep_curl_on_exercise_ball | 球上坐姿交替弯举 |
| exercises-dataset:1676 | dumbbell_seated_alternate_hammer_curl_on_exercise_ball | 球上坐姿交替锤式弯举 |
| exercises-dataset:1671 | dumbbell_one_arm_standing_hammer_curl | 站姿单臂锤式弯举 |
| exercises-dataset:1672 | dumbbell_one_arm_zottman_preacher_curl | 单臂 Zottman 牧师凳弯举 |
| exercises-dataset:1295 | dumbbell_pullover_on_exercise_ball | 球上坐姿哑铃套头拉 |
| exercises-dataset:1741 | dumbbell_standing_bent_over_two_arm_triceps_extension | 站姿俯身双臂三头屈伸 |
| exercises-dataset:1739 | dumbbell_standing_alternating_tricep_kickback | 站姿交替三头后摆 |
| exercises-dataset:2803 | dumbbell_supported_squat | 哑铃支撑深蹲 |
| exercises-dataset:3221 | half_knee_bends_male | 半蹲（male 变体） |
| exercises-dataset:3638 | push_to_run | 俯卧撑转跑 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0376` 站姿双臂侧展至肩高 T 形（与 `0355` 单臂/`0396` 坐姿/`dumbbell_full_can_lateral_raise` 拇指握变体区分）；`0416` 站姿双臂掌心朝前卷至肩（与 `0421` 单臂集中/`1648` 坐姿锤式握向区分）；`0392` 坐姿双臂同时前平举（与 `0387` 交替/`0388` 推举行程区分）；`0396` 坐姿双臂侧展（与 `0376` 站姿/`seated_bent_arm_lateral_raise` 屈肘版区分）；`1648` 坐姿中立握单臂交替（与 `1669` 肘抵大腿单臂/`1676` 球上版支撑区分）；`1650` 坐球掌心朝上交替（与 `1676` 锤式握向/`1679` 抬腿版区分）；`1676` 坐球中立握交替（与 `1650` 掌心朝上握向区分）；`1671` 站姿单臂中立握空手扶髋（与 `1648` 坐姿交替/`1672` 牧师凳支撑区分）；`1672` 上臂压垫单臂 Zottman 旋转（与 `2294` 双臂版臂数/`1663` 锤式不旋转握法区分）；`1295` 坐球双臂持单哑铃落头后（与 `1284`/`1736` 横卧球髋桥/`1620` 单臂锤式推体位区分）；`1741` 站姿髋铰俯身双臂后伸（与 `1739` 交替/`1737` 坐姿/`0394` 坐姿体位区分）；`1739` 站姿髋铰俯身单臂后伸交替（与 `1741` 双臂/ `1730` 坐姿交替体位区分）；`2803` 深蹲底手扶立柱单手持哑铃（与 `3221` 徒手半蹲/`3119` 蹲底保持支撑与深度区分）；`3221` 半蹲浅蹲挺胸（与 `3222` 半蹲跳腾空/`3119` 全蹲底深度区分）；`3638` 平板单膝驱动向胸（与 `1311` 俯卧撑/`3201` 卷腹动作模式区分）。

## 校验

- 双端 `exercise_metadata.json`：1272 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1272 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定；本轮 15 条均不在 curation 排除清单。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
