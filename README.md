# ALIVO Exercise Media

ALIVO 自研健身动作编辑插图库与动作目录数据——1,352 条稳定动作记录，配套自研插图、逐文件 SHA-256 完整性记录与公开审查工具。

> A curated library of original exercise editorial illustrations for the ALIVO fitness catalog: 1,352 stable exercise records, two licensing tracks (ALIVO-Branded-Free / ALIVO-Commercial unbranded edition), per-file SHA-256 integrity records, and a public review tool.

## 在线浏览与审查

**[动作目录审查页](https://zhanshuoliang.github.io/alivo-exercise-media/catalog-review.html)** — 浏览全部动作记录、配图状态与四版本对比；支持逐图判定（通过/拒绝）、导岀审查 JSON、一键生成 GitHub Issue 反馈。

**[动作 GIF 预览](https://zhanshuoliang.github.io/alivo-exercise-media/motion-preview.html)** — 自研动作 GIF 试稿（评审样例）。

## 插图规格

- 1254×1254 PNG，中性灰棚拍背景，统一服装规范（深灰绿背心 + 炭灰短裤 + 深色运动鞋）。
- **AI 辅助生成 + 逐张人工审核**；同一动作最多四个版本（男/女 × 带标/无标）。
- 图为静态**编辑插图**，表现动作某一瞬间，不是教学示范。
- 演示运动员为数字角色 **Kai**（男）与 **Liv**（女），角色基准见 `character/roster.md` 与 `character/` 三视图。

## 双轨授权

| 目录 | 内容 | 许可 |
|---|---|---|
| `media/` | 带 ALIVO 字标的编辑插图（男/女版） | `ALIVO-Branded-Free`：**可自由使用**，唯一义务是保留画面中的 ALIVO 字标（不得去除、遮挡或替换） |
| `media-commercial/` | 无字标商业版（男/女版），纯提示词独立生成，全图零文字零标志 | `ALIVO-Commercial`：**须商业授权**，作者 **Paul Leung**，授权洽谈 licensing@alivo.kuaige.cloud |

### 授权说明

- **免费使用** → 直接用 `media/` 带标版：保留画面字标即可，无需另署名、无需付费。
- **无标使用** → `media-commercial/` 目录图片须先取得 `ALIVO-Commercial` 书面商业授权；未授权不得复制、分发、展示或二次创作。
- 历史说明：2026-11-18 之前文档曾把无标版误标为 CC-BY-4.0「开源版」，现已订正为商业授权；`media-open/` 目录同步更名为 `media-commercial/`。

### 直接引用图片

图片文件也可通过 GitHub raw 访问（审查页即采用此方式）：

```
https://raw.githubusercontent.com/zhanshuoliang/alivo-exercise-media/main/media-commercial/<文件名>.png
https://raw.githubusercontent.com/zhanshuoliang/alivo-exercise-media/main/media/<文件名>.png
```

## 完整性与溯源

- `media/NOTICE.md`、`media-commercial/NOTICE.md`：逐文件记录 catalogId 与 SHA-256，按生成批次分节。
- `media-commercial/manifest.json`：无标商业版的机器可读索引（catalogId、文件名、作者、许可、SHA-256、审核日期）。
- `docs/round*/`：各批次的选题清单、逐图完整生成提示词、绑定清单与中文报告——每张图可沿 catalogId 溯源。

## 目录结构

```text
media/          带标编辑插图（ALIVO-Branded-Free，自由使用须留字标）+ NOTICE.md
media-commercial/  无字标商业版（ALIVO-Commercial，须购授权）+ manifest.json + NOTICE.md
character/      演示运动员角色资产（Kai / Liv 三视图双版本）+ roster.md + NOTICE.md
motion/         自研动作 GIF 试稿、关键帧与校验清单（评审样例，非生产资产）
catalog/        动作目录与媒体/计量元数据（生产仓库的镜像快照）
docs/           交接文档、各批次归档（选题/提示词/报告）、人工参考清单
tools/          审查页与预览页的生成脚本
catalog-review.html  动作目录审查页（GitHub Pages 部署）
motion-preview.html  GIF 预览页
```

`catalog/` 为 ALIVO 生产仓库目录数据的镜像快照，权威源以应用仓库为准；目录共 1,352 条稳定 ID，不合并、不改 ID。

## 当前覆盖

- 带标插图 **2336 个文件**（其中 **1333 条**已绑定为 App 生产媒体，HarmonyOS 与 Flutter 两端逐字节一致；历史遗留第三方 wger 文件已于 2026-11-18 全量审计时移除）。
- 无标商业版 **688 张**（ALIVO-Commercial，须授权）。
- **282 个动作**具备男/女 × 带标/无标四版本；另 120 个动作有无标男版待补女版、3 个待补男版、928 个待补双版；无标轨持续按批次扩充。
- 配图仍在按批次扩充；各批次进展见 `docs/round*/report.md`。

## 审查与反馈

- 审查页中每张图可独立判定"通过 / 拒绝"，判定结果可导出 JSON 或一键提交 GitHub Issue。
- 对插图的修改建议、动作姿势指正、授权问题，欢迎在 [Issues](https://github.com/zhanshuoliang/alivo-exercise-media/issues) 反馈。

## 约定

- 文件名规则：`[a-z0-9_-]+_(male|female).png`，按 catalogId 稳定对应。
- 不接入第三方动作媒体；每张图须对照目录动作步骤与器械/握法逐项核验。
- 历史遗留 `wger_plank_346.png`（从未绑定、未入包）已于 2026-11-18 全量审计时移除；第三方素材不再扩展。
