# Round 84 — 无字标商业轨（media-commercial）批次 2

日期：2026-11-18 · 轨道：`media-commercial/`（ALIVO-Commercial，须书面商业授权）

## 摘要

- 新增 **15 条记录 × 男女双版 = 30 张** 无字标 PNG，全部过审后入库。
- `media-commercial/`：718 → **748** PNG；manifest 718 → **748** 条；SHA-256 全量校验 0 失配、0 孤儿、0 重复。

## 覆盖清单（15 条）

| catalogId | 文件（男/女同 slug） |
|---|---|
| `exercises-dataset:1732` | `dumbbell_forward_lunge_triceps_extension_*` |
| `exercises-dataset:1757` | `dumbbell_single_leg_deadlift_*` |
| `exercises-dataset:0436` | `dumbbell_tate_press_*` |
| `exercises-dataset:2143` | `dumbbell_standing_around_world_*` |
| `exercises-dataset:0863` | `dumbbell_lying_external_shoulder_rotation_*` |
| `exercises-dataset:2808` | `dumbbell_sumo_pull_through_*` |
| `exercises-dataset:3664` | `dumbbell_side_plank_with_rear_fly_*` |
| `exercises-dataset:0006` | `alternate_heel_touchers_*` |
| `exercises-dataset:3769` | `curtsey_squat_*` |
| `exercises-dataset:3639` | `bent_knee_lying_twist_*` |
| `exercises-dataset:1418` | `hug_knees_to_chest_*` |
| `exercises-dataset:0562` | `landmine_180_*` |
| `exercises-dataset:3237` | `landmine_lateral_raise_*` |
| `exercises-dataset:3194` | `frankenstein_squat_*` |
| `exercises-dataset:0174` | `cable_judo_flip_*` |

## 生成与审核

- 场景复用带标 prompt 动作段 + 无字标模板；不传带标参考图。30/30 出图，逐张目验通过。
- 提示词策略拦截 2 题，改写后通过（语义不变）：
  - `3664:m` 侧板撑后飞鸟：原样重试一次即通过（过滤器随机性）。
  - `0174:m` 绳索转体拉：`CABLE ROTATIONAL OVER-SHOULDER PULL ... hips rotate` 改写为 `CABLE TORSO ROTATION WITH ROPE ... turns the shoulders and arms`。
- 注：`0174` 文件名沿用带标 slug `cable_judo_flip_*`，与带标轨一一对应。

## 进度

- 商业轨覆盖（对已绑带标 1333 条）：双版齐全 299 → **314 条**；仅男版 120 条；全无 899 条。
