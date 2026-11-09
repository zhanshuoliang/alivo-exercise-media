# 第九轮自研动作插图报告（30 张）

- 日期：2026-11-09
- 主仓库提交：`ce5799e`（12 张）、`716696c`（18 张）
- 目标：30 项常用无插图动作，全部首稿过审
- 基线：183 条媒体绑定（`media-baseline-183.json`）→ 213 条

## 过审清单（按批次）

### 批次一（commit ce5799e，12 张）

| catalogId | 文件 | 动作 |
| --- | --- | --- |
| exercises-dataset:0648 | barbell_power_clean.png | 杠铃高翻（接杠位） |
| exercises-dataset:0069 | barbell_overhead_squat.png | 杠铃过顶深蹲（底部） |
| exercises-dataset:1700 | dumbbell_push_press.png | 哑铃借力推（锁定） |
| exercises-dataset:0287 | dumbbell_arnold_press.png | 哑铃阿诺德推举（顶点） |
| exercises-dataset:0128 | battle_ropes.png | 战绳（交替波浪） |
| exercises-dataset:0488 | bench_hyperextension.png | 挺身凳 45° 背伸 |
| exercises-dataset:3193 | glute_ham_raise.png | 臀腘挺身（GHD） |
| exercises-dataset:1759 | pistol_squat.png | 单腿深蹲（底部） |
| exercises-dataset:0471 | handstand_push_up.png | 靠墙倒立俯卧撑 |
| exercises-dataset:1401 | muscle_up.png | 双立臂（过杠过渡位） |
| exercises-dataset:3360 | bear_crawl.png | 熊爬 |
| exercises-dataset:0628 | band_monster_walk.png | 弹力带怪兽行走 |

### 批次二（commit 716696c，18 张）

| catalogId | 文件 | 动作 |
| --- | --- | --- |
| exercises-dataset:0554 | kettlebell_windmill.png | 壶铃风车 |
| exercises-dataset:0551 | kettlebell_turkish_get_up.png | 壶铃土耳其起立（高桥位） |
| exercises-dataset:0407 | dumbbell_side_bend.png | 哑铃侧屈 |
| exercises-dataset:1412 | barbell_wrist_curl.png | 杠铃腕弯举 |
| exercises-dataset:1411 | barbell_reverse_wrist_curl.png | 杠铃反握腕弯举 |
| exercises-dataset:0439 | dumbbell_zottman_curl.png | 哑铃佐特曼弯举 |
| exercises-dataset:0009 | assisted_dip_machine.png | 助力臂屈伸机 |
| exercises-dataset:1432 | assisted_pull_up_machine.png | 助力引体机 |
| exercises-dataset:0970 | band_assisted_pull_up.png | 弹力带助力引体 |
| exercises-dataset:0860 | cable_triceps_kickback.png | 绳索三头后摆 |
| exercises-dataset:0620 | bench_lying_leg_raise.png | 平板凳仰卧举腿 |
| exercises-dataset:1490 | standing_calf_raise_step.png | 台阶站姿提踵 |
| exercises-dataset:3643 | weighted_cossack_squat.png | 负重哥萨克深蹲 |
| exercises-dataset:1354 | medicine_ball_slam.png | 药球过顶砸 |
| exercises-dataset:1604 | worlds_greatest_stretch.png | 伟大拉伸 |
| exercises-dataset:1017 | band_y_raise.png | 弹力带 Y 举 |
| exercises-dataset:0098 | barbell_side_squat.png | 杠铃侧分腿蹲（宽站距） |
| exercises-dataset:1298 | kettlebell_floor_press.png | 壶铃单臂地板卧推 |

## 审核要点

- 全部 30 张逐图核验姿态/握法/器械关系/解剖/字标，无一返工。
- `0098` 一审时曾误判为与动作不符（图中宽站距被误读为相扑蹲），核对目录原文步骤“双脚分开比肩宽、膝盖向两侧推出”后确认图文一致，予以通过。
- `0471` 倒立俯卧撑的 ALIVO 字标因倒立体位呈倒置，为物理一致表现，通过。

## 验证

- `audit_round8.cjs`（基线 183）：total=213、183 旧绑定逐字节保留、30 新增与审核文件一致、两端字节相同、NOTICE/SHA-256 全有效。
- Node 回归：774/774。
- Flutter `exercise_media_test.dart`：全部通过。

## 附件

- `plan_round8.json`：30 项目标与动作描述（沿用上一轮工作区命名）。
- `prompts/`：逐图完整提示词。
- `batch_05.json` / `batch_06.json`：两批绑定清单（`add_bindings.cjs` 输入）。
- `tools/`：`add_bindings.cjs`、`audit_round8.cjs`（基线 `media-baseline-183.json`）。
