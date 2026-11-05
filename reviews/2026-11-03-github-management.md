# GitHub 协作整理验证 / GitHub collaboration maintenance verification

本文记录 2026-11-03 时尚未合并的状态，其中“当前”“未来”和“本任务”均指当时状态。保留原结论；当前进度见 [总议题](https://github.com/kairyo/design-standards/issues/1)，现行许可见 [许可说明](../LICENSE-NOTICE.md)。

This is a historical snapshot dated 2026-11-03, when these changes had not yet been merged. “Current,” “future,” and “this task” refer to that time. Preserve the original conclusions; see the [tracking issue](https://github.com/kairyo/design-standards/issues/1) for current progress and the [license notice](../LICENSE-NOTICE.md) for applicable licensing.

## 首轮范围（历史记录） / Initial scope (historical record)

2026-11-03；基于 `fd2c9f030fe350e57ddd3508294ef93525b69b34` 的独立维护分支。覆盖 README、贡献与 Agent 维护入口、项目管理约定、Issue/PR 模板、文件及链接检查入口和本记录。十章规范、设计模板、示例、技能、来源登记、许可和版本号不变。

2026-11-03; a separate maintenance branch based on `fd2c9f030fe350e57ddd3508294ef93525b69b34`. Scope: README, contribution and agent maintenance entry points, project conventions, issue/PR templates, file/link check entries, and this record. The ten chapters, design templates, examples, skills, source registry, licensing, and version remain unchanged.

## 首轮检查（历史记录） / Initial checks (historical record)

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

## 双语整合复核 — 2026-11-03 / Bilingual integration recheck

输入固定为表单 PR #4 的 `1143563fa45d535d5536efbf8e30be78d715be75` 与管理 PR #9 的原提交 `c239c21c3a48f82649555dbdd90475c504ef9756`。在管理功能分支组合两者，保留已公开提交历史；PR #9 以 PR #4 的功能分支为审阅基线，设计条款仍由 PR #4 单独审阅。没有合并 GitHub PR 或修改 main。

Inputs are pinned to form PR #4 at `1143563fa45d535d5536efbf8e30be78d715be75` and management PR #9's original commit `c239c21c3a48f82649555dbdd90475c504ef9756`. Combine them on the management feature branch while preserving published history. PR #9 uses PR #4's feature branch as its review base; design clauses remain separately reviewed in PR #4. No GitHub PR is merged and main is unchanged.

英文 README 补齐两个表单示例的直接入口，以及跨章关系、草稿/有效数据/焦点往返、产品检查未执行和不代表可运行表单的说明。首轮记录中的“仍须同步英文入口”在本轮处理，不改写首轮检查结论。

The English README adds direct links to both form examples, their chapter connections, draft/active-data/focus return checks, and the boundaries that product checks are unexecuted and no runnable form is established. This round addresses the initial record's pending English alignment without rewriting its historical conclusions.

- 作者检查通过：39 个必需文件、35 份 Markdown、139 个内链、21 条来源；暂存差异空白检查通过。
- 两个 README 除互相切换语言的链接外，32 处链接指向相同的 31 个目标，包含两个表单示例；人工核对新增说明的含义、版本、声明分类与未验证边界。
- 组合后的检查器 13 个正反案例符合预期。两个模板及其他未改管理文件保持原内容，没有为本轮安装依赖。
- 十章正文、设计模板、示例、技能、来源、历史 REVIEW、版本和许可说明共 28 个文件与 PR #4 输入逐字一致；相对 PR #4 的管理 PR 差异仍为 11 个文件。未重跑设计案例或产品操作。
- 本轮独立复核通过：确认双语入口与含义、28 个文件保持、11 个文件差异及后续 PR 的依赖和合并边界，支持本范围提交审阅；不构成 GitHub 合并、全库复核或产品验收批准。

- Author checks passed: 39 required files, 35 Markdown documents, 139 internal links, and 21 sources; the staged whitespace check passed.
- Apart from reciprocal language switches, both README files have 32 link occurrences pointing to the same 31 targets, including both form examples. The added explanation's meaning, version, claim categories, and unverified boundaries were manually checked.
- All 13 positive/negative cases passed their expected outcomes with the combined checker. Both templates and other unchanged management files retain their content; no dependencies were installed.
- Twenty-eight files covering the ten chapters, design templates, examples, skills, sources, historical REVIEW, version, and licensing notices are byte-identical to PR #4's input. The management PR still changes 11 files relative to PR #4. No design-case or product-interaction tests were rerun.
- Independent review passed for this round: bilingual entries and meaning, preservation of 28 files, the 11-file diff, and the dependent PR's review/merge boundaries were confirmed for scoped submission. This is not approval for GitHub merging, repository-wide review, or product acceptance.

PR #9 当前只对照 PR #4 审阅，不向 PR #4 的功能分支合并。未来获得相应合并授权后，先将 PR #4 squash 合入 main，再将 main 同步到管理功能分支并把 PR #9 的目标改回 main；核对最终差异与检查结果后，另行决定 PR #9 是否合并。

PR #9 is currently reviewed against PR #4; do not merge it into PR #4's feature branch. Once the corresponding merge authorization exists, squash merge PR #4 into main first, then synchronize main into the management feature branch and retarget PR #9 to main. Check the final diff and validation results before separately deciding whether to merge PR #9.

## 当时边界（2026-11-03 历史快照） / Boundaries at the time (2026-11-03 historical snapshot)

GitHub 协作元数据通过 Issue、标签和里程碑维护。当前 CLI 缺少 Projects 权限，未创建看板或更改账号授权。模板在本 PR 合并前尚未在默认分支启用；本任务不合并 PR。版本仍为 `0.1.0-draft.3` / `REVIEW_CANDIDATE`，许可与正式发布决定保持待办。

GitHub collaboration metadata is maintained through issues, labels, and milestones. The current CLI lacks Projects permissions; no board was created and account authorization was not changed. The templates are not enabled on the default branch before this PR is merged; this task does not merge PRs. The version remains `0.1.0-draft.3` / `REVIEW_CANDIDATE`; licensing and formal-release decisions remain pending.

本轮只验证文档与管理配置，不重新执行设计案例，不代表全库独立复核、真实产品验收或全面安全认证。表单规范 PR 仍保留其文字验证结果与 18 项 `NOT_RUN` 产品检查；后续内容或基线改变时须重新核对两种语言与最终文件树。

This round verifies documents and management configuration only. It does not rerun design cases or establish repository-wide independent approval, real-product acceptance, or comprehensive security certification. The form-guidance PR retains its text-evaluation results and 18 `NOT_RUN` product checks. Recheck both languages against the final tree if content or the base changes later.
