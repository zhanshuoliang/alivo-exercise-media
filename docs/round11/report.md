# 第 11 轮自研动作插图报告（2026-11-10）

## 结果

- **带标版（`media/`）**：30 张，全部一次过审并接入 App 两端（`zhanshuoliang/alivo` 提交 `469c92e`）。
- **无标开源版（`media-open/`）**：同 30 个动作独立生成（纯提示词、无参考图），30 张全部过审入库。
- 新接入带标记录：`author: Paul Leung`、`license: ALIVO-editorial`；开源版：`license: CC-BY-4.0`、`author: Paul Leung`。
- 审核要点（两版均逐张核验）：动作姿态准确、器械关系正确、全身与器械入框、解剖正常；带标版仅一枚白色 ALIVO 字标；开源版全图无任何文字/标志/水印。
- 触发来源：`exercises-dataset:0001`（3/4 sit-up）来自审查页 `imageRequests`（GitHub Issue #2）；其余 29 项按常见度与类目平衡补齐。

## 批次清单

| catalogId | 动作 | 类目 |
| --- | --- | --- |
| exercises-dataset:0001 | 3/4 sit-up | 腰腹核心 |
| exercises-dataset:3296 | front lever | 自重技巧 |
| exercises-dataset:3297 | back lever | 自重技巧 |
| exercises-dataset:3299 | full planche | 自重技巧 |
| exercises-dataset:3294 | archer push up | 俯卧撑变体 |
| exercises-dataset:3293 | archer pull up | 引体变体 |
| exercises-dataset:0677 | ring dips | 吊环 |
| exercises-dataset:0283 | diamond push-up | 俯卧撑变体 |
| exercises-dataset:1273 | clap push up | 爆发力俯卧撑 |
| exercises-dataset:0500 | isometric wipers | 核心保持 |
| exercises-dataset:3217 | modified hindu push-up (male) | 俯卧撑变体 |
| exercises-dataset:3418 | l-pull-up | 引体变体 |
| exercises-dataset:3304 | skin the cat | 自重技巧/灵活 |
| exercises-dataset:2963 | captains chair straight leg raise | 器械核心 |
| exercises-dataset:0127 | barbell zercher squat | 杠铃深蹲 |
| exercises-dataset:0051 | barbell jefferson squat | 杠铃深蹲 |
| exercises-dataset:3017 | barbell pendlay row | 杠铃划船 |
| exercises-dataset:0074 | barbell rack pull | 杠铃硬拉 |
| exercises-dataset:1756 | barbell single leg deadlift | 单腿硬拉 |
| exercises-dataset:0052 | barbell jm bench press | 杠铃卧推变体 |
| exercises-dataset:1316 | barbell bent arm pullover | 杠铃拉伸/背 |
| exercises-dataset:0521 | kettlebell alternating renegade row | 壶铃复合 |
| exercises-dataset:1423 | reverse hyper on flat bench | 后侧链 |
| exercises-dataset:1270 | cable upper chest crossovers | 绳索夹胸 |
| exercises-dataset:0235 | cable standing shoulder external rotation | 肩袖/热身 |
| exercises-dataset:0299 | dumbbell cuban press | 哑铃肩 |
| exercises-dataset:3548 | dumbbell single arm overhead carry | 负重行走 |
| exercises-dataset:1353 | medicine ball catch and overhead throw | 药球爆发力 |
| exercises-dataset:2139 | hands bike | 上肢功率车（有氧） |
| exercises-dataset:1403 | neck side stretch | 热身/拉伸 |

## 验证

- Node 回归：774/774 通过；Flutter `exercise_media_test.dart`：5/5 通过。
- `media/`、`media-open/`、双端 `exercise_metadata.json`、NOTICE SHA-256 逐条一致。
- 审查页已重新生成：带标/无标双栏同审 + "热身/拉伸"独立分类（按动作名规则识别，66 条，标为推断待复核）。

## 备注

- 两版为独立生成，运动员外观在两版间不保证一致（以服装与风格规范定义角色）。
- `neck_side_stretch` 属热身/拉伸类，该类的完整配图计划见后续批次。
