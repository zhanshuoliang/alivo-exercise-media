# alivo-exercise-media

ALIVO 自研动作编辑插图与动作目录资源库。

- 快照基线：`alivo` 仓库 `origin/main` @ `8a03365`（含第八轮 3 张弹力带动作插图）。
- 快照日期：2026-11-09（Asia/Taipei）。
- 媒体许可：`ALIVO-editorial`；界面文案：“ALIVO 编辑插图，非动作教学示范”。图片为静态编辑插图，只表现动作某一瞬间，不是教学示范。

## 目录结构

```text
media/      两端字节一致的 exercise_media 全量图片 + NOTICE.md 署名清单
motion/     独立的自研动作 GIF 试稿、关键帧、许可与校验清单
catalog/    动作目录与媒体/计量元数据 JSON
docs/       交接文档、验收清单、历史报告、基线
docs/round7/ 第七轮目标清单、生成计划、逐图提示词与审查、绑定/审计脚本
```

### media/

- 185 个文件（184 张图片 + `NOTICE.md`）；其中 183 张为 ALIVO 自研编辑插图，`wger_plank_346.png` 为历史遗留的第三方 wger 文件（保留来源记录，不计入自研数量）。
- 每张自研图：1254×1254 PNG，中性灰棚拍背景、自然肤色与服装、深色背心短裤、服装带白色 `ALIVO` 字标。
- `NOTICE.md` 逐文件记录 catalogId 与 SHA-256；HarmonyOS 与 Flutter 两端图片逐字节相同。

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

## 使用约定

- 新增图片文件名规则：`exercise_media/[a-z0-9_-]+.(png|jpg)`。
- 不接入第三方动作媒体、不扩展 wger；每张图须对照目录维护步骤与器械/握法逐项核验。
- 生产仓库仍是 `zhanshuoliang/alivo`，本仓库为资源整理快照，不替代生产资源目录。
