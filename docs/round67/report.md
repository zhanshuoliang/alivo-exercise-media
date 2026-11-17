# Round 67 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（器械家族变体、绳索臂屈伸/下压、弹力带硬拉、负重转体、哑铃变式、自重核心）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0595 | lever_seated_crunch_chest_pad | 坐姿卷腹（胸垫） |
| exercises-dataset:1616 | lever_reverse_grip_preacher_curl | 反握牧师凳弯举 |
| exercises-dataset:2736 | lever_reverse_grip_lateral_pulldown | 反握下拉 |
| exercises-dataset:2364 | assisted_wide_grip_chest_dip_kneeling | 辅助跪姿宽握臂屈伸 |
| exercises-dataset:0869 | lever_shoulder_press_v_2 | 器械肩推 v2 |
| exercises-dataset:0186 | cable_lying_triceps_extension_v_2 | 仰卧绳索臂屈伸 v2 |
| exercises-dataset:1643 | cable_seated_overhead_curl | 坐姿过头弯举 |
| exercises-dataset:2405 | cable_triceps_pushdown_v_bar_with_arm_blaster | V杆臂板下压 |
| exercises-dataset:1023 | band_straight_back_stiff_leg_deadlift | 弹力带直背硬拉 |
| exercises-dataset:2371 | weighted_russian_twist_v_2 | 负重俄罗斯转体 v2 |
| exercises-dataset:1733 | dumbbell_incline_two_arm_extension | 上斜双臂伸展 |
| exercises-dataset:0379 | dumbbell_rear_lateral_raise_support_head | 扶头后束平举 |
| exercises-dataset:1666 | dumbbell_one_arm_prone_hammer_curl | 俯卧锤式弯举 |
| exercises-dataset:0138 | bottoms_up | 折刀收腿 |
| exercises-dataset:0508 | janda_sit_up | 詹达仰卧起坐 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0595` 胸抵垫前卷（与已绑 `lever_seated_crunch` 胸垫版区分）；`1616` 反握上臂压牧师垫（与已绑正握/锤式版握向区分）；`2736` 反握下拉杆拉至上胸；`2364` 跪垫+宽握+前倾辅助臂屈伸；`0869` 器械肩推 v2（与已绑 v1 把手位区分）；`0186` 仰卧头朝滑轮绳落前额；`1643` 背向坐姿双臂过头持绳；`2405` 臂板束带+V杆压至锁直；`1023` 髋铰直背带绷紧；`2371` 后仰坐姿杠片移至身侧；`1733` 上斜凳哑铃落头侧；`0379` 额抵凳顶俯身双臂侧展；`1666` 俯卧凳中性握单臂弯举；`0138` 臀离地膝卷向胸；`0508` 屈膝坐起手置头后。

## 校验

- 双端 `exercise_metadata.json`：1137 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1137 WebP 各，RIFF/WEBP 魔数全过。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
