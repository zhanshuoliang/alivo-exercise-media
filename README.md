# alivo-exercise-media

ALIVO 自研动作编辑插图与动作目录资源库（私有）。

- 快照基线：`alivo` 仓库 `origin/main` @ `c566345`（含第七轮全部 4 个媒体提交）。
- 快照日期：2026-11-09（Asia/Shanghai）。
- 媒体许可：`ALIVO-editorial`；界面文案：“ALIVO 编辑插图，非动作教学示范”。图片为静态编辑插图，只表现动作某一瞬间，不是教学示范。

## 目录结构

```text
media/      两端字节一致的 exercise_media 全量图片 + NOTICE.md 署名清单
catalog/    动作目录与媒体/计量元数据 JSON
docs/       交接文档、验收清单、历史报告、基线
docs/round7/ 第七轮目标清单、生成计划、逐图提示词与审查、绑定/审计脚本
```

### media/

- 181 个文件（180 张图片 + `NOTICE.md`）；其中 180 张为 ALIVO 自研编辑插图，`wger_plank_346.png` 为历史遗留的第三方 wger 文件（保留来源记录，不计入自研数量）。
- 每张自研图：1254×1254 PNG，中性灰棚拍背景、自然肤色与服装、深色背心短裤、服装带白色 `ALIVO` 字标。
- `NOTICE.md` 逐文件记录 catalogId 与 SHA-256；HarmonyOS 与 Flutter 两端图片逐字节相同。

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

## 使用约定

- 新增图片文件名规则：`exercise_media/[a-z0-9_-]+.(png|jpg)`。
- 不接入第三方动作媒体、不扩展 wger；每张图须对照目录维护步骤与器械/握法逐项核验。
- 生产仓库仍是 `zhanshuoliang/alivo`，本仓库为资源整理快照，不替代生产资源目录。
