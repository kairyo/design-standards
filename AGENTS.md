# 本仓库 Agent 维护入口 / Agent maintenance entry point

## 中文

本文件只约束此文档仓库的维护，不是供其他项目自动继承的全局配置。设计正文的适用关系见 [README](README.md)；权限和工程工作方式沿用任务及项目已有规则。

Issue、PR、状态与双语要求见 [项目管理约定](PROJECT_MANAGEMENT.md)；仍须遵守当前任务的有效授权和停止点。

### 工作范围

- 先定位相关章节与公开来源，再做范围明确的修改；不为小改动重读或重写全库。
- 保留四种声明分类、来源实际读取范围和待验证状态。正文中的团队建议不可冒充平台要求。
- 只写可公开的原创归纳；不要复制私有文件后改名，不提交内部地址、身份、数据或资产。
- 不安装工具，不修改消费项目、全局规则或服务；需要这些工作时另行获得授权。
- 不规定对话模型、账号或委派方式；不因读取本仓库而启动其他 Agent。

### 提交与审阅

- 经任务授权后使用短期 `ai/<feature>` 或 `ai/<type>/<feature>` 分支，不直接推送 main/master，不绕过 Git 防护。
- 一次逻辑完整的文档变更形成清晰的 Conventional Commit 和 PR；不逐行提交。
- 先自检，再由独立审阅者复核。作者不能把自检写成独立批准；合并与发布需要相应授权，合并采用 squash。
- 遇到来源冲突、公开性或许可不明，停止该项发布并报告；其他不受影响的工作可以继续。
- 工具失败遵守已有任务的有界重试要求；本仓库不新增通用次数或轮询策略。

### 验证

使用 Python 3.9 或更新版本运行 `python3 tools/check_docs.py`，并运行 `git diff --check`。检查器只检查文本结构、内部链接、来源入口和少量公开性风险；不能证明事实、版权、审美或产品运行正确。

推送前人工审阅完整候选树、待公开历史、提交作者/邮箱、提交消息及 PR 文字。源文件、来源版本、采用范围改变时，同步相关引用和 CHANGELOG。不得通过自动更新上游来替代差异审查。

## English

This file governs maintenance of this documentation repository only. It is not global configuration for other projects to inherit automatically. See [README](README.en.md) for how the design guidance applies; retain the current task's and project's permission and engineering rules.

See [Project management](PROJECT_MANAGEMENT.md) for issue, PR, status, and bilingual conventions. Continue to honor the active task's valid authorization and stopping point.

### Scope of work

- Locate relevant chapters and public sources before making scoped changes. Do not reread or rewrite the entire repository for a small edit.
- Preserve the four claim categories, actual source-reading scope, and unverified status. Team recommendations must not be presented as platform requirements.
- Publish only original synthesis suitable for public disclosure. Do not rename copied private files or commit internal addresses, identities, data, or assets.
- Do not install tools or change consumer projects, global rules, or services without separate authorization.
- Do not prescribe conversation models, accounts, or delegation methods. Reading this repository does not itself authorize starting other agents.

### Commits and review

- Once authorized by the task, use a short-lived `ai/<feature>` or `ai/<type>/<feature>` branch. Do not push directly to main/master or bypass Git safeguards.
- Use a clear Conventional Commit and PR for a coherent documentation change; do not commit line by line.
- Self-check first, then obtain independent review. Authors cannot present self-checks as independent approval. Merging and release require corresponding authorization; use squash merging.
- Stop publication of affected material when sources conflict or disclosure/licensing is unclear, and report it. Unaffected work may continue.
- Follow the active task's bounded-retry requirements for tool failures. This repository adds no general retry count or polling policy.

### Verification

Run `python3 tools/check_docs.py` with Python 3.9 or newer, and `git diff --check`. The checker covers text structure, internal links, source entry points, and a few disclosure risks. It does not prove factual, copyright, visual, or product-runtime correctness.

Before pushing, manually inspect the complete candidate tree, history to be published, author/email metadata, commit messages, and PR text. When source files, source versions, or adoption scope change, update references and CHANGELOG accordingly. Automatic upstream updates must not replace diff review.
