# GitHub 协作整理验证 / GitHub collaboration maintenance verification

## 范围 / Scope

2026-11-03；基于 `fd2c9f030fe350e57ddd3508294ef93525b69b34` 的独立维护分支。覆盖 README、贡献与 Agent 维护入口、项目管理约定、Issue/PR 模板、文件及链接检查入口和本记录。十章规范、设计模板、示例、技能、来源登记、许可和版本号不变。

2026-11-03; a separate maintenance branch based on `fd2c9f030fe350e57ddd3508294ef93525b69b34`. Scope: README, contribution and agent maintenance entry points, project conventions, issue/PR templates, file/link check entries, and this record. The ten chapters, design templates, examples, skills, source registry, licensing, and version remain unchanged.

## 检查记录 / Check record

- 作者自检：`python3 -B tools/check_docs.py` 通过（37 个文件、33 份 Markdown、96 个内链、17 条来源）；`git diff --cached --check` 通过。
- 两个 Issue 模板的 YAML frontmatter 使用现有 Ruby 安全解析器核对，未安装依赖。
- 检查器 13 个正反案例符合预期：合法任务/PR/里程碑链接通过；其他仓库、相似前缀、未登记文件 URL、查询参数、非 HTTPS、非标准端口、空或非空 URL 身份、额外文件和缺失模板被拒绝。
- 与表单 PR head `1143563fa45d535d5536efbf8e30be78d715be75` 在临时副本做三方文本整合，无冲突，组合结构检查通过（39 文件、35 Markdown、137 内链、21 来源）。没有实际合并分支；表单 PR 新增入口仍须同步英文 README。
- 人工核对两个 README 的现有入口、管理文本和元数据草稿的双语事实；确认 11 个变更文件未涉及受保护的设计正文、模板、技能、来源或许可内容。
- 首次独立复核要求恢复总议题的作者验收关口，并将管理 PR 改为只关联任务，待默认分支模板入口核验后再关闭；另建议收紧新增 GitHub 跟踪链接的格式。三项发现修订后，独立定向复核通过，支持本范围 PR 提交；不构成全库批准或合并授权。

- Author checks: `python3 -B tools/check_docs.py` passed (37 files, 33 Markdown documents, 96 internal links, 17 sources); `git diff --cached --check` passed.
- Both issue-template YAML headers were checked using the existing Ruby safe parser; no dependency was installed.
- All 13 positive/negative checker cases matched expectations: valid issue/PR/milestone links passed; other repositories, lookalike prefixes, unregistered file URLs, query parameters, non-HTTPS schemes, nonstandard ports, empty or nonempty URL identity, extra files, and missing templates were rejected.
- Three-way text integration with form PR head `1143563fa45d535d5536efbf8e30be78d715be75` in a temporary copy had no conflicts, and combined structural checks passed (39 files, 35 Markdown documents, 137 internal links, 21 sources). No branch was actually merged; the form PR's added entry points still require English README alignment.
- Manually checked existing README entry points and bilingual facts in management text/metadata drafts; confirmed that the 11 changed files exclude protected design chapters, templates, skills, source content, and licensing.
- Initial independent review required restoring the umbrella issue's author-check gates and referencing the management task without closing it until default-branch template entry points are verified; it also recommended stricter formatting for new GitHub tracking links. All three findings were addressed and passed independent targeted re-review for scoped PR submission, not repository-wide approval or merge authorization.

## 边界 / Boundaries

GitHub 协作元数据通过 Issue、标签和里程碑维护。当前 CLI 缺少 Projects 权限，未创建看板或更改账号授权。模板在本 PR 合并前尚未在默认分支启用；本任务不合并 PR。版本仍为 `0.1.0-draft.3` / `REVIEW_CANDIDATE`，许可与正式发布决定保持待办。

GitHub collaboration metadata is maintained through issues, labels, and milestones. The current CLI lacks Projects permissions; no board was created and account authorization was not changed. The templates are not enabled on the default branch before this PR is merged; this task does not merge PRs. The version remains `0.1.0-draft.3` / `REVIEW_CANDIDATE`; licensing and formal-release decisions remain pending.

本轮只验证文档与管理配置，不重新执行设计案例，不代表全库独立复核、真实产品验收或全面安全认证。表单规范的独立 PR 仍自行保留其文字验证结果与 18 项 `NOT_RUN` 产品检查；合并并行 PR 时须同步中英文 README。

This round verifies documents and management configuration only. It does not rerun design cases or establish repository-wide independent approval, real-product acceptance, or comprehensive security certification. The separate form-guidance PR retains its text-evaluation results and 18 `NOT_RUN` product checks; synchronize both README languages when merging concurrent PRs.
