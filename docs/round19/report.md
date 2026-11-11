# Round 19 — 有氧/小器械补全批（15 动作 × 4 轨 = 60 张）

日期：2026-11-10。选题原则：补此前未配图的有氧器械与小器械——跳绳、绳索高锚点、奥杆、地雷管、健身车、弹力带、滚轴、雪橇机、瑜伽球系列。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| alivo:extra-007 | jump rope | rope |
| exercises-dataset:0609 | london bridge | cable rope |
| exercises-dataset:0637 | olympic barbell triceps extension | olympic barbell |
| alivo:extra-012 | standing split stance single arm landmine press | landmine |
| exercises-dataset:2138 | stationary bike run v. 3 | stationary bike |
| exercises-dataset:3236 | resistance band hip thrusts on knees | resistance band |
| exercises-dataset:3007 | resistance band leg extension | resistance band |
| exercises-dataset:2203 | roller seated shoulder flexor depresor retractor | roller |
| exercises-dataset:2209 | roller seated single leg shoulder flexor depresor retractor | roller |
| exercises-dataset:1384 | hack one leg calf raise | sled machine |
| exercises-dataset:0740 | sled 45° leg wide press | sled machine |
| exercises-dataset:0655 | push-up on stability ball | stability ball |
| exercises-dataset:1296 | exercise ball pike push up | stability ball |
| exercises-dataset:2297 | stability ball crunch, full range, hands behind head | stability ball |
| exercises-dataset:0675 | reverse hyper extension on stability ball | stability ball |

## 产出（60/60 过审；1 组初版返工）

- `media/<base>_male.png` ×13：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端，绑定数 408 → 421
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定；`jump_rope_extra007_female.png`、`landmine_press_female.png` 对齐已绑定文件名 base
- `media-open/<base>_male.png` + `<base>_female.png` ×30：纯提示词独立生成（无参考图），CC-BY-4.0，`media-open/manifest.json` 270 → 300
- `extra-007`（跳绳）与 `extra-012`（地雷管）男版早前已绑定（`jump_rope_extra007.png`、`landmine_press.png`），本轮为其补齐女带标 + 开源双轨，男带标不重复入库

## 审核要点

- 跳绳：绳弧过顶、前掌轻跳、手柄腰位。
- 伦敦桥：高位滑轮绳索、背对前倾、肘屈贴头侧。
- 奥杆臂屈伸：窄握过头、上臂竖直、杆落头后。
- 地雷管：枢轴底座、前后分腿站、单臂前上推。
- 健身车：直立坐姿、握把踩踏中程。
- 弹力带跪姿臀推：带绕髋前侧、髋部前送伸展；站姿腿伸展踝带前伸绷直。
- 滚轴两件：坐姿直腿压轴下压回缩；单腿版一腿屈一腿直持轴前伸。
- 哈克机单腿提踵：肩垫承托、单脚踏板边沿、另腿抬起。
- 45° 宽距腿举：双脚宽距上沿、腿蹬伸展。
- 瑜伽球俯卧撑：双手球顶支撑平板、俯卧撑中程；派克俯卧撑倒 V、脚踩球顶、头贴近地（高难度姿态四轨均准确）。
- 球上反向挺身：躯干俯卧球上、双手撑地、双腿后伸抬起。
- **返工**：`stability_ball_crunch` 初版 4 张为上下双画面拼图（"full range" 被理解成两阶段对比），重写提示词限定"单帧、卷起顶点瞬间"后重生成 4 张，全部通过。

## 归档

- `plan_round19.json` / `batch_round19.json`：目标、文件名、绑定清单。
- `prompts/male/`、`prompts/female/`、`prompts/open_male/`、`prompts/open_female/`：四轨逐图完整提示词（各 15 份；`exec_2297.txt` 为修订后的单帧版本）。

## 验证

- 双端 `exercise_media/` 各 422 文件，新增 13 张逐字节相同；`exercise_metadata.json` 绑定 408 → 421。
- `media/` 513 个文件、`media-open/` 302 个文件；双 NOTICE 各记 Round 19 分节 + SHA-256（带标 28 条、开源 30 条）。
- 审查页女带标列规则扩展：绑定文件名无 `_male` 后缀时按 `base+_female.png` 匹配性别变体（extra-007/012 可正常显示女版）。
- Node 回归：与 Round 17/18 相同的 3 项预存/手动集成失败（`coach-postgres`、`sync-postgres` 需 SSH host 参数；`terrain-preview` 预存 manifest hash 不符），其余全过；Flutter 媒体测试 5/5。
