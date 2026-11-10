# 变更记录

## 未发布 — 自适应保真与回归验收 / Unreleased adaptive fidelity and regression verification

2026-11-09，新增通用方法与原创合成案例；版本号、许可和 `REVIEW_CANDIDATE` 状态不变。

- 03 章补充原稿差异与已批准修正的保护、父容器/图片/文字几何读回和字体引用保护；沿用既有二维画布整理方法。
- 04 章区分图片用途、素材/容器/显示比例与裁剪，补充横向内容的发现和到达；05 章细化功能保留、内容分栏和控件/安全区域的分别核验。
- 08 章与现有验收模板补充适配矩阵、相邻影响联合复验及问题来源证据；新增不含项目资料或具体尺寸的合成案例，八项产品检查仍为 `NOT_RUN`。
- 同步双语入口、审阅状态与检查器文件清单；未增加外部来源或官方要求，未修改技能、消费项目采用记录或现有设计。作者检查与独立审阅分别记录于 REVIEW，未执行产品或真机验证。

On 2026-11-09, add general methods and an original synthetic example. Version, licenses, and `REVIEW_CANDIDATE` status remain unchanged.

- Extend chapter 03 with source-delta and approved-fix preservation, parent/image/text geometry readback, and font-reference protection; retain the existing two-dimensional canvas organization method.
- Distinguish image roles, source/container/display proportions, and cropping in chapter 04, including discovery of and access to horizontal content. Clarify feature preservation, content-based columns, and separate control/safe-area checks in chapter 05.
- Extend chapter 08 and the existing verification template with an adaptation matrix, joint checks of adjacent effects, and evidence for issue origin. Add a synthetic example without project material or concrete dimensions; all eight product checks remain `NOT_RUN`.
- Align bilingual entry points, review status, and the checker inventory. Add no external sources or official requirements, and change no skills, consumer adoption records, or existing designs. Record author checks and independent review separately in REVIEW; no product or physical-device validation was performed.

2026-11-10，整合主线表单纠错增补，保留双方内容；按独立初审补清问题归因所需的修复前后目标证据，以及 A08 的加载与失败恢复动作。验证与复核范围见 REVIEW，八项产品检查仍为 `NOT_RUN`。

On 2026-11-10, integrate the main-branch form-correction additions while preserving both sets of guidance. Following independent initial review, clarify the before/after target evidence needed for attribution and A08's loading and failure-recovery actions. See REVIEW for validation and review scope; all eight product checks remain `NOT_RUN`.

## 未发布 — 表单纠错与验收判据 / Unreleased form correction and acceptance criteria

2026-11-06，补充三条团队检查建议；版本、来源与发布状态不变。

- 第 07 章区分仅回看字段、实际编辑与重新提交；已确认的错误不因焦点切换而自行消失。
- 第 08 章增加纠正后第一次提交的连续操作检查，分别记录指针、键盘、请求与业务结果，不限定固定高度等实现。
- 验收模板要求拆分组合检查的子项并保留未完成条件；暂缓安排与验收结论分开，历史记录不改写为通过。这些文字增补不新增产品或读屏测试通过结论。
- 增加[双语验证记录](reviews/2026-11-06-form-validation.md)并同步两个 README 入口与检查器清单；分开历史合成演示、当前文字复核和按需恢复的读屏暂缓安排。

On 2026-11-06, add three team-level checking recommendations; version, sources, and release status remain unchanged.

- Chapter 07 distinguishes revisiting a field, editing it, and resubmitting; confirmed errors do not disappear solely because focus changes.
- Chapter 08 adds a continuous-action check of the first submission after correction, recording pointer and keyboard paths, requests, and business results separately without prescribing fixed-height layouts or another implementation.
- The verification template separates composite checks into subchecks and retains outstanding conditions. Deferral is distinct from acceptance, and historical records are not rewritten as passes. These text additions establish no new product or screen-reader test passes.
- Add a bilingual verification record and align both README entry points and the checker inventory; distinguish the historical synthetic demo, current document review, and deferred screen-reader checks that resume only when requested.

## 未发布 — 全库复核后续 / Unreleased repository-review follow-ups

2026-11-05 入库整理：以已合并 PR #12 的 main 为基线，保留下面的原轮结果；题面与判据作为可选维护材料，原答和历史评分不作为当前组合的新验证。补记配置证据边界，未重跑历史案例。

Publication preparation on 2026-11-05 uses main after PR #12, preserving the original results below. Prompts and criteria are optional maintenance material; original responses and historical scores are not new validation of the combined candidate. Clarify configuration-evidence limits without rerunning historical cases.

- 保存对 `4102b2bf8ce2bd29a69c0cde5436aa8fba64f322` 的首轮全库独立内容复核及21条来源的实际核对范围；保留真实产品、技能加载与效果验证缺口。
- 限定历史报告的时点及技能 WCAG 来源说明的主语；第03章增加普通卡片、有意溢出与漂浮说明的合成短例，保留原保护边界。
- 增加题面、判据与运行记录分开的最小文字案例包及双语使用说明；同步入口和结构检查。版本号、许可和正式发布状态不变。

