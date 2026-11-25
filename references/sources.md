# 公开来源登记

实际读取日期按条目保留：**S01–S16 首次读取为 2026-10-26，S17 为 2026-11-02，S18–S21 为 2026-11-03，S22–S23 为 2026-11-05**；S12 的 2026-11-03 补读范围另列。新增来源不表示旧来源已全部重新核对。以下均为 `READ_SCOPED`，只表示读取了列出的部分；不表示全文、嵌入视频、附件或子链接均已读，也不表示任何产品已采用或通过验证。

2026-11-17 定向补读 S02 的控件位置、标题/符号和背景延展说明，新增 S24 材质来源；未重新认证其余来源或平台 API。

2026-11-25 为电视端补读 S01、S03，新增 S27–S37。以下电视条目均为 `READ_SCOPED`，列出实际核对的页面与主题。Apple HIG 和 UIKit 读取官方 Markdown，App Store 提交条件读取官方网页。Android 条目括号内为原页所示的 UTC 更新日期。两者均只收录公开链接与原创归纳。Apple 资料遵循其页面条款，Android Developers 资料适用各页的 Content License。

未标不可变版本的网页为动态资料，核对日期不是永久快照。内容只作短摘要和链接，不保存第三方正文。独立复核按 [审阅记录](../REVIEW.md)的具体范围分别记录，读取或复核来源不表示项目已批准采用。权利边界见 [第三方资料声明](../THIRD-PARTY-NOTICES.md)。

2026-11-04 全库复核的实际读取范围及限制见 [独立内容复核记录](../reviews/2026-11-04-repository-review.md)。该记录不覆盖下列首次读取日期，也不把动态页面追溯认定为旧时点的固定快照。

## S01

- 发布者 / 标题：Apple — Layout。
- URL：https://developer.apple.com/design/human-interface-guidelines/layout
- 版本：页面 Change log 最新所示 2026-09-09；读取官方 Markdown 正文，重点为 Visual hierarchy、Adaptability、Size classes、Guides and safe areas。
- 2026-11-25 补读 Platform considerations 中的 tvOS，核对主要内容的屏边内距、额外焦点空间及屏幕边缘可能裁切的条件，供 05 章使用。
- 平台 / 采用范围：Apple 的布局判断；01、05 章只选择层级、可用空间、安全区和适配建议，不采用其他平台的固定尺寸表。
- 分类 / 状态：`TEAM_RECOMMENDATION`，官方设计建议的有限归纳；`READ_SCOPED`，采用待复核。
- 许可：页面 Apple 版权与 Terms of Use；无再分发内容。

## S02

- 发布者 / 标题：Apple — Designing for iPhone Duo。
- URL：https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo
- 版本：页面 Change log 2026-09-09；读取官方 Markdown 的设备结构、Dynamic layouts、Reserved regions、Vertical controls。
- 补读：2026-11-17 读取当前官方 Markdown 的 Vertical controls，重点为导航顺序、内容区局部操作、标题/符号及背景延展；页面所示 Change log 仍为 2026-09-09。未执行链接中的 API、视频或设备预览。
- 修订核对：同日按复核意见再次核对标题/符号段的适用限定；同时提供标题和符号的建议针对非纯文本工具栏项，纯文本项不由此被强制增加符号。未扩大来源读取或平台验收范围。
- 平台 / 采用范围：iPhone Duo；05 章的内外屏、系统栏及保留区说明。不是所有系统版本的 API 可用性证明。
- 分类 / 状态：`TEAM_RECOMMENDATION`，以官方设计指导解释适用场景；`READ_SCOPED`，未做项目运行验收。
- 许可：页面 Apple 版权与 Terms of Use；未复制图片、UI Kit 或 SDK 文件。

## S03

