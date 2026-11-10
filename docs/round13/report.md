# 第 13 轮报告 · 热身补完 + 常见动作（30 项）

日期：2026-11-10

## 范围

- **25 项单人热身/拉伸补完**：`warmup` 规则标记中尚未配图且不依赖双人辅助的全部动作（四肢跪姿拉伸、背阔肌/胸大肌靠墙、推墙小腿、绳索小腿、椅子腘绳肌、瑜伽球系列 ×6、腓骨肌/胫骨后肌、仰卧手抓大脚趾式、泡沫轴系列 ×4、坐姿小腿、侧卧地板、站姿侧屈、三头肌、负重弓步拉伸、肩胛引体）。
- **5 项常见动作**：跳蹲 v.2（0513）、杰克波比（0501）、滑冰跳（3361）、杠铃臀桥（1409）、凳上双腿臀桥（3523）。
- **未纳入**：8 项 assisted 双人辅助拉伸，留作双人插图专项批。

## 产出

- 带标版 30 张（`new/` → `media/`）：逐张人工审核通过——姿态正确、ALIVO 字标合规、无杂字。
- 无标开源版 30 张（`new_open/` → `media-open/`）：独立生成、纯提示词无参考图；逐张人工审核通过——全图零文字/标志/水印。
- App 绑定 303 → **333**；HarmonyOS/Flutter 双端各 334 个媒体文件。
- `media-open/manifest.json` 90 → **120** 条；`media-open/NOTICE.md` 同步 120 行 SHA-256。
- App NOTICE 新增"第十三批"分节 + 30 条 SHA-256。

## 同批附带：运动员名册扩容

- 新增女运动员 **Liv · 莉芙** 三视图双版本（`character/turnaround_female_*`），外观锚点"棕色低马尾"，定位灵活性与柔韧担当。
- 男运动员命名 **Kai · 凯**，首席演示运动员。
- `character/roster.md` 建立名册；审查页"运动员三视图"弹层改为名册布局（每角色一卡：名字/定位/性格 + 双版本三视图）。

## 审核记录

- 带标版：30/30 一次过审。
- 无标版：30/30 一次过审（含 Liv 出镜的柔韧/瑜伽球镜头）。
- 女运动员三视图：2/2 过审。

## 测试

- `node tests/regression.cjs`：774 pass / 0 fail。
- `flutter test mobile/alivo_app/test/exercise_media_test.dart`：5/5。

## 存档

- `plan_round13.json`、`batch_round13.json`
- `prompts/`（30 份带标提示词）、`prompts_open/`（30 份无标提示词）
- 女运动员三视图提示词：`character/prompts/turnaround_female_{branded,open}.txt`

## 备注

- 无标版中 Kai/Liv 分工：Liv 主力柔韧镜头，Kai 主力力量/器械镜头；名册规则见 `character/roster.md`。
- 8 项 assisted 双人动作待专项批。