- Preserve the first repository-wide independent content review of `4102b2bf8ce2bd29a69c0cde5436aa8fba64f322` and actual checking scope for 21 sources; retain gaps in real-product, skill-loading, and effectiveness evidence.
- Date historical report statements and clarify the subject of the skill's WCAG source scope. Add a short synthetic chapter-03 example distinguishing ordinary cards, intentional overflow, and floating annotations while preserving protection boundaries.
- Add a minimal text-case suite with separate prompts, criteria, and run records plus bilingual instructions; align entry points and structural checks. Version, licenses, and formal-release state are unchanged.

## 未发布 — Figma 变量示例与落地页附页 / Unreleased Figma variable example and landing-page appendix

2026-11-05，新增两项设计文档补充，版本、许可与发布状态不变。

- 新增最小 Figma 变量/样式关联、基础样本、Light/Dark 往返、单变量传播与恢复示例；七项实操仍为 NOT_RUN，不替代代码主题或原有十八项产品验收。
- 新增落地页 brief 可选附页及合成填写示例，补充来访入口、主要动作、顾虑、主张证据和收敛条件；不覆盖批准设计或冒充转化效果验证。
- 连接 02、03、04、08 章与现有模板，同步双语入口、第三方归属和验证记录；新增固定版本方法参考 S22 与官方能力来源 S23。检查器仅扩展文件/来源清单及三个精确 GitHub 地址，没有安装或执行外部技能。

On 2026-11-05, add two design documentation supplements. Version, licenses, and release status are unchanged.

- Add a minimal example covering Figma variable/style associations, bound samples, Light/Dark round trips, propagation of a single-variable change, and restoration. Seven execution checks remain NOT_RUN; they do not replace code-theme checks or the existing eighteen product checks.
- Add an optional landing-page brief appendix and synthetic filled example covering visitor entry, the primary action, objections, claim evidence, and convergence. It neither overrides approved designs nor establishes conversion effectiveness.
- Connect chapters 02, 03, 04, and 08 with existing templates; align bilingual entry points, third-party attribution, and the verification record. Add pinned method reference S22 and official capability source S23. Extend only checker inventories and three exact GitHub URLs, without installing or executing external skills.

## 未发布 — 许可与贡献条件 / Unreleased licensing and contribution terms

2026-11-04，按维护者决定为包含本变更的版本明确许可范围；版本号及审阅候选状态保持不变。

- 原创文档、模板、示例和技能文本采用 CC BY 4.0；现有检查脚本采用 MIT。随附标准许可全文，并明确第三方例外、署名和修改说明。
- 两个技能包各自携带 CC BY 4.0 许可原文和署名，界面描述元数据一并明确归属；技能行为与描述保持不变。
- 同步双语 README、许可说明、贡献指南、第三方声明、项目说明与 PR 模板。贡献者保留版权，按对应许可提供有权提交的内容；历史许可待定记录保留。
- 检查器增加许可文件清单、已核对文本的完整性检查及两个精确许可/署名 URL；设计来源登记与原有检查边界保留。

On 2026-11-04, the maintainer's decision defines license scope for versions carrying this change. The version number and review-candidate status remain unchanged.

- Original documentation, templates, examples, and skill text use CC BY 4.0; the existing checker uses MIT. Include the standard full texts and define third-party exceptions, attribution, and modification notices.
- Each skill package carries the CC BY 4.0 text and attribution, with interface-description metadata explicitly covered; skill behavior and descriptions are unchanged.
- Align both READMEs, the bilingual license notice, contribution guide, third-party notices, project guidance, and PR template. Contributors retain copyright and submit authorized material under the applicable license; historical pending-license records are preserved.
- Extend the checker with the license-file inventory, integrity checks for reviewed texts, and two exact licensing/attribution URLs. Preserve the design-source registry and existing checking boundaries.

## 未发布 — 表单提交与纠错（功能分支审阅）

基于 `0.1.0-draft.3` 增补 02、04、07、08 章，版本号与正式发布状态不变。