- 发布者 / 标题：Apple — Accessibility。
- URL：https://developer.apple.com/design/human-interface-guidelines/accessibility
- 版本：动态页面，未据此确认固定发行号；读取 Introduction、Vision、Hearing、Mobility、Speech 的相关段落。
- 2026-11-25 补读 Vision 中各平台系统字号及自定义字体建议、Hearing 的字幕与音频描述，以及辅助技术和减少动态的相关说明。05、07 章只将 tvOS 的 pt 值用于对应平台与文字类型。
- 平台 / 采用范围：Apple；07 章对放大、提示、读屏、控制与输入的检查建议，不导入全平台统一字号或命中数值。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`，不是符合性证明。
- 许可：页面 Apple 版权与 Terms of Use；只链接和归纳。

## S04

- 发布者 / 标题：Figma — Explore component properties。
- URL：https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties
- 版本：动态帮助页，未显示可靠固定版本；读取概念、属性种类及其使用边界。
- 平台 / 采用范围：Figma Design；03 章的可定制面与组件关系，不声称已实际检查任何文件。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`。
- 许可：Figma 资料，未核定全文再分发许可；不复制正文或 Community 资源。

## S05

- 发布者 / 标题：Figma — Guide to variables in Figma。
- URL：https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma
- 版本：动态帮助页；读取 Variables for designs and design systems、模式用途及访问前提，未观看嵌入视频。
- 平台 / 采用范围：Figma Design；03 章的变量、模式及绑定记录。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`。
- 许可：Figma 资料，全文再分发许可未核定；仅链接。

## S06

- 发布者 / 标题：Figma — The difference between variables and styles。
- URL：https://help.figma.com/hc/en-us/articles/15871097384471-The-difference-between-variables-and-styles
- 版本：动态帮助页；读取 Foundational differences、Scalability and management、Final thoughts。
- 平台 / 采用范围：Figma Design；03 章仅引用变量与组合样式的概念区别。页面个别功能路线描述不作为当前可用性承诺。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`。
- 许可：Figma 资料，全文再分发许可未核定；未复制示例和图像。

## S07

- 发布者 / 标题：Figma — Compare changes in Dev Mode。
- URL：https://help.figma.com/hc/en-us/articles/15023193382935-Compare-changes-in-Dev-Mode
- 版本：动态帮助页；读取访问条件、Compare changes、Version history、Compare properties。
- 平台 / 采用范围：Figma Dev Mode；03 章可选的版本差异辅助，不代替批准或运行验收。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`，没有验证具体账户功能。
- 许可：Figma 资料，全文再分发许可未核定；只链接和归纳。

2026-11-04 补核：原页面当前读回支持套餐前提及差异查看用途；席位与文件权限另参照 [Guide to inspecting](https://help.figma.com/hc/en-us/articles/22012921621015-Guide-to-inspecting) 的访问条件段落，说明检查方式取决于套餐、席位及文件权限，付费套餐的 Dev Mode 需 Full 或 Dev 席位。此补核不代表用户账户功能已验证，也不反推历史页面当时的完整内容。

## S08

- 发布者 / 标题：Google Android Developers — Use window size classes。
- URL：https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes
- 版本：页面 Last updated 2026-10-23 UTC；读取窗口分类、动态变化、Manage layouts 和 Test window size classes。
- 平台 / 采用范围：Android；06 章基于当前窗口决策，不抄写断点表或假定所有库版本一致。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`，未验证项目依赖/API。
- 许可：页面 Content License，未携带代码样例。

## S09

- 发布者 / 标题：Google Android Developers — Get started with adaptive apps。
- URL：https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps
- 版本：动态页面；读取 Content panes、Compose Material 3 Adaptive、Configuration and continuity、Posture、Input beyond touch 及测试方式。
- 平台 / 采用范围：Android；06 章的 pane、导航、姿态和连续性建议；不执行页面里的技能安装命令。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`，不作为技术栈强制迁移。
- 许可：页面 Content License；未复制代码或资产。

## S10

- 发布者 / 标题：Google Android Developers — Adapt layouts。
- URL：https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout
- 版本：页面 Last updated 2026-10-22 UTC；读取适配方法、pane 与内容宽度指导。
- 平台 / 采用范围：Android；06 章的重排、信息展示与避免无意义拉伸。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`。
- 许可：页面 Content License；仅链接与原创短摘要。

## S11

