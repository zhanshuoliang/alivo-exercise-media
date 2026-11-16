# Round 24 — EZ 杠收尾 + 壶铃/史密斯续补批（15 动作 × 4 轨 = 60 张）

日期：2026-11-16。选题原则：EZ 杠铃器械桶收尾（卧姿臂屈伸/面推/JM 推/臂托板弯举）+ 壶铃推举补全 + 史密斯机续补。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:3010 | ez bar lying bent arms pullover | ez barbell |
| exercises-dataset:1748 | ez bar lying close grip triceps extension behind head | ez barbell |
| exercises-dataset:0448 | ez barbell decline close grip face press | ez barbell |
| exercises-dataset:0449 | ez barbell incline triceps extension | ez barbell |
| exercises-dataset:0450 | ez barbell jm bench press | ez barbell |
| exercises-dataset:2404 | ez-bar biceps curl (with arm blaster) | ez barbell |
| exercises-dataset:0520 | kettlebell alternating press | kettlebell |
| exercises-dataset:0525 | kettlebell bottoms up clean from the hang position | kettlebell |
| exercises-dataset:0531 | kettlebell extended range one arm press on floor | kettlebell |
| exercises-dataset:0547 | kettlebell seesaw press | kettlebell |
| exercises-dataset:0545 | kettlebell plyo push-up | kettlebell |
| exercises-dataset:0746 | smith back shrug | smith machine |
| exercises-dataset:0750 | smith chair squat | smith machine |
| exercises-dataset:1433 | smith front squat (clean grip) | smith machine |
| exercises-dataset:0775 | smith upright row | smith machine |

选题备注：初拟 `exercises-dataset:0530`（kettlebell double windmill）因与 Round 23 已入库的 `0517`（kettlebell advanced windmill）姿态过近，替换为 `0531`；`extra-007`/`extra-012`（已完成四轨）与 `0656`（`0655` 重复条目）、`0763/1394` 近重复对在候选池阶段即排除。

## 产出（60/60 一次过审，无返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端，绑定数 480 → 495
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` + `<base>_female.png` ×30：纯提示词独立生成（无参考图），CC-BY-4.0，`media-open/manifest.json` 418 → 448

## 审核要点

- EZ 杠六件（器械桶收尾）：仰卧屈臂上拉（仰卧曲杆过头后落）、仰卧窄握颈后臂屈伸（窄握杆落头后）、下斜窄握面推（下斜凳腿托固定、杆落前额）、上斜臂屈伸（45° 上斜凳曲杆过头落头后）、JM 卧推（仰卧肘贴身杆落上胸）、臂托板弯举（arm blaster 托板固定上臂、曲杆弯举中程——带标轨 ALIVO 字标位于托板，合规）。
- 壶铃五件：交替推（一臂过头锁定一臂肩位持铃，交替相位清晰）、底朝上悬垂翻（铃球倒置于把手上方收位）、地板单臂伸展推（仰卧屈膝单臂垂直锁定）、跷跷板推（一臂锁定一臂肩位+躯干微转）、爆发俯卧撑（双手撑壶铃把手平板支撑位——四轨定格为支撑顶点而非腾空瞬间，动作主体与器械呈现准确，特此注明）。
- 史密斯四件：后耸肩（背向导轨、杆在臀后、耸肩顶点）、椅式深蹲（前移站姿斜靠导杆深屈膝）、前蹲挺举握法（指尖托杆高肘深蹲位）、直立划船（窄握肘高拉至胸骨位）。
- 全 60 张均为单帧编辑插图，无拼图/多画面；带标轨单一 ALIVO 字标，开源轨完全无标识。
- 收集插曲：`1748` 开源女版日志未回传 PNG 路径，从生成会话缓存目录按时间戳定位并补回暂存，经审核为正确的颈后臂屈伸画面。

## 归档

- `plan_round24.json` / `batch_round24.json`：目标、文件名、绑定清单（15 条，无重复条目冲突）。
- `prompts/m/`、`prompts/f/`、`prompts/open_m/`、`prompts/open_f/`：四轨逐图完整提示词（各 15 份）。

## 回归

- Flutter 媒体测试 5/5；Node 文件级回归仅 3 项已知失败（`coach-postgres`、`sync-postgres` 需 SSH host 参数的手动集成测试；`terrain-preview` 预存 manifest hash 不符，与媒体无关）。
