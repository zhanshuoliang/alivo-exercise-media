# Round 62 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（未绑定池经归一化撞名 + 语义排雷 + 步骤核查后选定）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:3295 | front_lever_reps | 前水平 |
| exercises-dataset:3300 | lean_planche | 前倾俄挺 |
| exercises-dataset:3298 | straddle_planche | 分腿俄挺 |
| exercises-dataset:3314 | straddle_maltese | 分腿马耳他（吊环） |
| exercises-dataset:1429 | wide_grip_pull_up | 宽握引体 |
| exercises-dataset:1686 | squat_to_overhead_reach_with_twist | 深蹲过顶前伸转体 |
| exercises-dataset:0372 | dumbbell_preacher_curl | 哑铃牧师凳弯举 |
| exercises-dataset:0353 | dumbbell_one_arm_concentration_curl_on_stability_ball | 球上单臂集中弯举 |
| exercises-dataset:1285 | dumbbell_one_arm_bench_fly | 凳上单臂飞鸟 |
| exercises-dataset:3560 | dumbbell_standing_alternate_hammer_curl_and_press | 站姿交替锤式弯举推举 |
| exercises-dataset:3215 | hands_reversed_clasped_circular_toe_touch | 反交握绕环触趾 |
| exercises-dataset:0661 | push_up_inside_leg_kick | 俯卧撑内踢腿 |
| exercises-dataset:0419 | dumbbell_standing_front_raise_above_head | 站姿前平举过头 |
| exercises-dataset:0267 | crunch_hands_overhead | 过顶卷腹 |
| exercises-dataset:1306 | plyo_push_up | 爆发俯卧撑 |

## 审核

30/30 逐张视觉审核通过。静态高难动作（前水平/俄挺/马耳他）逐帧核对支撑点与体姿；`3215` 反交握、`0661` 内踢腿、`1306` 腾空位均明确呈现。

## 校验

- 双端 `exercise_metadata.json`：1062 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1062 WebP 各，RIFF/WEBP 魔数全过。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
