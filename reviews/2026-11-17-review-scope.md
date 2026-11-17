# 规范复核、执行偏差与项目验收 / Standards review, execution deviations, and project acceptance

日期 / Date：2026-11-17。分类 / Classification：`TEAM_RECOMMENDATION`。关联 / Related：[Issue #7](https://github.com/kairyo/design-standards/issues/7)。

本轮整理基于本地提交 `13203a6564f737609a2b6a81a507bd1d6d7a2ac2`，只调整复核范围、记录归属与入口说明；没有重新执行历史案例或修复演示。下述归类不是当前全库复核通过、正式发布、项目采用或产品验收的声明。

This reorganization uses local commit `13203a6564f737609a2b6a81a507bd1d6d7a2ac2` as its base. It changes review scope, record ownership, and entry-point explanations only; it neither reruns historical cases nor repairs the demo. The classification below is not a claim that the current whole repository has passed review, been formally released, been adopted, or passed product acceptance.

## 三类问题与责任 / Three categories and ownership

| 归属 / Category | 判断与处理 / Assessment and action | 对 Issue #7 的影响 / Effect on Issue #7 |
| --- | --- | --- |
| 规范问题 / Standards issue | 规则错误、歧义、冲突、适用边界或必要判据缺失，由规范维护者修订。/ Incorrect, ambiguous, conflicting rules, unclear applicability, or missing necessary criteria belong to standards maintainers. | 阻断性问题解决后才能完成对应复核；非阻断建议保留处置决定。/ Blocking issues must be resolved for the relevant review to finish; record dispositions for non-blocking suggestions. |
| 执行偏差 / Execution deviation | 已有明确规则，但设计、实现或验证执行未遵守；由执行方负责。夹具与批准材料不一致属于验证执行偏差。/ Clear guidance was not followed in design, implementation, or verification; the executor owns it. Fixture/approved-material mismatches are verification-execution deviations. | 保留失败及规则如何识别它的证据；演示无缺陷不是规范复核结项条件。/ Retain failures and evidence of how the rule identified them; a defect-free demo is not a standards-review closure condition. |
| 实际项目验收 / Consumer-project acceptance | 采用项目按批准范围决定真机、后台、原生材质、完整辅助技术及交付验收。/ Each adopting project defines physical-device, backend, native-material, full assistive-technology, and delivery acceptance within its approved scope. | 不作为本议题的一揽子前提，也不因本议题结项获得通过。/ It is not a blanket prerequisite for this issue and does not pass when this issue closes. |

技能宿主加载、隐式激活及跨客户端行为属于采用环境验证。若要宣称这些能力可用，仍须取得相应证据；它们不是规范内容复核的一揽子前提。缺少证据时保留未验证状态。

Skill loading, implicit activation, and cross-client behavior are adoption-environment checks. Claims that these capabilities work still require corresponding evidence; they are not blanket prerequisites for content review. Missing evidence remains unverified.

同一观察可以暴露两类问题，但须分别给出理由。只有在规则缺失、相互冲突或难以形成一致判断时，才将执行样本另列为规范问题；不把每个演示缺陷直接转成新增条款，也不凭一次正确判断证明规则普遍有效。

One observation can reveal more than one category, but each needs its own rationale. Escalate an execution sample to a standards issue when guidance is absent, contradictory, or cannot support consistent judgment. Do not turn every demo defect into a new rule or treat one correct judgment as universal validation.

## 既有记录的归属 / Existing-record classification

| 记录 / Record | 可支持的结论 / Supported conclusion | 限制及后续归属 / Limits and ownership |
| --- | --- | --- |
| [2026-11-04 全库独立复核 / Repository-wide review](2026-11-04-repository-review.md) | 当时版本的 43 文件内容复核及逐章发现。/ Content review and chapter findings for 43 files at that version. | 不扩展成后续所有增补或当前全库的认证。/ Does not certify every later increment or the current whole repository. |
| [最小文字案例 / Text cases](text-cases/2026-11-04-run.md) | 历史六例、18 项必要判断的回答证据；原评分保留。/ Historical responses to six cases and 18 required judgments; original assessments remain intact. | 不等于产品实测、技能加载或当前版本重跑。/ Not product execution, skill loading, or a rerun on the current version. |
| [变量与落地页增补 / Variable and landing-page additions](2026-11-05-figma-landing.md) | 对应增补的文档、来源边界及独立复核。/ Documentation, source boundaries, and independent review of that increment. | 七项示例检查仍按原记录；无落地页效果结论。/ The seven example checks retain their original record; no landing-page effectiveness conclusion. |
| [表单纠错记录 / Form correction record](2026-11-06-form-validation.md) | 历史本地演示 18 项中 16 项限定 PASS；据此细化三项操作判据。/ Of 18 historical local-demo checks, 16 passed within scope; the findings informed three more precise operational criteria. | F09/B06 已执行的键盘与语义结果、历史父项 BLOCKED、实际读屏 NOT_RUN 及暂缓安排分别保留；不是全套通过。/ Retain executed keyboard/semantic results, historical parent BLOCKED results, actual screen-reader NOT_RUN states, and deferral separately; no full-suite pass. |
| 自适应保真与回归增补（见[审阅记录 / review log](../REVIEW.md)）/ Adaptive-fidelity and regression increment | 限定范围的独立文档复核及两项修订。/ Scoped independent document review and two corrections. | A01–A08 示例执行栏保持 NOT_RUN；不从文档复核推导产品通过。/ A01–A08 example execution fields remain NOT_RUN; document review does not establish product acceptance. |
| [导航、材质与原型修订 / Navigation, material, and prototype corrections](2026-11-17-navigation-review.md) | 固定初审版本、三项发现与修订、十个作者文字对照及独立复核。/ Fixed initial-review version, three findings/corrections, ten author text comparisons, and independent review. | N01–N12 示例执行栏保持 NOT_RUN；单独试点的证据另记，不回填历史示例。/ N01–N12 example execution fields remain NOT_RUN; separate pilot evidence does not overwrite historical examples. |

上述复核版本、实际输入身份和读取范围以各原记录为准；不能把不同版本的部分通过拼成一次全库通过。现有记录支持追溯，但本轮没有重新完成十章逐项实证复核。

Each original record controls its reviewed version, actual input identity, and reading scope. Partial passes from different versions do not combine into one repository-wide pass. These records provide traceability; this round does not repeat evidence-based review of all ten chapters.

## 阅读合成试点的归类摘要 / Classification of the synthetic reading pilot

以下是既有受控本地记录的公开文字归纳，本轮未重跑。仅保留通用现象与判断边界，不发布设计链接、节点、项目参数、源码或原始画面。它不是公开可复跑的证据包。RP 编号仅用于本摘要，避免与表单检查编号混淆。

This is a public textual summary of existing controlled local records, without a rerun. It retains general observations and judgment boundaries, excluding design links, nodes, project parameters, source code, and raw images. It is not a publicly reproducible evidence package. RP identifiers are local to this summary to avoid confusion with form-check identifiers.

| ID | 既有观察与归类 / Existing observation and category | 规则依据及结论边界 / Rule basis and conclusion boundary |
| --- | --- | --- |
| RP-01 | 宽窄往返后阅读位置漂移；执行偏差。/ Reading position drifts after a width round trip; execution deviation. | [08 章](../docs/08-implementation-acceptance.md)要求保留约定任务状态与阅读位置。失败限当前载体的变体，不冒充精确夹具。/ Chapter 08 requires agreed task state and reading-position preservation. The failure concerns the carrier variant, not the exact fixture. |
| RP-02 | 另行生成的长列表变体位置漂移；执行偏差。/ Position drifts in a separately generated long-list variant; execution deviation. | 08 章联合复验与状态保留可识别问题；原定精确长列表的所测往返路径通过，不能推广成所有长列表失败。/ Chapter 08 joint regression and state preservation identify the issue; the tested round trip for the exact planned long list passed, so the failure does not cover all long lists. |
| RP-03 | 某布局形态裁切受保护的前景；执行偏差。/ A layout form clips protected foreground content; execution deviation. | [04 章](../docs/04-design-systems.md)区分背景延展与前景保护；所测其他形态不能替代失败形态。/ Chapter 04 separates background extension from foreground protection; other tested forms do not replace the failing one. |
| RP-04 | 空库预览仍可激活却无反馈；执行偏差。/ Empty-library preview remains activatable without feedback; execution deviation. | [03 章](../docs/03-figma-handoff.md)动作/目的地语义及 08 章空态、实际路径检查可识别；恢复新建通过不消除该缺陷。/ Chapter 03 action/destination semantics and chapter 08 empty-state/path checks identify it; successful creation recovery does not remove the defect. |
| RP-05 | 初始状态、正文展开、锚点及部分数据入口与批准夹具不一致；验证执行偏差。/ Initial state, content expansion, anchors, and some data entries differ from the approved fixture; verification-execution deviation. | 08 章身份链与合成输入要求已存在；变体证据只能证明变体。后来精确长列表/空库补测不消除其他差异；原定长正文精确夹具仍有初始状态、正文展开和锚点一致性缺口，不能记 PASS。/ Chapter 08 already requires artifact identity and identified synthetic input; variant evidence covers the variant only. Later exact long-list/empty-library checks do not remove other mismatches; the exact planned long-content fixture still lacks matching initial state, content expansion, and anchor identity, and cannot be recorded as PASS. |
| RP-06 | 删除后焦点目标存在但不在可视区域；执行偏差。/ After deletion, the focus target exists outside the visible area; execution deviation. | [07 章](../docs/07-inclusive-design.md)键盘焦点要求与 08 章实际操作检查可识别；仅 activeElement 正确不足以通过。/ Chapter 07 keyboard-focus guidance and chapter 08 action checks identify it; a correct activeElement alone is insufficient. |

这六项保留为五项实现执行偏差及一项验证执行偏差；不因重新归类宣称已修复。既有条款足以支持这些有限判断，当前没有据此确认新的阻断性规范缺陷。有关“逻辑锚点恢复”和“夹具身份”的两项措辞建议保留为非阻断候选，本轮不写入正文；后续若出现歧义或判断不一致，再评估必要性。

These six findings remain five implementation-execution deviations and one verification-execution deviation; reclassification does not claim they are fixed. Existing guidance supports these bounded judgments, and these observations currently establish no new blocking standards defect. Two wording suggestions on logical-anchor restoration and fixture identity remain non-blocking candidates, without chapter changes in this round; reconsider them if ambiguity or inconsistent judgments arise.

试点已有的导航适用性、绑定/模式/嵌套依赖、重复材质与合法浮层、热区/目的地、异常与未知结果、信息不足等样本，可支持相应限定范围的规则判断；Figma Design、Code Layer、本机运行、文字判断和受控故障模型仍是不同证据。Figma 材质不等于原生系统材质，模拟结果不等于真实后台结果；未执行的分支和原型历史失败继续保留；原 Figma Design 的键盘 FAIL 不由 Code Layer 的通过结果覆盖，不计算合并通过率。

Existing pilot samples concerning navigation applicability, binding/modes/nested dependencies, duplicate material and legitimate overlays, hit regions/destinations, failure/unknown outcomes, and insufficient information support bounded rule judgments. Figma Design, Code Layer, local execution, textual judgments, and controlled fault models remain distinct evidence. Figma material does not establish native material behavior, and simulated outcomes do not establish backend behavior. Unexecuted branches and historical prototype failures remain recorded; Code Layer passes do not overwrite the original Figma Design keyboard FAIL, and no combined pass rate is calculated.

## 记录方式与完成条件 / Recording and completion criteria

每项至少分别记：规则/适用条件、载体与版本、观察和原始结果、问题归属、对规范的判断、责任方/下一步及是否影响本次规范复核。实现 FAIL 可以与“该样本支持规则识别偏差”同时成立；后者不写回实现的通过栏。证据不足时保留 UNKNOWN 或未验证，不强行归责。

For each item, separately record the rule/applicability, carrier/version, observation and original result, issue category, standards assessment, owner/next action, and effect on this standards review. An implementation FAIL can coexist with “this sample supports the rule detecting the deviation”; the latter does not replace the implementation result. Insufficient evidence remains UNKNOWN or unverified rather than forcing attribution.

示例的 NOT_RUN 是该示例未执行的事实，不自动变成本仓库必须逐项清零的任务。范围归属和原始结果是两列；不得仅因移出 Issue #7 就改成 PASS 或 NOT_APPLICABLE。采用项目仍遵守[验收模板](../templates/verification-record.md)：任一适用的必需子项 FAIL、BLOCKED 或 NOT_RUN，父项不得 PASS。两项实际读屏继续暂缓，保留 NOT_RUN 与历史 BLOCKED；只有维护者明确恢复时才安排测试，不以键盘或属性读回替代。

Example NOT_RUN states describe unexecuted examples; they do not automatically create a repository obligation to clear every field. Scope ownership and original results are separate: moving an item out of Issue #7 does not turn it into PASS or NOT_APPLICABLE. Adopting projects retain the [verification template](../templates/verification-record.md) rule: a parent cannot PASS if an applicable mandatory subcheck is FAIL, BLOCKED, or NOT_RUN. The two actual screen-reader checks remain deferred, retaining NOT_RUN and historical BLOCKED states; schedule them only after explicit maintainer resumption, without substituting keyboard or attribute evidence.

Issue #7 的建议完成条件：

1. 全库历史复核与后续增量的版本、章节覆盖和未覆盖范围可追溯；没有将局部结论外推到全库。
2. 已确认的阻断性规范问题得到解决；非阻断建议有明确处置或后续入口。
3. 代表性的正常、异常、信息不足与适用边界样本能够支撑判断，证据局限已说明；不要求穷举产品组合。
4. 执行偏差、实际项目验收与采用环境验证已分别归属；原始结果和暂缓决定保留。
5. 由维护者确认上述范围完成后再决定结项；本轮整理本身不关闭 Issue #7、总议题或正式发布里程碑。

Proposed completion criteria for Issue #7:

1. Historical repository review and later increments have traceable versions, chapter coverage, and gaps, without extrapolating partial findings to the whole repository.
2. Confirmed blocking standards issues are resolved; non-blocking suggestions have dispositions or follow-up entries.
3. Representative normal, failure, insufficient-information, and applicability-boundary samples support judgment with stated evidence limits; exhaustive product combinations are not required.
4. Execution deviations, consumer-project acceptance, and adoption-environment checks have separate ownership; original results and deferrals remain intact.
5. The maintainer decides closure after confirming this scope is complete. This reorganization alone closes neither Issue #7, the tracking issue, nor the formal-release milestone.
