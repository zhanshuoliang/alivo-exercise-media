# Round 30 — 负重/弹力带/杠杆机批（15 动作 × 4 轨 = 60 张）

日期：2026-11-17。选题原则：负重续补（取可单人呈现 5 条）+ 弹力带续补 + 杠杆机续补；smith 桶剩余 2 条均为上轮近重复排除项（实际已收尾），assisted 桶剩余条目均需第二人配合，本轮不取。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:3290 | weighted one hand pull up | weighted |
| exercises-dataset:3312 | weighted muscle up (on bar) | weighted |
| exercises-dataset:1767 | weighted triceps dip on high parallel bars | weighted |
| exercises-dataset:1310 | weighted drop push up | weighted |
| exercises-dataset:0833 | weighted donkey calf raise | weighted |
| exercises-dataset:1002 | band lying straight leg raise | band |
| exercises-dataset:0986 | band one arm overhead biceps curl | band |
| exercises-dataset:0990 | band one arm twisting seated row | band |
| exercises-dataset:0992 | band push sit-up | band |
| exercises-dataset:0998 | band side triceps extension | band |
| exercises-dataset:1300 | lever decline chest press | leverage machine |
| exercises-dataset:0604 | lever shrug | leverage machine |
| exercises-dataset:0601 | lever seated reverse fly (parallel grip) | leverage machine |
| exercises-dataset:0592 | lever preacher curl | leverage machine |
| exercises-dataset:2611 | lever horizontal one leg press | leverage machine |

选题备注：负重桶原剩 10 条——`1754` 凳上负重臂屈伸与刚绑定 `1755` 近重复排除、`3313`/`1767` 同为双杠臂屈伸只取 `1767`、`3641` 与已绑定 `3644` 近重复、`2371` 与刚绑定 `0845` 近重复、`0844` 实为侧平举排除；弹力带 `3116`/`3117`/`0983` 下拉系、`0984`/`0996` 髋内旋对、`0987`/`1001` 分腿蹲对、`0999`/`1000`/`1369` 提踵三胞胎、`0994`/`1016` 腕弯举对、`1007`/`1011` 扭转近重复延续不取。

## 产出（60/60 一次过审，零返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端（570 → **585**）
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` ×15 / `media-open/<base>_female.png` ×15：纯提示词独立生成（无参考图），无字标
- manifest：598 → **628**；`media/` 810 → **840** PNG

## 返工与插曲

- 本轮零生成失败、零错图：两波各 30 并发策略下 60/60 一次过审，为 r14 以来首个无返工轮次
- 工具插曲：`make_notice` 脚本首次运行在 manifest 写入后因 `media/` 缺男带标 PNG 崩溃（该批男版先 `cp` 失败顺序靠后），补拷后二次运行成功，但 manifest 被重复追加同一批 30 条——已去重（658 → 628 唯一条目），NOTICE 未受影响
- `new/` 暂存区残留的 r29 母版已清理，仅保留本轮 15 张

## 审核记录

逐组审核 15 组 × 4 轨共 60 张，全部通过。审核点：动作主体、器械呈现、单人画面、品牌字标（带标轨恰好一个小号白色 ALIVO；开源轨无字标）、全身入框、无拼贴/分屏。亮点：`1310` 爆发俯卧撑抓到双手离地瞬间；`0833` 驴式提踵髋前倾+腰背置片姿态准确；`0601` 反向飞鸟胸垫支撑+双臂后张正确。

## 接入

- 主仓：15 张男带标 PNG 母版按迁移规格打包（1024px + lossy WebP q82 method 4），写入双端 `exercise_media/`；`exercise_metadata.json` media 570 → **585**；双端 NOTICE + PROVENANCE.csv + `exercise_media_test.dart` 同步；Node 回归、Flutter 测试见提交前验证
- 媒体仓：`media/` +30、`media-open/` +30、manifest +30、双 NOTICE Round 30 分节、`docs/round30/` 归档 plan/batch + 60 份提示词 + 本报告
