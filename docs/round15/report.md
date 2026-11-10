# Round 15 — 双角色四轨批（15 动作 × 4 版本 = 60 张）

日期：2026-11-10

## 选题

从 `exercises-dataset` 未绑定清单中选 15 个常用器械/自重动作，覆盖胸、肩、臂、背、腿后链、核心：

| catalogId | 动作 |
|---|---|
| exercises-dataset:0122 | barbell wide bench press（杠铃宽卧推） |
| exercises-dataset:0116 | barbell straight leg deadlift（杠铃直腿硬拉） |
| exercises-dataset:0120 | barbell upright row（杠铃直立划船） |
| exercises-dataset:0023 | barbell alternate biceps curl（杠铃交替弯举） |
| exercises-dataset:0061 | barbell lying triceps extension（杠铃仰卧臂屈伸） |
| exercises-dataset:0302 | dumbbell decline fly（哑铃下斜飞鸟） |
| exercises-dataset:0330 | dumbbell incline triceps extension（哑铃上斜臂屈伸） |
| exercises-dataset:0290 | dumbbell bench seated press（哑铃坐姿肩推） |
| exercises-dataset:0160 | cable floor seated wide-grip row（绳索地板坐姿宽握划船） |
| exercises-dataset:0219 | cable shoulder press（绳索肩推） |
| exercises-dataset:0868 | cable curl（绳索弯举） |
| exercises-dataset:0664 | push-up to side plank（俯卧撑侧平板） |
| exercises-dataset:0796 | standing wheel rollerout（站姿健腹轮滚出） |
| exercises-dataset:0090 | barbell seated good morning（杠铃坐姿早安式） |
| exercises-dataset:0075 | barbell rear delt raise（杠铃俯身后束举） |

## 产出（60/60 一次过审）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` / `<base>_female.png` ×30：无标开源轨，纯提示词独立生成，CC-BY-4.0 · Paul Leung

视觉审核：带标轨仅含合规 "ALIVO" 字标；开源轨全图零文字零标志零水印；四轨动作姿态均符合描述。

## 授权与记录

- 带标轨：`ALIVO-editorial`，作者 Paul Leung，SHA-256 见 `media/NOTICE.md` Round 15 分节
- 开源轨：`CC-BY-4.0`，作者 Paul Leung，`media-open/manifest.json` 180 条、SHA-256 见 `media-open/NOTICE.md`

## 集成

- App 绑定 348 → 363（仅男带标主媒体，App 为单媒体记录模型）
- `prompts/` 存档 60 份生成提示词（male/female/open_male/open_female 四组）
