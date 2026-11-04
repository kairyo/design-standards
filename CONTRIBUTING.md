# 贡献与公开检查 / Contributing and publication checks

## 中文

Issue、分支、PR、状态和双语要求见 [项目管理约定](PROJECT_MANAGEMENT.md)。

本仓库仍为审阅稿；原创文档采用 CC BY 4.0，原创代码采用 MIT，文件范围见 [许可与署名](LICENSE-NOTICE.md)。提交拟合入的 PR 时，请确认下列贡献条件：

- 你拥有所提交内容的相应权利，或已取得足以按对应许可提交的授权；需要雇主或其他权利人同意时，先取得同意。
- 你有意提交的原创文档按 CC BY 4.0、原创代码按 MIT 提供给本项目及接收者；你保留版权和应保留的署名，不要求版权转让、额外再许可权或另签贡献者协议。
- 第三方内容单独注明作者、原始地址、版本、许可、修改及必要通知，并说明授权依据。先讨论是否适合纳入；不要把他人的内容重新标为本项目原创，或仅凭可访问就提交。
- 新增代码明确标注 MIT，并附相应许可通知；技能包被单独复制时仍应携带许可原文与署名。来源不明或无权按对应条件提供的内容，先保留为讨论，不合入。

这些是向本仓库提供贡献的条件，不改变标准许可证对复用者授予的权利。PR 接收、合并、正式发布和消费项目采用仍按各自的授权及验收执行。

### 一项改进的最小输入

说明问题、受影响章节、适用平台、建议分类、公开来源及读取范围、预期收益和不适用情形。以能审查的范围提交；不要把技术迁移或生产项目修改夹在文档 PR 中。

官方网页的标题、链接或搜索摘要不足以证明正文已读取。写明阅读日期和具体章节；对于持续更新网页，保留来源标注版本/日期，并承认它不是不可变快照。需要更新时人工比较差异。

### 写作要求

- 采用原创解释与小型合成案例；避免大段转载官方文档或第三方代码。
- 说明建议为什么有用、在哪种条件下失效、如何验证；不靠“高级”“有审美”等形容词充当标准。
- 数值注明平台单位、适用组件与版本。不把一个项目的语言数量、品牌色、字号或设备矩阵推广为默认值。
- 例外必须解释边界，不能以“项目选择”为名伪造对外符合性声明。

### 发布前检查

1. 检查整棵候选文件树，而不只是最后一次 diff。确认不存在媒体、字体、UI 套件、内部截图或未审阅二进制。
2. 检查分支上全部待公开提交、提交信息与作者元数据；私密内容曾进入历史时，不能仅在最终文件删除后就发布。
3. 检查正文、示例、文件名、链接、PR 标题/正文中的私人地址、内部项目名、设备标识和真实数据。公开引用只采用登记过的资料来源。
4. 检查许可与归属，确认没有把“能访问”理解成“能再分发”。
5. 使用 Python 3.9 或更新版本运行 `python3 tools/check_docs.py`，并运行 `git diff --check`；再人工通读关键章节。
6. 作者填写自检结果和未完成项，独立审阅者检查事实、适用范围与公开边界，维护者作出合并/发布决定。

技能变更另需检查名称与触发描述、完整文件夹的自包含性、界面元数据和许可状态；可用时运行宿主提供的技能格式校验器。用适用与相邻不适用请求检查决定边界，并标明是作者推演还是实际独立执行。结构检查通过不等于自动选择、跨客户端兼容或审美收益已经验证；不得为了测试擅自安装到用户全局目录或修改消费项目。

遇到疑似敏感信息，先阻止进一步传播，使用已有私密沟通渠道处理。不要把敏感内容复制进公开 issue 来解释问题。

## English

See [Project management](PROJECT_MANAGEMENT.md) for issue, branch, PR, status, and bilingual conventions.

This repository remains a review draft. Original documentation uses CC BY 4.0 and original code uses MIT; see [Licensing and attribution](LICENSE-NOTICE.md) for file scope. When submitting a PR intended for inclusion, confirm these contribution terms:

- You hold the relevant rights or have authorization sufficient to submit under the applicable license. Obtain any required employer or other rights-holder consent first.
- Original documentation you intentionally contribute is provided under CC BY 4.0, and original code under MIT, to this project and its recipients. You retain copyright and applicable attribution; no copyright assignment, additional relicensing rights, or separate contributor agreement is required.
- Identify third-party authors, original URLs, versions, licenses, changes, required notices, and the basis for authorization separately. Discuss suitability before inclusion; do not relabel another party's work as this project's original material or submit solely because you can access it.
- Explicitly mark new code MIT and provide the corresponding notices. Independently copied skill packages should still carry the full license and attribution. Material with unclear provenance or insufficient permission remains a discussion item until resolved, rather than being merged.

These conditions govern contributions to this repository; they do not change the rights granted to reusers by the standard licenses. PR acceptance, merging, formal release, and consumer-project adoption retain their respective authorization and acceptance requirements.

### Minimum input for an improvement

Describe the problem, affected chapters, applicable platforms, claim category, public sources and reading scope, expected benefit, and cases where the proposal does not apply. Keep changes reviewable; do not include technology migrations or production-project modifications in a documentation PR.

An official page title, link, or search snippet does not establish that its body was read. Record the reading date and specific sections. For continuously updated pages, preserve the source's stated version/date and acknowledge that it is not an immutable snapshot. Compare changes manually when updating.

### Writing requirements

- Use original explanations and small synthetic examples. Avoid lengthy reproduction of official documents or third-party code.
- Explain why a recommendation helps, when it fails, and how to verify it. Adjectives such as “advanced” or “aesthetic” are not standards.
- Specify platform units, applicable components, and versions for numerical values. Do not generalize one project's language count, brand colors, type sizes, or device matrix into defaults.
- Explain exception boundaries. A project choice cannot justify a false public conformance claim.

### Before publication

1. Review the entire candidate tree, not just the last diff. Check for media, fonts, UI kits, internal screenshots, or unreviewed binaries.
2. Review all commits to be published, their messages, and author metadata. Deleting private content from the final tree is insufficient if it remains in history.
3. Review text, examples, filenames, links, and PR titles/bodies for private addresses, internal project names, device identifiers, and real data. Cite only registered public sources.
4. Check licensing and attribution; access does not establish redistribution rights.
5. Run `python3 tools/check_docs.py` with Python 3.9 or newer, and `git diff --check`; then read the key chapters manually.
6. The author records self-check results and outstanding work, an independent reviewer checks facts, applicability, and public boundaries, and the maintainer decides merging/release.

For skill changes, also check names and trigger descriptions, complete-folder self-containment, interface metadata, and licensing. Run the host's skill-format validator when available. Check decision boundaries with applicable and adjacent inapplicable requests, distinguishing author walkthroughs from actual independent execution. Structural success does not establish automatic selection, cross-client compatibility, or visual-quality benefit. Testing does not authorize global installation or consumer-project changes.

If sensitive information is suspected, prevent further propagation and use an existing private communication channel. Do not copy sensitive details into a public issue to explain the problem.
