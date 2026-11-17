# Round 77 — branded-only edition (2026-11-18)

Kai（男）/ Liv（女）双角色带标轨批次；开源轨继续暂停，后续独立补生成。

## 范围

- 选题：15 个 exercises-dataset 记录（站姿单臂侧平举、球上单臂/双臂弯举、坐姿双臂/内弯举、站姿交替侧举、站姿俯身单臂三头屈伸、站姿内弯举 v2、绳索侧屈、交叉卷腹、深蹲 potty squat、跑步、反向腿弯举机 v2、坐姿俯身三头屈伸、坐姿后摆）。
- 生成：30 张 PNG（男版 15 + 女版 15），一次过审，零返工。
- 绑定：男版 → 双端 App 目录（1024px lossy WebP q82/m4）；女版仅入媒体库备用，未绑定。
- 缓办：`3203`/`3016`/`3533`（与已绑 `0001`/`3119` 同文副本）；`1667`/`1675`/`0370`（名称与步骤语义冲突，留待冲突处理轮）；`3562` 黑名单永不绑定；9 条双人辅助拉伸持续缓办。

## 记录

| catalogId | slug | 动作 |
|---|---|---|
| exercises-dataset:0355 | dumbbell_one_arm_lateral_raise | 站姿单臂哑铃侧平举 |
| exercises-dataset:1668 | dumbbell_one_arm_seated_bicep_curl_on_exercise_ball | 球上坐姿单臂弯举 |
| exercises-dataset:0390 | dumbbell_seated_biceps_curl_on_stability_ball | 球上坐姿双臂弯举 |
| exercises-dataset:0391 | dumbbell_seated_curl | 坐姿哑铃弯举 |
| exercises-dataset:0393 | dumbbell_seated_inner_biceps_curl | 坐姿内弯举（上臂抵腿） |
| exercises-dataset:0415 | dumbbell_standing_alternate_raise | 站姿交替侧举 |
| exercises-dataset:1740 | dumbbell_standing_bent_over_one_arm_triceps_extension | 站姿俯身单臂三头屈伸 |
| exercises-dataset:2321 | dumbbell_standing_inner_biceps_curl_v_2 | 站姿内弯举 v2 |
| exercises-dataset:0221 | cable_side_bend_crunch_bosu_ball | 绳索侧屈卷腹 |
| exercises-dataset:0262 | cross_body_crunch | 交叉卷腹 |
| exercises-dataset:3119 | potty_squat | 下蹲 potty squat |
| exercises-dataset:0684 | run_equipment | 跑步（器械） |
| exercises-dataset:1766 | self_assisted_inverse_leg_curl_v2 | 反向腿弯举机（v2 slug） |
| exercises-dataset:1737 | dumbbell_seated_bent_over_triceps_extension | 坐姿俯身三头屈伸 |
| exercises-dataset:0394 | dumbbell_seated_kickback | 坐姿三头后摆 |

## 审核

30/30 逐张视觉审核通过。重点核对：`0355` 站姿单臂侧展空手扶髋（与 `0376` 双臂版/`0396` 坐姿版体位臂数区分）；`1668` 坐球单臂弯举空手撑腿（与 `0390` 双臂/`1659` 锤式握向区分）；`0390` 坐球双臂卷至肩（与 `1668` 单臂/`1650` 交替区分）；`0391` 坐凳双臂弯举（与 `0393` 上臂抵腿支撑/`0390` 球上支撑区分）；`0393` 坐姿上臂抵大腿内侧弯举（与 `0391` 悬空上臂/`1669` 单臂肘抵区分）；`0415` 站姿单臂侧举另臂垂侧（与 `0355` 空手扶髋/`0387` 坐姿前平举区分）；`1740` 站姿髋铰俯身单臂后伸（与 `1741` 双臂/`1739` 交替/`1737` 坐姿体位区分）；`2321` 站姿双臂外旋内弯举（与 `0416` 正握弯举手肘角度区分）；`0221` 低位滑轮侧倾拉手把（侧屈动作清晰，BOSU 未入镜）；`0262` 仰卧肘触对膝躯干扭转（与 `0456` 直臂/`2312` 对侧触膝腿位区分）；`3119` 深蹲底双臂前伸平衡（与 `3221` 半蹲深度/`2803` 扶柱支撑区分）；`0684` 原地高膝跑姿（与 `3638` 平板转跑体位区分）；`1766` 俯卧腿弯举机小腿卷向臀（与 `0697` 自重仰卧版器械区分，slug 加 `_v2` 避撞）；`1737` 坐姿前倾双臂后伸（与 `0394` 后摆行程/`1741` 站姿体位区分）；`0394` 坐姿俯身双臂向后踢出（与 `1737` 近亲，同轮双绑均独立成图）。

## 校验

- 双端 `exercise_metadata.json`：1287 条，byte-identical；id/localPath/sha256 零重复。
- 双端 `exercise_media/`：1287 WebP 各，SHA-256 与记录一致。
- 黑名单：`free-exercise-db:Kettlebell_Halo_With_Overhead_Extension`、`exercises-dataset:3562` 保持未绑定；本轮 15 条均不在 curation 排除清单。
- 媒体仓：`media/` 2244 PNG（2214 + 30）；`catalog-review.html` 1352 记录含本轮 15/15。
- 回归：`tests/regression.cjs` 777/777；Flutter exercise-media 测试 10/10。
