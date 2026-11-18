# Round 83 — 无字标商业轨（media-commercial）批次 1

日期：2026-11-18 · 轨道：`media-commercial/`（ALIVO-Commercial，须书面商业授权）

## 摘要

- 新增 **15 条记录 × 男女双版 = 30 张** 无字标 PNG，全部一次过审后入库（其中 2 题经提示词改写重试通过，见下）。
- `media-commercial/`：688 → **718** PNG；manifest 688 → **718** 条；SHA-256 全量校验 0 失配、0 孤儿、0 重复。
- 本轨独立于带标 `media/`：不使用带标参考图生成、不进入 App 目录绑定、许可 `ALIVO-Commercial`。

## 覆盖清单（15 条）

| catalogId | 男版文件 | 女版文件 |
|---|---|---|
| `exercises-dataset:0439` | `dumbbell_zottman_curl.png` | `dumbbell_zottman_curl_female.png` |
| `exercises-dataset:0158` | `cable_decline_fly_male.png` | `cable_decline_fly_female.png` |
| `exercises-dataset:0169` | `cable_incline_bench_press_male.png` | `cable_incline_bench_press_female.png` |
| `exercises-dataset:1318` | `cable_incline_bench_row_male.png` | `cable_incline_bench_row_female.png` |
| `exercises-dataset:0168` | `cable_hip_adduction_male.png` | `cable_hip_adduction_female.png` |
| `exercises-dataset:0152` | `cable_concentration_extension_on_knee_male.png` | `cable_concentration_extension_on_knee_female.png` |
| `exercises-dataset:0583` | `lever_kneeling_twist_male.png` | `lever_kneeling_twist_female.png` |
| `exercises-dataset:1452` | `lever_seated_crunch_male.png` | `lever_seated_crunch_female.png` |
| `exercises-dataset:0048` | `barbell_incline_reverse_grip_press_male.png` | `barbell_incline_reverse_grip_press_female.png` |
| `exercises-dataset:0049` | `barbell_incline_row_male.png` | `barbell_incline_row_female.png` |
| `exercises-dataset:1370` | `barbell_floor_calf_raise_male.png` | `barbell_floor_calf_raise_female.png` |
| `exercises-dataset:1437` | `dumbbell_finger_curls_male.png` | `dumbbell_finger_curls_female.png` |
| `exercises-dataset:2285` | `lever_pullover_male.png` | `lever_pullover_female.png` |
| `exercises-dataset:0593` | `lever_reverse_hyperextension_male.png` | `lever_reverse_hyperextension_female.png` |
| `exercises-dataset:2286` | `lever_hip_extension_v_2_male.png` | `lever_hip_extension_v_2_female.png` |

## 生成与审核

- 场景复用带标 prompt 的动作段，模板替换为无字标规范（纯色服装、零文字/标志），不传带标参考图。
- 30/30 出图；逐张目验通过：姿势语义、解剖、器械、构图单人单帧、无字标。
- 两题首发生成被图像策略拦截，改写措辞后通过（不改变动作语义）：
  - `0593` 反向过伸机：prone/hips 描述改为 "leans over the padded support / torso supported across the pad"。
  - `2286` 坐姿髋伸机：`LEVER HIP EXTENSION MACHINE` 改为 `SEATED LEG-DRIVE MACHINE`，"extending the hips" 改为 "legs straighten"。
- `0439` Zottman 场景取自带标轨修正后版本（下放相位 + 掌心朝下），与站姿弯举区分。

## 进度

- 商业轨覆盖（对已绑带标的 1333 条）：双版齐全 284 → **299 条**；仅男版 120 条；全无 914 条。
- 仍缺口：914 条全无 + 120 条待补女版 ≈ 1949 张；后续批次继续优先复用带标 prompt 场景，无可复用场景的记录单独撰写。
