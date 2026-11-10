# Round 14 — Kai/Liv 双角色同动作四轨批次

日期：2026-11-10

## 概要

首个双性别批次：15 个动作 ×（Kai 男 / Liv 女）×（带标 / 无标开源）= **60 张插图**，全部一次过审。

- 带标轨：30 张入 `media/`。男版（`*_male.png`，Kai）经 `add_bindings.cjs` 绑定入 App 双端目录（HarmonyOS `entry/` + Flutter `mobile/`），绑定数 333 → **348**。女版（`*_female.png`，Liv）为同动作性别变体资产，仅入媒体库、未绑定 App。
- 开源轨：30 张入 `media-open/`（男/女各 15），`manifest.json` 增至 **150 条**，纯提示词独立生成、无参考图。
- 审查页升级：同一动作最多并排展示 **4 个变体**（Kai 带标 / Liv 带标 / Kai 开源 / Liv 开源），每列独立判定键（`branded` / `brandedF` / `openM` / `openF`），开源聚合状态按组计。

## 动作清单（15）

| catalogId | 动作 | 变体 |
|---|---|---|
| exercises-dataset:1430 | chest dip (on dip-pull-up cage) | 4/4 |
| exercises-dataset:3302 | handstand | 4/4 |
| exercises-dataset:0253 | chin-ups (narrow parallel grip) | 4/4 |
| exercises-dataset:3543 | bodyweight drop jump squat | 4/4 |
| exercises-dataset:0803 | superman push-up | 4/4 |
| exercises-dataset:1761 | hanging oblique knee raise | 4/4 |
| exercises-dataset:1374 | box jump down with one leg stabilization | 4/4 |
| exercises-dataset:1399 | bench dip on floor | 4/4 |
| exercises-dataset:1201 | dumbbell burpee | 4/4 |
| exercises-dataset:0295 | dumbbell clean | 4/4 |
| exercises-dataset:0114 | barbell step-up | 4/4 |
| exercises-dataset:0053 | barbell jump squat | 4/4 |
| exercises-dataset:1410 | barbell lateral lunge | 4/4 |
| exercises-dataset:0029 | barbell clean-grip front squat | 4/4 |
| exercises-dataset:3327 | full planche push-up | 4/4 |

## 生成与审核

- 带标轨：ALIVO 编辑插图提示词（photorealistic-natural，灰色摄影棚，森林绿背心/炭灰短裤/深色运动鞋，唯一白色 ALIVO 字标）。男轨以既有 Kai 插图为风格参考；女轨以 Liv 三视图为风格参考。
- 开源轨：纯提示词独立生成（无任何参考图），纯色服装、全图零文字/标志/水印。
- 逐张人工审核 60/60 通过：姿态正确、单运动员、无裁切、字标/无标合规。
- 记录：`author: Paul Leung`，带标 `ALIVO-editorial`，开源 `CC-BY-4.0`；双 NOTICE 各记 30 条 SHA-256。
- 提示词存档：`docs/round14/prompts/{branded_male,branded_female,open_male,open_female}/` 各 15 份；`plan_round14.json` / `batch_round14.json` 同档。

## 回归

- Node 回归 774/774 通过
- Flutter `exercise_media_test.dart` 5/5 通过
- 双端 `exercise_media/` 各 349 个文件，metadata `media[]` 348 条

## 备注

- App 绑定仍按单记录模型（每 catalogId 一条 media 记录），男版为默认演示版本；女版入库备用，若后续 App 需要按性别切换插图可直接取用。
- R13 开源文件以 `_male` 后缀命名但无女版配对，页面上以"Kai · 无标开源版"单列呈现，语义正确。
