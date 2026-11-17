# Round 72 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（哑铃上斜单臂飞鸟/推/侧平举、球上套头拉、仰卧单臂推/交替臂屈伸、锤式/Zottman 牧师凳、站姿对握推举、俯身后束飞鸟、绳索站姿下拉、握式耸肩机/牧师凳弯举机、凳上反向划船、直臂屈腿起坐）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 排除：`0422`（与已绑 `1680` 同 slug 同文副本）——slug 撞名；`1735`（与本轮 `1729` 仰卧臂屈伸同族）——去重后替换为 `0457` 直臂屈腿起坐。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:1279 | dumbbell_incline_one_arm_fly | 哑铃上斜单臂飞鸟 |
| exercises-dataset:1281 | dumbbell_incline_one_arm_press | 哑铃上斜单臂推 |
| exercises-dataset:0323 | dumbbell_incline_one_arm_lateral_raise | 哑铃上斜单臂侧平举 |
| exercises-dataset:1284 | dumbbell_lying_pullover_on_exercise_ball | 球上哑铃套头拉 |
| exercises-dataset:0342 | dumbbell_lying_one_arm_press_v_2 | 仰卧单臂哑铃推 v2 |
| exercises-dataset:1729 | dumbbell_lying_alternate_extension | 仰卧交替哑铃臂屈伸 |
| exercises-dataset:1663 | dumbbell_one_arm_hammer_preacher_curl | 单臂锤式牧师凳弯举 |
| exercises-dataset:2294 | dumbbell_zottman_preacher_curl | Zottman 牧师凳弯举 |
| exercises-dataset:0424 | dumbbell_standing_one_arm_palm_in_press | 站姿单臂对握推举 |
| exercises-dataset:0378 | dumbbell_rear_fly | 俯身哑铃后束飞鸟 |
| exercises-dataset:0232 | cable_standing_pulldown_with_rope | 站姿绳索下拉 |
| exercises-dataset:1439 | lever_gripless_shrug_v_2 | 握式耸肩机 v2 |
| exercises-dataset:1614 | lever_preacher_curl_v_2 | 牧师凳弯举机 v2 |
| exercises-dataset:2298 | inverted_row_on_bench | 凳上反向划船 |
| exercises-dataset:0457 | flexion_leg_sit_up_straight_arm | 直臂屈腿起坐 |

## 审核

30/30 逐张视觉审核通过。重点核对：`1279` 上斜凳单臂宽弧展开（与已绑双臂飞鸟/`1281` 推起臂部轨迹区分）；`1281` 上斜凳单哑铃推至顶（与 `1619`/`1620` 锤式上斜推握向区分）；`0323` 前倾撑腿单臂侧举至肩高（与已绑站姿侧平举支撑面区分）；`1284` 球撑上背髋桥双手哑铃落头后（与已绑凳上套头拉支撑面区分）；`0342` 平躺凳单哑铃推至顶（与 `1281` 上斜体位区分）；`1729` 一臂屈落头侧一臂保持伸展（交替臂屈伸）；`1663` 上臂压垫中性握单臂弯举（与 `1640` 绳式/`2294` Zottman 握向器械区分）；`2294` 双臂压垫旋前握可辨（Zottman 转腕）；`0424` 站姿中立握单臂过顶（与坐姿/上斜版体位区分）；`0378` 髋铰俯身双臂后展（与 `0348` 俯卧凳版支撑面区分）；`0232` 高位滑轮绳把压至大腿（站姿下拉，与坐姿下拉/三头下压体态区分）；`1439` 坐姿耸肩机肩耸向耳（与已绑站姿杠铃/哑铃耸肩器械区分）；`1614` 上臂压垫杠杆把手卷起（器械牧师凳 v2）；`2298` 身体斜直胸拉向凳缘（与 `2300` 屈膝/`0498` 悬带版支撑面区分）；`0457` V形起坐直臂触脚尖（与已绑卷腹/仰卧起坐臂位腿位区分）。

## 校验

- 双端 `exercise_metadata.json`：1212 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1212 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
