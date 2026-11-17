# Round 73 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（双凳臂屈伸、双杠反向臂屈伸、杠铃/反握/哑铃腕弯举、坐姿俯身交替后摆、坐姿臂屈伸、反握/肩宽正握引体、窄握/毛巾站姿划船、Zercher/速度深蹲、屈膝直臂起坐、自辅助反向腿弯举）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 排除：`1371`（与已绑 `0088` 同 slug 同文副本）——slug 撞名，留待后续以独立 slug 处理；本轮替换为 `0697`。
- 补收：`3161` 男版生成日志未打印输出路径（PostToolUse 钩子失败），按完成时间从 generated_images 回收对应文件后目验通过。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0813 | triceps_dip_between_benches | 双凳臂屈伸 |
| exercises-dataset:0672 | reverse_dip | 双杠反向臂屈伸 |
| exercises-dataset:0126 | barbell_wrist_curl | 杠铃腕弯举 |
| exercises-dataset:0079 | barbell_revers_wrist_curl_v_2 | 杠铃反握腕弯举 v2 |
| exercises-dataset:0367 | dumbbell_over_bench_one_arm_wrist_curl | 凳上单臂哑铃腕弯举 |
| exercises-dataset:1730 | dumbbell_seated_bent_over_alternate_kickback | 坐姿俯身交替后摆 |
| exercises-dataset:0389 | dumbbell_seated_bench_extension | 坐姿哑铃臂屈伸 |
| exercises-dataset:0674 | reverse_grip_pull_up | 反握引体 |
| exercises-dataset:1763 | shoulder_grip_pull_up | 肩宽正握引体 |
| exercises-dataset:3158 | bodyweight_standing_close_grip_row | 窄握站姿划船 |
| exercises-dataset:3161 | bodyweight_standing_one_arm_row_with_towel | 毛巾单臂站姿划船 |
| exercises-dataset:1545 | barbell_full_zercher_squat | Zercher 深蹲 |
| exercises-dataset:0101 | barbell_speed_squat | 速度深蹲 |
| exercises-dataset:0456 | flexion_leg_sit_up_bent_knee | 屈膝直臂起坐 |
| exercises-dataset:0697 | self_assisted_inverse_leg_curl | 自辅助反向腿弯举 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0813` 手撑一凳脚搭二凳屈臂下放（与已绑 `3287` 凳缘脚着地腿位区分）；`0672` 平行杠悬撑直身下放（与凳式臂屈伸器械区分）；`0126` 前臂搁腿掌心朝上屈腕（与 `0079` 掌心朝下/已绑杠铃站姿背后腕弯举握向支撑面区分）；`0079` 掌心朝下前臂搁腿仅伸腕；`0367` 跪姿前臂搁凳单哑铃掌心朝上（与杠铃版器械臂数区分）；`1730` 坐姿深俯一臂后伸一臂保持屈肘（交替后摆，与站姿后摆体位区分）；`0389` 直坐双手托单哑铃落头后（与 `2189` 同族不同支撑面）；`0674` 反握窄距下巴过杠（与 `1763` 正握/`0660` 已绑近亲握向区分）；`1763` 正握肩宽下巴过杠；`3158` 后倾直身双手紧握柱拉胸（与 `3161` 单臂毛巾握法区分）；`3161` 毛巾套柱单臂后倾拉；`1545` 肘弯托杠蹲至大腿过平行（与背扛深蹲杠位区分）；`0101` 背杠快速浅蹲至平行上（与 `1435`/`1436` 深位和 `0063`/`0124` 站距变体深度区分）；`0456` 屈膝卷至膝前双臂直伸（与本轮前作 `0457` 直腿臂位腿位区分）；`0697` 仰卧双臂贴地双膝卷向胸（与卷腹上身卷曲方向区分）。

## 校验

- 双端 `exercise_metadata.json`：1227 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1227 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
