# Round 65 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（未绑定池经归一化撞名 + 语义排雷 + 步骤核查后选定）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 命名特例：`2800` 为数据集 "(female)" 同名副本（孪生 `2799` 已占基础 slug），改用 `barbell_sitted_alternate_leg_raise_female_{male,female}` 文件名绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:1467 | push_up_on_lower_arms | 前臂支撑俯卧撑 |
| exercises-dataset:0666 | raise_single_arm_push_up | 单臂外伸俯卧撑 |
| exercises-dataset:3699 | shoulder_tap | 平板交替拍肩 |
| exercises-dataset:0341 | dumbbell_lying_one_arm_deltoid_rear | 俯卧单臂后束举 |
| exercises-dataset:0433 | dumbbell_straight_arm_pullover | 直臂哑铃套头拉 |
| exercises-dataset:0410 | dumbbell_single_leg_split_squat | 单腿分腿蹲 |
| exercises-dataset:0037 | barbell_decline_wide_grip_pullover | 下斜宽握直臂套头拉 |
| exercises-dataset:1720 | barbell_lying_back_of_the_head_tricep_extension | 仰卧脑后臂屈伸 |
| exercises-dataset:2800 | barbell_sitted_alternate_leg_raise_female | 杠铃坐姿交替举腿（女标副本） |
| exercises-dataset:1269 | cable_standing_up_straight_crossovers | 站姿绳索交叉飞鸟 |
| exercises-dataset:2616 | cable_lateral_pulldown_with_v_bar | V 杆下拉 |
| exercises-dataset:1639 | cable_rope_hammer_preacher_curl | 绳式锤式牧师凳弯举 |
| exercises-dataset:0211 | cable_russian_twists_on_stability_ball | 球上绳索俄罗斯转体 |
| exercises-dataset:0772 | smith_standing_behind_head_military_press | 史密斯站姿颈后推举 |
| exercises-dataset:3241 | exercise_ball_on_the_wall_calf_raise_tennis_ball_between_ankles | 球靠墙提踵 |

## 审核

30/30 逐张视觉审核通过。重点核对：`1467` 前臂支撑推起与标准俯卧撑区分；`0666` 单臂支撑另臂离地平伸；`0037` 下斜凳直臂过顶落杠（与已绑弯臂版 `0034` 区分）；`1720` 仰卧杠落头后臂屈伸；`2800` 坐凳杠置大腿交替直腿举；`1269` 双臂交叉飞鸟；`1639` 肘压牧师凳绳式锤握弯举；`0211` 坐球双手持把躯干旋转；`0772` 站姿史密斯架宽握杠过顶；`3241` 球夹背墙之间提踵顶点。

## 校验

- 双端 `exercise_metadata.json`：1107 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1107 WebP 各，RIFF/WEBP 魔数全过。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
