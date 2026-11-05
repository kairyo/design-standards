# 变量示例与落地页附页验证 / Variable example and landing-page appendix verification

## PR 候选整理 / PR candidate preparation — 2026-11-05

维护者随后授权提交、推送并创建双语 PR，暂不合并。本次以实际远端 main `4102b2bf8ce2bd29a69c0cde5436aa8fba64f322` 整理独立候选：只包含下述两个增补、相关入口/来源及本记录，不携带上轮全库复核资料、文字案例包或检查器的 JSON 扩展。原工作副本保留。下文 51 文件的本地验证记录是先前组合候选的历史证据，不代表此 PR 文件树。

两个新增示例与先前独立复核后的正文逐字节一致；只按 main 的实际文件清单调整衔接和来源检查，并追加本段。作者重新检查完整 PR 候选：46 个预期文件、38 份 Markdown、193 个内部链接、23 条来源；`python3 -B tools/check_docs.py` 和追踪/新增文件空白检查通过。十三项定向场景均以完整检查器在临时副本执行，结果符合预期；双语 README 链接一致。相对 main 新增 3 个、修改 12 个文件，版本、许可、技能及原表单示例未改。公开性与提交元数据另在提交/推送前核对；实际提交标识在 PR 记录，不以本文件自引用 SHA 标识自身。

整理后的候选已完成独立定向复核，限定范围内无阻断问题：复核者重算 46 文件清单哈希，确认两份示例与修后版本一致，独立运行结构及空白检查、八项完整检查器正常/异常场景，核对双语入口、来源/公开边界和七项加十八项未执行状态。没有发现对未带入文件或 JSON 检查逻辑的隐含依赖；下文原独立复核仍只覆盖当时组合。最终提交树和对外 PR 文字继续在推送前核对。

The maintainer subsequently authorized committing, pushing, and creating a bilingual PR, without merging. This independent candidate uses actual remote main `4102b2bf8ce2bd29a69c0cde5436aa8fba64f322` and contains only the two additions, related entry points/sources, and this record. It does not carry the earlier repository-wide review materials, text-case suite, or checker JSON extensions; the original worktrees are preserved. The 51-file local results below are historical evidence for the earlier combined candidate, not this PR's tree.

Both new examples are byte-identical to their independently reviewed versions. Only integration and source checks were adapted to main's actual file inventory, with this section added. Author checks of the complete PR candidate passed: 46 required files, 38 Markdown files, 193 internal links, and 23 sources; `python3 -B tools/check_docs.py` and whitespace checks for tracked/new files passed. All thirteen targeted scenarios ran through the complete checker in temporary copies and matched expectations; bilingual README links match. Against main, three files are added and twelve modified; version, licenses, skills, and existing form examples are unchanged. Disclosure and commit metadata are checked separately before committing/pushing; the actual commit is recorded in the PR rather than using a self-referential SHA here.

Independent targeted review of the repackaged candidate found no blocking issues within scope. The reviewer recalculated the 46-file manifest, confirmed both examples match the fixed versions, independently ran structural/whitespace checks and eight complete-checker positive/negative scenarios, and checked bilingual entry points, source/disclosure boundaries, and the seven plus eighteen unexecuted checks. No hidden dependency on excluded files or JSON-checking logic was found. The earlier review below retains its original scope; the final commit tree and outgoing PR text are checked before pushing.

## 范围与基线 / Scope and baseline

2026-11-05，本轮只在本地追加 [Figma 变量与主题示例](../examples/figma-variable-theme.md)、[落地页 brief 附页](../templates/landing-page-brief.md)及章节入口、来源归属和结构清单。未提交或推送；版本仍为 `0.1.0-draft.3` / `REVIEW_CANDIDATE`。

基线为基于 `4102b2bf8ce2bd29a69c0cde5436aa8fba64f322` 的上轮未提交 48 文件候选，而非该 commit 单独内容。开始前保留基线逐文件 SHA-256；本轮差异与验证材料在本地单独保留。旧案例输入、原答、历史复核记录、许可及技能文件不因本轮重新签署；原六例回答及历史旧新版对照没有重跑或改分。

