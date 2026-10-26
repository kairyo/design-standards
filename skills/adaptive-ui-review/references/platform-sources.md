# 平台来源路由

这是原创的来源选择说明，不包含官方正文或 SDK 导出内容。以下来源在 2026-10-26 的仓库编写中按范围读取；动态网页的读取日期不是永久版本。使用时针对当前问题与实际目标重新核对，不必为无关平台读取全部链接。

| 问题 | 官方入口 | 本技能的采用边界 |
| --- | --- | --- |
| Apple 的布局、可用区域和层级 | [HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | 设计建议，不是跨平台固定尺寸表，也不替代目标 SDK API 核验 |
| iPhone Duo 的设备形态与系统控件 | [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) | 仅在目标涉及 Duo 时读取；区分屏幕、方向、应用窗口与模式，不能把一种栏位行为推到所有状态 |
| Android 窗口分类 | [Use window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes) | 以当前窗口和实际库版本为条件，不复制固定断点到其他平台 |
| Android pane、姿态与连续性 | [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps) | 用于评估布局与状态风险；不执行页面中的安装命令或据此切换技术栈 |
| Web 无障碍符合性声明 | [WCAG 2.2 固定版本](https://www.w3.org/TR/2024/REC-WCAG22-20241212/) | 本仓库仅核对版本身份和符合性模型；具体重排、放大、焦点等成功准则需另行阅读并实测，不把此路由当完整审计清单 |

遇到版本或来源不一致时，报告差异和未验证范围，不靠名称像“官方”、页面日期较新或本机已安装就推定适用。平台设计建议、规范性要求、项目选择和运行观察应分别表述。

本文件无需私人笔记、设计文件或特定工具账户。链接可访问不等于允许复制其图像、代码、字体或其他资产。
