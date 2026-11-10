# alivo-exercise-media

ALIVO 自研动作编辑插图与动作目录资源库。

- 快照基线：`alivo` 仓库 `origin/main` @ `9d25a98`（含第十轮 30 张动作插图）。
- 快照日期：2026-11-10（Asia/Taipei）。
- 图片为静态编辑插图，只表现动作某一瞬间，不是教学示范。
- **双版本授权**（2026-11-10 起）：
  - `media/`：带 ALIVO 字标版，`ALIVO-editorial` 许可，可自由使用（字标本身即署名），App 两端生产绑定使用此版本。
  - `media-open/`：无字标开源版，`CC-BY-4.0` 许可，作者 `Paul Leung`，使用时须署名；独立于 App 生产绑定，不进 App bundle。

## 目录结构

```text
media/       两端字节一致的 exercise_media 全量带标图片 + NOTICE.md 署名清单
media-open/  无字标开源版图片（CC-BY-4.0）+ 独立 NOTICE.md 署名清单
motion/      独立的自研动作 GIF 试稿、关键帧、许可与校验清单
catalog/     动作目录与媒体/计量元数据 JSON
docs/        交接文档、验收清单、历史报告、基线
docs/round7..10/ 各轮目标清单、生成计划、逐图提示词与审查、绑定/审计脚本
```

### media/（带标版）

- 245 个文件（244 张图片 + `NOTICE.md`）；其中 243 张为 ALIVO 自研编辑插图，`wger_plank_346.png` 为历史遗留的第三方 wger 文件（保留来源记录，不计入自研数量）。
- 每张自研图：1254×1254 PNG，中性灰棚拍背景、自然肤色与服装、深色背心短裤、服装带白色 `ALIVO` 字标。
- 许可 `ALIVO-editorial`，可自由使用；第七轮起新增记录 `author` 为 `Paul Leung`（早期记录仍为 `ALIVO`，历史不改写）。
- `NOTICE.md` 逐文件记录 catalogId 与 SHA-256；HarmonyOS 与 Flutter 两端图片逐字节相同。

### media-open/（无标开源版）

- 与 `media/` 同 catalogId、同文件名的无字标版本，纯色服装，全图无任何文字、标志或水印。
- 许可 **CC-BY-4.0**（https://creativecommons.org/licenses/by/4.0/），作者 **Paul Leung**；使用须署名 "Paul Leung — ALIVO open exercise illustrations" 并标明许可。
- `media-open/NOTICE.md` 逐文件记录 catalogId 与 SHA-256；本目录为独立发行物，不写入 App 的 `exercise_metadata.json`，不进入 App bundle。
- 按生成轮次逐步补齐，不一次性全量重制。

### motion/（GIF 试稿）

- [查看两个动作 GIF 样例](motion-preview.html)：徒手深蹲（`alivo:extra-022`）和俯卧撑（`exercises-dataset:0662`）。动作目录审查页的对应详情也可切换至 GIF。
- 样例由自研插图作风格参考，经 AI 生成动作关键帧及插帧制作；保留关键帧、提示词和 SHA-256，具体见 `motion/NOTICE.md` 与 `motion/manifest.json`。
- 样例独立于生产 `media[]` 绑定，供风格及效果评审；“ALIVO 编辑插图，非动作教学示范”。
- 更新清单后可运行 `python -B tools/build_motion_preview.py` 与 `python -B tools/build_catalog_page.py`，重新生成两个审查页面。

### catalog/

| 文件 | 内容 |
| --- | --- |
| `exercises_zh.json` | 主动作目录（`exercises-dataset:ID`，1324 条） |
| `exercises_extra.json` | 自编补充动作（`alivo:extra-*`，25 条） |
| `exercises_reviewed.json` | reviewed 补充动作（`free-exercise-db:*`，3 条） |
| `exercise_metadata.json` | 维护层覆盖（instructionSteps、reviewStatus 等）+ `media[]` 绑定记录（含 SHA-256） |
| `exercise_measures.json` | 逐条计量方式（次数/时长） |

目录共 1352 条稳定 ID，不合并、不改 ID；`exerciseImageUrl` / `exerciseGifUrl` 保持为空。

### docs/

