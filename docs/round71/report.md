# Round 71 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（凳缘臂屈伸、墙壁/箱上俯卧撑、星形跳、侧桥、仰卧腿臀举/肘触膝、绳索转体/划船/腕弯举/前肩举、屈膝反向划船、哑铃对握上斜推/台阶分腿蹲）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 排除：`0656`（与已绑 `0655` 同名同文副本）、`1394`（与已绑 `0763` 同名同文副本）——slug 撞名，留待后续以独立 slug 处理；本轮替换为 `2300`/`0164`。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:3287 | elbow_dips | 凳缘臂屈伸 |
| exercises-dataset:0658 | push_up_wall_v_2 | 墙壁俯卧撑 v2 |
| exercises-dataset:3785 | incline_push_up_on_box | 箱上上斜俯卧撑 |
| exercises-dataset:3223 | star_jump_male | 星形跳 |
| exercises-dataset:0705 | side_bridge_v_2 | 侧桥 v2 |
| exercises-dataset:0865 | lying_leg_hip_raise | 仰卧腿臀举 |
| exercises-dataset:2312 | lying_elbow_to_knee | 仰卧肘触膝 |
| exercises-dataset:0862 | cable_twist_up_down | 绳索上下转体 |
| exercises-dataset:1323 | cable_rope_seated_row | 绳式坐姿划船 |
| exercises-dataset:0233 | cable_standing_rear_delt_row_with_rope | 站姿绳索后束划船 |
| exercises-dataset:0224 | cable_standing_back_wrist_curl | 站姿背后腕弯举 |
| exercises-dataset:2300 | inverted_row_bent_knees | 屈膝反向划船 |
| exercises-dataset:0164 | cable_front_shoulder_raise | 绳索前肩举 |
| exercises-dataset:1623 | dumbbell_palms_in_incline_bench_press | 哑铃对握上斜推 |
| exercises-dataset:2812 | dumbbell_step_up_split_squat | 哑铃台阶分腿蹲 |

## 审核

30/30 逐张视觉审核通过。重点核对：`3287` 凳缘撑+直腿跟着地屈臂下放（与已绑地板臂屈伸支撑面区分）；`0658` 手撑墙身体斜直线（与已绑地面俯卧撑支撑面区分）；`3785` 手撑箱沿上斜直线（与已绑地面/球上俯卧撑支撑面区分）；`3223` 腾空四肢展开 X 形（与已绑深蹲跳姿态区分）；`0705` 前臂撑髋离地侧直线（与已绑侧平板髋内收/外展变体动作区分）；`0865` 平躺双腿垂直朝天髋将离（与已绑上斜腿臀举支撑面区分）；`2312` 扭转肘触对膝+另腿伸直悬空（与已绑抱膝/标准卷腹区分）；`0862` 面向机器双手胸前躯干旋出（与已绑 `0243` 侧对机器转体朝向区分）；`1323` 坐姿脚踏板绳索拉向腹（与已绑 `1320` 交叉握绳/`0239` 直背划船握具体态区分）；`0233` 站姿绳索拉向上胸肘外展（后束划船）；`0224` 低位绳索直杆掌心朝下仅屈腕（与已绑杠铃/史密斯背后腕弯举器械区分）；`2300` 屈膝脚踏地胸拉向杠（与已绑直腿反向划船/`0498` 悬带版腿位器械区分）；`0164` 背向低位轮臂前平举至肩高；`1623` 上斜凳掌心相对哑铃推起（与已绑上斜锤式单臂推臂数/握向区分）；`2812` 前脚踩台后腿在后哑铃垂侧分腿蹲（与已绑 `2796` 上步弓步动作模式区分）。

## 校验

- 双端 `exercise_metadata.json`：1197 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1197 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
