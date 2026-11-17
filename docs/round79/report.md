# Round 79 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 尾部记录（正握引体、站姿单臂划船、上斜哑铃推、站姿单臂/双臂反握弯举、锤式-正握弯举、俯身后束飞鸟、站姿集中弯举、抱头半程起坐、自重深蹲、小幅度卷腹、臀桥、原地慢跑、仰卧起坐 v2、扶墙三头撑）。尾部同文/近亲记录全部以各自独立 slug 绑定。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 缓办：`3016`/`1753`/`0814`/`0812` 收尾轮；`3562` 黑名单永不绑定；9 条双人辅助拉伸持续缓办。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0140 | biceps_pull_up | 正握引体 |
| exercises-dataset:3162 | bodyweight_standing_one_arm_row | 站姿单臂划船 |
| exercises-dataset:0316 | dumbbell_incline_breeding | 上斜哑铃推（源名 breeding，按步骤为卧推下放相位） |
| exercises-dataset:1667 | dumbbell_one_arm_reverse_spider_curl | 站姿单臂反握弯举（名为 spider，步骤实为站姿单臂） |
| exercises-dataset:0370 | dumbbell_peacher_hammer_curl | 站姿锤式-正握弯举（名为 preacher，步骤实为站姿双臂） |
| exercises-dataset:0380 | dumbbell_rear_lateral_raise | 俯身后束飞鸟 |
| exercises-dataset:1675 | dumbbell_reverse_spider_curl | 站姿双臂反握弯举（名为 spider，步骤实为站姿双臂） |
| exercises-dataset:0418 | dumbbell_standing_concentration_curl | 站姿集中弯举（空手撑腿） |
| exercises-dataset:3203 | prisoner_half_sit_up_male | 抱头半程起坐（45°） |
| exercises-dataset:3533 | quads | 自重深蹲 |
| exercises-dataset:3201 | quarter_sit_up | 小幅度卷腹（肩胛刚离地） |
| exercises-dataset:0668 | rear_decline_bridge | 臀桥 |
| exercises-dataset:3656 | short_stride_run | 原地短步幅慢跑 |
| exercises-dataset:0735 | sit_up_v_2 | 仰卧起坐 v2（卷至 45°） |
| exercises-dataset:0816 | triceps_press | 扶墙三头撑 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0140` 正握下巴过杠（与 `0139` 窄距反握/`0674` 反握/`1763` 肩宽正握握法握距区分）；`3162` 髋铰站姿单臂哑铃拉向肋空手撑腿（与 `3156` 窄距/`3161` 毛巾立柱支撑方式区分）；`0316` 45°凳双臂哑铃下放至胸侧（与 `0325` 推举上伸/`0328` 肩推轨迹相位区分）；`1667` 站姿单臂反握卷至肩（与 `1675` 双臂/`1672` 牧师凳体位臂数区分）；`0370` 站姿双臂锤式转握卷至肩（与 `0429` 牧师凳/`2294` Zottman 支撑与握法区分）；`0380` 髋铰俯身双臂侧展至水平（与 `0377` 划船拉肘/`0378` 后束飞鸟同族已绑体位一致、哑铃轨迹区分）；`1675` 站姿双臂掌心朝前卷至肩（与 `1667` 单臂臂数区分）；`0418` 微俯站姿空手撑腿单臂卷至肩（与 `0421` 直腿版体位/`0422` 扶凳支撑区分）；`3203` 双手抱头躯干卷至 45°（与 `0634` 慢下相位/`0001` 全程幅度区分）；`3533` 自重深蹲大腿近水平双臂前伸（与 `3119` potty squat 同族已绑、`3221` 半蹲深度区分）；`3201` 肩胛刚离地小幅度（与 `0001` 45°/`3203` 半程幅度区分）；`0668` 臀桥膝-肩直线手置体侧（与 `0484` 屈膝臀桥腿部姿势区分）；`3656` 原地慢跑单膝抬起摆臂（与 `3637` 健腹轮/`3638` 登山跑姿式区分）；`0735` 仰卧卷至 45°手抱头（与 `0001` 全程/`3203` 半程幅度区分）；`0816` 掌贴墙身体斜直屈肘下放（与 `0658` 墙壁俯卧撑臂距/发力肌群区分）。

## 校验

- 双端 `exercise_metadata.json`：1317 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1317 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定；本轮 15 条均不在 curation 排除清单。
- 媒体仓：`media/` 2304 PNG（2274 + 30）；`catalog-review.html` 1352 记录含本轮 15/15。
- 回归：`tests/regression.cjs` 777/777；Flutter exercise-media 测试全过。
