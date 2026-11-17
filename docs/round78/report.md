# Round 78 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（窄握引体、悬垂直腿举、器械肩推、健腹轮、仰卧弯举、上斜肩推、坐姿单臂后摆、坐姿单腿提踵×2 握法、驴式单腿提踵、球上抬腿弯举、慢下卷腹、站姿单臂划船、扶上斜凳弯举、俯身后束划船）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 缓办：`0140`/`3162`/`0380`/`0418`/`0668`/`0735`/`0316`/`3201`/`3203`/`3016`/`3533`/`3656`/`0812`/`0814`/`1753`/`0816`（与已绑记录同文或近亲，留待后续轮）；`1667`/`1675`/`0370` 名称与步骤语义冲突；`3562` 黑名单永不绑定；9 条双人辅助拉伸持续缓办。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0139 | biceps_narrow_pull_ups | 窄握反握引体 |
| exercises-dataset:0474 | hanging_straight_leg_hip_raise | 悬垂直腿举 |
| exercises-dataset:2318 | lever_shoulder_press_v_3 | 器械肩推 v3 |
| exercises-dataset:3637 | wheel_run | 健腹轮滚出 |
| exercises-dataset:0350 | dumbbell_lying_supine_curl | 仰卧哑铃弯举 |
| exercises-dataset:0328 | dumbbell_incline_shoulder_raise | 上斜哑铃肩推 |
| exercises-dataset:0398 | dumbbell_seated_one_arm_kickback | 坐姿单臂后摆 |
| exercises-dataset:1380 | dumbbell_seated_one_leg_calf_raise_hammer_grip | 坐姿单腿提踵（锤式握） |
| exercises-dataset:1381 | dumbbell_seated_one_leg_calf_raise_palm_up | 坐姿单腿提踵（掌心朝上） |
| exercises-dataset:1386 | one_leg_donkey_calf_raise | 单腿驴式提踵 |
| exercises-dataset:1679 | dumbbell_seated_one_arm_bicep_curl_on_exercise_ball_with_leg_raised | 球上抬腿单臂弯举 |
| exercises-dataset:0634 | negative_crunch | 慢下卷腹 |
| exercises-dataset:3156 | bodyweight_standing_close_grip_one_arm_row | 站姿单臂划船（中立握） |
| exercises-dataset:0422 | dumbbell_standing_one_arm_curl_over_incline_bench_v2 | 站姿扶凳弯举（v2 slug） |
| exercises-dataset:0377 | dumbbell_rear_delt_row_shoulder | 俯身后束划船 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0139` 窄距反握下巴过杠（与 `0674` 肩宽反握/`1763` 正握握距区分）；`0474` 全悬双腿直伸至水平（与 `1764` 屈膝腿位区分）；`2318` 挂片肩推机双臂近伸展（与 `2397` 自由重量/`1439` 耸肩机动作区分）；`3637` 跪姿健腹轮完全伸展（与 `0684` 跑步/`0377` 站姿动作模式区分）；`0350` 平躺凳双臂卷至肩（与 `0342` 单臂推/`0391` 坐姿体位臂数区分）；`0328` 45°凳双臂过顶（与 `0325` 上斜卧推轨迹/`0388` 交替区分）；`0398` 坐姿前倾单臂后伸空手撑腿（与 `0394` 双臂/`1737` 双臂屈伸臂数区分）；`1380` 掌踏块缘哑铃竖置大腿（与 `1381` 掌心朝上/`0400` 哑铃横置握法区分）；`1381` 腿前伸哑铃置大腿掌心朝上（与 `1380` 锤式/`0400` 踏块支撑区分）；`1386` 双手扶墙一腿后抬跟提起（与 `0409` 台阶缘/`1397` 双腿支撑区分）；`1679` 坐球一腿离地空手扶髋弯举（与 `1668` 双脚着地/`1650` 交替区分）；`0634` 肩胛离地半途慢下（与 `0001` 45°顶点/`3202` 半程起坐相位区分）；`3156` 髋铰站姿单臂哑铃拉向肋（与 `0377` 双臂/`3161` 毛巾立柱器械区分）；`0422` 站姿空手扶上斜凳单臂弯举（与 `0421` 撑腿/`1663` 牧师凳支撑区分，slug `_v2` 避撞）；`0377` 髋铰俯身双肘外展划船（与 `0348` 俯卧凳/`0378` 侧平举轨迹体位区分）。

## 校验

- 双端 `exercise_metadata.json`：1302 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1302 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定；本轮 15 条均不在 curation 排除清单。
- 媒体仓：`media/` 2274 PNG（2244 + 30）；`catalog-review.html` 1352 记录含本轮 15/15。
- 回归：`tests/regression.cjs` 777/777；Flutter exercise-media 测试全过。