On 2026-11-05, this local-only change adds a Figma variable/theme example, an optional landing-page brief appendix, and their chapter links, attribution, and structural inventories. Nothing is committed or pushed; version `0.1.0-draft.3` and `REVIEW_CANDIDATE` remain unchanged. The baseline is the previous uncommitted 48-file candidate based on the commit above, not that commit alone. Per-file SHA-256 hashes were preserved before editing, with incremental diff and verification artifacts retained locally. Earlier case inputs, answers, review records, licenses, and skill files are not re-signed; the six earlier responses and historical old/new comparison were neither rerun nor rescored.

## 来源与取舍 / Sources and selection

[S22](../references/sources.md#s22) 固定 `456d9e0d3e2d84c748bb143c6ca3d90c45e16213`，选择基础样本实际绑定及落地页输入/证据组织方法；[S23](../references/sources.md#s23) 核对 Figma 官方变量应用、模式继承和冲突的限定范围。新表格、数据和文案为原创合成内容，不带入技能文件、图像、字体或固定品牌偏好；动态帮助页不冒充永久快照。未执行外部技能、安装工具或操作设计文件。

S22 pins the commit above and informs bound samples plus landing-page input/evidence organization. S23 checks scoped official Figma guidance on applying variables, mode inheritance, and conflicts. New tables, data, and copy are original synthetic material; no skill files, images, fonts, or fixed brand preferences are imported. Dynamic help pages are not permanent snapshots. No external skill was executed, tool installed, or design file operated on.

## 作者文字走查 / Author document walkthrough

这是针对新说明的人工覆盖与矛盾检查，不是独立模型试答、真实画布操作或产品测试。逐项用下列情境核对实际条款能否支持预期处理，检查范围限于新文件及相邻章节。

This is a manual check of coverage and consistency in the new guidance, not independent model responses, real canvas execution, or product testing. Each scenario was checked against the actual new text and adjacent chapters for the expected handling below.

| 情境 | 条款与走查结论 |
| --- | --- |
| W01 正常绑定与主题往返 | Figma 示例第 2–3 节及 V01–V02 要求对象/属性/标识/别名/模式映射、Light → Dark → Light 的读回和画面；不能只凭截图签收绑定。文字覆盖。 |
| W02 显式固定主题的新消费者 | 初稿第 3 节及 V02 区分继承与固定 Light，但未明确同一父容器，作者初次走查漏掉该歧义；独立复核发现后补明共同父容器及对象级显式值，修后文字覆盖。见下方复核记录。 |
| W03 外观相同但断绑 | 第 4 节及 V04 允许获准副本构造同值直接填色，要求结构发现断绑并恢复；不冒称已发现真实缺陷。文字覆盖。 |
| W04 缺权限、别名缺失或库版本冲突 | 第 1、3 节及 V05 保留受阻/失败区别；无法确认原因时不补值，不修改生产库以凑结果。文字覆盖。 |
| W05 传播、说明过期与恢复 | 第 4 节及 V03/V06/V07 对照间距和样本、手工标签、布局、恢复和保护范围；并发修改时停止覆盖。文字覆盖。 |
| W06 仅单主题或只读任务 | 第 1 节允许有理由的不适用；缺少修改授权时不能为测试新建主题或操作对象。文字覆盖。 |
| W07 已知入口、主要动作与合理候选 | 落地页附页第 1、3 节区分入口承诺、CTA 目标、完成结果及 A/B 选择条件；内容顺序不固定。文字覆盖。 |
| W08 缺营销事实或公开依据 | 第 2–3 节分开事实可靠性和公开依据，数字/评价/价格/账号条件不编造；发布前补证据或去除主张，缺证言不阻断全部探索。文字覆盖。 |
| W09 后台、原生流程或冻结设计小修 | 附页适用说明、第 4 节及 02 章限制重开探索，不套用营销布局或强制填写全表。文字覆盖。 |
| W10 点击成功但目标未打开，效果未知 | 附页第 1、3–4 节分别记录点击与目标打开；设计稿和入口操作不能证明转化改善，运行项仍需证据。文字覆盖。 |

## 结构检查与独立复核 / Structural checks and independent review

作者自检完成：文档检查器通过，51 个预期文件、41 份 Markdown、272 个内部链接、23 条来源。追踪文件及全部新增文件的空白检查通过；双语 README 链接目标及次数一致，人工核对新增双语说明等义。上轮工作副本及基线快照逐文件哈希和原工作区状态未变；旧复核、案例、技能、许可与版本文件保持原样。

检查器只扩展清单和精确网址，十三项定向检查符合预期：正常候选、三个允许的固定文件网址、三个未登记路径（动态分支/其他文件/其他所有者）、缺少/重复/额外来源编号，以及三个新增文件各自缺失。故障注入只发生在临时副本，不进入仓库。

Author self-checks passed: 51 required files, 41 Markdown files, 272 internal links, and 23 sources. Whitespace checks cover tracked and all untracked files. Both README versions have matching link targets/counts, and new bilingual text was manually checked for equivalence. The previous worktree and baseline retain their file hashes and original worktree status; earlier reviews, cases, skills, licenses, and version files are unchanged.

The checker changes only inventories and exact URLs. Thirteen targeted scenarios matched expectations: the valid candidate, three allowed pinned-file URLs, three unregistered paths (a moving branch, another file, and another owner), missing/duplicate/extra source IDs, and each of the three missing new files. Fault injection remained in temporary copies outside the repository.

独立初审发现 `FL-IR-01`：初稿未明确固定 Light 对照与继承对象同属被切换父容器；放到容器外会使“不变色”失去鉴别能力。作者已在示例第 3 节和 V02 补明共同父容器、对象上的显式模式与三阶段读回；同时采纳非阻断建议，写清本例横向 Auto Layout 间距及样本条固定宽度。初次作者走查遗漏在 W02 保留，修后定向独立复核已确认问题关闭。

Independent initial review found `FL-IR-01`: the draft did not require the fixed-Light control and inheriting objects to share the switched parent container. Outside that container, an unchanged appearance would not discriminate the intended behavior. The author clarified the shared parent, object-level explicit mode, and three-stage readback in section 3 and V02. A nonblocking suggestion was also adopted to specify this example's horizontal Auto Layout gap and the sample bar's fixed width. W02 preserves the omission in the initial author walkthrough; targeted independent review of the fixes confirmed closure.

独立复核结论为限定范围内无阻断问题：复核者独立核对修前/修后候选清单哈希、增量和来源采用边界，运行结构与空白检查，确认历史记录保真及七项加十八项未执行状态。修后结构检查仍为 51 / 41 / 272 / 23；没有发现新的相关矛盾。该结论只针对文档候选，不构成真实 Figma、产品效果、用户批准或发布放行。

Independent review found no blocking issues within its scope. The reviewer independently checked the initial/fixed candidate hashes, incremental changes, source-adoption boundaries, structure and whitespace, historical-record fidelity, and the seven plus eighteen unexecuted checks. The fixed candidate still passed with 51 / 41 / 272 / 23; no new related contradiction was found. This conclusion concerns the documentation candidate only, not actual Figma execution, product effectiveness, user approval, or release clearance.

## 保留的未验证项 / Remaining unverified work

七项新增 Figma 实操 V01–V07 全为 `NOT_RUN`；原表单 F01–F12、分步 B01–B06 共十八项也继续为 `NOT_RUN`。没有真实 Figma 文件、账户能力、变量绑定/切换/恢复结果、代码主题加载、落地页或演示服务、用户理解研究、转化效果或完整无障碍验收。文字覆盖和结构通过不能改写这些状态，也不代表用户已批准发布或采用。

All seven new Figma execution checks V01–V07 remain `NOT_RUN`, as do the existing eighteen form/stepped-form checks F01–F12 and B01–B06. No actual Figma file, account capability, binding/switching/restoration result, code-theme loading, landing page or demo service, user-comprehension study, conversion effect, or full accessibility acceptance was tested. Document coverage and structural success cannot change those statuses or establish user approval to publish or adopt.
