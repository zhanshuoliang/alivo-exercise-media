# 第八轮验证记录

2026-11-09（Asia/Taipei）；以下均为本轮实际执行结果。

- `node tools/build-common-exercise-checklist.cjs --check`：100/100，missing=[]。
- `node tools/build-exercise-measures.cjs --check`：1352 条，1250 reps、101 duration、1 blocked。
- `node --test tests/regression.cjs`：774/774，0 fail；117765.6222ms。日志 `D:/codex-temp/alivo-round8-node.log`。
- `flutter test --no-pub test/exercise_media_test.dart test/domain_test.dart`：28/28。日志 `D:/codex-temp/alivo-round8-flutter.log`。
- 两个仓库 `git diff --check`：通过；仅有 Windows 行尾提示。
- `python -B tools/audit_media.py --app-root D:/codex-temp/alivo --baseline c56634583252ac1505cccb1e71addc806daa2f45 --expected docs/round8/accepted.json --out docs/round8/audit-result.json`：183 条，180 旧绑定原样保留，3 新绑定；双端与资源快照字节、NOTICE 行、SHA-256 一致；历史未绑定 wger 原文件保留；生产无 GIF 绑定；2 试稿清单 SHA 校验通过。
- `python -B tools/build_catalog_page.py`：1352 条、183 有图；原有分类、筛选、缩放、动态检视与试稿切换保留。
- `python -B tools/build_motion_preview.py`：2 个既有 experimental 样例；生成内容未变化。

主仓库普通推送：`c566345` → `8a03365f49f81d0974fdd51ef6680bb27370eb69`，`git push origin HEAD` 成功。未修改业务实现，只新增双端媒体、media[]、NOTICE，以及现有 Node/Flutter 媒体加载断言中的 3 条映射。

## 本地浏览器验收

通过隔离 Playwright Chrome 和仅监听 127.0.0.1 的临时 HTTP 服务验证。

- 有图筛选为 183/1352；叠加 band 搜索只显示本轮 3 个动作。
- 三项详情分别返回 1004、1408、3006，图片 URL 与绑定一致，三张 PNG 均实际解码为 1254×1254。
- 放大细节使图像进入 zoomed 状态；动态检视使图像进入 kb 状态。
- 0662 详情点击“动作 GIF 样例”后实际加载 `motion/push_up_preview.gif`（414×414），出现“返回静态插图”。
- GIF 汇总页两个图片均加载为 414×414；返回动作库、两个下载及两个原静态图链接正确。
- 1280px 桌面与 390px 手机宽度无横向溢出，两张卡片完整。
- 仅观察到未设置 favicon 的 404，不涉及动作媒体或脚本错误；不将其作为本轮修复范围。

## 线上部署

接手时最新 run `42595402171` 仍失败，构建/上传成功，deploy 的 syncing_files 约 10 分钟超时；原审查页 200，GIF 汇总页 404。

已于台北时间 18:13 使用本机已有 Git 凭据请求重跑失败作业（插件 Actions 写权限 403，改用本地凭据后请求成功）；截至 18:34，重试仍 queued，尚无新作业启动。GitHub 官方 18:00 报告 Actions/Webhooks degraded performance，18:28 明确说明 Actions 启动与 webhook 投递延迟：https://www.githubstatus.com/ 。本次排队与该平台故障吻合，属于推断，不能据此确定更早的 Pages 同步超时根因。

资源普通推送后的新部署、最终线上验证和 Git 结果，记录到 `D:/codex-temp/alivo-selfmade-media-report-round8.md`。本地通过不代替线上通过；线上部署未完成时不得宣称 Pages 已修复。