- `handoff-20261109.md`：第七轮交接文档（风格、限制、流程）。
- `report-round6.md`：第六轮中文报告（20 张新增、审计与推送记录）。
- `common-media-checklist.md` / `common-media-selection.json`：100 项人工常用参考清单及其生成结果（当前 100/100 有图）。
- `media-baseline-153.json`：第六轮末的 153 项媒体基线（用于全量审计比对）。
- `remaining-common-targets.json`：交接时遗留的两个缺口（0404、0218，已在第七轮补齐）。

### docs/round7/

- `target_selection_round7.md`：第七轮 25 项目标清单与选取依据。
- `plan_round7.json`：每个目标的文件名、风格参考图、完整动作提示词。
- `prompts/exec_*.txt`：实际交给 ImageGen 的完整执行提示词。
- `round7_style_check.md`：0404/0218 两张风格确认稿的审查记录。
- `targets_round7.json`：本轮累计绑定目标 27 项（审计脚本读取）。
- `batch_01..04.json`：四批绑定清单（`add_bindings.cjs` 输入）。
- `../report-round7.md`：第七轮中文报告。
- `tools/`：`make_prompts.cjs`（生成提示词文件）、`add_bindings.cjs`（双端绑定写入）、`audit_round7.cjs`（全量媒体审计，基线 153）。

## 第八轮（2026-11-09）

- 新增 3 张自研静态图，现有 183 条绑定；catalog 仍为 1352 条；人工 100 项清单仍为 100/100。
- [逐图与 GIF 审查](docs/round8/review.md)、[本轮绑定与 SHA-256](docs/round8/accepted.json)、[下一批候选](docs/round8/next-targets.json)。
- [本轮完整提示词](docs/round8/prompts.json)（内置 ImageGen）；[媒体审计结果](docs/round8/audit-result.json)以接手的 `c566345` / 180 条为基线。
- 重跑审计：`python -B tools/audit_media.py --app-root D:/codex-temp/alivo --baseline c566345 --expected docs/round8/accepted.json`。该工具不写死轮次或旧基线数量。
- Node 774/774、Flutter 指定媒体和领域测试 28/28、清单、计量及 diff 检查通过。GIF 仍为独立 experimental 试稿，未经用户确认，不绑定生产。

## 第九轮（2026-11-09）

- 新增 30 张自研静态图（主仓库 `ce5799e` + `716696c`），现有 213 条绑定；catalog 仍为 1352 条。
- [本轮中文报告](docs/round9/report.md)：逐张清单、审核要点与验证结果。
- `docs/round9/`：`plan_round8.json`（30 项目标与动作描述）、`prompts/`（逐图完整提示词）、`batch_05.json`/`batch_06.json`（两批绑定清单）、`tools/`（`add_bindings.cjs`、`audit_round8.cjs`）、`media-baseline-183.json`（本轮审计基线）。
- 审计：total=213、183 旧绑定保留、30 新增与审核文件一致、两端字节相同、NOTICE/SHA-256 全有效；Node 774/774、Flutter 媒体测试全过。

## 第十轮（2026-11-10）

- 新增 30 张自研带标静态图（主仓库 `9d25a98`），现有 243 条绑定；catalog 仍为 1352 条。
- 本轮起确立双版本授权：新绑定记录 `author: Paul Leung`、`license: ALIVO-editorial`；同批动作另生成无字标开源版入 `media-open/`（CC-BY-4.0）。
- `docs/round10/`：`plan.json`（30 项目标与动作描述）、`prompts/`（无标版逐图提示词）、`bindings.json` / `targets.json`（绑定清单）、`audit_round10.cjs`、`media-baseline-213.json`（本轮审计基线）。
- 审计：total=243、213 旧绑定保留、30 新增与审核文件一致、两端字节相同、NOTICE/SHA-256 全有效；Node 774/774、Flutter 媒体测试全过。

## 使用约定

- 新增图片文件名规则：`exercise_media/[a-z0-9_-]+.(png|jpg)`。
- 不接入第三方动作媒体、不扩展 wger；每张图须对照目录维护步骤与器械/握法逐项核验。
- 生产仓库仍是 `zhanshuoliang/alivo`，本仓库为资源整理快照，不替代生产资源目录。
