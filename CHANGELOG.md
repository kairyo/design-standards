# 变更记录

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
