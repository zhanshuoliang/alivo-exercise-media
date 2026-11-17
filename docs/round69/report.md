# Round 69 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（杠铃仰卧/坐姿/站姿变体、绳索弯举/划船/下压、自重悬垂/引体/臂屈伸/平板家族、哑铃上斜/球上/俯卧变式）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0056 | barbell_lying_close_grip_triceps_extension | 仰卧窄距臂屈伸 |
| exercises-dataset:0089 | barbell_seated_close_grip_concentration_curl | 坐姿窄距集中弯举 |
| exercises-dataset:0108 | barbell_standing_leg_calf_raise | 站姿杠铃提踵 |
| exercises-dataset:1640 | cable_rope_one_arm_hammer_preacher_curl | 单臂绳式牧师凳弯举 |
| exercises-dataset:0239 | cable_straight_back_seated_row | 直背坐姿划船 |
| exercises-dataset:2406 | cable_reverse_grip_triceps_pushdown_sz_bar_with_arm_blaster | SZ杆反握臂板下压 |
| exercises-dataset:0475 | hanging_straight_leg_raise | 悬垂直腿举 |
| exercises-dataset:1327 | close_grip_chin_up | 窄握反手引体 |
| exercises-dataset:2363 | wide_grip_chest_dip_on_high_parallel_bars | 宽握高杠臂屈伸 |
| exercises-dataset:3147 | pelvic_tilt | 骨盆倾斜 |
| exercises-dataset:0498 | inverted_row_with_straps | 悬带反向划船 |
| exercises-dataset:3239 | kneeling_plank_tap_shoulder_male | 跪姿平板拍肩 |
| exercises-dataset:1619 | dumbbell_incline_one_arm_hammer_press | 上斜单臂锤式推举 |
| exercises-dataset:1291 | dumbbell_one_arm_pullover_on_exercise_ball | 球上单臂套头拉 |
| exercises-dataset:0348 | dumbbell_lying_rear_lateral_raise | 俯卧后束平举 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0056` 仰卧凳上窄握杠落前额（与已绑站姿/坐姿臂屈伸体位区分）；`0089` 坐姿双肘抵大腿内侧+窄握杠铃弯举（与单臂集中弯举族握具/臂数区分）；`0108` 杠置背上站姿提踵顶点（与已绑坐姿/器械提踵支撑区分）；`1640` 单臂压牧师凳垫+绳式中握（与已绑双臂绳式牧师凳臂数区分）；`0239` 躯干完全垂直把拉至腰（与已绑前倾划船躯干角区分）；`2406` 臂板束带+反握SZ杆压至锁直（与已绑V杆臂板下压握具/握向区分）；`0475` 悬垂直腿水平L形；`1327` 反握窄距下巴过杠（与已绑正握引体握向区分）；`2363` 宽距双杠躯干前倾胸向下降（与已绑窄距臂屈伸握距区分）；`3147` 仰卧屈膝腰背压地静态呈现；`0498` 悬带身体斜直胸拉向把手（与已绑杠下反向划船器械区分）；`3239` 膝触地平板手拍对侧肩（与已绑全平板拍肩体位区分）；`1619` 上斜凳中性握单臂过顶（与已绑双臂上斜推举臂数区分）；`1291` 球撑上背髋桥单臂哑铃过顶（与已绑双臂球上套头拉臂数区分）；`0348` 俯卧凳双臂后展（与已绑俯卧单臂后束臂数区分）。

## 校验

- 双端 `exercise_metadata.json`：1167 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1167 WebP 各，RIFF/WEBP 魔数全过。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
