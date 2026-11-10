# 第 12 轮：热身 / 拉伸 / 灵活性专题批次

日期：2026-11-10

## 范围

从审查页 `warmup` 标记的 66 条热身/拉伸/灵活性动作中，选取 30 个最常用、覆盖面最广的目标，生成双版本（ALIVO 带标 + 无标开源）编辑插图。

已排除已配图动作：inchworm（1471）、world greatest stretch（1604）、neck side stretch（1403，第 11 轮）。

## 目标清单（30 项）

动态热身：inchworm v. 2（3698）、walking high knees lunge（3655）、high knee against wall（3636）、dynamic chest stretch（1167）、circles knee stretch（0257）、ankle circles（1368）、wrist circles（1428）

静态拉伸：hamstring stretch（1511）、leg up hamstring stretch（1576）、runners stretch（1585）、seated glute stretch（1424）、seated piriformis stretch（2567）、butterfly yoga pose（1494）、seated wide angle pose sequence（1587）、rocking frog stretch（2571）、iron cross stretch（1419）、intermediate hip flexor and quad stretch（1564）、lying (side) quads stretch（0613）、standing hamstring and calf stretch with strap（1599）、calf stretch with hands against wall（1377）、standing calves calf stretch（1398）、kneeling lat stretch（1346）、overhead triceps stretch（0643）、rear deltoid stretch（0669）、chest and front of shoulder stretch（1271）、side push neck stretch（0716）、side wrist pull stretch（0721）、upper back stretch（1365）、spine stretch（1363）、seated lower back stretch（0690）

## 生成

- 带标版：`prompts12/`，`codex exec -i <inchworm.png 风格参考>` + stdin 提示词，`photorealistic-natural`，要求恰好一个白色 ALIVO 字标
- 无标版：`prompts12_open/`，纯提示词无参考图，要求全图零文字/标志/水印
- 两版独立生成；无标版多名运动员为女性形象，属正常独立创作

## 审核结果

- 带标版 **30/30 一次过审**：姿态准确、解剖正常、全身入框、字标合规、无杂字
- 无标版 **30/30 一次过审**：全图零文字/标志/水印、姿态准确、风格统一

## 接入

- App（HarmonyOS `entry/` + Flutter `mobile/`）：30 张 PNG 双端落位，`media` 绑定 273 → **303**
- 新记录 `author: Paul Leung`、`license: ALIVO-editorial`、逐文件 SHA-256
- `media-open/`：90 条 manifest、NOTICE 表 90 行 SHA-256，`license: CC-BY-4.0`
- Flutter `exercise_media_test.dart` 补 30 条映射

## 验证

- Node 回归 **774/774**、Flutter 媒体测试 **5/5**
- 审查页重建：1352 记录，热身标记 66（其中 33 条现有图），开源版 90

## 归档

`docs/round12/`：plan_round12.json、batch_round12.json、prompts12/（30 份带标提示词）、prompts12_open/（30 份无标提示词）、本报告
