# Round 29 — 史密斯收尾/负重/弹力带/杠杆机批（15 动作 × 4 轨 = 60 张）

日期：2026-11-17。选题原则：史密斯机收尾（可取 3 条）+ 负重续补 + 弹力带续补 + 杠杆机首次多取；assisted 桶剩余条目均需第二人配合，本轮不取。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:1309 | smith wide grip decline bench press | smith machine |
| exercises-dataset:1395 | smith seated one leg calf raise | smith machine |
| exercises-dataset:0771 | smith standing back wrist curl | smith machine |
| exercises-dataset:2987 | weighted close grip chin-up on dip cage | weighted |
| exercises-dataset:0845 | weighted russian twist (legs up) | weighted |
| exercises-dataset:0849 | weighted seated twist (on stability ball) | weighted |
| exercises-dataset:0850 | weighted side bend (on stability ball) | weighted |
| exercises-dataset:1755 | weighted tricep dips | weighted |
| exercises-dataset:0971 | band assisted wheel rollerout | band |
| exercises-dataset:0980 | band bent-over hip extension | band |
| exercises-dataset:0985 | band kneeling twisting crunch | band |
| exercises-dataset:0989 | band one arm twisting chest press | band |
| exercises-dataset:1008 | band step-up | band |
| exercises-dataset:0587 | lever military press | leverage machine |
| exercises-dataset:1349 | lever reverse t-bar row | leverage machine |

选题备注：史密斯桶原剩 5 条，两条主动避开后取 3——`1396` smith toe raise 与已绑定 `0773` 站姿提踵步骤实质相同（近重复排除）；`1625` 下斜窄握推与 `1309` 下斜宽握推、已绑定 `0754` 下斜反握推三个下斜推同轮过密，只取 `1309`。`0530`/`0656`/`0763`/`1394`/`0772`/`1010`/`1023`/`1626` 延续排除；弹力带 `3116`/`3117`/`0983` 下拉系与已绑定下拉过近、`0984`/`0996` 髋内旋对、`0987`/`1001` 分腿蹲对、`0999`/`1000`/`1369` 提踵三胞胎本轮均未取。

## 产出（60/60 过审，2 轨返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端（555 → **570**）
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` ×15 / `media-open/<base>_female.png` ×15：纯提示词独立生成（无参考图），无字标
- manifest：568 → **598**；`media/` 780 → **810** PNG

## 返工与插曲

- `0989`/`1349` 开源男轨：首跑与第一次重试均因 imagegen 网络错误未出图（`network error`，共失败两次），第三次重试产出正确图像通过审核
- 审核备注：`1395` 开源女版非工作脚仍搭在踏板上（未悬空），画面仍可辨认为单腿提踵工作侧，未返工记入报告
- 并发策略延续两波各 30（上两轮验证稳定），本波零内存崩溃
- 插曲：一次手动重试命令因 `&` 链丢失工作目录，误在无关仓库下执行 cat（目标文件不存在，无实际副作用）；后续重试命令改为 `bash -c` 内显式 cd

## 审核记录

逐组审核 15 组 × 4 轨共 60 张，全部通过。审核点：动作主体、器械呈现、单人画面、品牌字标（带标轨恰好一个小号白色 ALIVO；开源轨无字标）、全身入框、无拼贴/分屏。

## 接入

- 主仓：15 张男带标 PNG 母版按迁移规格打包（1024px + lossy WebP q82 method 4），写入双端 `exercise_media/`；`exercise_metadata.json` media 555 → **570**；双端 NOTICE + PROVENANCE.csv + `exercise_media_test.dart` 同步；Node 回归、Flutter 测试见提交前验证
- 媒体仓：`media/` +30、`media-open/` +30、manifest +30、双 NOTICE Round 29 分节、`docs/round29/` 归档 plan/batch + 60 份提示词 + 本报告
