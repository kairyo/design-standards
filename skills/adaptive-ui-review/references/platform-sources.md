# 平台来源路由

本页列出不同审阅问题对应的官方资料。第一组于 2026-10-26 按范围读取，电视专题的读取范围另列。动态网页按读取日记录，使用时针对当前问题与目标平台核对。

| 问题 | 官方入口 | 本技能的采用边界 |
| --- | --- | --- |
| Apple 的布局、可用区域和层级 | [HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | 设计建议，不是跨平台固定尺寸表，也不替代目标 SDK API 核验 |
| iPhone Duo 的设备形态与系统控件 | [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) | 仅在目标涉及 Duo 时读取；区分屏幕、方向、应用窗口与模式，不能把一种栏位行为推到所有状态 |
| Android 窗口分类 | [Use window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes) | 以当前窗口和实际库版本为条件，不复制固定断点到其他平台 |
| Android pane、姿态与连续性 | [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps) | 用于评估布局与状态风险；不执行页面中的安装命令或据此切换技术栈 |
| Web 无障碍符合性声明 | [WCAG 2.2 固定版本](https://www.w3.org/TR/2024/REC-WCAG22-20241212/) | 本技能在 2026-10-26 的初始来源范围为版本身份和符合性模型，不代表整个仓库的后续补读范围。具体重排、放大、焦点等成功准则仍须针对当前问题阅读并实测，不把此路由当完整审计清单 |

## tvOS 与 Android TV

以下入口于 2026-11-25 按表中主题读取。先选平台，再选本次要判断的行为。

| 审阅问题 | 官方入口 | 读取范围与适用条件 |
| --- | --- | --- |
| Apple TV 的观看距离与可见区 | [Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos) · [HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | 前者说明观看与输入情境，后者的 tvOS 小节说明主要内容安全区和聚焦放大的间距。 |
| Siri Remote 经过、确认或原项消失 | [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) · [About focus interactions for Apple TV](https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv) | 按 HIG 区分定向移动与选择。UIKit 文档说明系统标签短暂停焦后可以自动选择，业务按钮需单独判断。 |
| Android TV 的观看距离与过扫描 | [Design for TV](https://developer.android.com/design/ui/tv/guides/foundations/design-for-tv) · [Layouts](https://developer.android.com/design/ui/tv/guides/styles/layouts) | 核对远距可读、背景延展与可操作区域。Layouts 中的边距示例有差异，交付时记录目标设备的实际可见边界。 |
| Android TV 的方向键、确认和返回 | [TV navigation](https://developer.android.com/training/tv/get-started/navigation) · [TV app quality](https://developer.android.com/docs/quality-guidelines/tv-app-quality) | 前者区分方向键、中心键以及不同导航结构的返回落点。需要判断质量要求时，再按目标等级及功能查后者的 TV-OV、TV-DP 或 TV-DB。 |

遇到版本或来源不一致时，报告差异和未验证范围，不靠名称像“官方”、页面日期较新或本机已安装就推定适用。平台设计建议、规范性要求、项目选择和运行观察应分别表述。

本文件无需私人笔记、设计文件或特定工具账户。链接可访问不等于允许复制其图像、代码、字体或其他资产。
