# Round 28 — 史密斯/弹力带/负重批（15 动作 × 4 轨 = 60 张）

日期：2026-11-16。选题原则：史密斯机续补 + 弹力带续补 + 负重补；assisted 桶剩余条目均需第二人配合，本轮不取。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:0754 | smith decline reverse-grip press | smith machine |
| exercises-dataset:0756 | smith hip raise | smith machine |
| exercises-dataset:0759 | smith incline shoulder raises | smith machine |
| exercises-dataset:1752 | smith machine incline tricep extension | smith machine |
| exercises-dataset:0769 | smith sprint lunge | smith machine |
| exercises-dataset:0969 | band alternating v-up | band |
| exercises-dataset:0972 | band bicycle crunch | band |
| exercises-dataset:0981 | band jack knife sit-up | band |
| exercises-dataset:1005 | band standing crunch | band |
| exercises-dataset:1012 | band twisting overhead press | band |
| exercises-dataset:0641 | otis up | weighted |
| exercises-dataset:0866 | weighted hanging leg-hip raise | weighted |
| exercises-dataset:3644 | weighted lunge with swing | weighted |
| exercises-dataset:0840 | weighted overhead crunch (on stability ball) | weighted |
| exercises-dataset:0854 | weighted standing hand squeeze | weighted |

选题备注：`0530`/`0656`/`0763`/`1394`/`0772` 延续排除（近重复/重复条目）；`1010`/`1023` 与已绑定 `1009` 直腿硬拉过近未取；`1626` 与 `1625` 同为下斜窄握系，本轮取其一未选。

## 产出（60/60 过审，1 轨返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，已绑定入 App 双端（540 → **555**，WebP 迁移后首个按新规格接入的批次）
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` ×15 / `media-open/<base>_female.png` ×15：纯提示词独立生成（无参考图），无字标
- manifest：538 → **568**；`media/` 750 → **780** PNG

## 返工与插曲

- 本轮将 60 个生成任务改分两波各 30 并发（上轮 60 并发曾致 4 个任务内存分配失败），两波均零崩溃完成
- `0754` 男带标：任务声称出图成功但日志未回传 PNG 路径。按"批次窗口内未被其他任务占用的唯一文件"从 `generated_images` 找回，目检为**错图**（登山者式而非下斜反握推）——时间窗口推断依旧不可靠，已重发该轨产出正确图像
- 教训复核：日志无路径时应直接重发，不要从 `generated_images` 推断归属（r27/r28 两次找回均为错图）

## 审核记录

逐组审核 15 组 × 4 轨共 60 张，全部通过。审核点：动作主体、器械呈现、单人画面、品牌字标（带标轨恰好一个小号白色 ALIVO；开源轨无字标）、全身入框、无拼贴/分屏。

## 接入

- 主仓：15 张男带标 PNG 母版按迁移规格打包（1024px + lossy WebP q82 method 4），写入双端 `exercise_media/`；`exercise_metadata.json` media 540 → **555**；双端 NOTICE + PROVENANCE.csv + `exercise_media_test.dart` 同步；Node 回归 777/777、Flutter 全过
- 媒体仓：`media/` +30、`media-open/` +30、manifest +30、双 NOTICE Round 28 分节、`docs/round28/` 归档 plan/batch + 60 份提示词 + 本报告
