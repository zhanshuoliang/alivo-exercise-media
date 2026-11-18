# 带标图片全量核查报告（2026-11-18）

范围：媒体仓 `media/` 全部带标 PNG 源图 + 双端已绑 WebP（1321/1352 记录）。

## 一、完整性审计（程序化）

- 已绑记录 1321 条：双端 `exercise_media/*.webp` 全部存在、1024px、SHA-256 与元数据一致 → **0 问题**
- `media/` PNG 全部可解码 → **0 坏文件**
- 已绑记录源 PNG 全在：992 条性别命名 + 329 条早期无性别命名 → **0 缺失**
- 配对差异（历史命名，非缺陷）：4 男无女（`dynamic_chest_stretch` / `modified_hindu_push_up` / `seated_calf_stretch` / `glute_bridge_two_legs_on_bench`），2 女无男（`jump_rope_extra007` / `landmine_press`）

## 二、感知哈希查重

全库两两比对（aHash+dHash 16×16）：0 完全重复；1 对近相似：

- `dumbbell_zottman_curl.png` ↔ `standing_dumbbell_curl.png`

全分辨率复核：两文件独立生成（不同 SHA/尺寸/时间），但 Zottman 弯举顶峰位与站姿哑铃弯举视觉上不可区分 —— Zottman 的识别特征是"顶端旋转→正握下放"，静态帧未体现 → **判定为需修复项**，已按下放相位+掌心朝下（正握）构图重生（男版，`0439` 绑定的 `dumbbell_zottman_curl.webp` 为遗留无性别命名，无女版文件）。

## 三、逐张目验（78 张缩略拼图 × 30 图，全 2312 张覆盖）

逐表核对：动作语义 vs 文件名、解剖/四肢、单人不拼版、器械握法、男女轨、构图裁切、杂字/乱码。结果：

- **缺陷 1 处（已修）**：`dumbbell_zottman_curl.png` 构图与站姿弯举不可区分 → 重生为下放相位正握帧，`0439` 双端 WebP/元数据 SHA/PROVENANCE/NOTICE 已全部更新
- **遗留孤儿 1 处（已清）**：`wger_plank_346.png`（wger CC BY-SA 遗留，从未绑定、未入 App 包）→ 从 `media/` 移除，`NOTICE.md`/`README.md` 更新为移除记录；App 实际绑定的平板支撑为 `plank.png`（`alivo:extra-001`）
- 其余 2310 张：姿势语义、解剖、单人构图、器械、字标均合格，**无需返工**

## 四、变更清单

媒体仓：
- `media/dumbbell_zottman_curl.png` — 重生（下放相位+掌心朝下），SHA-256 `bfbbce7c…df77`
- `media/wger_plank_346.png` — 删除（孤儿遗留）
- `media/NOTICE.md` — wger 段改为移除记录 + zottman SHA 更新
- `catalog/exercise_metadata.json` / `tools/catalog_snapshot.json` — 同步主仓新元数据（`0439` webp SHA `8503bd2e…`、reviewedAt 2026-11-18）
- `README.md` — 覆盖数 2312/1321 + wger 移除说明

主仓：
- `entry/.../exercise_media/dumbbell_zottman_curl.webp` + `mobile/.../exercise_media/dumbbell_zottman_curl.webp` — 重建（1024px q82），双端一致
- 双端 `exercise_metadata.json`（`0439` sha/reviewedAt）、`PROVENANCE.csv`、`NOTICE.md` — 已更新，双端 byte-identical

## 五、验证

- 绑定数仍为 1321/1352（本次为替换非新增）
- 双端元数据/WebP 逐字节一致；`0439` SHA 与 WebP 对账通过
- 回归与 Flutter 测试：见下方测试结论（本次提交附）