- 发布者 / 标题：Google Android Developers — Principles for improving app accessibility。
- URL：https://developer.android.com/guide/topics/ui/accessibility/principles
- 版本：动态页面；读取指导概览、Label elements、辅助动作/标准能力/非颜色提示的说明。
- 平台 / 采用范围：Android；07 章的语义与输入检查。不将某段 Compose 实现推定为所有框架均自动支持。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`。
- 许可：页面 Content License；未复制实现代码。

## S12

- 发布者 / 标题：W3C — Web Content Accessibility Guidelines (WCAG) 2.2。
- URL：https://www.w3.org/TR/2024/REC-WCAG22-20241212/
- 版本：固定 W3C Recommendation，2024-12-12；读取版本身份及第 5 节符合性模型，重点 5.1–5.3。
- 补读：2026-11-03 读取同一固定版本的 2.4.3、3.3.1–3.3.3、4.1.2–4.1.3 正文；用于表单焦点、输入帮助、名称/角色/值和状态消息的适用条款定位。未扩展成整份逐条审计。
- 平台 / 采用范围：Web；07 章中声明 WCAG 2.2 符合性时的边界，以及表单操作检查的条款依据。本仓库不是完整 checklist；错误摘要、具体焦点落点和合成例文案是团队/项目选择，不冒充 WCAG 唯一实现。
- 分类 / 状态：`OFFICIAL_REQUIREMENT` 仅限符合性声明的适用条件；`READ_SCOPED`，不声明任何项目达标。
- 许可：W3C 文档版权与使用规则；无正文镜像。

## S13

- 发布者 / 标题：Design Tokens Community Group — Design Tokens Format Module 2025.10。
- URL：https://www.designtokens.org/tr/2025.10/format/
- 版本：固定 2025.10，2025-10-28 Final Community Group Report；读取 Status、Introduction、Types/Dimension 的相关内容。
- 平台 / 采用范围：跨工具 token 交换；04 章仅说明格式用途、状态与数值表达，未实现或认证导出器。
- 分类 / 状态：`TEAM_RECOMMENDATION`（评估选项）；`READ_SCOPED`。若项目要宣称兼容，规范性条款需另行逐项验证。
- 许可：来源标注 W3C Community Final Specification Agreement；不是 W3C Recommendation，不复制规范。

## S14

- 发布者 / 标题：Material Components — Material Components for Android README。
- URL：https://github.com/material-components/material-components-android
- 版本：动态默认分支，2026-10-26 读取；不是固定 SHA，不作代码依赖。读取维护模式声明和相关方向说明。
- 平台 / 采用范围：Android Views 生态；06 章仅报告读取时的维护状态，不自动迁移现有项目。
- 分类 / 状态：`TEAM_RECOMMENDATION` 中的官方仓库状态依据；`READ_SCOPED`，后续选型需重新核对。
- 许可：仓库标示 Apache-2.0；本仓库未复制代码，其许可证不传递成本仓库统一许可。

## S15

- 发布者 / 标题：W3C — Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT)。
- URL：https://www.w3.org/TR/2025/NOTE-wcag2ict-22-20251211/
- 版本：固定 Group Note，2025-12-11；读取版本身份、Abstract、Status of This Document。
- 平台 / 采用范围：非 Web 文档和软件；07 章仅说明其非规范性指导身份，不宣称原生符合性认证。
- 分类 / 状态：`TEAM_RECOMMENDATION`（可参考来源）；`READ_SCOPED`，未读完逐条适配。
- 许可：W3C 文档版权与使用规则；不转载正文。

## S16

- 发布者 / 标题：OpenAI — Build skills。
- URL：https://learn.chatgpt.com/docs/build-skills
- 版本：动态官方页面，2026-10-26 读取；范围为技能目录结构、显式/隐式调用、Codex 本地发现路径及可选界面元数据。
- 平台 / 采用范围：技能目录的格式与接入边界；普通仓库 `skills/` 与发现目录分开，不宣称其他客户端已验证兼容，不执行安装或配置操作。
- 分类 / 状态：`TEAM_RECOMMENDATION` 中的官方格式依据；`READ_SCOPED`，未进行实际客户端加载或触发评估。
- 许可：OpenAI 资料；只链接和原创短说明，不转载系统技能、脚本或插件文件。

## S17

- 发布者 / 标题：Figma — Create and manage pages。
- URL：https://help.figma.com/hc/en-us/articles/360038511293-Create-and-manage-pages
- 版本 / 读取日期：动态帮助页，未显示可靠固定版本；2026-11-02 读取正文中的画布范围与 Page 组织说明、Create pages 的访问边界、Move layers between pages。未扩展到页面链接的其他文档。
- 平台 / 采用范围：Figma Design；03 章的每 Page 每轴约 `-130000` 至 `+130000`、跨页移动保持坐标与评论的能力说明。近似范围不作精确裁切线、性能承诺或布局目标；没有测试账户功能、极限坐标或原型依赖。
- 分类 / 状态：用于 `TEAM_RECOMMENDATION` 的官方产品能力依据，不属于 `OFFICIAL_REQUIREMENT`；`READ_SCOPED`。分组、内容包络、换行与增页判断是本仓库原创建议，不冒称官方布局规范。
- 许可：Figma 资料，全文再分发许可未核定；仅公开链接与原创短摘要，不复制正文、截图或设计资产。

## S18

- 发布者 / 标题：Ant Design — 表单页。
- URL：https://github.com/ant-design/ant-design/blob/46f0421cb8db963e35a41b822ceb9232d5c8ef57/docs/spec/research-form.zh-CN.md
- 版本 / 读取日期：固定提交 `46f0421cb8db963e35a41b822ceb9232d5c8ef57`；2026-11-03 读取设计目标、设计原则、普通布局、基础分步表单和分组表单相关文字。未读取外链图片内容，不视为视觉案例已核验。
- 平台 / 采用范围：Web 设计模式参考；02 章与完整表单例借鉴按任务关系比较组织方式、理解输入及反馈的方法。具体候选表、恢复状态及验证计划为原创归纳；不采用固定字段数量、企业后台视觉、组件尺寸或 React 技术栈。
- 分类 / 状态：`TEAM_RECOMMENDATION` 的外部参考；`READ_SCOPED`，不是平台官方要求或效果验证。
- 许可：同一提交根 LICENSE 为 MIT；仅链接与原创有限归纳，不复制代码、图片或模板，不由根许可推定外链素材可再分发。

## S19

- 发布者 / 标题：Style Dictionary — Design Tokens。
- URL：https://styledictionary.com/info/tokens/
- 版本 / 读取日期：动态官方文档，2026-11-03 读取 Overview、Default design token metadata、Referencing / Aliasing、Collision warnings。页面区分原有格式与 DTCG 表达；未据此确认当前项目导出器版本或兼容性。
- 平台 / 采用范围：04 章和完整表单例的 token 来源、引用、覆盖与消费者追踪。采用记录思路，不采用工具的默认合并顺序作为通用规则，不复制 schema、数值或代码，不要求安装工具。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`，没有运行导出器或验证主题加载。
- 许可：本网页全文再分发许可未核定；仅公开链接与原创短说明，不保存正文镜像或示例代码。

