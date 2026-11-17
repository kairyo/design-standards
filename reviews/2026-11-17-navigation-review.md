# PR #17：导航、材质与原型修订验证记录

> 2026-11-17 归属说明：本记录按原日期、版本和范围保留；后续如何区分规范问题、执行偏差与实际项目验收，见[复核范围索引](2026-11-17-review-scope.md)。本次只增加入口，不改写以下历史结论或执行状态，也不表示重新运行。
>
> Scope note, 2026-11-17: this record retains its original date, version, and scope. See the [review-scope index](2026-11-17-review-scope.md) for the distinction between standards issues, execution deviations, and consumer-project acceptance. This entry neither rewrites the historical conclusions/results below nor reports a rerun.

日期：2026-11-17。关联 [Issue #16](https://github.com/kairyo/design-standards/issues/16) 和 [PR #17](https://github.com/kairyo/design-standards/pull/17)。本记录是原创文档检查证据，不是产品或平台符合性证明。

## 版本与范围

初审固定提交为 `6ed3ec1b790348643d16f5e242017a354576b5f2`，相对主线 `816adfc55e3564052801b405528b6b1ec39ec9fb` 覆盖十二个文件的导航、材质与原型增补。初审发现一项 P2 问题和两项 P3 非阻塞建议。随后获准本地修订，作者完成定向文字对照与结构检查，再由另一执行者只读复核修订。

修订的七文件本地差异经独立复核，`git diff --binary --no-ext-diff` 的 SHA-256 为 `dae4c4b5d370186e033231aad49824d87b0535930c5dd7635b608e6baa9a2f6a`。该哈希识别当时未提交的修订差异，不是提交 SHA，也不包含随后新增的本记录及提交说明整理。核心三项条款的已审文件 SHA-256 如下，用于区分条款复核与后续记录整理：

| 文件 | 已审文件 SHA-256 |
| --- | --- |
| docs/05-apple.md | 8c80bcfe99e82b6bac4fa5de6afa2ac2fcfcab660f4871e2e1e092886949ebf0 |
| examples/adaptive-navigation-materials.md | 2c6eab171254c518728ea821a741055291f53e9cf08a81ba05e10669dbc3bb75 |
| references/sources.md | cd1489e3bf33f2bc4b009bbd741fcc2b7176c07ad490aeb1210a7c0fa29b662c |

本记录所在提交保留原固定提交为父版本，并一起提交修订与公开验证记录。最终远端 SHA 和状态以 PR 的提交及说明为准；固定采用版本不因本 PR 更新而改变。

## 发现与处理

| 编号与严重程度 | 固定提交中的位置及原因 | 修订与独立复核结论 |
| --- | --- | --- |
| R1 / P2 | 05 章第 35 行把标题和符号建议套用到全部工具栏项，遗漏纯文本项例外。 | 限定为非纯文本项，纯文本项不被强制增加符号；保留菜单文字和辅助语义。N02、反例与 S02 核对记录同步。独立复核确认解决。 |
| R2 / P3 | 案例第 62 行 N06 未限定“同一动作”的语义操作范围，复合控件可能被误判。 | 同一操作内部热区一致；列表行与独立收藏子按钮分别执行各自契约。旧连接截获仍需检查，合法变体保留。独立复核确认解决。 |
| R3 / P3 | 案例第 65 行 N09 只强调标注未模拟的后台结果，模拟过的结果仍可能被误读。 | 每条路径标注原型证据和后台状态；模拟成功、失败、未知均不证明后台行为，缺失适用分支不汇总通过。独立复核确认解决。 |
| 状态澄清 / P3 | 修订复核发现 CHANGELOG 的历史待审文字易与当前状态混淆。 | 新条目注明旧待审段是当时快照，保留旧文；中英说明定向复核确认一致。 |

S02 的标题/符号限定在 2026-11-17 对照 Apple 官方 Markdown 的 Vertical controls 段核实；采用范围及链接见 [来源登记 S02](../references/sources.md#s02)。没有新增来源或扩展 SDK 承诺，S24 与其他来源没有因本次三项修订重新认证。

## 作者旧新版文字对照

下面十项是阅读条款、反例和相邻约束后的文档判断，没有操作设计文件或运行应用。每项均符合预期；这不把合成执行项 N01–N12 改成通过。

| 编号 | 场景 | 旧版判断或歧义 | 修订后的判断 |
| --- | --- | --- | --- |
| T01 | 非纯文本工具栏项已有标题和符号 | 原要求适用。 | 两者要求保留，不因补例外而允许只存符号不存标题。 |
| T02 | 批准方案中的纯文本工具栏项 | 可能被要求额外加图标。 | 明确不强制增加符号，N02 与反例一致。 |
| T03 | 图标可见，但菜单文字或辅助语义被删 | 原条款不允许删除相关语义。 | 保护继续保留，隐藏视觉文字不构成例外。 |
| T04 | 单个操作的图标、文字、可点留白 | N06 要求一致触发。 | 同一语义操作内部继续一致。 |
| T05 | 列表行打开详情，行内收藏按钮切换收藏 | 单独使用 N06 时可能被要求统一动作。 | 作为独立操作分别划热区和核对动作。 |
| T06 | 图标残留旧跳转，另一个子控件合法切换变体 | 正文要求检查旧触发并保护合法变体。 | 两类分别处理，不以独立子控件为由保留错误连接，也不一律删除变体。 |
| T07 | 原型演示成功，无真实后台证据 | 正文已有限制，但旧 N09 单独使用时不够明确。 | N09 明确模拟成功不能证明后台已成功。 |
| T08 | 失败和结果未知均由 fixture 演示 | 旧 N09 特别标注未模拟结果。 | 已模拟的失败和未知同样保持后台未验证，恢复前提依契约。 |
| T09 | 成功已演示，必需的取消或恢复分支未做 | 模板禁止父项越过必需未满足子项。 | N09 与模板一致，缺失或未演示的适用分支不汇总为通过。 |
| T10 | 子控件图形像收藏，实际契约未确认 | 03 章要求先确认对象与动作。 | 继续列缺口，不能凭图层名猜动作或判定命中一致。 |

相邻约束对照了 [03 章](../docs/03-figma-handoff.md)、[08 章](../docs/08-implementation-acceptance.md)与[验收模板](../templates/verification-record.md)。没有改变模板的必需子项汇总规则。

## 独立复核与检查分层

- 独立执行者复核旧/新条款、正常及异常反例、证据边界和双语状态；确认 R1、R2、R3 解决。新增的历史状态澄清也经限定复核确认解决。该结果与作者自检分开，不代表用户签收或合并批准。
- 本地修订阶段结构检查通过：54 个预期文件、44 份 Markdown、319 个内部链接、24 条来源；差异格式检查通过。这是该阶段快照，本记录加入后的结构数量另列于当前审阅记录。
- 提交整理仅增加公开验证记录、预期文件清单和对应入口/状态说明。三项核心规则及案例不再改变；公开记录不包含本机路径、私有设计地址、节点、媒体、资产或真实产品参数。
- 当前阶段和提交整理检查见 [审阅记录](../REVIEW.md)。所有检查都保留版本和范围，历史成绩不转作本轮产品成绩。

## 未验证项与授权

N01–N12 全部保留 `NOT_RUN`。没有 Figma、原型点击、辅助技术、模拟器、真机、SDK 行为或后台实测；暂缓的读屏项未启动。历史产品和文字案例未重跑，没有实际审美、效率或产品效果提升结论。没有用本地结构检查代替 GitHub CI。

维护者随后授权提交、推送至原功能分支并更新中英双语 PR 说明；未授权合并、自动合并、正式发布或消费项目采用。公开验证记录只提供已做检查、结果和未验证边界，不改变主线或固定采用版本。

## English summary

Independent review of fixed commit `6ed3ec1b790348643d16f5e242017a354576b5f2` found one P2 issue and two non-blocking P3 suggestions. The corrections preserve the text-only toolbar-item exception, scope hit-region consistency to one semantic operation while retaining independent child actions, and explicitly separate all simulated outcomes from actual backend evidence. A separate reviewer confirmed all three resolved, followed by a targeted check of historical-status wording.

The ten comparisons above are author document judgments, not executed interaction tests. The reviewed local patch hash identifies the seven-file correction snapshot, not a commit and not this later publication package. The 54-file / 44-Markdown / 319-link / 24-source structural result belongs to that local stage; the current review record distinguishes the later packaging checks.

All N01–N12 remain NOT_RUN. No Figma, prototype, assistive-technology, simulator, physical-device, SDK, or backend checks were performed; deferred screen-reader checks remain deferred and historical cases were not rerun. The maintainer authorized committing, pushing to the original feature branch, and updating bilingual PR information, but not merging, auto-merge, formal release, or consumer adoption. Historical conclusions and pinned adoption remain unchanged.
