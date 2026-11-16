# Round 27 — 史密斯/弹力带/负重批（15 动作 × 4 轨 = 60 张）

日期：2026-11-16。选题原则：史密斯机续补 + 弹力带续补 + 负重补；assisted 桶剩余条目均需第二人配合（throw down / 双人拉伸），本轮不取。

## 选题（15）

| catalogId | 动作 | 器械 |
|---|---|---|
| exercises-dataset:0758 | smith incline reverse-grip press | smith machine |
| exercises-dataset:0764 | smith reverse-grip press | smith machine |
| exercises-dataset:0774 | smith standing military press | smith machine |
| exercises-dataset:1426 | smith seated wrist curl | smith machine |
| exercises-dataset:0773 | smith standing leg calf raise | smith machine |
| exercises-dataset:1308 | smith wide grip bench press | smith machine |
| exercises-dataset:0974 | band close-grip pulldown | band |
| exercises-dataset:1013 | band underhand pulldown | band |
| exercises-dataset:0991 | band pull through | band |
| exercises-dataset:0988 | band one arm standing low row | band |
| exercises-dataset:0976 | band concentration curl | band |
| exercises-dataset:0832 | weighted crunch | weighted |
| exercises-dataset:3670 | weighted decline sit-up | weighted |
| exercises-dataset:0851 | weighted sissy squat | weighted |
| exercises-dataset:2135 | weighted front plank | weighted |

选题备注：`0530`、`0656` 延续排除（近重复/重复条目）；`0763`/`1394` 同名对、`0772` 站姿颈后军事推（与已绑定 `0747` 过近）主动避开；assisted 桶 10 条剩余均为双人配合动作，暂不取。

## 产出（60/60 过审，2 轨返工）

- `media/<base>_male.png` ×15：Kai 带标，风格参考 `media/handstand_male.png`，待绑定入 App 双端（主仓 WebP 迁移提交后接入，预计绑定数 525 → 540）
- `media/<base>_female.png` ×15：Liv 带标，风格参考 `media/handstand_female.png`，性别变体未绑定
- `media-open/<base>_male.png` ×15 / `media-open/<base>_female.png` ×15：纯提示词独立生成（无参考图），无字标
- manifest：508 → **538**；`media/` 720 → **750** PNG

## 返工与插曲

- 首批 4 个开源男轨任务（`0774`/`0974`/`0976`/`1308`）因并发过高内存分配失败（`memory allocation of 1073741824 bytes failed`），统一重试后全部出图通过
- `0773` 男带标、`0976` 女带标：任务声称出图成功但日志未回传 PNG 路径；按日志内 UUID 从会话目录取回的文件经目检为**错图**（分别为单腿壶铃硬拉、倒立参考图）——日志中的 UUID 是 codex 会话 id 而非图像会话目录，不能用来定位产物。两轨重发后正确出图通过
- 收集器改进（`collect27.cjs`）：优先只认"回复整行即 PNG 路径"的任务答复格式；回退到日志扫描时校验文件 mtime 在批次窗口内，并输出 SUSPECT 清单——从机制上规避 r26 的目录转储误拾问题

## 审核记录

60 张逐张目检：动作/器械/姿态/解剖/字标（带标轨恰一处 ALIVO 小字标；开源轨无任何文字商标）全部合规。0758/0764 反握方向在成图分辨率下不易辨认，但器械/凳角/推举构图与动作语义一致，判过（如需精确反握呈现可在后续审查中提出）。

## 验证

- `media/` 750 PNG、`media-open/` 538 PNG、manifest 538 条
- 双 NOTICE Round 27 分节 + 60 条 SHA-256
- `docs/round27/`：plan/batch + 60 份提示词（male/female/open_male/open_female 各 15）+ 本报告
- App 端绑定暂缓：主仓 PNG→WebP 迁移与 Round 26 绑定尚未提交；Round 27 男带标 WebP 打包与双端接入将在迁移提交后进行
