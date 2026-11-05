# 全库独立内容复核 / Repository-wide independent content review

## 入库整理 / Publication preparation — 2026-11-05

维护者授权将本轮复核资料和文字案例包单独提交、推送并创建双语 PR，暂不合并。当前候选基于 main `ac4e89cbdb789f502ea609427bdec84256ab7d55`，保留已合入的 Figma 变量示例、落地页附页及其验证记录。本次整理不重做下文的全库来源核验、六例文字运行或旧新版对照，不把历史成绩追认到当前组合。

保留内容按维护用途选择：逐章结论和来源读取台账用于追溯依据；三个有限后续修正解决记录歧义与交接示例缺口；题面/判据提供可选的回归入口，原答/评分保留证据。案例不进入十章正文，也不作为每次修改或发布的强制门槛。原工作副本保持原样，原始回答、题面/判据及输入哈希核对保真；模型配置说明另以归档注记澄清，未覆盖旧叙述。

The maintainer authorized a separate commit, push, and bilingual PR for these review materials and text cases, without merging. The candidate is based on main `ac4e89cbdb789f502ea609427bdec84256ab7d55`, retaining the merged Figma variable example, landing-page appendix, and their verification record. This preparation does not repeat the source review, six text responses, or historical old/new comparison below, or extend old scores to the current composition.

Content is retained for specific maintenance purposes: chapter findings and the source-reading ledger make decisions traceable; three limited follow-ups address record ambiguities and a handoff-example gap; prompts/criteria provide an optional regression entry point, while original responses/assessments preserve evidence. The cases do not enter the ten design chapters or become mandatory for every edit or release. The original worktree is preserved; original responses, prompts/criteria, and input hashes are checked for fidelity. An archive note clarifies the model-configuration evidence without overwriting the historical narrative.

当前组合作者自检通过：51 个预期文件、41 份 Markdown、272 个内部链接、23 条来源；追踪与新增文件空白检查通过。二十八项完整检查器场景在临时副本执行，正常及登记来源通过，异常 JSON、布尔版本、重复键/案例、判据/输入缺失、历史答卷混入、转义网址/私人路径及未登记来源等按预期拒绝。两个技能通过现有宿主格式校验器，自包含链接和许可不变；没有安装或加载技能。双语入口一致，六份原答及二十二个历史输入/判据哈希核对保真，两个 PR #12 示例及其验证记录逐字节保留。

现有 20 份规范输入中，02、03、04、08 章、来源登记和通用 brief 共六份因后续增补不同于历史哈希。历史输入可在原工作副本核对，本 PR 不打包一套重复的旧正文快照；仅凭基线 commit 或当前文件不能复原原轮输入。重新执行应记录新的输入身份，不能称本轮案例已通过。当前组合的独立差异复核已完成，在核对范围内未发现阻断问题；下方各轮结果只适用于各自版本。七项 Figma 实操和十八项产品检查仍为 `NOT_RUN`。

Author checks of the current composition passed: 51 required files, 41 Markdown files, 272 internal links, and 23 sources, plus whitespace checks for tracked/new files. Twenty-eight complete-checker scenarios ran in temporary copies: valid input and registered sources passed; malformed JSON, Boolean versions, duplicate keys/cases, missing criteria/inputs, historical answers mixed into guidance, escaped URLs/private paths, and unregistered sources were rejected as expected. Both skills passed the existing host format validator; self-contained links and licenses remain intact, without installation or loading. Bilingual entry points match. All six original responses and twenty-two historical input/rubric hashes were verified, and both PR #12 examples and their verification record remain byte-identical.

Six of the twenty current guidance inputs differ from historical hashes because of later additions: chapters 02, 03, 04, and 08, the source registry, and the general brief. Historical inputs can be checked in the preserved original worktree; this PR does not duplicate a snapshot of the old guidance. Neither the base commit alone nor current files reconstruct the original run. Any new execution must record new input identity; this round does not establish a case pass. Independent diff review of the current composition is complete, with no blocking findings in the checked scope. Historical results below retain their version-specific scope; seven Figma execution checks and eighteen product checks remain `NOT_RUN`.

