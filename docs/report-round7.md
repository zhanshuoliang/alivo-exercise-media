# ALIVO 自研动作媒体 第七轮报告

日期：2026-11-09（Asia/Shanghai）
仓库：`D:\codex-temp\alivo`
基线：`origin/main @ 2773155ea88b6aaf28fdcbb966999d56af093b94`（第六轮末，153 张自研绑定）

## 本轮目标

按交接文档：先重生并严审 0404 平行握肩推、0218 宽握坐姿划船两个遗留缺口，再补充一批常用无图动作（目标 20–30 张，以实际过审为准）。沿用中性灰棚拍、自然色服装、ALIVO 字标；两端同步、NOTICE、SHA-256，保留旧绑定；不扩 wger、不接第三方动作媒体、不动 `wip-wger-before-selfmade` stash。

## 结果概览

- 本轮新增绑定：**27 张**（全部自审通过，首次生成即通过 20 张，定向重生通过 7 张中的 0404/0218 各用第 4 稿）。
- 媒体总数：**180**（153 历史 + 27 新增；历史 `wger_plank_346.png` 仍为未绑定遗留文件，不计入自研）。
- 100 项人工常用清单：100/100 有图（0404、0218 补齐后达成，本轮新增在此基础上继续扩展覆盖）。
- 提交：4 个小步提交（`9ec4cd8`、`4d23be3`、`5f8857d`、`c566345`），均为普通 commit。

## 逐批明细

### 第一批：遗留缺口补齐（commit `9ec4cd8`）

| catalogId | 文件 | 说明 |
| --- | --- | --- |
| exercises-dataset:0404 | dumbbell_neutral_shoulder_press.png | 第 4 稿通过；前 3 稿掌心朝前/握把被片遮挡被拒。近正面端视哑铃构图使掌心相对可核验 |
| exercises-dataset:0218 | cable_wide_seated_row.png | 第 4 稿通过；前 3 稿脚踏悬空/低滑轮—配重走线不清被拒。保留：踏板为一整块斜板、杆位在下胸/上腹交界 |

### 第二批：杠铃/哑铃/绳索 12 张（commit `4d23be3`）

0041 杠铃前平举、0080 杠铃反握弯举、0095 杠铃耸肩、0091 坐姿杠铃过顶推、0109 站姿过顶臂屈伸、0046 哈克深蹲、0301 哑铃下斜卧推、0319 哑铃上斜飞鸟、0351 哑铃仰卧臂屈伸、0426 哑铃站姿过顶推、0447 曲杠弯举、0179 绳索低飞鸟。全部首稿通过。

### 第三批：史密斯与器械 6 张（commit `5f8857d`）

1359 史密斯俯身划船、0753 史密斯下斜卧推、0575 器械弯举、0581 器械高位划船、1299 器械上斜推胸、1451 器械坐姿臂屈伸。全部首稿通过。

### 第四批：自重/核心/壶铃 7 张（commit `c566345`）

0129 凳上臂屈伸、0499 仰卧划船、0277 下斜卷腹、0507 两头起、0271 瑜伽球卷腹、0534 壶铃高脚杯深蹲、free-exercise-db:Kettlebell_Halo 壶铃光环。全部首稿通过。Kettlebell_Halo 为 reviewed 补充动作，获得 `ALIVO-editorial` 独立署名绑定；回归测试断言同步更新（该动作由"无媒体"改为期望 `kettlebell_halo.png`），另一条 Kettlebell_Halo_With_Overhead_Extension 仍保持未绑定。

## 审核要点

- 每张图对照目录维护的 `instructionSteps` 逐项核验：姿态、握法、器械连接（滑轮/配重块/导杆）、脚踏接触、全身与器材入镜、ALIVO 字标唯一。
- 静态图只表现动作一个瞬间；有歧义的图直接拒稿重生（0404×3、0218×3 拒稿保留在 `rejected/`）。
- `exerciseImageUrl` / `exerciseGifUrl` 保持为空；文件名符合 `exercise_media/[a-z0-9_-]+.png`。

## 验证

- `node --test tests/regression.cjs`：**774/774 通过**（首次运行 773/774，因 Kettlebell_Halo 绑定更新断言后全过）。
- `flutter test test/exercise_media_test.dart`：全部通过（媒体门控、真实目录加载、列表/详情署名、缺失媒体占位）。
- 全量审计（`audit_round7.cjs`，基线 153）：total=180，priorPreserved=153，newCount=27，两端字节一致、metadata/NOTICE 一致、SHA-256 全部有效、缺失目标无。
- 计量审计：1352 条 = 1250 次数 + 101 时长 + 1 未知，无回归。

## 已知事项

- 生成过程两次 WebSocket 超时自动回退 HTTPS，出图未受影响。
- Windows 下 LF→CRLF 警告无功能影响。
- 压缩/JPG 转换/在线下载方案本轮未实施，PNG 原样入库。
- `zhanshuoliang/alivo-exercise-media`（私有）资源仓库已建快照：media/ 全量图 + catalog/ 目录 JSON + docs/ 交接与轮次文档，随本轮结束同步至最新状态。
