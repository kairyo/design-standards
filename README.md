# Design Standards

跨项目、跨平台的设计方法与验收指南。目标是让设计决定有依据、实现可追溯、质量可验证，而不是让所有产品长得一样。

**版本：v0.1 / `0.1.0-draft.2`。状态：REVIEW_CANDIDATE，尚未完成独立复核或正式发布。**

适用于 Web/HTML、Apple 原生客户端和 Android 的设计规划、交接与验收。框架、操作系统、字体和渲染方式不同，不能保证一套数值或一个工具流程直接适用所有项目。本仓库不是平台官方规范，也不是“安装即提高审美”的技能包。

## 从哪里开始

| 工作 | 入口 |
| --- | --- |
| 明确设计目标、层级与品牌 | [01 原则](docs/01-principles.md)、[02 探索](docs/02-exploration.md) |
| 组织 Figma、准备实现输入 | [03 Figma 与交接](docs/03-figma-handoff.md) |
| 建立可复用视觉语言 | [04 设计系统](docs/04-design-systems.md) |
| 处理系统与窗口差异 | [05 Apple](docs/05-apple.md)、[06 Android](docs/06-android.md) |
| 本地化、主题与无障碍 | [07 包容性设计](docs/07-inclusive-design.md) |
| 从设计到真实运行验收 | [08 实现与验收](docs/08-implementation-acceptance.md) |
| 判断资料是否可信、是否适用 | [09 来源与经验](docs/09-reference-library.md)、[来源登记](references/sources.md) |
| 项目采用、例外、更新与退出 | [10 采用与维护](docs/10-adoption-maintenance.md) |
| 用技能执行设计方向或自适应审阅 | [技能目录与复用边界](skills/README.md)、[边界案例](skills/review-cases.md) |

可直接讨论的材料：[设计 brief](templates/design-brief.md)、[采用记录](templates/adoption-record.md)、[验收记录](templates/verification-record.md)、[匿名合成案例](examples/anonymous-cases.md)。

`skills/` 内新增两个自包含的原创审阅技能；它们仍是候选，没有全局安装、自动注册或启用到现有项目。已有第三方设计插件只作能力索引，不随本仓库分发。

## 四种声明，不混在一起

- `OFFICIAL_REQUIREMENT`：有明确出处与适用条件的官方规范性要求；不是所有官方建议都属于此类。
- `TEAM_RECOMMENDATION`：本仓库提出的方法，包括对官方设计建议的选择性采用；不是官方背书。
- `PROJECT_CHOICE`：由具体项目决定的品牌、语言、范围、数值、技术栈与流程。
- `UNVERIFIED`：尚未读到有效来源或尚无对应验证证据；不能拿来签署通过。

“来源已读取”“建议值得采用”“项目已批准”“实现已验收”分别记录。正文默认是 `TEAM_RECOMMENDATION`，其他分类在相应段落明确标注。

## 边界

本仓库不改变任何现有项目的设计、规则或权限。采用需由项目明确选择章节并固定完整 commit SHA，处理冲突后再执行；不能因为本仓库更新就自动覆盖冻结设计。

本仓库不统一模型、账号、权限、记忆、个人设置、工程流水线或数据库规则，也不新增发布授权。具体工作仍遵守当前项目的管理与安全要求。

这里只存原创方法、公开资料的链接及简短适用说明。没有私有项目标识、真实用户资料、设计文件、字体、图标包、第三方文档镜像或 SDK 导出文件。

## 维护与状态

- [贡献与公开检查](CONTRIBUTING.md)
- [本仓库 Agent 维护入口](AGENTS.md)
- [变更记录](CHANGELOG.md)
- [审阅记录与未完成项](REVIEW.md)
- [许可待定说明](LICENSE-NOTICE.md)、[第三方资料声明](THIRD-PARTY-NOTICES.md)

公开可读不等于已授予统一开源许可；许可由维护者另行决定。本审阅稿不宣称已被任何生产项目采用。
