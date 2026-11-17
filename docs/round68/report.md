# Round 68 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（杠铃深蹲/牧师凳变体、绳索划船/弯举/卷腹、自重引体/双力臂/仰卧起坐家族、哑铃仰卧变式）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0039 | barbell_front_chest_squat | 胸前深蹲（交臂托杠） |
| exercises-dataset:1461 | barbell_full_squat_back_pov | 深蹲后视角 |
| exercises-dataset:0059 | barbell_lying_preacher_curl | 俯卧牧师凳弯举 |
| exercises-dataset:0081 | barbell_reverse_preacher_curl | 反握牧师凳弯举 |
| exercises-dataset:1320 | cable_rope_crossover_seated_row | 交叉握绳坐姿划船 |
| exercises-dataset:1642 | cable_seated_one_arm_concentration_curl | 坐姿单臂集中弯举 |
| exercises-dataset:0242 | cable_tuck_reverse_crunch | 踝扣团身反向卷腹 |
| exercises-dataset:0678 | rocky_pull_up_pulldown | 洛奇式交替颈后下拉 |
| exercises-dataset:0558 | kipping_muscle_up | 摆浪双力臂 |
| exercises-dataset:1367 | wide_grip_rear_pull_up | 宽握颈后引体 |
| exercises-dataset:0282 | decline_sit_up | 下斜仰卧起坐 |
| exercises-dataset:3679 | sit_up_with_arms_on_chest | 抱胸仰卧起坐 |
| exercises-dataset:2333 | arm_slingers_hanging_straight_legs | 悬带吊臂直腿举 |
| exercises-dataset:0338 | dumbbell_lying_elbow_press | 仰卧肘触凳推 |
| exercises-dataset:0374 | dumbbell_prone_incline_curl | 俯卧上斜弯举 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0039` 双臂交叉压杠胸前（与已绑 clean-grip 前蹲握法区分）；`1461` 正后方视角蹲至平行下（与已绑 full squat 前视角区分）；`0059` 俯卧凳顶向下弯举（与坐姿牧师凳族区分）；`0081` 上臂压垫+正手反握；`1320` 双绳把手交叉拉向腹部；`1642` 肘抵大腿内侧单臂绳索（与已绑器械集中弯举器械区分）；`0242` 踝带+低位滑轮+膝卷臀离；`0678` 站姿宽握拉杆侧倾拉向颈侧（洛奇交替式）；`0558` 摆浪躯干越杠转换瞬间（与已绑 strict muscle up 区分）；`1367` 后视宽握杠落颈后（与已绑常规颈后引体握距区分）；`0282` 下斜凳脚固定坐起（与已绑负重下斜卷腹区分）；`3679` 双臂交叉抱胸坐起；`2333` 肘悬带吊挂直腿水平（与普通悬垂举腿支撑区分）；`0338` 哑铃仰卧肘落凳面底部；`0374` 俯卧斜凳垂臂弯举（与已绑杠铃俯卧版器械区分）。

## 校验

- 双端 `exercise_metadata.json`：1152 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1152 WebP 各，RIFF/WEBP 魔数全过。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
