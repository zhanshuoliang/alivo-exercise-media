# Round 16 — 双角色四轨批（15 动作 × 4 版本 = 60 张）

日期：2026-11-10

## 选题

从 `exercises-dataset` 未绑定清单中选 15 个动作，补此前基本无配图的器械空白（壶铃、史密斯架、杠杆器械、弹力带、瑜伽球、药球）：

| catalogId | 动作 |
|---|---|
| exercises-dataset:0533 | kettlebell front squat（壶铃前蹲） |
| exercises-dataset:0541 | kettlebell one arm row（壶铃单臂划船） |
| exercises-dataset:0550 | kettlebell thruster（壶铃火箭推） |
| exercises-dataset:0532 | kettlebell figure 8（壶铃8字） |
| exercises-dataset:0752 | smith deadlift（史密斯架硬拉） |
| exercises-dataset:0755 | smith hack squat（史密斯架哈克深蹲） |
| exercises-dataset:0751 | smith close-grip bench press（史密斯架窄距卧推） |
| exercises-dataset:0576 | lever chest press（杠杆推胸） |
| exercises-dataset:2287 | lever alternate leg press（杠杆交替腿举） |
| exercises-dataset:1254 | band bench press（弹力带卧推） |
| exercises-dataset:0977 | band front lateral raise（弹力带前侧平举） |
| exercises-dataset:0997 | band shoulder press（弹力带肩推） |
| exercises-dataset:0272 | crunch on stability ball, arms straight（瑜伽球卷腹臂直） |
| exercises-dataset:1333 | exercise ball back extension with arms extended（瑜伽球背伸展配臂伸展） |
| exercises-dataset:0640 | one arm slam with medicine ball（单臂药球砸） |

## 产出（60/60 一次过审）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` / `<base>_female.png` ×30：无标开源轨，纯提示词独立生成，CC-BY-4.0 · Paul Leung

视觉审核：带标轨仅含合规 "ALIVO" 字标；开源轨全图零文字零标志零水印；四轨动作姿态均符合描述（史密斯架导轨结构、腿举机、弹力带固定方式、瑜伽球/药球器械均正确呈现）。

## 授权与记录

- 带标轨：`ALIVO-editorial`，作者 Paul Leung，SHA-256 见 `media/NOTICE.md` Round 16 分节
- 开源轨：`CC-BY-4.0`，作者 Paul Leung，`media-open/manifest.json` 210 条、SHA-256 见 `media-open/NOTICE.md`

## 集成

- App 绑定 363 → 378（仅男带标主媒体，App 为单媒体记录模型）
- `prompts/` 存档 60 份生成提示词（male/female/open_male/open_female 四组）
