# Round 70 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（自重双力臂/髋外展/半程卷腹/宽手俯卧撑、杠杆机划船、绳索弯举/转体、哑铃坐姿/球上/仰卧/后视角/提踵变式、上斜转体仰卧起坐、转体举腿 female 副本）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 中途换题：原候选 `1731`（哑铃窄距卧推）与已绑 `0296` 同 slug/同动作，替换为 `2189` 坐姿双手单哑铃过顶臂屈伸。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0631 | muscle_up | 标准双立臂 |
| exercises-dataset:0710 | side_hip_abduction | 站姿侧髋外展 |
| exercises-dataset:3202 | half_sit_up_male | 半程仰卧起坐 |
| exercises-dataset:1311 | wide_hand_push_up | 宽手俯卧撑 |
| exercises-dataset:0574 | lever_bent_over_row | 杠杆机俯身划船 |
| exercises-dataset:0209 | cable_reverse_preacher_curl | 绳索反握牧师凳弯举 |
| exercises-dataset:0243 | cable_twist | 站姿绳索转体 |
| exercises-dataset:2189 | dumbbells_seated_triceps_extension | 坐姿双手单哑铃臂屈伸 |
| exercises-dataset:1620 | dumbbell_incline_one_arm_hammer_press_on_exercise_ball | 球上单臂锤式上斜推 |
| exercises-dataset:1736 | dumbbell_one_arm_french_press_on_exercise_ball | 球上单臂法式臂屈伸 |
| exercises-dataset:1661 | dumbbell_lying_supine_biceps_curl | 仰卧哑铃弯举 |
| exercises-dataset:1765 | dumbbell_upright_row_back_pov | 哑铃直立划船后视角 |
| exercises-dataset:0495 | incline_twisting_sit_up | 上斜转体仰卧起坐 |
| exercises-dataset:1387 | one_leg_floor_calf_raise | 单腿地板提踵 |
| exercises-dataset:2801 | twisted_leg_raise_female | 转体举腿（female 副本） |

## 审核

30/30 逐张视觉审核通过。重点核对：`0631` 杠上支撑位静态双立臂（与已绑 `0558` 摆浪转换瞬间区分）；`0710` 站姿单腿侧抬手扶髋（髋外展而非内收）；`3202` 45° 半卷+手抱头（与全程仰卧起坐幅度区分）；`1311` 手距明显超肩宽（与标准/窄距俯卧撑区分）；`0574` 杠杆机俯身拉把（与已绑 V 杆版器械区分）；`0209` 双臂压垫+绳索直杆反握（与已绑单臂/双臂绳式版握具臂数区分）；`0243` 侧对滑轮双臂前伸躯干旋出；`2189` 坐姿双手托单哑铃落头后（与已绑站姿/EZ杆臂屈伸体位器械区分）；`1620` 球撑上背髋桥+中性握单臂过顶（与已绑上斜凳版支撑面区分）；`1736` 坐球单哑铃落头后（法式/过顶臂屈伸与推举动作方向区分）；`1661` 平躺哑铃卷至肩（与站姿/上斜弯举体位区分）；`1765` 正后方视角肘引领哑铃上提（直立划船新视角）；`0495` 45° 凳脚固定+躯干扭转坐起；`1387` 扶墙一腿抬起提踵顶点（与已绑踩哑铃版支撑区分）；`2801` 仰卧屈膝侧转（`2799`/`twisted_leg_raise` 同动作 female 副本，slug 加 `_female` 区分）。

## 校验

- 双端 `exercise_metadata.json`：1182 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1182 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