## S20

- 发布者 / 标题：Adobe / React Aria — Quality。
- URL：https://react-aria.adobe.com/quality
- 版本 / 读取日期：动态官方文档，2026-11-03 读取 Accessibility、Labeling、Supported screen readers、Automated testing、Internationalization 概述及 Interactions。列出的兼容测试是发布者陈述，不是本仓库执行证据。
- 平台 / 采用范围：Web；07 章采用语义、输入、焦点与通知应和视觉设计一起检查的思路，不假定安装组件库就完成无障碍工作，不把网页属性或其支持矩阵直接推广到原生应用。
- 分类 / 状态：`TEAM_RECOMMENDATION`；`READ_SCOPED`，不声称任何消费项目已加载或通过验证。
- 许可：本网页全文再分发许可未核定；仅链接与原创短说明，不复制组件实现或代码样例。

## S21

- 发布者 / 标题：Deque / axe-core — README。
- URL：https://github.com/dequelabs/axe-core/blob/6b52b841461bd23345970b91ec75fdaff6bad31a/README.md
- 版本 / 读取日期：固定提交 `6b52b841461bd23345970b91ec75fdaff6bad31a`；2026-11-03 读取用途概述和 The Accessibility Rules 中关于 `incomplete` 需要人工判断的说明，未进行全规则审计。
- 平台 / 采用范围：Web/HTML；08 章、验收模板与完整表单例保留自动结果并另记人工复核。`NOT_RUN` / `BLOCKED` 映射是本仓库的记录约定；不采用平均检出率作为项目覆盖保证，不安装工具或将其用于原生验收。
- 分类 / 状态：`TEAM_RECOMMENDATION` 中的工具能力边界依据；`READ_SCOPED`，没有运行扫描。
- 许可：同一提交 LICENSE 标示 MPL-2.0；未复制源码、规则或原始报告，不将该许可传递成本仓库统一许可。

