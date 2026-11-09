# ALIVO 自制动作媒体报告 · 第六轮

报告日期：2026-11-09（Asia/Shanghai）。仓库：`D:\codex-temp\alivo`；起点：`240c3210364e9d92976b456443e9aef2e21a42ff`。

## 结果

- 本轮通过审核并接入 20 张原创图，其中 2 张补齐上轮未通过的空中单车和固定器械单臂侧向下拉；本轮后续批次接入 18 张。原有 133 项绑定的记录和图片保持完整。
- 当前动作目录共 1352 条，其中 153 条已绑定 ALIVO-editorial 图片，1199 条暂无图。既有 42 项维护参考已全部配图；人工选择的 100 项常用场景验收清单中 98/100 已配图。这些是人工参考，不代表真实用户使用排行。
- 保留中性灰背景、自然肤色和服装色彩、深色运动服及 ALIVO 字标；图片注明“ALIVO 编辑插图，非动作教学示范”。未扩展 wger，未接入 Gym Visual / ExerciseDB 图片；exerciseImageUrl 和 exerciseGifUrl 继续为空。
- 通过项目维护层修正 0313 锤式弯举、0599 坐姿腿弯举、0404 哑铃平行握肩推、0572 辅助反手引体的冲突步骤；保留原始目录及历史 ID。跳绳搜索显示“分步说明”和“简要说明”，保留两个原条目。无图时有清晰占位和提示，跳绳器械标签统一为中文。
- 两端 NOTICE 的三条旧记录原有乱码标点已修复；未修改其目录 ID、许可或哈希。`wip-wger-before-selfmade` stash 未使用。

## 本轮新增绑定

| 动作 | catalogId | 两端相同路径 | SHA-256 |
| --- | --- | --- | --- |
| 固定器械单臂侧向宽握下拉 | `exercises-dataset:1347` | `exercise_media/lever_one_arm_lateral_pulldown_v3.png` | `aebf93c3a8b085f0c8f1575712738cb2ac860ab56262ad695c64ef58906212f4` |
| 空中单车 | `exercises-dataset:0003` | `exercise_media/bicycle_crunch_v3.png` | `c0fc5c3bfa11d8b3fe4dd6a93bfb07907d621563d170ce0f145f8439f72aed2a` |
| 哑铃锤式弯举 | `exercises-dataset:0313` | `exercise_media/dumbbell_hammer_curl_0313.png` | `055752edfb26977825d37a6557649d33ed2aa800cf02d9d9e28bdf456e66bf7a` |
| 哑铃俯身划船 | `exercises-dataset:0293` | `exercise_media/dumbbell_bent_over_row.png` | `b35dca00266f4fa16771d5e3ae7afd8adc374985e0d8b913b6dfd06631f47fda` |
| 绳索低坐姿划船 | `exercises-dataset:0180` | `exercise_media/cable_low_seated_row.png` | `41900e729a119d39c7c2ddfe7a5f6d58b577d6db51ced8fa17ebf3a31dbdc7b0` |
| 绳索反握下拉 | `exercises-dataset:0245` | `exercise_media/cable_underhand_pulldown.png` | `9fbfecd8129fe5b4a68010d0867ebd6903eaf8adc9614eaeb18549e9fc949489` |
| 杠杆辅助反手引体 | `exercises-dataset:0572` | `exercise_media/assisted_chin_up.png` | `095110d3af880f1fe20cc6c5ef89692cc7ccd4491d5325e8fb7c67b1754093e5` |
| 史密斯架上斜卧推 | `exercises-dataset:0757` | `exercise_media/smith_incline_bench.png` | `9d35ec757614432f72ee6b9e195982b7c2d0b6572f5ff1a98887e22b551f36a6` |
| 器械坐姿腿弯举 | `exercises-dataset:0599` | `exercise_media/seated_leg_curl_0599.png` | `3a237e4d929a09716ffdd41aa0f0b148b81ae917ea6d80c3859211fb9fea2163` |
| 哑铃对握卧推 | `exercises-dataset:0352` | `exercise_media/dumbbell_neutral_bench_press.png` | `02913f48f69cbde74a09f4f3e090766c877124b5b206b517173941292bbef62c` |
| 杠铃下斜卧推 | `exercises-dataset:0033` | `exercise_media/barbell_decline_bench.png` | `24969f031773900b65d9628882570bb4feb6c365a0a17d471f4f70e229bb0553` |
| 哑铃上斜弯举 | `exercises-dataset:0315` | `exercise_media/dumbbell_incline_curl.png` | `9d7fa87ce585b276bc8e7adaf1473af8db756c96672b1cbe3b8422b81dae79df` |
| 哑铃站姿臂屈伸 | `exercises-dataset:0430` | `exercise_media/dumbbell_standing_triceps_extension.png` | `c34144f8fe376e690ee82e538526d4666bde394248bc2d70b7bef592bf95b194` |
| 杠铃站姿提踵 | `exercises-dataset:1372` | `exercise_media/barbell_standing_calf_raise.png` | `1556ddaf98f39dc260995c9498a8074fc2f45b1874c8be729436f7ffe43c474b` |
| 杠铃后弓步 | `exercises-dataset:0078` | `exercise_media/barbell_reverse_lunge.png` | `e0881f768bd1da655e0edbd6fc141a88405bcfc1a02c60d1d9117131be8e44ee` |
| 哑铃弓步 | `exercises-dataset:0336` | `exercise_media/dumbbell_lunge.png` | `adc2cf81b9191bf1b2a1e8b5434dabd61e064326665d4f7f118c05ed0529674f` |
| 史密斯架坐姿肩推 | `exercises-dataset:0765` | `exercise_media/smith_seated_shoulder_press.png` | `83117c221f5c5809a71b68bf584e3e4f47c91855e085893979a269dd47431f29` |
| 杠铃弓步 | `exercises-dataset:0054` | `exercise_media/barbell_lunge.png` | `893445d440b60475d649fc21d8b17385abde4c87ef3f8c40c9ec794fa302e469` |
| 杠杆站姿提踵 | `exercises-dataset:0605` | `exercise_media/lever_standing_calf_raise.png` | `3be69b0a7092a44cde8be862cb1def2bbb992613268b9167ccac5e8506e5685d` |
| 哑铃坐姿提踵 | `exercises-dataset:1379` | `exercise_media/dumbbell_seated_calf_raise.png` | `33d97b2ace7cf1cf97feccb42db14316a713ed4a948c855971b23c3f9ffd51f0` |

