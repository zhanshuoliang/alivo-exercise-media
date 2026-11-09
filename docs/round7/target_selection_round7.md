# 第七轮目标清单（25 项）与选取依据

日期：2026-11-09。来源：`exercises_zh.json`（exercises-dataset）与 `exercises_reviewed.json`（free-exercise-db）。全部条目共 1352，本清单开始时 155 条已有媒体（0404、0218 已在本轮先前批次绑定）。

## 选取规则

1. 仅选当前 `exercise_metadata.json` 中无 `media` 记录的动作。
2. 优先健身房常见的基础力量动作与主流器械变式（杠铃/哑铃/绳索/曲杠/史密斯/固定器械/自重/壶铃均匀分布）。
3. 排除与已绑定图近重复的条目：同动作同器械的 POV 变式（1461/1462）、同动作同器械的低差异变式（如 dumbbell standing biceps curl≈已绑定 0294、barbell high/low bar squat≈0043、straight leg deadlift≈0085）；另剔除 `cable curl`（0868，与 alivo:extra-011 直杆绳索弯举重复）和 `cable upright row`（0246，与 alivo:extra-019 直立划船、0123 宽握直立划船重复）。
4. 同一动作不同器械（如 barbell front raise vs 已绑定 dumbbell front raise）按历史先例保留——姿态与器械关系明显不同，属于不同教学场景，非凑数近重复。
5. 排除罕见/难核验变式（bosu/exercise ball 复合变式、with arm blaster、towel 变式、单腿复合动作、旋转复合动作等）。
6. 全部条目已核对目录 ID、器械标签与原始 `st` 步骤；候选均无 instructionSteps 维护覆盖（已逐一查 overrides）。

## 清单（25）

| catalogId | 文件名 | 动作 | 选取理由 |
| --- | --- | --- | --- |
| exercises-dataset:0041 | barbell_front_raise.png | 杠铃前平举 | 肩部经典动作；已有哑铃版，杠铃双手同杆属不同器械场景 |
| exercises-dataset:0080 | barbell_reverse_curl.png | 杠铃反握弯举 | 前臂/肱肌常用反握变式，正手握与已绑定正手弯举明显区分 |
| exercises-dataset:0095 | barbell_shrug.png | 杠铃耸肩 | 斜方经典动作；已有哑铃耸肩，杠铃版力学与姿态不同 |
| exercises-dataset:0091 | barbell_seated_overhead_press.png | 杠铃坐姿过顶推举 | 坐姿自由杠铃肩推；与史密斯坐姿、站姿宽握军推均不同 |
| exercises-dataset:0109 | barbell_overhead_triceps_extension.png | 杠铃站姿过顶臂屈伸 | 站姿双臂持短杠脑后臂屈伸；与哑铃单臂/仰卧版不同 |
| exercises-dataset:0046 | barbell_hack squat→barbell_hack_squat.png | 杠铃哈克深蹲 | 身后持杠经典动作；与史密斯/器械哈克机制完全不同 |
| exercises-dataset:0301 | dumbbell_decline_bench_press.png | 哑铃下斜卧推 | 哑铃卧推家族缺下斜；杠铃下斜已绑定 |
| exercises-dataset:0319 | dumbbell_incline_fly.png | 哑铃上斜飞鸟 | 飞鸟家族缺上斜；平凳飞鸟已绑定 |
| exercises-dataset:0351 | dumbbell_lying_triceps_extension.png | 哑铃仰卧臂屈伸 | 仰卧双手各持哑铃中立握；与杠铃碎颅者器械不同 |
| exercises-dataset:0426 | dumbbell_standing_overhead_press.png | 哑铃站姿过顶推举 | 站姿哑铃肩推；已有坐姿版，站姿为不同场景 |
| exercises-dataset:0447 | ez_barbell_curl.png | 曲杠弯举 | EZ 杆为极常见器械，W 形杆身是辨识点 |
| exercises-dataset:0179 | cable_low_fly.png | 绳索低飞鸟 | 低滑轮上收交叉；已绑定站姿飞鸟为高位下收，轨迹不同 |
| exercises-dataset:1359 | smith_bent_over_row.png | 史密斯架俯身划船 | 史密斯导轨上的俯身划船；自由杠铃版已绑定 |
| exercises-dataset:0753 | smith_decline_bench.png | 史密斯架下斜卧推 | 史密斯卧推家族缺下斜（平推/上斜已绑定） |
| exercises-dataset:0575 | lever_bicep_curl.png | 杠杆弯举 | 坐姿器械弯举机，极常见固定器械 |
| exercises-dataset:0581 | lever_high_row.png | 杠杆高划船 | 坐姿胸垫高划船机，与低位坐姿划船机型不同 |
| exercises-dataset:1299 | lever_incline_chest_press.png | 杠杆上斜推胸 | 器械推胸家族缺上斜角度（平推已绑定） |
| exercises-dataset:1451 | lever_seated_dip.png | 杠杆坐姿臂屈伸 | 坐姿下压臂屈伸机，常见固定器械；与双杠臂屈伸机制不同 |
| exercises-dataset:0129 | bench_dip.png | 凳上臂屈伸 | 自重屈膝凳上臂屈伸，常见家庭动作；与双杠 chest dip 器械不同 |
| exercises-dataset:0499 | inverted_row.png | 反向划船 | 自重水平划船（澳式引体），常见背部入门动作 |
| exercises-dataset:0277 | decline_crunch.png | 下斜卷腹 | 下斜凳卷腹，常见腹肌动作；地面卷腹已绑定 |
| exercises-dataset:0507 | jackknife_sit_up.png | 折刀仰卧起坐 | V-up 两端起，常见核心动作 |
| exercises-dataset:0271 | stability_ball_crunch.png | 卷腹瑜伽球 | 稳定球卷腹，常见腹肌变式 |
| exercises-dataset:0534 | kettlebell_goblet_squat.png | 壶铃高脚杯深蹲 | 壶铃持角把贴胸深蹲；与哑铃高脚杯器械明显不同 |
| free-exercise-db:Kettlebell_Halo | kettlebell_halo.png | 壶铃绕头 | 壶铃环绕头部，独特常见灵活性动作；接入 reviewed 源有 Pallof 先例 |

## 执行约定

- 每项最多 2 稿定向重生；仍无法严格核验则留 rejected 不强绑。
- 通过稿入 `new/`，拒稿入 `rejected/`，全部提示词、原始输出、审查结论记入 `reports/`。
- 分批绑定提交，全量审计基线为 153 + 本轮累计。