## S22

- 发布者 / 标题：Elaya — ai-design-skills 中的 figma-designer、landing-page-design。
- URL：[figma-designer](https://github.com/elayadesign/ai-design-skills/blob/456d9e0d3e2d84c748bb143c6ca3d90c45e16213/skills/figma-designer/SKILL.md)、[landing-page-design](https://github.com/elayadesign/ai-design-skills/blob/456d9e0d3e2d84c748bb143c6ca3d90c45e16213/skills/landing-page-design/SKILL.md)、[根 LICENSE](https://github.com/elayadesign/ai-design-skills/blob/456d9e0d3e2d84c748bb143c6ca3d90c45e16213/LICENSE)。
- 版本 / 读取日期：固定提交 `456d9e0d3e2d84c748bb143c6ca3d90c45e16213`；2026-11-05 读取两个技能的完整文字及根 LICENSE。采用范围限于基础样本与实际变量关联，以及落地页的受众、来访入口、主要动作、顾虑和证据组织；未执行技能或外部脚本，未审图像素材。
- 平台 / 采用范围：03、04、08 章的合成 Figma 示例及 02 章的可选落地页 brief 附页。主题恢复、断绑对照和本库表格为原创归纳；不采用固定字体/字号、完整色板、组件变体数量、全局 Auto Layout、固定章节数或动效偏好，不宣称方法提高转化率。
- 分类 / 状态：`TEAM_RECOMMENDATION` 的第三方方法参考；具体数值和业务假设为合成 `PROJECT_CHOICE`。`READ_SCOPED`，不是 Figma 官方要求、安装记录或效果验证。
- 许可：根文件为 MIT，署名 Copyright (c) 2026 Elaya；landing-page-design 内另保留 Taste 的许可/署名说明。本库只链接并原创归纳，不复制技能正文、表格、模板、代码或资产；不把本库 CC BY 4.0 扩展到这些外部文件，也不由根许可推定外链素材权利。

## S23

- 发布者 / 标题：Figma — Modes for variables；Apply variables to designs。
- URL：[Modes for variables](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables)、[Apply variables to designs](https://help.figma.com/hc/en-us/articles/15343107263511-Apply-variables-to-designs)。
- 版本 / 读取日期：动态帮助页，2026-11-05 核对。前者读取模式概念及访问前提、默认模式、Switch between modes、Auto 继承与 Mode conflicts；后者读取编辑/库访问前提及颜色、数值变量应用，含填充/描边、尺寸、间距、内边距和圆角。未观看视频或逐项核对所有可绑定属性。
- 平台 / 采用范围：Figma Design；新示例中的变量关联、容器模式选择、Auto 父级/默认模式继承及模式版本冲突检查。实际权限、模式可用性、库版本及对象支持在消费项目另验；未验证任何账户、文件或界面操作，不据此声称 API、导入导出或 DTCG 兼容。
- 分类 / 状态：用于 `TEAM_RECOMMENDATION` 的官方产品能力依据；`READ_SCOPED`，不是 `OFFICIAL_REQUIREMENT` 或产品验收。
- 许可：Figma 资料，全文再分发许可未核定；仅链接和原创短摘要，不转载正文、截图或设计文件。

## S24

- 发布者 / 标题：Apple — Materials。
- URL：https://developer.apple.com/design/human-interface-guidelines/materials
- 版本 / 读取日期：动态官方资料，2026-11-17 读取官方 Markdown 的 Liquid Glass 及 Standard materials 开头，重点为材质分层、自定义效果、变体与系统设置；没有据此确认 SDK 版本或链接中的 API 行为。
- 平台 / 采用范围：05 章中导航/控件层与内容层材质的用途、谨慎使用自定义材质，以及不同背景、减少透明度和增强对比度设置下的检查。具体材质参数、控件尺寸、Figma 效果与原生实现的对应关系由项目另验。
- 分类 / 状态：`TEAM_RECOMMENDATION`，官方设计指导的有限归纳；`READ_SCOPED`，不是统一采用玻璃的要求或产品验收。
- 许可：页面 Apple 版权与 Terms of Use；仅公开链接和原创短摘要，未复制正文、图片、UI Kit 或 SDK 文件。

## S25

- 发布者 / 标题：pbakaus / Impeccable — typeset、polish。
- URL：[typeset](https://github.com/pbakaus/impeccable/blob/c3bb418ee38ee49a6b999b7752c1368f3123a2bd/.agents/skills/impeccable/reference/typeset.md)、[polish](https://github.com/pbakaus/impeccable/blob/c3bb418ee38ee49a6b999b7752c1368f3123a2bd/.agents/skills/impeccable/reference/polish.md)、[根 LICENSE](https://github.com/pbakaus/impeccable/blob/c3bb418ee38ee49a6b999b7752c1368f3123a2bd/LICENSE)。
- 版本 / 读取日期：固定提交 `c3bb418ee38ee49a6b999b7752c1368f3123a2bd`；2026-11-06 读取两个参考文件全文，并核对根 LICENSE 首部 Apache-2.0 标示。未运行外部工具、下载引擎或审计依赖。
- 平台 / 采用范围：设计方向审阅技能、02 章及视觉方向记录的排版角色、内容压力、局部润色与渲染证据方法。按实际语言与任务判断，不采用固定行长/字号、检测器、钩子、自动下载或委派流程，也不继承其权限与发布行为。
- 分类 / 状态：`TEAM_RECOMMENDATION` 的第三方参考；`READ_SCOPED`。原创合成例为 `PROJECT_CHOICE`，不是技能效果或原生平台验证。
- 许可：根 LICENSE 首部标示 Apache-2.0；仅链接与原创有限归纳，没有复制技能、源码、数值表或素材，不推定附属资产与依赖的许可。

## S26

- 发布者 / 标题：Damola Akinleye / Interface Design — SKILL.md。
- URL：[SKILL.md](https://github.com/Dammyjay93/interface-design/blob/2f9be3206855bcb2d1d0af262c8bae25cba6658d/.claude/skills/interface-design/SKILL.md)、[根 LICENSE](https://github.com/Dammyjay93/interface-design/blob/2f9be3206855bcb2d1d0af262c8bae25cba6658d/LICENSE)。
- 版本 / 读取日期：固定提交 `2f9be3206855bcb2d1d0af262c8bae25cba6658d`；2026-11-06 读取该技能全文与根 MIT LICENSE，未执行技能或审计其他命令。
- 平台 / 采用范围：产品界面的任务、视觉层级、信息密度与组间节奏；用于审阅技能及视觉记录的原创归纳。不将产品 UI 方法扩成营销页或原生平台统一要求；不采用固定字体比例、像素/间距公式、风格禁令、命中区 WCAG 概括、动效数值或其专属记录路径。
- 分类 / 状态：`TEAM_RECOMMENDATION` 的第三方参考；`READ_SCOPED`。没有安装、效果对照试验或平台背书。
- 许可：根 LICENSE 为 MIT，Copyright (c) 2026 Damola Akinleye。只链接并作原创有限归纳，未复制技能正文、表格、代码或资产；本库许可不覆盖外部文件。

## S27

- Apple HIG 的 [Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos) 与 [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)。读取平台特点、观看距离、共用屏幕、输入方式和 Top Shelf，以及 tvOS 图标的图层、焦点视差及 Xcode 堆栈说明。
- 05 章用于确定设计情境。观看距离和遥控器须结合目标设备记录，分类为 `TEAM_RECOMMENDATION`。
- HIG 的 Change log 最新所列日期分别为 Designing for tvOS 的 2022-09-14 和 App icons 的 2026-10-28。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用 Apple 各页条款，见 [Apple 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S28

- Apple HIG 的 [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) 与 [Remotes](https://developer.apple.com/design/human-interface-guidelines/remotes)。读取焦点与选择、当前对象消失、tvOS 控件状态、手势及遥控器按键。UIKit 的 [About focus interactions for Apple TV](https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv) 补充系统标签等控件停焦后自动选择，以及焦点引擎如何根据方向寻找下一对象。
- 05、07 章用于检查遥控浏览和激活、焦点反馈、Back 与 Play/Pause。游戏的暂停行为以及定向输入时原焦点对象消失的处理都有各自前提。分类为 `TEAM_RECOMMENDATION`。
- Focus and selection 的 Change log 最新所列日期为 2023-10-24。所读 Remotes 与 UIKit 页面未列 Change log。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用 Apple 各页条款，见 [Apple 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S29

- Apple HIG 的 [Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts) 与 [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards)。读取两页的 tvOS 部分，覆盖共享设备上的用户资料、通过其他设备认证、系统键盘与辅助输入。
- 05 章用于减少遥控录入和设计账户切换。具体登录协议、过期处理与数据隔离策略由采用项目核实。分类为 `TEAM_RECOMMENDATION`。
- Virtual keyboards 的 Change log 最新所列日期为 2025-06-09。所读 Managing accounts 页面未列 Change log。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用 Apple 各页条款，见 [Apple 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S30

- Apple HIG 的 [Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video) 与 [Top Shelf](https://developer.apple.com/design/human-interface-guidelines/top-shelf)。读取系统播放控制、音轨与字幕、与系统 TV App 整合时的观看者和续播及退出，以及 Top Shelf 概述、备用静态图、操作和详情轮播的目的地。
- 05 章及电视附页用于已提供媒体或对应系统入口的应用。按入口实际提供的按钮检验“播放”和“更多信息”，分类为 `TEAM_RECOMMENDATION`。
- Playing video 的 Change log 最新所列日期为 2023-09-12。所读 Top Shelf 页面未列 Change log。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用 Apple 各页条款，见 [Apple 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S31

- Android Developers 的 [Design for TV](https://developer.android.com/design/ui/tv/guides/foundations/design-for-tv)（原页更新 2023-05-08 UTC）、[Layouts](https://developer.android.com/design/ui/tv/guides/styles/layouts)（原页更新 2025-05-09 UTC）与 [Typography](https://developer.android.com/design/ui/tv/guides/styles/typography)（原页更新 2026-07-06 UTC）。读取远距与共用情境、画布与密度、overscan、排版角色和可读性。
- 06 章及电视附页采用安全区域与背景分开处理的设计方法。Layouts 的原则段举例为左右 48 dp、上下 27 dp。Overscan margins 段的算式又将 27 dp 取整为 24 dp，其后正文举例为左右 58 dp、上下 28 dp。约 5% 用作设计起点，具体边界由项目实测。分类为 `TEAM_RECOMMENDATION`。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用各页的 Content License，见 [Android Developers 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S32

- Android Developers 的 [Focus system](https://developer.android.com/design/ui/tv/guides/styles/focus-system)（原页更新 2024-03-21 UTC）、[TV navigation](https://developer.android.com/training/tv/get-started/navigation)（原页更新 2026-10-23 UTC）、[Use Jetpack Compose on Android TV](https://developer.android.com/training/tv/playback/compose)（原页更新 2026-10-28 UTC）及 [Manage TV controllers](https://developer.android.com/training/tv/get-started/controllers)（原页更新 2026-10-26 UTC）。读取焦点反馈、同页与深链返回、Live 标签直达播放及其例外、两种首键路径、Compose 组件的输入特点和控制器重连。
- 06 章用于方向图、返回落点及已接入 Live 的合作方深链。Compose 作为实现选项，分类为 `TEAM_RECOMMENDATION`。Live 的条件性返回要求与 S33 的 TV-DL 对读。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用各页的 Content License，见 [Android Developers 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S33

- Android Developers 的 [TV app quality](https://developer.android.com/docs/quality-guidelines/tv-app-quality)（原页更新 2026-11-17 UTC）与 [Create and run a TV app](https://developer.android.com/training/tv/get-started/create)（原页更新 2026-09-28 UTC）。核对 Tier 3 的启动器、overscan、遥控与手柄、返回与 Live、最低 SDK（TV-PS）、播放与后台媒体控件、Ambient Mode，以及 Tier 2 的 TV-4K。读取 TV Activity、leanback 及触屏声明、图标和横幅的设置条件。
- 06 章只在对应 Android TV 等级、分发及功能适用时使用 `OFFICIAL_REQUIREMENT`。TV-PC 的左右定位顺序与 S34 有文字分歧，该点单列 `UNVERIFIED`。本库没有进行商店认证。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用各页的 Content License，见 [Android Developers 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S34

- Android Developers 的 [Playback controls on TV](https://developer.android.com/training/tv/playback/controls)（原页更新 2026-10-23 UTC）。读取控制汇总表、播放或暂停、定位和进度预览。
- 06 章及电视附页分别记录播放器上下文、实际按键及播放位置。汇总表写右键前进、左键回退，S33 的 TV-PC 以相反顺序描述。左右键映射的官方一致性为 `UNVERIFIED`，其余动作按各自适用范围核对。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用各页的 Content License，见 [Android Developers 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S35

- Android Developers 的 [Accessibility best practices for Android TV](https://developer.android.com/training/tv/accessibility)（原页更新 2026-11-17 UTC）及 [TalkBack evaluation examples for TV apps](https://developer.android.com/training/tv/accessibility/talkback)（原页更新 2026-10-23 UTC）。读取文本缩放、辅助音轨支持与 TalkBack 首次使用、遥控导航示例。
- 07 章及电视附页用于为项目选择可用设置、实际遥控输入与可核对的反馈。分类为 `TEAM_RECOMMENDATION`。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用各页的 Content License，见 [Android Developers 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S36

- Android Developers 的 [On-screen keyboard](https://developer.android.com/training/tv/get-started/onscreen-keyboard)（原页更新 2026-10-23 UTC）及 [Authenticate across form factors](https://developer.android.com/identity/form-factors)（原页更新 2026-10-12 UTC）。读取电视键盘的输入方式与位置，以及后者的 Android TV 部分，包括共享设备、跨设备通行密钥与系统、Google 服务和手机前提。
- 06 章及电视附页用于搜索和认证流程。项目需核实所用输入法、设备与登录方式，分类为 `TEAM_RECOMMENDATION`。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用各页的 Content License，见 [Android Developers 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## S37

- Apple 的 [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/)（App Store Connect 的 Apple TV 表）及 [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)（2.1、2.3.3、2.4.3）。读取电视截图规格、实际使用画面、含账户功能时的审核访问和演示模式条件，以及遥控器、可选外设和必需手柄的元数据要求。
- 05 章与电视附页只在准备 App Store 提交时使用 `OFFICIAL_REQUIREMENT`。HIG 的图标、焦点及 Top Shelf 建议另见 S27、S28、S30。实际提审结果由项目记录。
- App Review Guidelines 页脚标明 Last Updated 为 2026-10-16。所读 Screenshot specifications 页面未标示更新日期。
- 动态网页实际读取于 2026-11-25（`READ_SCOPED`）。本库仅链接并作原创归纳。外部资料适用 Apple 各页条款，见 [Apple 许可说明](../THIRD-PARTY-NOTICES.md#中文)。

## 原创部分与未验证项

探索流程、交接包结构、分层验收、匿名案例、完整表单示例、维护方法和新增审阅技能为本仓库原创团队建议，不声称出自平台官方。表单状态、校验时机、查询/防重复前提及文案是合成项目选择；没有产品或服务实现证据。平台实际 SDK 兼容性、账户功能、技能自动选择、产品质量和方法效果均未由本次文档编写验证；具体项目采用前继续记录为 `UNVERIFIED`。

Figma 变量示例与落地页附页依据 S22–S23 作选择性原创归纳；示例数据、文案与检查表没有来自真实项目，不构成实测记录。设计文件验证与营销主张核实仍由实际项目取得证据。
