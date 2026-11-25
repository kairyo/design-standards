---
name: adaptive-ui-review
description: "Review adaptive layouts and state continuity across window resizing, split views, fold states, and changing content or input on Web, Apple or Android. Includes TV viewing distance, overscan and remote focus across navigation, Back or list updates. Pure visual styling, build work and API-only migrations are outside scope."
license: "CC-BY-4.0; see LICENSE and attribution below."
metadata:
  version: "0.1.0-draft.3"
  provenance: "Original design-standards workflow; not an official platform skill."
---

# 自适应界面审阅

检查空间、内容或输入方式变化后，用户能否继续原来的任务，当前位置、焦点与输入能否保留。以下是团队审阅方法。实际操作设备、修改代码或启动服务依任务授权执行。

## 界定本次判断

确认目标平台、相关系统/框架版本、当前布局与用户关心的变化。分清设计方案审阅、代码分析和真实运行验证，说明手头证据能证明到哪一步。保留批准的导航、品牌、组件及产品专属验收条件。

当需要判断系统行为、平台限制或规范性要求时，先读 [平台来源路由](references/platform-sources.md)，只核对相关来源。不要把某个设备、SDK 导出技能或历史经验直接推广到所有项目；不可访问的来源保持未验证。

## 拆开空间、结构与状态

1. **空间输入**：识别组件真正获得的容器/窗口尺寸，以及安全区域、系统控件、键盘和局部遮挡。物理屏幕尺寸不能代替当前可用空间；宽高、方向、布局方向和输入方式各自记录，不假定左右留白相等。
2. **结构选择**：判断内容应重排、折叠、切换 pane、限制阅读宽度，还是允许滚动。改变布局前先说清哪些内容必须同时可见、如何返回以及主操作在哪里；不要只把单栏无限拉宽，也不要让关键操作在窄空间失去入口。
3. **状态连续性**：列出此次变化应保留的具体状态，例如当前对象、导航位置、未提交输入、焦点和阅读位置。哪些状态允许重置由产品决定，不自造一套全局策略。

布局断点、尺寸单位和控件最小值应来自实际平台与内容压力，不从设计画布等比例除算、不跨平台复制数值。只在问题涉及绘制或对齐时核对像素精度，不将整数尺寸强制施加到所有布局计算。

## 电视上的可见范围与遥控焦点

审阅 tvOS 或 Android TV 的远距布局时，记录目标观看距离和电视的显示设置。背景可以延伸到屏边。检查长标题、操作和放大后的焦点轮廓在过扫描（overscan）裁切后是否仍完整可见，在目标距离能否辨认。安全区按各平台来源和目标电视核对。

审阅遥控操作时，标出首个焦点和关键控件在四个方向上的可达邻项。用 Siri Remote 的方向输入或 Android TV 的 D-pad，分别记录移动、停留与按下确认的结果。tvOS 的 UIKit 系统标签可在短暂停焦后切换面板。经过普通卡片可以显示约定的预览，收藏、购买等业务动作应等用户主动确认。

从列表进入详情或打开面板后，按返回并核对目的地、滚动位置和重新接收输入的控件。异步重排后按内容身份核对焦点。原项换了格位时，检查焦点是否跟随它，下一次确认是否仍打开同一项。定向输入时若原项已下架，检查焦点是否落在可见、合理的邻项。若列表已空，检查遥控器能否返回上一级。画面有重试等操作时，再检查这些控件能否获焦并执行。只有静态画面时，记录预期路径，把焦点恢复与真机裁切留待实测。

## 选择能暴露风险的验证

针对已发现的风险选择条件，不要求每次全排列：

- 在结构切换附近改变可用窗口，观察临界两侧；不要只测试设备预设的最大和最小画面。
- 对可能受影响的区域加入长内容、较大文字、布局方向或键盘变化；只测试项目支持的能力，不擅自增加平台/语言范围。
- 记录一次相关的“变化前—变化—返回”过程，检查布局与上一步列出的状态；两张独立静态截图不能证明状态连续。
- 有运行权限与工具时，实际检查内容可达、主操作、返回路径、滚动和输入；说明构建/版本与测试环境。没有权限或工具时给出可执行的验证计划，不启动设备、服务或安装依赖补齐证据。

发现问题时，分清容器输入、结构策略、系统行为和状态保存各自的证据。不要一次改多个变量后就宣布根因已确定；仅有源代码检查或短时恢复时，保留运行缺口。

## 输出

给出需保留的行为、具体适配风险和下一步验证。每个关键发现说明条件、证据、用户影响及最小建议；无证据的假设单列。将设计建议、代码检查、实际运行结果分开，不用一种证据替代另一种。

达到本次约定的审阅范围即收尾；对未跑的平台或状态写明未验证。审阅本身不改变项目的最终放行权或独立审查要求。

## 许可与署名 / License and attribution

本包原创技能文本、引用说明及界面描述元数据采用 [CC BY 4.0](LICENSE)。Copyright (c) 2026 kairyo and contributors。来源：[Design Standards](https://github.com/kairyo/design-standards)。分享时按许可保留署名、来源、许可及免责声明信息，并注明修改；外部链接材料保留原权利。原内容按许可原文“现状”提供。

Original skill text, reference notes, and interface-description metadata in this package use [CC BY 4.0](LICENSE). Copyright (c) 2026 kairyo and contributors. Source: [Design Standards](https://github.com/kairyo/design-standards). When sharing, retain attribution, source, license, and disclaimer information as required, and indicate changes. Linked external material retains its original rights. The original material is provided as-is under the full license.
