# Round 74 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（凳上反握/坐姿中立腕弯举、绳索交叉飞鸟、哑铃直腿硬拉、屈膝臀桥、悬垂屈膝举腿、斜肌卷腹 v2、Scott 坐姿推举、杠杆坐姿卷腹 v2、站姿提踵、球上锤式弯举、球上单臂飞鸟、站姿单臂反握弯举、单腿台阶提踵、半蹲跳）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 更正：extras 池（25 条）其实早已以 `alivo:` 前缀全部绑定；本轮全部从 exercises-dataset 剩余池选题。
- 缓办：`0474`/`0140`/`0139`（与已绑悬垂直腿举/正握/反握引体同文）、`0634`/`0735`/`3016`/`0262`/`3201`（与已绑卷腹同文族）、`0812`/`0814`/`1753`（单凳臂屈伸同文族）、`0816`/`1386`/`2318`/`0221`/`0350`/`0668`/`1295`/`0377`/`0380`/`3156`/`3162`（近亲或同文）、`1737`/`0394`/`0398`（坐姿后摆近 `1730`）——留待后续批次以独立 slug/语义差异化处理。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0368 | dumbbell_over_bench_revers_wrist_curl | 凳上反握哑铃腕弯举 |
| exercises-dataset:0397 | dumbbell_seated_neutral_wrist_curl | 坐姿中立握腕弯举 |
| exercises-dataset:0155 | cable_cross_over_variation | 绳索交叉飞鸟变式 |
| exercises-dataset:0434 | dumbbell_straight_leg_deadlift | 哑铃直腿硬拉 |
| exercises-dataset:0484 | hip_raise_bent_knee | 屈膝臀桥 |
| exercises-dataset:1764 | hanging_leg_hip_raise | 悬垂屈膝举腿 |
| exercises-dataset:1495 | oblique_crunch_v_2 | 仰卧斜肌卷腹 v2 |
| exercises-dataset:2397 | dumbbell_scott_press | Scott 坐姿哑铃推举 |
| exercises-dataset:3760 | lever_seated_crunch_v_2 | 杠杆坐姿卷腹机 v2 |
| exercises-dataset:1397 | standing_calves | 站姿自重提踵 |
| exercises-dataset:1659 | dumbbell_hammer_curl_on_exercise_ball | 球上锤式弯举 |
| exercises-dataset:1288 | dumbbell_one_arm_fly_on_exercise_ball | 球上单臂飞鸟 |
| exercises-dataset:0425 | dumbbell_standing_one_arm_reverse_curl | 站姿单臂反握弯举 |
| exercises-dataset:0409 | dumbbell_single_leg_calf_raise | 台阶单腿哑铃提踵 |
| exercises-dataset:3222 | semi_squat_jump_male | 半蹲跳 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0368` 前臂搁凳掌心朝下（与已绑 `0367` 掌心朝上配对握向相反）；`0397` 前臂搁腿+掌心相对中立握（与 `0368`/`0385` 握向区分）；`0155` 高位滑轮双臂胸前合拢（与已绑坐姿/单臂飞鸟体位区分）；`0434` 平背髋铰哑铃垂腿前（与已绑 `1023` 弹力带硬拉器械区分）；`0484` 膝-肩直线臀桥（与 `0865` 仰卧腿垂直举腿姿区分）；`1764` 悬垂屈膝大腿至水平（与 `0475` 直腿 L 形/ `2333` 悬带版区分）；`1495` 肩胛离地躯干侧旋（与 `0495` 上斜转体坐起/ `2801` 仰卧举腿转体体位区分）；`2397` 坐姿双哑铃全伸过顶（与 `0869` 器械肩推/`1620` 球上单臂锤式推区分）；`3760` 背垫固定胸卷向膝（与 `0595` 胸垫式卷腹机区分）；`1397` 站姿足尖顶点（与 `0108` 杠铃版/`0409` 台阶单腿版器械与腿数区分）；`1659` 坐球中立握双臂弯举（与凳/牧师凳弯举支撑面区分）；`1288` 球撑上背髋桥单臂侧展（与 `1279` 上斜凳单臂飞鸟支撑面区分）；`0425` 站姿掌心朝下弯举（与 `0428`/`1675` 反握族支撑与臂数区分）；`0409` 掌踏台阶缘+扶墙+单手持哑铃（与 `1387` 平地版/`3240` 球墙版支撑区分）；`3222` 半蹲腾空顶点（与已绑深蹲站姿/ `3223` 星形跳空中姿态区分）。

## 校验

- 双端 `exercise_metadata.json`：1242 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1242 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定。
- 审查页 `catalog-review.html`：15/15 记录就位。
- Node 回归：777/777；Flutter 媒体/目录测试：通过。

## 许可

ALIVO-editorial；作者 Paul Leung；源 `https://openai.com/policies/terms-of-use/`。
编辑插图非教学示范。
