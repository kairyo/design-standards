# v0.1 审阅记录

状态：`REVIEW_CANDIDATE`，不是正式发布、项目采用或产品验收结论。

2026-11-04 许可状态更新：本版本原创文档采用 CC BY 4.0、原创代码采用 MIT，范围和贡献条件见 [许可说明](LICENSE-NOTICE.md)。以下各日期的“许可待定”均保留为历史快照；许可变更不补认全库审阅或产品验收。

## 2026-11-25 · 电视端设计与排查 / TV design and verification

本地候选基于 `29bd9e8f1adf467640933bc7fdc8b14887322c8d`。定向补读 S01、S03，并将 25 个官方页面登记在 S27–S37。作者核对双语入口、两端章节、十二条排查动作与合成例。[来源登记](references/sources.md#s27) · [电视附页](templates/tv-design-review.md)

文档走查涵盖停焦与确认、原项下架、普通返回与 Live 深链、共享账户与缺少手机、媒体中断与遥控重连、两家商店交付，以及真机与辅助技术的证据条件。结构检查通过，覆盖 60 个必需文件、50 份 Markdown、456 个内部链接和 37 条来源，`git diff --check` 通过。电视附页的表格与两端 `NOT_RUN` 示例均可正常解析。在临时副本分别移除附页及 S37，检查器均按预期报错，恢复后通过。

独立复核对照官方原文，修正了系统标签停焦、Live 直达播放与返回、后台音频与视频、旧设备认证前提、TV 商店素材与输入硬件等适用条件。Android 左右定位键的官方符合性仍为 `UNVERIFIED`。报告只覆盖规范、来源与文字场景。运行、辅助技术、SDK 兼容和商店审核由实际项目取证。

This local candidate is based on `29bd9e8f1adf467640933bc7fdc8b14887322c8d`. The author revisited S01 and S03, registered 25 official pages in S27–S37 and checked both README entry points, the platform chapters, twelve checks and the synthetic example. [Source register](references/sources.md#s27) · [TV worksheet](templates/tv-design-review.md)

Document walkthroughs covered focus versus activation, a removed item, ordinary Back and Live deep links, a shared account without a phone, playback interruptions and remote reconnection, store deliverables, and the evidence needed for hardware and assistive technology. The structural check passed for 60 required files, 50 Markdown documents, 456 internal links and 37 source entries. `git diff --check` passed. The worksheet tables and both `NOT_RUN` examples parsed correctly. Removing the worksheet or S37 from a temporary copy caused the checker to fail, and restoring each fixture restored the passing result.

Independent review against official sources led to corrections for focus-driven tab selection, Live playback and Back, background audio and video, authentication on older devices, store assets and input hardware. Official Android left/right seek conformance remains `UNVERIFIED`. This review covers the standards, sources and text scenarios. Adopting projects provide runtime, assistive technology, SDK compatibility and store-review evidence.

### 会议室预约电视应用的文字案例 / Meeting-room booking TV app text cases

本轮使用上述本地候选，电视附页的 Git 文件对象为 `fa7e55ae4ecf830f26f9a63dac259957ecefc350`。作者先记录判定，再由未见预期答案的独立审阅者按相同条文判读三个案例。下表中的录像、输入和预约记录都是题设。

The author recorded the expected decisions before an independent reader applied the same local candidate to the three cases without seeing those decisions. The TV worksheet is identified by the Git blob above. The recording, inputs and booking event below are hypothetical.

| 案例 / Case | 条文在本题中的判定 | Decision within the case |
| --- | --- | --- |
| 功能范围 / Feature scope | 两端均能浏览会议室、选择时段、确认预约和返回。该版本没有音视频，TV08 播放与 TV09 字幕、音轨均记 `NOT_APPLICABLE` 并写明原因。TV02 焦点、TV03 确认、TV04 返回仍适用，实际执行另行记录。 | Both platforms support choosing a room and time, booking it and returning. With no audio or video, TV08 playback and TV09 captions and tracks are `NOT_APPLICABLE`, with the reason recorded. TV02 focus, TV03 activation and TV04 Back still apply. Execution is recorded separately. |
| 停焦与预约 / Focus and booking | 在 UIKit 系统标签「本周」停焦后切换面板，符合该控件约定。普通「确认预约」按钮只有停焦、没有按下，却创建了预约，题内为 `FAIL`，归为执行偏差。 | Dwelling on the UIKit “This week” tab may switch panels. In the second sequence, dwelling on the ordinary “Confirm booking” button created a booking without a press. That action is a `FAIL` in the fixture and an implementation deviation. |
| 两端证据 / Platform evidence | 两端都要求验证返回与物理遥控器休眠重连。题设录像完整显示 Apple TV 按 Back 回到原会议室和原列表位置，只有这一子项可判 `PASS`。Apple TV 重连未执行。Android TV 只有设计截图，返回与重连均未执行。这三项各记 `NOT_RUN`，保留已验子项，两端合并不能判通过。 | Back and physical remote reconnection are required on both platforms. The hypothetical recording supports `PASS` only for Apple TV Back to the original room and list position. Apple TV reconnection was not run. Android TV has only design screenshots and neither action was run. These three subchecks remain `NOT_RUN`, so the combined flow cannot pass. |

三题的两次判读一致，现有条文足以识别题内偏差和证据缺口。本轮规范抽查完成，实际产品验收未执行。Both readers reached the same decision on all three cases. The clauses distinguish the execution deviation and missing evidence. The standards check is complete. Product acceptance was not run.

判定依据 / Rules used · [电视附页 / TV worksheet](templates/tv-design-review.md) · [tvOS 焦点 / tvOS focus](docs/05-apple.md#tvos) · [子项与汇总 / Subchecks and aggregation](templates/verification-record.md) · [问题归属 / Finding ownership](reviews/2026-11-17-review-scope.md)

## 2026-11-17：视觉技能提交候选 / Visual-skill submission candidate

本轮在主线 `881ef4a81b1226e48a3be1194f0ebc62ac5fb4b7` 上整合已留存的视觉方法草案，范围与证据见[视觉方法记录](reviews/2026-11-06-visual-craft.md)。维护者授权提交、推送功能分支并创建中英双语 PR；不合并或开启自动合并，不安装技能、改变固定采用版本或关闭总议题 #1。PR #19 已合并；下方状态入口整理等段落均为各自阶段的快照，不代表本次待办或授权。

本候选的仓库 `VERSION` 仍为 `0.1.0-draft.3`；`design-direction-review` 元数据为 `0.1.0-draft.3`，`adaptive-ui-review` 为 `0.1.0-draft.2`。历史段落中“两技能均为 draft.2”只描述旧版。2026-11-06 的 44 项合成断言和 14 张截图保留其原输入与运行范围，本轮仅核对留存材料并验证文档整合；不据此宣称自动加载、跨客户端兼容或实际审美收益通过。

This round integrates the retained visual-method draft onto main `881ef4a81b1226e48a3be1194f0ebc62ac5fb4b7`; see the [visual-method record](reviews/2026-11-06-visual-craft.md) for scope and evidence. The maintainer authorizes a feature-branch commit, push, and bilingual PR, excluding merge, auto-merge, skill installation, pinned-adoption changes, or closure of tracking issue #1. PR #19 is merged. The entry-point cleanup and other sections below are snapshots of their respective stages, not this round's tasks or authorization.

In this candidate, repository `VERSION` remains `0.1.0-draft.3`; metadata is `0.1.0-draft.3` for `design-direction-review` and `0.1.0-draft.2` for `adaptive-ui-review`. Historical statements that both skills are draft.2 refer only to the earlier version. The 44 synthetic assertions and 14 screenshots from 2026-11-06 retain their original inputs and execution scope. This round checks retained evidence and document integration only, without establishing automatic loading, cross-client compatibility, or real-world aesthetic benefit.

## 提交整理与当前授权 / Submission preparation and current authorization — 2026-11-17

维护者已授权将状态入口整理提交并推送到功能分支、创建中英双语 PR，并按已审草稿更新 [Issue #1](https://github.com/kairyo/design-standards/issues/1)。本轮不合并、不启用自动合并、不关闭 #1，也不决定正式发布或消费项目采用。实际候选提交、PR 状态和台账更新结果在关联 PR 与 #1 记录；下方本地快照中的“未提交”“尚未更新 GitHub”只描述提交前阶段。

The maintainer has authorized committing and pushing the status entry-point cleanup to a feature branch, creating a bilingual PR, and updating [Issue #1](https://github.com/kairyo/design-standards/issues/1) from the reviewed draft. Do not merge, enable auto-merge, close #1, or decide formal release or consumer-project adoption in this round. The linked PR and #1 record the actual candidate commit, PR state, and register-update outcome. Uncommitted and not-yet-updated statements in the local snapshot below describe the pre-submission stage only.

本地独立复核覆盖四文件差异与 Issue #1 双语草稿；完成勾选的范围与证据、持续公开前关口、专项归档范围和草稿阶段表述四项发现均已修订并回核，限定范围内无剩余发现。已审本地补丁 SHA-256 为 `dc208d93c2544a465fde624b5c7b357af537031ad86e1452f7e921e0a9a990fa`；这是提交整理前的差异标识，不是提交 SHA。本轮只补充阶段与证据说明，未修改规范条款或重跑产品验收；最终候选仍按公开前要求核对。

Local independent review covered the four-file diff and bilingual Issue #1 draft. All four findings on completed-gate scope/evidence, continuing publication gates, archived-test scope, and draft-stage wording were corrected and rechecked, with no remaining findings within scope. The reviewed local patch SHA-256 is `dc208d93c2544a465fde624b5c7b357af537031ad86e1452f7e921e0a9a990fa`; this identifies the diff before submission preparation, not a commit. This round adds stage and evidence notes only, without changing standards clauses or rerunning product acceptance. The final candidate still receives the required pre-publication checks.

## 提交前本地状态快照 / Pre-submission local status snapshot — 2026-11-17

核对主线基线为 `04a59c89ac63d7fbb35d346d10dfefb1b1890af0`：[PR #18](https://github.com/kairyo/design-standards/pull/18) 已合并，[Issue #7](https://github.com/kairyo/design-standards/issues/7) 已由维护者确认按“规范复核与执行一致性”的限定范围结项。[总议题 #1](https://github.com/kairyo/design-standards/issues/1) 仍开放。本轮状态入口整理是该基线之上的本地未提交增量；Issue #1 更新稿另行准备，尚未更新 GitHub。

The checked main baseline is `04a59c89ac63d7fbb35d346d10dfefb1b1890af0`: [PR #18](https://github.com/kairyo/design-standards/pull/18) is merged, and the maintainer confirmed [Issue #7](https://github.com/kairyo/design-standards/issues/7) complete within its defined scope of standards review and execution consistency. [Tracking issue #1](https://github.com/kairyo/design-standards/issues/1) remains open. This entry-point cleanup is an uncommitted local increment on that baseline; a separate Issue #1 update draft has been prepared but not applied to GitHub.

| 归属 / Category | 当前处置 / Current disposition |
| --- | --- |
| 本库维护待办 / Repository maintenance tasks | 审阅本轮状态入口差异与 Issue #1 草稿；后续提交、推送及台账更新须按维护者授权执行。本轮不修改结项条件，不关闭 #1。/ Review this entry-point diff and the Issue #1 draft. Subsequent commits, pushes, and register updates require maintainer authorization. This round neither changes closure criteria nor closes #1. |
| 维护者待决定 / Maintainer decisions | 总议题的结项范围、时机与正式发布分别决定。子议题完成不自动关闭总议题，也不创建稳定发布标签。/ Decide the tracking issue's closure scope and timing separately from formal release. Completing a child issue neither closes the tracking issue automatically nor creates a stable-release tag. |
| 历史证据与限制 / Historical evidence and limitations | 首轮复核、增量修订及复验按各自版本解释；原始结果与范围保留。已确认规范问题的处置见 #7 及[范围索引](reviews/2026-11-17-review-scope.md)，不据局部记录宣称当前全库重新通过。#7 归档备忘仅涉及 F09/B06 两项实际读屏：已移出本库待办、结项前提和固定提醒，仅供查询；实际读屏 NOT_RUN 与历史父项 BLOCKED 保留。该决定不改变其他检查的范围。/ Interpret the initial review, incremental corrections, and rechecks within their own versions; retain original results and scope. See #7 and the [scope index](reviews/2026-11-17-review-scope.md) for dispositions of confirmed standards issues, without claiming a fresh whole-repository pass. The archived memo in #7 concerns only actual F09/B06 screen-reader checks: removed from repository tasks, closure prerequisites, and recurring reminders, for reference only; actual execution remains NOT_RUN and historical parent results remain BLOCKED. This decision does not change the scope of other checks. |
| 采用项目与环境验证 / Adopting projects and environment checks | 具体产品验收、SDK/账户能力、技能加载与自动选择、跨客户端兼容及实际效果由相应采用范围决定。缺少证据仍是未验证；不是本库内容复核的一揽子前提。本轮未执行这些检查。/ Product acceptance, SDK/account capabilities, skill loading and automatic selection, cross-client compatibility, and real-world effects depend on the relevant adoption scope. Missing evidence remains unverified, not a blanket prerequisite for repository content review. None of these checks ran in this round. |

版本标识分别保留：仓库 `VERSION` 为 `0.1.0-draft.3`，两个技能的元数据为 `0.1.0-draft.2`；本轮不改号，不据这些标识推断正式发行、宿主兼容或实际采用。许可继续按现有说明执行。下方日期条目与折叠的旧“待决定 / 未验证”清单均是历史记录，其中“未提交”“待审”“未启用”等表述只描述各自时点，不覆盖本摘要或相应项目的后续证据。

Retain the version identifiers separately: repository `VERSION` is `0.1.0-draft.3`, while both skills' metadata says `0.1.0-draft.2`. This round changes neither identifier and infers no formal release, host compatibility, or actual adoption from them. Existing licensing remains in effect. Dated entries below and the folded former pending/unverified list are historical records: statements such as uncommitted, awaiting review, or not enabled describe their respective stages, rather than overriding this summary or later evidence from the relevant project.

## 2026-11-17：规范复核范围与记录归属 / Standards-review scope and record ownership

本轮基于本地提交 `13203a6564f737609a2b6a81a507bd1d6d7a2ac2` 整理 Issue #7 的记录归属；见[范围索引](reviews/2026-11-17-review-scope.md)。规范问题、执行偏差与实际项目验收分别记录，技能宿主能力另归采用环境验证。历史各轮结论只覆盖其原版本、载体与输入；下方包含“未合并”等当时阶段说明，不用于判断后续远端状态。

阅读合成试点的六项发现保留为五项实现执行偏差与一项验证执行偏差；失败未修复、未改为通过。本轮没有重跑案例、修演示或补做产品/读屏验收。两项实际读屏继续暂缓；示例 NOT_RUN 与历史 BLOCKED 保留，实际项目的必需子项汇总规则不变。是否完成规范复核仍由维护者按明确范围决定，不自动关闭 Issue #7 或发布。

This round uses local commit `13203a6564f737609a2b6a81a507bd1d6d7a2ac2` to reorganize Issue #7 record ownership; see the [scope index](reviews/2026-11-17-review-scope.md). Standards issues, execution deviations, and consumer-project acceptance are recorded separately; skill-host capabilities belong to adoption-environment verification. Historical conclusions retain their original version, carrier, and input scope. Earlier statements such as “not merged” describe their own stage, not subsequent remote status.

The six synthetic reading-pilot findings remain five implementation-execution deviations and one verification-execution deviation; failures have not been fixed or converted to passes. No cases, demo repairs, product acceptance, or screen-reader checks were run in this round. The two actual screen-reader checks remain deferred. Example NOT_RUN and historical BLOCKED states, and the project mandatory-subcheck aggregation rule, remain intact. The maintainer still decides whether the defined standards-review scope is complete; this does not automatically close Issue #7 or authorize release.

## 2026-11-17：修订与验证记录的提交整理 / Packaging corrections and verification records

维护者已授权将三项修订和验证记录提交、推送到 PR #17 的原功能分支，并更新中英双语说明；不合并、不启用自动合并，不改变主线或固定采用版本。下方“本地未提交”等表述是上一阶段的历史快照，不描述后续远端状态。

新增[公开验证记录](reviews/2026-11-17-navigation-review.md)，保留初审版本、三项发现与修订、十个作者文字对照、独立复核结论及未验证项。提交整理只增加记录、文件清单及入口/状态说明，不再修改已审的三项规则。最终远端 SHA 和状态以 PR 的提交及说明为准；未执行产品检查仍为 NOT_RUN。

作者提交整理检查：结构校验通过（55 个预期文件、45 份 Markdown、326 个内部链接、24 条来源），差异格式检查通过。此结果覆盖新增公开记录的候选树；不改写下方本地修订阶段 54/44/319/24 的历史结果，也不是 GitHub CI 或产品验收成绩。

The maintainer authorized committing and pushing the three corrections and verification records to the original branch for PR #17, and updating bilingual information. Merging and auto-merge remain excluded; main and pinned adoption stay unchanged. Statements such as “uncommitted local changes” below are historical snapshots of the preceding stage, not later remote status.

The new [public verification record](reviews/2026-11-17-navigation-review.md) retains the initial review version, findings and corrections, ten author text comparisons, independent-review conclusions, and limitations. Packaging only adds evidence, the file inventory, and entry/status information; it does not change the three reviewed rules. The PR commits and description identify final remote SHA and status. Unexecuted product checks remain NOT_RUN.

Author packaging checks passed: 55 expected files, 45 Markdown files, 326 internal links, and 24 sources, plus diff-format checking. These results cover the candidate tree including the new public record; they do not rewrite the earlier local-stage 54/44/319/24 snapshot and are not GitHub CI or product-acceptance results.

## 2026-11-17：PR #17 三项意见的本地修订 / Local corrections for three PR #17 review items

固定提交 `6ed3ec1b790348643d16f5e242017a354576b5f2` 已完成独立文档复核，发现一项 P2：05 章遗漏纯文本工具栏项的例外；以及两项 P3 非阻塞建议：N06 需限定同一语义操作的热区，N09 需明确模拟结果也不证明后台行为。下方较早的作者自检与待审状态保留为历史快照。

该提交上的本地未提交修订已补回上述限定，同步 N02、N06、N09、两条反例、S02 核对记录及双语入口。此次没有新增来源、改变版本或许可，也未更改验收模板的必需子项汇总规则。

- 作者定向复验：对照旧、新文字走查十个正常、例外、异常与信息不足场景，未发现三项问题继续存在；标题/辅助语义、合法子操作与变体、未知结果及缺分支的保护规则保留。这是文档判断，不是十个真实交互测试。
- 作者结构检查：54 个预期文件、44 份 Markdown、319 个内部链接、24 条来源通过；差异格式检查通过。最终本地差异及验证证据另行保留，不把未提交工作目录冒充新提交 SHA。
- 修订的独立复核：独立执行者对三项修订及相邻条款逐项复核，确认 R1、R2、R3 均已解决，所检规则未发现新增问题。另提示 CHANGELOG 的历史待审文字可能与当前状态混淆，已在新条目标明旧段为当时快照并保留原文。复核仅覆盖文档修订，不代表产品或合并批准。
- 未验证与授权：N01–N12 全部保持 NOT_RUN；未执行 Figma、原型、辅助技术、模拟器、真机或后台验证，历史案例未重跑。本轮仅本地修订，未提交、推送、合并或开启自动合并，未更改主线或固定采用版本；没有新增 GitHub CI 结果。

Independent document review of fixed commit `6ed3ec1b790348643d16f5e242017a354576b5f2` found one P2 issue: chapter 05 omitted the text-only toolbar-item exception. Two non-blocking P3 suggestions asked N06 to scope hit regions to one semantic operation and N09 to state that simulated outcomes also do not prove backend behavior. The earlier author checks and pending-review status below remain historical snapshots.

Uncommitted local changes on that commit restore these boundaries and align N02, N06, N09, two counterexamples, the S02 recheck, and bilingual entry points. No sources were added, version or licensing changed, or mandatory-subcheck aggregation rules in the verification template altered.

- Author targeted recheck: compare old and new wording across ten normal, exceptional, failure, and insufficient-information scenarios. The three issues no longer appear in these textual judgments. Title/accessibility semantics, valid child actions and variants, unknown outcomes, and missing-branch safeguards remain intact. These are document checks, not ten real interaction tests.
- Author structural checks: passed with 54 expected files, 44 Markdown files, 319 internal links, and 24 sources; diff-format checking also passed. Final local differences and verification evidence are retained separately; an uncommitted working tree is not presented as a new commit SHA.
- Independent review of the corrections: a separate reviewer checked each correction and adjacent guidance, confirmed R1, R2, and R3 resolved, and found no new issues in the reviewed rules. The reviewer also noted possible confusion between historical pending-review wording in CHANGELOG and current status; the new entry now identifies the earlier wording as a historical snapshot and preserves it. This review covers document corrections only, not product or merge approval.
- Limitations and authorization: all N01–N12 remain NOT_RUN. No Figma, prototype, assistive-technology, simulator, physical-device, or backend checks were performed; historical cases were not rerun. This round only changes local files: no commit, push, merge, or auto-merge, and no changes to main or pinned adoption. No new GitHub CI result exists.

## 2026-11-17：导航、材质与原型增补 / Navigation, material, and prototype increment

基于 `816adfc55e3564052801b405528b6b1ec39ec9fb` 的本地文档候选，修改 03、04、05、08 章、验收模板和相关入口，新增[合成案例](examples/adaptive-navigation-materials.md)。本轮只提炼通用方法，没有引入真实项目的设计链接、图层标识、资产、设备尺寸或材质参数。当前固定采用版本保持不变。

This local documentation candidate is based on `816adfc55e3564052801b405528b6b1ec39ec9fb`. It updates chapters 03, 04, 05, and 08, the verification template, and related entry points, and adds a [synthetic example](examples/adaptive-navigation-materials.md). It derives general methods without importing real project design links, layer identifiers, assets, device dimensions, or material parameters. The current pinned adoption version remains unchanged.

- 作者检查：结构校验通过（54 个预期文件、44 份 Markdown、319 个内部链接、24 条来源），`git diff --check` 通过。完整候选文件清单均可按 UTF-8 读取；定向检查未发现所检私有项目标识、设计链接、本机路径或新增具体尺寸/透明度数值。已通读完整增量、相邻条款和双语入口；这不构成全库事实、隐私或许可认证。
- 内容边界走查：核对局部操作与重复导航、视觉标签与徽标/辅助名称、嵌套材质与重复效果、变量/组件消费者、自动布局后的几何、子图标截获、合法变体动作、无前序返回、单项删除与空列表、隐藏历史层、渲染未就绪、抽样覆盖和受限图片变化。澄清官方材质分层中的短暂交互例外，并将来源读取范围写为实际段落。以上为作者对条款与反例的走查，没有执行合成案例或独立评测。
- 来源：2026-11-17 定向补读 S02 的导航位置、内容区局部操作、标题/符号与背景延展，新增 S24 材质用途及辅助设置来源；具体读取范围见来源登记。未核实 SDK 行为，未重新认证其他来源或许可。
- 独立文档审阅：`NOT_RUN`，由维护者安排主管复核；作者内容走查不构成独立批准。
- 实际执行：合成案例 N01–N12 全部 `NOT_RUN`；没有执行该合成应用的 Figma 操作、原型、辅助技术、模拟器、真机或后台验证。历史产品和文字案例未重跑，成绩保持原记录。
- 授权与边界：上述结果是本地自检快照。维护者随后授权提交、推送并创建写明改进与验证边界的双语 Issue/PR，交主管复核，明确不合并；最终提交与远端状态在 GitHub 交接中记录。本次不正式发布、安装技能或修改消费项目/全局规则。自检时 GitHub CI 未运行。

- Author checks: structural validation passed (54 expected files, 44 Markdown files, 319 internal links, 24 sources), as did `git diff --check`. The full candidate file inventory is readable as UTF-8. Targeted checks found none of the inspected private project identifiers, design links, local paths, or newly added numeric dimensions/opacity values. The full increment, adjacent clauses, and bilingual entry points were read; this does not certify repository-wide facts, privacy, or licensing.
- Content-boundary walkthrough: checked local actions versus duplicate navigation, visual labels versus badges/accessibility names, nested versus duplicated materials, variable/component consumers, post-layout geometry, child-icon interception, valid variant actions, return without prior history, single-item deletion versus an empty list, hidden history, render readiness, sample coverage, and constrained image edits. Clarified the transient-interaction exception in official material guidance and recorded the actual paragraphs read. These are author checks of guidance and counterexamples, not synthetic-case execution or independent evaluation.
- Sources: on 2026-11-17, re-read the scoped S02 guidance on navigation placement, content-local actions, titles/symbols, and background extension; add S24 on material roles and accessibility settings. The registry records exact scope. SDK behavior was not verified, and other sources or licenses were not recertified.
- Independent document review: `NOT_RUN`; the maintainer will arrange supervisor review. Author content checks are not independent approval.
- Execution: all synthetic checks N01–N12 remain `NOT_RUN`. No Figma, prototype, assistive-technology, simulator, physical-device, or backend validation of the synthetic application was performed. Historical product and text cases were not rerun; their recorded results remain unchanged.
- Authorization and boundaries: the results above are a local self-check snapshot. The maintainer subsequently authorized committing, pushing, and creating a bilingual issue/PR describing improvements and validation limits for supervisor review, explicitly without merging. The final commit and remote state are recorded in the GitHub handoff. Formal release, skill installation, and consumer/global-rule changes are excluded. GitHub CI had not run at the time of the self-check.

## 2026-11-10：主线整合与增量复核 / Main integration and incremental review

本轮将 main `de153e4258c187a7983f7d2da6c74320f6c07cf7` 整合进自适应分支 `eca5ea1fbb78e154e8f069f7fdb4a2e662bb6c21`。共同基线为 `9dfe4618e58fc2d84f97b19f38f52d0928b96bff`。唯一合并冲突在 CHANGELOG，保留双方完整段落；07、08 章、验收模板、表单验证记录、双语入口和检查器中的 PR #14 内容均保留。下方 2026-11-09 记录及当时 `NOT_RUN` 独立审阅状态保留为历史快照。

This round integrates main `de153e4258c187a7983f7d2da6c74320f6c07cf7` into adaptive branch `eca5ea1fbb78e154e8f069f7fdb4a2e662bb6c21`, with common base `9dfe4618e58fc2d84f97b19f38f52d0928b96bff`. The only merge conflict was in CHANGELOG; both complete sections are retained. PR #14 content remains in chapters 07 and 08, the verification template, form-validation record, bilingual entry points, and checker. The 2026-11-09 record below, including its then-`NOT_RUN` independent review, remains a historical snapshot.

- 作者检查：整合后的结构检查通过，53 个预期文件、43 份 Markdown、301 个内部链接、23 条来源；`git diff --check` 通过。完整候选清单均为 UTF-8 文本，未新增媒体、字体或二进制。通读完整增量与相邻条款，核对双语、公开边界、待公开历史及作者元数据；该范围不构成全库事实或许可重新认证。
- 保真检查：独立初审前的组合树 `a6302df964a9600423e8f90bf00d4ddd6ffc9378` 保留两个父版本的全部原行。随后只做下列两项定向澄清及审阅状态/变更记录更新；原主线条款、来源、技能、许可和版本不变。
- 独立复核：独立上下文的审阅者复核上述组合树的完整增量、保真、声明边界和公开清单；请求配置为 `gpt-6.1-sol` / `high`，没有独立运行时配置读回，不把请求参数当作实际配置证明。初审发现两项：问题归因缺少修复前目标证据（P2）；A08 预期包含加载与恢复，但动作未覆盖（P3）。作者已分别补清 08 章/模板/案例的对照要求和 A08 的分路径动作；审阅者对修订树 `43cfbc254c7fa78fd5d6435e94aba75b353a9724` 定向复核，确认两项解决，所检范围未发现新增问题，并核对拟公开的双语 PR 与提交文字。随后仅更新当前审阅状态说明，历史记录和规范条款保留；这不是合并或产品验收批准。
- 验证边界：八项自适应产品检查仍为 `NOT_RUN`。历史 F09/B06 读屏子项继续暂缓并保留原受阻结果；没有重跑旧文字案例、产品、Figma、辅助技术、模拟器或真机测试。本地检查不是 GitHub CI 通过，也不是产品验收或方法效果证明。
- 授权：维护者授权整合、验证、提交、推送并创建中英双语 PR，明确暂不合并。本地视觉技能草案保留不动；不启用自动合并，不正式发布或启用到消费项目。

- Author checks: integrated structure checks passed with 53 expected files, 43 Markdown files, 301 internal links, and 23 sources; `git diff --check` passed. The complete candidate inventory contains UTF-8 text only, with no added media, fonts, or binaries. The full increment and adjacent clauses were read, including bilingual consistency, disclosure boundaries, history to be published, and author metadata. This does not recertify repository-wide facts or licensing.
- Preservation: the pre-review combined tree `a6302df964a9600423e8f90bf00d4ddd6ffc9378` retained every original line from both parents. Subsequent changes are limited to the two clarifications below and review-status/changelog updates; original main-branch guidance, sources, skills, licenses, and version remain unchanged.
- Independent review: a reviewer in a separate context checked the full increment, preservation, claim boundaries, and public inventory at that tree. The requested configuration was `gpt-6.1-sol` / `high`; no independent runtime readback was available, so requested parameters are not proof of actual configuration. Two findings were raised: missing pre-fix target evidence for attribution (P2), and A08 expecting loading/recovery without corresponding actions (P3). The author clarified the comparisons in chapter 08, the template, and the example, and added path-specific A08 actions. Focused re-review of corrected tree `43cfbc254c7fa78fd5d6435e94aba75b353a9724` confirmed both findings resolved, with no new issue in the checked scope, and checked the proposed bilingual PR and commit text. Only current review-status statements were subsequently updated; historical records and substantive guidance were retained. This is not merge or product-acceptance approval.
- Validation limits: all eight adaptive product checks remain `NOT_RUN`. Historical F09/B06 screen-reader subchecks remain deferred with original blocked results retained. Historical text cases, product, Figma, assistive-technology, simulator, and physical-device tests were not rerun. Local checks are not GitHub CI success, product acceptance, or proof of method effectiveness.
- Authorization: the maintainer authorized integration, validation, committing, pushing, and a bilingual PR, explicitly without merging. The local visual-skill draft remains untouched. Do not enable auto-merge, formally release, or enable consumer adoption.

## 2026-11-09：自适应保真与回归增补 / Adaptive fidelity and regression increment

基于 `9dfe4618e58fc2d84f97b19f38f52d0928b96bff` 的文档候选，范围为 03、04、05、08 章、现有验收模板、[合成案例](examples/adaptive-fidelity-regression.md)及相关入口/文件清单。只增加原创团队方法与合成项目选择；未增加或重新认证平台官方事实，没有引用私有项目材料或具体尺寸。

This documentation candidate is based on `9dfe4618e58fc2d84f97b19f38f52d0928b96bff`, covering chapters 03, 04, 05, and 08, the existing verification template, a [synthetic example](examples/adaptive-fidelity-regression.md), and related entry points/inventory. It adds original team methods and synthetic project choices only, without adding or recertifying official platform facts or referencing private project material or concrete dimensions.

- 作者检查：结构校验通过（52 个预期文件、42 份 Markdown、295 个内部链接、23 条来源）；`git diff --check` 通过。已通读完整增量及合成案例，核对双语入口和声明范围。对完整候选文本树做定向公开性检查，未发现所检项目标识、私有链接/路径或新增具体尺寸；这不构成全面隐私或事实认证。
- 适用边界走查：未知素材比例不推定通过；允许经批准的等比裁剪与排版变化；无溢出时不制造内容；留白不自动判错；共享页面可保留不同状态；背景延展与操作遮挡分开；历史隐藏层不自动清理；原稿更新保护无冲突的已批准修正。以上为作者对条款的内容走查，不是独立模型评测或产品测试。
- 独立文档审阅：`NOT_RUN`，待安排；历史全库复核不覆盖本次增量。
- 产品验证：合成案例八项检查全部 `NOT_RUN`；没有 Figma 实操、原型拖动、辅助技术、模拟器或真机证据，不声称方法效果或产品验收通过。
- 采用与发布：上述结果是提交前的本地自检快照；用户随后授权将候选提交并推送至功能分支。该授权不代表独立审阅、合并、正式发布或消费项目采用已完成。

- Author checks: structural validation passed (52 expected files, 42 Markdown files, 295 internal links, and 23 source entries); `git diff --check` passed. The full increment and synthetic example were read, including bilingual entry points and claim scope. Targeted inspection of the complete candidate text tree found none of the checked project identifiers, private links/paths, or newly added concrete dimensions. This is not comprehensive privacy or factual certification.
- Applicability walkthrough: unknown source proportions do not establish a pass; approved proportional cropping and typography changes remain allowed; no overflow does not justify invented content; whitespace is not automatically a defect; shared pages may preserve distinct states; background extension and obstructed controls are assessed separately; hidden historical layers are not automatically cleaned up; source updates preserve nonconflicting approved fixes. These are author content checks, not independent model evaluations or product tests.
- Independent document review: `NOT_RUN`, unassigned; historical repository-wide review does not cover this increment.
- Product validation: all eight synthetic checks remain `NOT_RUN`. There is no Figma execution, prototype-dragging, assistive-technology, simulator, or physical-device evidence, and no claim of proven effectiveness or product acceptance.
- Adoption and publication: the results above are a local pre-commit self-check snapshot. The user subsequently authorized committing and pushing the candidate to a feature branch. That authorization does not establish completion of independent review, merge, formal release, or consumer adoption.

## 内容范围

十个主题已形成正文，另有来源登记、三个模板和六个匿名合成案例。`0.1.0-draft.2` 新增两个原创审阅技能、能力目录与九个技能边界案例；`0.1.0-draft.3` 补充 03 章的 Figma 画布边界、空间组织和整理验证。已纳入 main、尚未正式发布的表单增补扩展 02、04、07、08 章及两个现有模板，新增完整表单合成示例及分步往返示例。官方资料仅以公开链接及短摘要引用；没有复刻设计资源或原样复制第三方文档。

2026-11-04，已对 `4102b2bf8ce2bd29a69c0cde5436aa8fba64f322` 完成首轮全库独立内容复核；结论和局限见 [全库复核记录](reviews/2026-11-04-repository-review.md)。该结论只覆盖所列版本、来源与文字证据；下列旧轮次仍保留各自时点和范围。

2026-11-05，本地追加 Figma 变量与主题示例、落地页 brief 附页及相关入口。增量范围、文字走查、独立复核与未执行项见 [本轮验证记录](reviews/2026-11-05-figma-landing.md)。它不重写旧轮次成绩，也不表示实际 Figma 或产品检查通过。

On 2026-11-05, local additions introduce a Figma variable/theme example, an optional landing-page brief appendix, and related entry points. See the [verification record](reviews/2026-11-05-figma-landing.md) for the incremental scope, document walkthrough, independent review, and unexecuted checks. This does not rewrite earlier scores or establish actual Figma or product acceptance.

## 自检记录

2026-10-26，作者对候选内容完成下列自检；它不是独立复核。

### 0.1.0-draft.1

- 结构检查：24 个预期文件，22 份 Markdown，47 个内部链接，15 条来源登记，检查通过。
- 公开性定向检查：未发现所检查的内部项目标识、主机个人路径、私有设计/笔记链接或节点格式；文件清单只有正文、版本文件和原创检查脚本。此类扫描不能证明所有隐私风险均不存在，仍需人工复核。
- 范围审阅：固定语言数、品牌数值、Cloud-only、整数尺寸、重试次数和 ImageGen 均未作为无条件通用要求；官方建议、条件性规范要求与项目选择分开。
- 来源审阅：正文采用登记的读取范围；动态网页不假称已固定 SHA，WCAG 与 WCAG2ICT 的适用地位分开。
- 许可检查：未添加统一开源许可证，未携带第三方正文、设计资源或 SDK 导出文件。

上述结果针对候选内容。实际提交历史、元数据、远端分支与 PR 身份在发布交接中单独核对；本文件不以自引用 SHA 冒充该核验。

### 0.1.0-draft.2

- 结构检查通过：31 个预期文件、27 份 Markdown、54 个内部链接、16 条来源登记；`git diff --check` 通过。
- 两个技能完整文件夹分别复制到隔离临时目录，使用系统 Ruby 的 YAML 安全解析器检查 frontmatter、名称、描述、界面字段及调用名称；本地引用均留在各自技能包内。没有读取私人笔记或依赖仓库外的本地文件。
- 宿主自带 `quick_validate.py` 因所用 Python 缺少 PyYAML 未能运行完成；没有安装依赖。上项是替代结构核对，不冒称该校验器通过，也不代表其他客户端运行已验证。
- 在隔离副本注入两个合成错误：技能越界引用、界面元数据中的示例私人路径；文档检查器均报告失败，恢复正常副本后重新通过。测试材料未进入公共文件树。
- 九个合成请求完成作者手工走查，具体处理记录在技能目录；没有运行独立 Agent、自动选择评估或真实设备测试，不据此声称审美效果提升。
- 新内容是原创短工作流；所见第三方技能仅作能力与许可边界索引，未复制其文件。原有十章正文、已安装技能与消费项目均未改动。

这些结果不延伸此前候选的审阅结论；新增技能与检查脚本变化仍需独立复核。

### 0.1.0-draft.3

2026-11-02，本轮仅增加通用 Figma 方法与来源，不重新认证旧版的全部官方资料或技能效果。

- 已读取 S17 指定正文，近似坐标范围和跨页操作描述作为产品能力事实；团队排布与保护建议没有标作 `OFFICIAL_REQUIREMENT`。
- 结构检查通过：31 个预期文件、27 份 Markdown、56 个内部链接、17 条来源登记；`git diff --check` 通过。检查器仅将来源编号上限同步到 S17，其余逻辑未变。
- 使用内存替换输入检查来源登记：正常 S17 通过，缺少 S17、重复 S17、意外 S18 均按预期失败；没有改写真实来源文件或安装依赖。
- 已人工通读完整候选树，并定向扫描候选文本和既有可达历史，未发现本轮发布的隐私或凭据阻碍；扫描不是全面安全认证。最终待公开提交、署名及 PR 文案在提交后另行核对，准确 SHA 和结果留在 PR 交接中；独立复核尚待完成，不预先记作通过。
- 没有访问或修改设计文件，没有操作真实节点或验证极限坐标、跨页依赖、账户功能与性能；这些项目运行证据仍为 `UNVERIFIED`。
- 没有更改许可、安装工具、启用技能、构建或修改消费项目。本轮独立复核只针对明确候选与差异，不替代全仓库正式发布决定。

### 未发布：表单提交与纠错

2026-11-03，基于 `0.1.0-draft.3` / `fd2c9f030fe350e57ddd3508294ef93525b69b34` 完成本地文档增补；记录当时未提交、推送或更改版本号，本记录不代表正式发布或消费项目升级。

- 作者自检：四章分别负责模式选择、组件/token、操作可访问性及验收；完整示例维护一份状态定义，两个模板沿用原有字段与案例。
- 来源：登记 S18–S21 的读取范围、固定提交或动态页面身份、采用与不采用部分；补读同一固定 WCAG 版本的所列条款，不重新认证旧来源的全部内容。
- 结构检查通过：32 个预期文件、28 份 Markdown、85 个内部链接、21 条来源登记；`git diff --check` 通过。
- 检查器在隔离临时副本完成 7 项检查：正常候选通过；缺少 S21、重复 S21、意外 S22、使用未登记的 GitHub 分支或文件、缺少完整示例均按预期失败。测试输入未进入仓库，没有放宽到任意 GitHub 路径。
- 内容与范围：示例输入为原创合成数据；未知提交结果不直接归入可重试失败，原始工具结果与人工判断分开。11 项产品验收全部为 `NOT_RUN`，没有运行产品、服务查询、读屏或自动无障碍扫描。
- 独立文档初审发现两项：查询确认字段拒绝时需要回到纠错状态；重复操作验收需要分别验证客户端拦截与服务端防重复。作者已修订状态表及 F03、F06、F08；独立审阅者完成定向再审，确认两项已解决，未发现新增需修正问题。
- 独立审阅者另核对 S12、S18–S21 的本次相关正文；S18 外链图像与其 LICENSE 未由审阅者重读。复核只覆盖本次文档增补，不追认旧版整库审阅、许可证或任何项目的产品验收；本条为作者对审阅结果的记录，不是审阅者的发布批准。

### 未发布：案例验证后的定向修订

2026-11-03，在上述本地增补后进行案例验证并按发现修订；前节的数量与结论保留为当时快照。该阶段仍为本地候选，当时未提交、推送或更改版本号。

- 前轮对相同 12 个合成文字案例做新旧版对照；独立审阅者依据匿名回答评判，评判时未知版本映射。旧版 11 项完整、1 项部分，新版 10 项完整、2 项部分，两组没有预定义危险建议。单轮结果不证明新版更好或更差，也不属于产品验收。
- 本轮补齐分步往返的草稿、有效字段、依赖步骤与确认关系及具体焦点；增加不可重试整单拒绝的直接/查询路径；把纠错重提后的业务结果核对写入模板和示例。08 章已有原则沿用，未重复追加；并发编辑恢复示例留待后续。
- 作者按原案例与验收条件定向走查上述三类问题，同时检查正常成功、仅回看不修改和结果已知但恢复条件不明的边界；这是文档覆盖检查，没有重新进行一轮模型效果对照。焦点落点及状态名仍为合成项目选择，未改变官方要求或扩大来源采用范围。
- 结构检查通过：33 个预期文件、29 份 Markdown、97 个内部链接、21 条来源登记；`git diff --check` 通过。检查器仅增加分步示例的预期文件入口；原来源与 GitHub 路径限制保留。
- 独立初审指出四处验收表述缺口：整单拒绝查询前后的状态时序、自取分支的实际提交证据、使用非默认排序检验保留、模板中的查询触发动作。作者已逐项修订；独立审阅者完成定向再审，确认四项已解决，未发现新的行为矛盾。本条为作者对该范围审阅结果的记录，不代表发布批准。
- 创建示例 F01–F12、分步示例 B01–B06 共 18 项产品检查全部为 `NOT_RUN`；没有运行产品、服务请求、读屏或自动无障碍扫描。独立文档复核与产品、整库及发布验收分别记录。

### 未发布：修复后完整案例复测

2026-11-03，对原始旧版、修复前快照和修复后快照各执行一轮合成文字案例；这是规范应用的案例评估，不是产品测试。以下是可公开的验证摘要，原始手册包、完整题面/判据、回答和匿名评分保存在作者受控的本地记录中，未随本 PR 公开；本节不是可直接复跑的测试套件。

#### 输入、方法与判定

- 原始旧版为固定提交 `fd2c9f030fe350e57ddd3508294ef93525b69b34`。各组均读取十章正文、三个模板、匿名案例和来源登记；修复前另含完整表单示例，修复后再含分步往返示例。未向执行者提供历史成绩、修复报告或版本映射。
- 三个执行者分别使用独立上下文，均指定 `gpt-6.1-sol` / `high`，按同一指令与顺序各回答 16 例，共 48 份回答。每例三个必要判断及危险建议在执行前固定；另由独立上下文中的同配置模型评审，每例回答次序随机排列，评分时不提供版本映射，评分保存后再解盲。
- 原 12 例覆盖正常、异常、信息不足和原新增场景；追加 C13–C16 四项边界。C12 将过时的“当前七种状态未覆盖”改为中性要求核对所给手册是否覆盖，第三判据相应核对覆盖与项目选择边界；业务事实及危险判据不变，三组采用同一题面。其余原案例和判据保留。
- `PASS` 为三个必要判断完整满足且无危险建议；`PARTIAL` 为存在遗漏或含混但无危险建议；`FAIL` 为危险建议或实质矛盾。这些评级只针对文字回答，不映射为产品验收状态。
- 124 处手册引文均核对到各自原文与章节；48 份评分覆盖 144 项必要判断，其中 354 处证据短引逐字匹配回答字段。结构与引文检查不能替代内容判断。

下列 SHA-256 标识当时提供的 JSON 手册包，供持有原始材料的审阅者核对，不是 Git 提交 SHA，也不单独证明评估有效：

| 手册包 | 文档数 | SHA-256 |
| --- | --- | --- |
| 原始旧版 | 15 | `2d5f5f0a463330867072c50cea3d41f0e78999e8c954966c1f244e734877dfd8` |
| 修复前 | 16 | `78cada5611ba22f1067fca40b10dc8d9c4f9840ff84d9e6cf7d6fd32704d7c37` |
| 修复后 | 17 | `3f87d49c27f18641ceafae9beaea0b489be97c9338d07adba7646e94169484bb` |

#### 本轮结果

| 版本 | 原 12 例 PASS / PARTIAL | 加测 4 例 PASS / PARTIAL | 全部 PASS / PARTIAL / FAIL |
| --- | --- | --- | --- |
| 原始旧版 | 9 / 3 | 3 / 1 | 12 / 4 / 0 |
| 修复前 | 11 / 1 | 2 / 2 | 13 / 3 / 0 |
| 修复后 | 12 / 0 | 4 / 0 | 16 / 0 / 0 |

| 编号 | 合成情境 | 原始旧版 | 修复前 | 修复后 |
| --- | --- | --- | --- | --- |
| C01 | 批准方向内的小文案调整 | PASS | PASS | PASS |
| C02 | 已确认成功后的反馈与操作 | PARTIAL | PASS | PASS |
| C03 | 已批准且可追溯的 Token 覆盖 | PASS | PASS | PASS |
| C04 | 超时却准备清空并自动重提 | PASS | PASS | PASS |
| C05 | 丢失字段拒绝响应后查询、纠错并重提 | PASS | PARTIAL | PASS |
| C06 | 导出成功掩盖循环引用与未批准备用值 | PASS | PASS | PASS |
| C07 | 仅凭按钮截图签收服务端防重复 | PASS | PASS | PASS |
| C08 | 自动检查 incomplete 且人工环境受阻 | PASS | PASS | PASS |
| C09 | 查询、防重复能力和测试权限尚未确认 | PASS | PASS | PASS |
| C10 | 编辑已有记录时发生版本冲突 | PARTIAL | PASS | PASS |
| C11 | 分步表单修改前序分支 | PARTIAL | PASS | PASS |
| C12 | 当前条件下不可重试的整单拒绝 | PASS | PASS | PASS |
| C13 | 已确认未创建，但重试条件未知 | PASS | PARTIAL | PASS |
| C14 | 分步流程仅回看，没有修改选择 | PASS | PASS | PASS |
| C15 | 拒绝到达时焦点仍有效或所在控件被移除 | PASS | PASS | PASS |
| C16 | 批量 6 条成功、2 条字段拒绝、2 条未知 | PARTIAL | PARTIAL | PASS |

#### 发现、修复对应与限制

- C05：修复前再次遗漏重提后的实际业务结果检查；修复后明确比对原标识未创建、新提交标识与输入快照、新记录内容。输入保留、主动定位及不抢焦点的边界同时保留。
- C11：修复后明确返回、分支切换、主动进入下一步及缺项纠错的焦点落点，并检查草稿、确认与请求一致。修复前本轮也通过，而上一轮为部分通过；不能把本例写成稳定的评分提升。
- C12：三组回答均通过。修复后已能直接引用新增整单拒绝条款；旧版和修复前依原则推导并指出覆盖缺口。这里补齐的是明确表达，不能改写成旧版曾失败。
- 修复后四项边界加测均通过。C13 的修复前回答对请求对应关系仍含混，C16 的旧版及修复前回答未明确核对纠正重提后的新业务记录；修复后均补齐。未出现任何一项低于修复前的评级，也没有预定义危险建议。
- 本轮旧版 C02、C10 的部分通过，分别来自成功反馈的焦点边界与冲突解决后数据核对不够明确。历史成绩保持原样；同一快照的单轮生成与判读存在变化，不能把不同轮次直接当作稳定效果测量。
- 案例与判据由已知文档内容的作者准备；C11/C12 已进入修复后示例，新增边界只是有限的迁移检查。版本映射虽隐藏，内容及引用仍可能暴露版本线索；上下文隔离不是操作系统级隔离证明。单轮、模型执行与模型评分不支持统计显著或普遍效果承诺。
- 结构检查通过：33 个预期文件、29 份 Markdown、97 个内部链接、21 条来源登记；`git diff --check` 通过。复测前后 33 个文件哈希、分支、HEAD、暂存区和工作区差异一致。随后仅整理本审阅记录与 CHANGELOG，所测规范正文、模板、示例和来源内容保持不变。
- 18 项产品检查继续为 `NOT_RUN`；没有真实服务、设备、辅助技术或用户试用证据。批量与并发编辑的完整产品契约仍由采用项目定义；本轮不据此扩大采用、许可、发布或合并范围。

## 独立复核重点

- 官方要求与建议分类、动态来源的时效边界、Duo 系统行为的适用条件。
- 本地化、单位、布局精度、构建方式与工具选择没有混入单个项目的绝对规则。
- 交接、真实运行证据和审阅独立性保持清晰，而不引入平行权限体系。
- 原创性、公开性、许可和实际可用性；作者检查不替代独立复核。
- 技能的触发边界、自包含性和真实使用效果；平台建议不得变成默认改配置、设备操作或委派授权。

<details>
<summary>历史清单原样保留：整理前的待决定与未验证项 / Historical list retained verbatim: pending and unverified items before this cleanup</summary>

以下原文保留整理前的状态与结论边界；当前待办及责任归属见上方状态摘要，不把旧清单直接作为新的任务安排。
The original text below preserves the prior state and evidence boundaries. See the status summary above for current tasks and ownership; this historical list does not itself schedule new work.

## 待决定 / 未验证

- 首轮全库独立内容复核已完成，后续修订及复验分别记录；技能加载、实际产品效果和维护者的正式发布决定仍未完成，不创建稳定发布标签。
- 当前版本的原创文档与代码分别按 CC BY 4.0 和 MIT 提供，具体范围见许可说明；历史阶段的许可待定记录保留，第三方权利另行核对。
- 没有对任何现有项目启用规范；没有验证平台 SDK、Figma 账户功能或真实产品运行。
- 没有证据证明采用此文档能提高某个可量化的审美评分；可用性应在获准的代表性任务中评估。
- 没有安装、配置或建立自动更新机制。
- 新技能尚未完成宿主自动选择、跨客户端兼容、独立行为评估或真实项目验收；未创建插件分发包。

</details>