## 结论与范围 / Conclusion and scope

2026-11-04，针对 [Issue #7](https://github.com/kairyo/design-standards/issues/7) 完成首轮全库独立内容复核。输入为 commit `4102b2bf8ce2bd29a69c0cde5436aa8fba64f322`、tree `6e9310a9dcff22d1e7db4d417017cdcae7f68ffb` 的 43 个公开文件。独立审阅者使用新任务上下文，与候选作者分开；作者固定输入并核对哈希。结论为 `NO_BLOCKING_FINDINGS_WITH_LIMITATIONS`：未发现阻断内容错误，留下两项记录歧义与一项可选短例建议。它不是合并、正式发布、项目采用或产品通过结论。

On 2026-11-04, the first repository-wide independent content review for [Issue #7](https://github.com/kairyo/design-standards/issues/7) covered 43 public files at commit `4102b2bf8ce2bd29a69c0cde5436aa8fba64f322`, tree `6e9310a9dcff22d1e7db4d417017cdcae7f68ffb`. An independent reviewer worked separately from the candidate author in a fresh task context; the author fixed the input and checked its hashes. The verdict was `NO_BLOCKING_FINDINGS_WITH_LIMITATIONS`: no blocking content errors, two record ambiguities, and one optional short-example suggestion. This is not approval to merge, formally release, adopt, or accept a product.

通读范围包括十章正文、三份模板、三份示例、两个技能及元数据、来源登记、双语入口与 GitHub 协作文件、历史审阅记录、许可材料和检查器。21 条来源均取得核心引用对应的实质正文；S04、S11 未逐一读完所有登记操作/示例细节。下表逐项限定范围，不能将“取得正文”写成全文审计。原轮六个文字试答由该审阅者基于完整候选与来源核对上下文生成，作者另按判据评为六项 PASS；这不是盲评、版本对照、技能单独贡献或产品运行证据。

The reading covered all ten chapters, three templates, three examples, both skills and metadata, the source registry, bilingual entry points and GitHub collaboration files, historical reviews, licensing material, and the checker. Substantive text supporting the core citations was obtained for all 21 sources; S04 and S11 did not cover every registered operation/example detail. The ledger below defines each limit; obtaining substantive text is not a full-source audit. The reviewer also produced six text responses using the full candidate and source-review context. The author separately rated all six PASS against the criteria. This was not blinded grading, a version comparison, evidence of the skills' separate contribution, or a product-runtime test.

本文件由作者整理独立审阅结果，详细证据保留中文。下述后续本地修改与新案例运行分别记账；原轮结论不会自动延伸至修改后的候选。记录不含私人聊天、主机路径或第三方正文镜像。

This author-prepared record summarizes the independent review; detailed evidence remains in Chinese. Follow-up local changes and the new case run are recorded separately below; the original verdict does not automatically cover the modified candidate. No private chats, host paths, or third-party document mirrors are included.

## 按章节复核

| 章节 | 发现与建议 |
| --- | --- |
| 01 设计原则 | 无阻断发现。任务、层级、标准控件语义和品牌选择分工清楚，S01对应采用范围成立。 不建议新增固定字号、审美分数或跨平台样式表。 |
| 02 探索与收敛 | 无阻断发现。模式按信息关系及恢复成本选择，不依字段数量；已有批准方向可限制探索范围。T1可据此给出暂定选择及改变选择的条件。 在实际采用中保留访谈推断与真实可用性证据的区别，现有条款已支持。 |
| 03 Figma与交接 | 无阻断发现。S04–S07/S17的核心概念和能力声明有出处，授权、保护、依赖与实际画布验证分开。 可讨论IR7-FIGMA-03；不是要求全面Figma操作教程。 |
| 04 设计系统与素材 | 无阻断发现。DTCG身份、数值表达、别名/冲突/覆盖追踪及运行加载边界清楚。T5能发现暗色循环与同名来源冲突，不让预览掩盖它们。 无需为当前候选补一个导出器或强制schema；真实采用另核验解析与消费者。 |
| 05 Apple | 无阻断发现。Duo内外屏、方向、Split View栏位及条件性保留区与官方Markdown相符，未将建议升级成普遍审核要求。 继续保留SDK/最低系统/运行系统需另核对，以及模拟器与真机证据分离。 |
| 06 Android | 无阻断发现。当前窗口、pane、状态连续性和框架差异有来源；Views维护状态不自动授权迁移。T4无需新增技术栈即可提出有边界调查。 实际项目补齐SDK、依赖和重建路径后再选API；本库没有平台教程义务。 |
| 07 包容性设计 | 无阻断发现。WCAG条件性规范声明、非完整清单和WCAG2ICT非规范地位正确；不靠截图/扫描签署完整流程。T3/T6保留RTL与辅助技术缺口。 可在采用项目建立完整条款清单，本库不应因不是审计器而被判不完整。 |
| 08 实现与验收 | 无阻断发现。版本身份、六类结论、真实动作/业务结果、incomplete与人工复核、例外和复验分离。 原始产品证据仍须由项目提供；本轮文档审阅或试答不能替代。 |
| 09 来源库与经验 | 无阻断发现。读取/采用/运行状态和动态页面边界明确，合成案例未冒充真实事故。 技能内WCAG路由可按IR7-SOURCE-02收紧范围主语；21条实际核验范围见独立台账。 |
| 10 采用维护与回退 | 无阻断发现。完整SHA、选择性采用、冲突处理、升级与产品回退的边界明确。 可按IR7-STATE-01补历史状态就地说明，保留已有历史结论。 |

模板、示例、许可划分与协作边界之间未发现阻断矛盾。原轮检查器结果为 43 个预期文件、35 份 Markdown、166 个内部链接、21 条来源；这组计数仅属于原轮。两个技能元数据通过当时的 YAML 安全解析及包内链接核对，不代表宿主加载或自动选择成功。

## 来源实际读取台账

读取日期均为 2026-11-04。原始地址、版本和采用范围继续由 [来源登记](../references/sources.md) 管理；本表记录这一轮的实际读取，不覆盖初读日期，也不能重构动态网页的历史内容。具体事实采用范围没有因本轮新增为完整认证。

| 来源 | 本轮实际读取 | 限制 |
| --- | --- | --- |
| [S01](../references/sources.md#s01) | 动态官方Markdown；本轮读取Visual hierarchy、Adaptability、Size classes、Guides and safe areas及Change log；当前显示2026-09-09。 | 未读取子链接、视频或验证SDK；图片未作视觉审阅。 |
| [S02](../references/sources.md#s02) | 动态官方Markdown正文，包括Anatomy/Device poses、Dynamic layouts/Reserved regions、Vertical controls和Change log；当前显示2026-09-09。 | 没有设备、系统版本或API运行证据；没有查看图片或视频。 |
| [S03](../references/sources.md#s03) | 动态官方Markdown的Discussion、Vision、Hearing、Mobility、Speech；文字正文与表格。 | 没有逐条采纳源表格数值；没有辅助技术运行或链接文档审计。 |
| [S04](../references/sources.md#s04) | 动态页概念、类型清单、访问条件、Boolean属性的原型连接警告；未逐一读取每类属性的所有创建步骤和限制。 | 本轮为部分登记范围复核；不是完整属性操作教程或真实文件验证。 |
| [S05](../references/sources.md#s05) | 动态页概念、Variables for designs and design systems、模式与上下文说明、发布变量访问前提。 | 嵌入视频、变量子文档和账号能力未验证。 |
| [S06](../references/sources.md#s06) | 动态页Foundational differences、Scalability and management、Final thoughts；亦见Supporting features中的路线文字。 | 没有逐项验证功能现状、图片或外链；动态页并非永久固定版本。 |
| [S07](../references/sources.md#s07) | 动态页访问套餐说明、Compare changes、Version history、Compare properties。 | 没有验证用户账号、席位或文件权限；补充来源另列，不伪称原登记页当前仍显示所有席位文字。 |
| [S08](../references/sources.md#s08) | 动态页窗口分类、动态变化、Manage layouts、Test window size classes，当前Last updated为2026-10-23。 | 未验证项目库/API；源例代码未执行。 |
| [S09](../references/sources.md#s09) | 动态页Content panes、Compose Material 3 Adaptive、Configuration and continuity、Posture、Input beyond touch、How to test及测试方式文字。 | 没有执行安装命令、代码、设备流或子链接。 |
| [S10](../references/sources.md#s10) | 动态页适配导言、Methods and quality、pane/containment与内容最大宽度文字。 | 未重核历史2026-10-22页日期，不将历史日期当版本；未审图像、链接与API。 |
| [S11](../references/sources.md#s11) | 动态页概览、Label elements的语义/标签概述，以及Add accessibility actions、Use built-in accessibility features、custom semantics和Use cues other than color相关文字。 | 未逐项读完Label elements全部示例与子章节，代码未执行；本轮为部分登记范围复核。 |
| [S12](../references/sources.md#s12) | 固定Recommendation身份、第5节5.1–5.3正文，以及2.4.3、3.3.1–3.3.3、4.1.2–4.1.3。为核验T6另读5.2.2的响应式变体注记、5.2.3完整流程和accessibility-supported定义。 | 不是完整成功准则审计、法律判断或产品符合证明；未据片段补全其他条款。 |
| [S13](../references/sources.md#s13) | 固定2025.10身份/Status、Introduction、Types与Dimension正文（包括整数/浮点和单位）。 | 没有审计完整格式、resolver/color附篇或认证导出器。 |
| [S14](../references/sources.md#s14) | GitHub connector读取默认分支README 1–55行；maintenance mode/无Views计划功能发行及Compose方向。LICENSE首部确认Apache 2.0标识。README blob 25897a2861a3f3ef297f89c61636624e418a72a7。 | 此为2026-11-04当前默认分支读回，不能重构2026-10-26快照；未完整审计许可证或依赖。 |
| [S15](../references/sources.md#s15) | 固定2025-12-11 Group Note身份、Abstract、Status。 | 没有通读逐条适配、实施或认证原生项目。 |
| [S16](../references/sources.md#s16) | 以本地候选SKILL.md/openai.yaml核对格式，再读取官方OpenAI Build skills完整文字，重点目录、显式/隐式调用、本地发现和Optional metadata。 | 本轮没有安装或执行客户端发现；官方格式与本地YAML解析不等于宿主加载、自动选择或跨客户端兼容通过。 |
| [S17](../references/sources.md#s17) | 动态页画布范围/Page组织、Create pages访问前提、Move layers between pages。 | 未验证极限坐标、文件权限、跨页依赖或性能；未读取所有子链接。 |
| [S18](../references/sources.md#s18) | GitHub connector读取固定提交文件文字，重点设计目标/原则、普通布局、基础分步和分组表单；同提交LICENSE全文。源文件blob 466e948159a6469d2243f43b41c06b6b8fee1325。 | 未打开外链图像、附件或参考文章；不推定图像再分发权，不作视觉案例已核验声明。 |
| [S19](../references/sources.md#s19) | 动态页Overview、Default design token metadata、Referencing/Aliasing、Collision warnings完整相关文字。 | 没有运行导出器、核对项目版本或宣称DTCG兼容；不复制schema。 |
| [S20](../references/sources.md#s20) | 动态页Accessibility、Labeling、Supported screen readers、Automated testing、Internationalization概述及Interactions文字。 | 发布者兼容测试不是本库运行证据；未读所有子链接、原生能力或执行测试。 |
| [S21](../references/sources.md#s21) | GitHub connector读取固定提交用途概述与The Accessibility Rules的incomplete说明；同提交LICENSE前10行确认MPL 2.0身份。 | 未进行全规则审计、扫描或完整许可证法律分析；未采用平均检出率作为覆盖保证。 |

S07 的席位与文件权限另用 Figma 官方 Guide to inspecting 的访问段落补核；现已登记在 S07 下。原 compare 页面本轮支持套餐条件和差异查看用途，不伪称该页仍显示所有席位文字。未验证任何用户账户、席位或文件功能。

## 发现与本地处理 / Findings and local follow-up

| 编号 | 原轮发现 | 本地处理 |
| --- | --- | --- |
| IR7-STATE-01 | 历史“当前”与当前仓库状态容易混读；低优先级 | [REVIEW](../REVIEW.md) 改为已入 main、未正式发布；[历史协作报告](2026-11-03-github-management.md) 增加日期与快照提示。原成绩、结论、日期不改。 |
| IR7-SOURCE-02 | 技能初读范围误用“本仓库”主语；低优先级 | [技能路由](../skills/adaptive-ui-review/references/platform-sources.md) 明确为该技能 2026-10-26 初始范围，不外推为全库后续范围，保留自包含性和非完整审计边界。 |
| IR7-FIGMA-03 | 可选教学短例，现规则已有主要保护边界 | [03 章](../docs/03-figma-handoff.md) 分别说明正确父子归属、已批准浮层溢出、无归属说明卡；结构判断仍不能替代实际画布证据。 |

The local follow-up dates historical “current” statements without rewriting old results; limits the skill's initial WCAG reading scope to that skill and date; and adds a short chapter 03 example separating semantic ownership from intentional overflow. These changes preserve package self-containment and the need for actual canvas evidence.

另按作者建议增加 [最小文字案例包](text-cases/README.md)。题面、判据与运行记录分开，使用明确的 20 份规范输入及文件哈希；它是今后维护的复跑入口，不把历史 16 例摘要改写成可复跑套件，也不将原轮六个试答冒充这套新协议的执行。

The author also proposed the [minimal text-case suite](text-cases/README.md). It separates prompts, criteria, and run records and identifies 20 guidance inputs by file hashes. It provides a rerun entry point for future maintenance. It neither relabels the historical 16-case summary as reproducible nor presents the original six responses as execution of this new protocol.

## 本地复验 / Local follow-up verification

本地候选基线为上述 commit；未提交改动的精确案例输入及原始回答见 [本轮运行记录](text-cases/2026-11-04-run.md)。2026-11-04 作者自检：

- 文档检查器通过：48 个预期文件、38 份 Markdown、245 个内部链接、21 条来源；追踪文件与五个新增文件的空白检查通过。
- 新增 JSON 检查逻辑以一项正常输入和十一项错误输入定向验证，全部符合预期；错误覆盖格式、重复/缺失案例、判据、输入路径、执行指令及评级定义。注入仅发生在内存，不进入仓库。
- 两个技能均通过现有宿主 `quick_validate.py`；名称、描述及界面元数据未改，包内链接与许可检查通过。此项不表示安装或运行成功。
- 中英文 README 的非语言切换链接目标及出现次数一致；新增材料完成公开性、历史状态与双语等义检查。六份公开回答与冻结原答一致，规范输入及判据哈希未变。
- 六例文字回答按十八项必要判断评为全 PASS，方法和限制详见运行记录；不是独立盲评或产品通过。

The local candidate uses the commit above as its base; see the [run record](text-cases/2026-11-04-run.md) for exact uncommitted inputs and original responses. Author checks on 2026-11-04:

- The documentation checker passed: 48 required files, 38 Markdown files, 245 internal links, and 21 sources. Whitespace checks passed for tracked files and all five new files.
- Targeted checks of the new JSON logic produced the expected result for one valid and eleven invalid inputs, covering format, duplicate/missing cases, criteria, input paths, shared instructions, and rating definitions. Injections remained in memory, outside repository files.
- Both skills passed the existing host's `quick_validate.py`; names, descriptions, and interface metadata are unchanged, and package links and licensing checks passed. This does not establish installation or runtime success.
- Chinese and English README link targets and occurrence counts match, excluding language-switch links. New material was checked for disclosure, historical-state accuracy, and bilingual equivalence. All six public answers match the frozen originals; guidance and rubric hashes are unchanged.
- The six text responses passed all eighteen required judgments under the method and limitations in the run record; this was not independently blinded grading or product acceptance.

独立差异初审确认文档内容与答卷保真没有阻断问题，同时发现检查器两处漏检：`IR7-FU-01` 允许历史技能走查文件混入规范输入，`IR7-FU-02` 未检查新增 JSON 中的网址；另指出布尔值可被当作整数版本 1。当前案例未包含这些问题输入。作者已收紧规范文件集合、让 JSON 解码后的文本复用原网址及公开性检查，并要求整数版本；未放宽网址允许范围。修后两项正常、十八项错误输入检查均符合预期。规范输入与原答哈希未变，无需重新生成六个回答。

The independent initial diff review found no blocking document-content or response-fidelity issue, but identified two checker gaps: `IR7-FU-01` allowed historical skill walkthrough answers into the guidance inputs, and `IR7-FU-02` did not check URLs in the new JSON files. It also noted that a Boolean could be accepted as integer version 1. The current cases contained none of those inputs. The author narrowed the guidance-file set, applied existing URL and disclosure checks to decoded JSON text, and required an integer version without broadening allowed URLs. Post-fix checks produced the expected results for two valid and eighteen invalid inputs. Guidance and original-answer hashes remained unchanged, so the six responses did not require regeneration.

随后定向复核确认初审三处行为修正，同时发现 `IR7-FU-03`：默认 JSON 解码会丢弃重复键的前值，可能遗漏其中的网址。作者改为拒绝重复对象键；正常、允许网址、五种重复键形式及前三项问题共十个完整检查器场景均符合预期。保留一个继承的诊断限制：畸形 IPv6 网址可能以解析异常而非友好错误退出，但不会报告通过；本轮未扩展处理。

Targeted review then confirmed the three initial behavior fixes and found `IR7-FU-03`: default JSON decoding discards earlier values of duplicate keys, potentially hiding a URL. The author changed parsing to reject duplicate object keys. Ten complete-checker scenarios matched expectations: normal input, an allowed URL, five duplicate-key forms, and the three earlier issues. One inherited diagnostic limitation remains: a malformed IPv6 URL may exit with a parser exception instead of a friendly error, but does not report a pass; this round did not expand that handling.

复核者亦为本轮六例执行者；独立差异复核只覆盖文档、协议、证据保真与检查器，不构成对自身回答的独立盲评。修订后的定向独立复核已完成，所列检查器问题均已关闭。

The reviewer also executed this round's six cases. Independent diff review covers the documents, protocol, evidence fidelity, and checker; it is not independent blinded grading of the reviewer's own answers. Targeted independent review of the fixes is complete, and all listed checker issues are closed.

## 保留的未验证项 / Remaining unverified work

18 项表单/分步产品检查继续为 `NOT_RUN`。未检查真实 Figma 画布、节点操作与账户功能、平台 SDK 或设备、RTL/键盘/读屏运行、完整 WCAG 符合性、token 导出与运行消费者、服务提交/查询/防重复，亦未安装技能或验证宿主加载、隐式触发及跨客户端兼容。没有重新执行历史 16 例对照或认证完整版权链。本次本地修改不变更版本号、许可、发布状态或任何消费项目。

All 18 form/stepped-form product checks remain `NOT_RUN`. No actual Figma canvas, node operations or account capabilities, platform SDK/device behavior, RTL/keyboard/screen-reader execution, full WCAG conformance, token export/runtime consumers, service submission/query/deduplication, skill installation, host loading, implicit triggering, or cross-client compatibility was tested. The historical 16-case comparison was not rerun, and the complete rights chain was not certified. These local changes do not change the version number, licenses, release status, or any consumer project.