## 验收与限制

- 清单及生成器：`D:\codex-temp\alivo\docs\exercise-common-media-checklist.md` 和 `D:\codex-temp\alivo\tools\build-common-exercise-checklist.cjs`。清单会核对两端目录、步骤、资源字节和 SHA-256。
- Android：在本轮中段使用独立包名、内存数据且无网络权限的真机测试包，检查了列表缩略图、图片详情、署名、无图提示、修正后的步骤和跳绳标签；测试包已卸载，原预览应用未覆盖。截图中的 0313 当时无图，后续已接入自研图；最终仍无图的是 0404 和 0218。最终验收包已重新构建并逐图核对包内哈希。截图位于 `C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\reports`。
- HarmonyOS：隔离副本未签名 HAP 构建通过，153 条媒体与元数据在包内逐项校验通过；构建有 SDK 兼容性警告，未配置签名；当前没有连接鸿蒙设备，未进行真机界面或离线验收。
- 图片资源当前 154 个文件，共 269.4 MiB（包括一份历史未绑定的 wger 图片）；最终独立 Android 验收 debug APK 为 427.3 MiB，不代表正式发布包体积。需要后续评估压缩与按需加载。
- 坐姿腿弯举（0599）侧视图中双腿重叠、连杆与配重之间部分遮挡；低坐姿划船（0180）的器械上端有裁切。关键动作关系可辨，按编辑插图接入。
- 单张静态图片仅显示动作一个瞬间，不能证明步伐方向、完整运动路径或替代动作教学；对器械、握法或脚踏关系不清的候选不做绑定。

## 当前清单中未配图的条目（2）

- 哑铃坐姿肩推平行握（`exercises-dataset:0404`）：三稿中掌心朝前或手被遮挡，无法确认维护后的掌心相对；暂不绑定。
- 绳索坐姿宽握划船（`exercises-dataset:0218`）：三稿均未能清楚呈现踏板贴合与滑轮受力连接；暂不绑定。

候选生成提示词和逐张审核见 `C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\reports\pulldown.md`、`C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\reports\bicycle.md` 及 `C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\next\reports\group_a.md`、`C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\next\reports\group_b.md`、`C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\next\reports\group_c.md`、`C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\next\reports\group_b_split.md`、`C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\next\reports\group_a_split.md`、`C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\next\reports\group_0404_retry.md`、`C:\Users\Paul\.codex\visualizations\2026\11\07\01a1b5ef-3a7c-7f52-b90e-42d7d50cf64e\alivo-round6\next\reports\group_calf_split.md`；未通过稿保留在对应 rejected 目录。

## 测试与同步

- Node 完整回归：774 项通过，0 失败。
- Flutter 动作媒体与领域测试：28 项通过，0 失败。
- 计量清单：1352 条：重复次数 1250、时长 101、待维护 1。
- 常用动作清单与全量资产审计：153 个媒体两端字节相同，元数据、NOTICE、路径与 SHA-256 一致；原有 133 个绑定保持不变，新增图与审核稿一致；100 项清单中 98 项有图。
- Git 差异检查：git diff --check 240c321 HEAD 通过；工作区干净；指定 stash 仍存在。
- 最终 HEAD：`2773155ea88b6aaf28fdcbb966999d56af093b94`；推送：普通推送 origin/main 成功；远端与本地 HEAD 2773155ea88b6aaf28fdcbb966999d56af093b94 一致。

## 本轮提交

```text
2773155 feat: add calf raise and barbell lunge illustrations
7348523 feat: add lunge and smith shoulder illustrations
354e8f3 feat: add barbell calf raise and reverse lunge illustrations
9bc79b2 feat: add decline bench and arm illustrations
355b827 feat: add leg curl and neutral bench illustrations
2108658 feat: add smith incline bench illustration
6a68884 fix: repair bundled media notice formatting
891a081 feat: add underhand pulling illustrations
f1e12aa feat: add reviewed arm and rowing illustrations
6c9f979 fix: resolve additional grip instruction conflicts
d9f46b9 fix: localize jump rope equipment label
01dec65 docs: add reproducible common exercise media checklist
dcc5197 fix: clarify missing exercise media in both apps
7589eed feat: complete reviewed high frequency media gaps
1878e9b fix: clarify exercise instructions and jump rope choices
```