- 02 章补充模式选择与代价；04 章补充 token 追踪及组件状态行为；07 章补充表单纠错操作检查；08 章补充问题影响、优先级、复验及自动结果的人工判断。
- 新增一个完整原创表单示例，串联 brief、模式取舍、状态转换、组件映射、无障碍动作和 12 项待执行验收；明确字段拒绝、可重试失败、不可重试整单拒绝、结果未知与成功的区别。
- 按案例验证发现的缺口补充 02、04、07 章及分步往返示例的 6 项待执行验收，区分草稿、有效字段、步骤完成与确认内容，并具体写出焦点保持/转移条件。验收模板与完整示例明确纠错重提后的实际业务结果核对；并发编辑恢复仍留待后续。
- 扩展现有设计 brief 与验收模板，保留原有示例及证据边界，不新增一套平行模板。
- 新增来源 S18–S21，补记 S12 的定向阅读范围和第三方归属；检查器增加两个表单示例、来源编号及两个固定 GitHub 文件入口，没有开放任意 GitHub 路径。案例修订是原创团队建议与合成项目选择，未增加外部来源或改变官方要求。
- 本地文档增补不包含产品实现、技能安装或消费项目升级；表单运行、读屏、服务查询和防重复效果均未验证。检查与独立文档复核记录见 REVIEW。
- 汇总两轮文字案例验证：保留首轮 12 例的历史结果；复测对原始旧版、修复前、修复后三个快照执行同一组 16 例，分别为 12、13、16 项完整通过，其余为部分通过，无失败项。REVIEW 记录逐案结果、题面调整、判读波动及原始材料未随库公开的边界；18 项产品检查仍未执行。

## 0.1.0-draft.3 — 2026-11-02

补充 Figma 画布边界与空间组织；仍为审阅候选，本轮独立复核与正式发布分开记录。

- 03 章区分官方近似坐标范围与团队排布建议，不把能力描述当作规范性要求、精确裁切线或推荐铺满目标。
- 补充 Page/Section 分组、完整外框与可见渲染外延、下一完整组预留、母组件来源和按用途增页的方法。
- 明确整理授权与节点/依赖保护、跨页核验、真实总览与局部证据，并区分自动化载荷限制和画布容量。
- 新增来源 S17，分别保留新旧来源的实际读取日期；同步来源编号检查上限和候选版本/审阅记录。
- 未修改许可证、安装技能、改动现有设计文件或消费项目；不据此宣称画布操作、依赖保留或方法效果已实测。

## 0.1.0-draft.2 — 2026-10-26

在同一审阅候选中补充设计技能，尚未完成独立复核或正式发布。

- 新增 `skills/` 目录：原创 `design-direction-review` 与 `adaptive-ui-review`，包含界面元数据及按需平台来源路由。
- 登记已有 Web、Figma、Apple、设备验证和字体工具的复用边界；不镜像第三方插件、SDK 文件或私人研究资料。
- 增加九个合成边界案例，明确作者推演不等于自动触发测试、独立评估或产品运行验收。
- 补充 OpenAI 技能格式与发现路径来源，扩展结构检查到技能内引用和元数据的定向公开性扫描。
- 原有十章设计方法和项目采用边界保持不变；未安装技能、调整本机配置或建立自动更新。

## 0.1.0-draft.1 — 2026-10-26

首次公开审阅候选，尚未正式发布或批准采用。

- 原创整理十个主题：设计原则、探索、Figma 交接、设计系统、Apple、Android、包容性设计、实现验收、来源管理、采用维护。
- 增加三个记录模板、六个匿名合成案例、公开来源登记与轻量文档检查器。
- 分开官方规范性要求、团队建议、项目选择与未验证项；为平台建议、单位差异、证据范围和许可设置明确边界。
- 未携带第三方资产或文档镜像；不改变现有项目，不设置自动更新。

独立复核和维护者的正式发布决定均待完成。后续修订须记录影响章节、来源差异及兼容性，不把审阅稿悄悄改称稳定版本。

## 未发布的仓库维护 / Unreleased repository maintenance

### 2026-11-03 — GitHub 项目管理与双语协作 / GitHub project management and bilingual collaboration

- 增加等价英文 README、双语贡献与 Agent 维护入口、项目管理约定及 Issue/PR 模板；十章正文与设计资料保持中文。
- 明确任务、PR、里程碑、状态标签、独立复核和授权的关系；保留历史结论、证据限制与许可待定状态。
- 检查器逐项登记新增文件，并仅允许本仓库任务/PR/里程碑链接；继续拒绝未登记的其他 GitHub 路径、带查询参数或身份信息的 URL。
- 验证范围与并行 PR 的双语合并注意事项见 [协作整理验证记录](reviews/2026-11-03-github-management.md)。不更改版本，不安装、不发布、不自动合并。
- 补齐两个表单示例的英文 README 入口与未执行产品检查说明；管理 PR 改为基于表单 PR 的后续审阅，组合内容在功能分支核对，main 保持不变。

- Add an equivalent English README, bilingual contribution and agent entry points, project conventions, and issue/PR templates; retain Chinese design chapters and materials.
- Define the relationship between tasks, PRs, milestones, status labels, independent review, and authorization; preserve historical conclusions, evidence limitations, and pending licensing.
- Register each new file in the checker and allow only this repository's issue/PR/milestone links; continue rejecting other unregistered GitHub paths and URLs with query parameters or identity information.
- See the [collaboration verification record](reviews/2026-11-03-github-management.md) for validation scope and bilingual integration considerations for concurrent PRs. No version change, installation, release, or automatic merge.
- Complete the English README entries for both form examples and their unexecuted-product-check boundary. Review the management PR on top of the form PR, verifying the combined content on a feature branch while leaving main unchanged.
