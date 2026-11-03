# GitHub 项目管理 / GitHub project management

## 中文

这个知识库按文档项目维护：Issue 定义任务，PR 保存差异，验证记录保留证据，里程碑汇总候选范围。约定只适用于本仓库，不改变消费项目的规则。

### 入口与职责

- [总议题](https://github.com/kairyo/design-standards/issues/1) 记录候选目标、历史交付和未完成关口；单项改动不自动关闭总议题。
- [任务列表](https://github.com/kairyo/design-standards/issues) 保存问题、范围、验收条件、依赖、证据和下一步；重要改动先查重，再使用专门 Issue。
- [PR 列表](https://github.com/kairyo/design-standards/pulls) 保存具体差异、自检、独立复核及未覆盖项；一个 PR 对应一项完整改进。
- [里程碑](https://github.com/kairyo/design-standards/milestones) 归集候选任务，不虚设截止日期，也不代表已经发布。
- 作者负责实现与自检，独立审阅者复核其范围，维护者决定合并、许可和正式发布。审阅者未安排时明确写待安排；自检不等于独立批准。

### 从任务到完成

1. Issue 写清问题、章节、授权范围、适用与不适用条件、验收证据。小改动可用简短描述，不强制填无关字段。
2. 经授权使用 `ai/<feature>` 或 `ai/<type>/<feature>` 短期分支，采用少而清晰的 Conventional Commits；不直推 main/master，不改写已公开历史或绕过防护。
3. PR 关联专门 Issue。只有合并能完成该任务时使用 `Closes #N`；总议题、许可决定、真实产品验收等未完成事项使用 `Refs #N`。
4. 运行 `python3 -B tools/check_docs.py` 和 `git diff --check`；按风险补充正常、异常、信息不足、边界与恢复案例。记录测试版本、方法、结果和未覆盖项，不强制重跑无关检查。
5. 自检后独立复核并保留证据。依据有效维护者授权 squash 合并，不启用自动合并。提交、推送、合并、发布和消费项目采用分别核对授权。
6. 合并后核对最终提交与验收条件，再确认任务状态。关闭时移除未完成状态标签；未执行或未通过的产品检查交给相应项目跟踪，不能因文档合并而标记通过。

没有 Projects 看板时，Issues、状态标签和里程碑就是台账；以后增加看板也复用这些 Issue，避免维护两套进度。

### 标签与状态

标签名是稳定的英文检索键，描述提供等价中文与英文。已有 `documentation`、`bug`、`enhancement`、`accessibility`、`question` 等说明类型，`tracking` 标记总议题；保留其他通用标签，不删除历史标签。

| 开放任务状态 | 含义 |
| --- | --- |
| `status:planned` | 待办：范围已记录，尚未实施 |
| `status:in-progress` | 进行中：已获授权，正在实施 |
| `status:review` | 待审：差异和自检可审阅，等待审阅或合并决定 |
| `status:decision` | 待决定：需要维护者决定许可、范围或发布等事项 |

专门任务最多一个 `status:*` 标签，状态变化时替换旧标签。总议题可只用 `tracking`；PR 使用类型标签，由关联任务保存进度。未确定的截止日期或负责人如实留空。不计划实施的任务关闭时保留原因，关闭不等于验收通过。

### 双语与证据

仓库简介、README、Issue/PR 标题与正文、任务状态说明、里程碑、标签描述和协作模板保持中英双语。推荐标题 `type: 中文 / English`，正文可按语言分区或并列表格；提交仍用 Conventional Commits，代码标识和 SHA 无需翻译。

十章正文、设计记录模板、示例、技能和历史证据暂保留中文。两个 README 与新增协作说明同步维护；并行 PR 若新增入口，合并前按最终文件树检查两种语言。

翻译保留相同日期、版本、数量、出处、授权和未验证项。历史 PR 可补译并注明历史快照，不改变原结论、合并状态或提交历史。局部独立复核与文字案例通过，不能替代全库复核或真实产品验收。

许可待定时不默认接受再许可；疑似敏感资料不复制到公开 Issue。其他公开检查见 [CONTRIBUTING](CONTRIBUTING.md)。

## English

Maintain this knowledge base as a documentation project: issues define tasks, PRs retain changes, verification records retain evidence, and milestones group candidate scope. These conventions apply only here, not to consumer projects.

### Entry points and responsibilities

- The [tracking issue](https://github.com/kairyo/design-standards/issues/1) records objectives, historical delivery, and outstanding gates; individual changes must not automatically close it.
- [Issues](https://github.com/kairyo/design-standards/issues) retain the problem, scope, acceptance criteria, dependencies, evidence, and next action. Search for duplicates before opening a dedicated issue for substantive work.
- [PRs](https://github.com/kairyo/design-standards/pulls) retain the diff, author checks, independent review, and limitations. Keep one complete improvement per PR.
- [Milestones](https://github.com/kairyo/design-standards/milestones) group candidate tasks without invented deadlines or implying a release.
- Authors implement and self-check; independent reviewers assess their assigned scope; maintainers decide merging, licensing, and formal release. Mark reviewers as unassigned when necessary. Self-checks are not independent approval.

### From task to completion

1. State the problem, chapters, authorized scope, applicability, exclusions, and acceptance evidence. A short description is sufficient for small changes; omit irrelevant fields.
2. Once authorized, use a short-lived `ai/<feature>` or `ai/<type>/<feature>` branch and a small number of coherent Conventional Commits. Do not push directly to main/master, rewrite published history, or bypass safeguards.
3. Link a dedicated issue. Use `Closes #N` only when merging completes that task. Use `Refs #N` for tracking issues, licensing decisions, real-product acceptance, and other unfinished work.
4. Run `python3 -B tools/check_docs.py` and `git diff --check`. Add normal, exceptional, insufficient-information, boundary, and recovery cases as warranted by risk. Record the tested version, method, results, and limitations; do not rerun unrelated checks by default.
5. Obtain independent review after author checks and retain evidence. Squash merge only with valid maintainer authorization; do not enable auto-merge. Check authorization separately for committing, pushing, merging, release, and consumer-project adoption.
6. After merging, verify the final commit and acceptance criteria before confirming task state. Remove unfinished status labels on closure. Track failed or unexecuted product checks in the relevant project; merging documentation does not make them pass.

Without a Projects board, issues, status labels, and milestones are the register. Reuse these issues if a board is added later, avoiding two parallel progress systems.

### Labels and status

Label names are stable English search keys, with equivalent Chinese and English descriptions. Existing labels such as `documentation`, `bug`, `enhancement`, `accessibility`, and `question` identify types; `tracking` identifies umbrella issues. Preserve other general-purpose and historical labels.

| Open-task status | Meaning |
| --- | --- |
| `status:planned` | Backlog: scope recorded, implementation not started |
| `status:in-progress` | In progress: authorized work is underway |
| `status:review` | In review: diff and author checks available; review or merge decision pending |
| `status:decision` | Decision needed: maintainer decision on licensing, scope, release, or a similar matter |

A dedicated task has at most one `status:*` label; replace it on transition. Umbrella issues may use `tracking` alone. PRs use type labels while linked issues hold progress. Leave unestablished deadlines or assignees unset. Retain the reason when closing work that is not planned; closed does not mean accepted.

### Bilingual content and evidence

Keep the repository description, README, issue/PR titles and bodies, task status notes, milestones, label descriptions, and collaboration templates bilingual. Prefer `type: 中文 / English` titles and language sections or paired tables. Retain Conventional Commits; code identifiers and SHAs need not be translated.

The ten chapters, design record templates, examples, skills, and historical evidence remain in Chinese for now. Keep both README versions and new collaboration guidance aligned. When concurrent PRs add entry points, check both languages against the final tree before merging.

Translations preserve dates, versions, counts, provenance, authorization, and unverified work. Historical PRs may receive translations with a historical-snapshot note; do not alter their conclusions, merge state, or commit history. Scoped independent review and text-case results do not replace repository-wide review or real-product acceptance.

While licensing is undecided, do not assume agreement to relicensing. Never copy suspected sensitive material into public issues. See [CONTRIBUTING](CONTRIBUTING.md) for other publication checks.
