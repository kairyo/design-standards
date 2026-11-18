# 视觉方法增补验证 / Visual-craft addition review

## 2026-11-17 提交整合说明 / Submission integration note

本次将留存草案整合到主线 `881ef4a81b1226e48a3be1194f0ebc62ac5fb4b7`，准备功能分支提交、推送和双语 PR；没有合并、自动合并、全局安装或消费项目采用。原本地草案单独保留。下方中文与英文正文是 2026-11-06 的历史报告；当时“本地、不提交”和来源编号不代表当前阶段。

原草案来源 S24（Impeccable）现为 [S25](../references/sources.md#s25)，原 S25（Interface Design）现为 [S26](../references/sources.md#s26)，固定提交与采用范围不变；主线 S24（Apple Materials）保持原样。下方保留旧来源标签，只将链接指向对应的新编号。本轮重新读取两份 Impeccable 参考全文及根 LICENSE 前 20 行、Interface Design 技能全文与 MIT LICENSE，核对固定版本、采用与舍弃项；没有执行外部技能或审计依赖。

留存结果核对：44 条断言均记录 PASS，14 张有效截图仍在；27 个历史证据文件的 SHA-256 与原清单一致；技能正文、视觉细化参考及方向记录三份核心文件也与历史候选清单哈希一致。这是证据完整性核对，没有重跑浏览器或重新作视觉验收。历史大字密度问题与偏好/理解/效率未验证状态保留，不因文档提交而视为解决或通过。下方读屏暂缓说明只属历史；后续处置以 [Issue #7 归档备忘](https://github.com/kairyo/design-standards/issues/7)为准，已移出当前任务与固定提醒，不据此启动测试。

This submission integrates the retained draft onto main `881ef4a81b1226e48a3be1194f0ebc62ac5fb4b7` for a feature-branch commit, push, and bilingual PR. It does not merge, enable auto-merge, install globally, or adopt into a consumer project. The original local draft is retained separately. The Chinese and English report below is a historical snapshot from 2026-11-06; its local-only authorization and source numbering do not describe the current stage.

Draft S24 (Impeccable) is now [S25](../references/sources.md#s25), and draft S25 (Interface Design) is now [S26](../references/sources.md#s26), with unchanged pinned commits and adoption scope. Main's S24 (Apple Materials) stays intact. The historical labels below are preserved, while their links target the corresponding new entries. This round re-read both Impeccable references in full and the first 20 lines of its root LICENSE, plus the Interface Design skill and MIT LICENSE, checking pinned versions and adopted/excluded material without executing external skills or auditing dependencies.

Retained evidence check: all 44 assertions record PASS, all 14 valid screenshots remain available, and all 27 historical evidence files match their recorded SHA-256 hashes. The core skill, visual-craft reference, and direction-record files also match the historical candidate manifest. This is an integrity check, not a browser rerun or fresh visual acceptance. Historical enlarged-text density findings and unverified preference, comprehension, and efficiency remain unresolved/unverified; documentation submission does not convert them to passes. The deferred screen-reader wording below is historical. The subsequent [Issue #7 archive memo](https://github.com/kairyo/design-standards/issues/7) removes these checks from current tasks and recurring reminders and does not authorize starting them.

### 本次作者检查 / Current author checks

- 文档整合：`python3 -B tools/check_docs.py` 通过（59 个预期文件、49 份 Markdown、390 个内部链接、26 条来源）；`git diff --cached --check` 与 `design-direction-review` 的 `quick_validate.py` 格式校验通过。全部候选文件可按 UTF-8 读取，没有新增二进制、设计稿、截图或字体；技能包的本地链接都在包内，名称、触发描述、界面元数据与 CC BY 4.0 署名/许可保留。
- 引用与版本：S01–S24 内容逐项与主线相同；新 S25/S26 的归属、固定 SHA 和正文/通知/清单一致。仓库版本保持 draft.3，视觉技能候选为 draft.3，自适应技能仍为 draft.2。
- 作者文字边界复核：按下方六项输入核对当前技能；已批准品牌的小修、高密度工作台和混排文字均保留项目约束；没有画面时不编造观察；偏好票不推成效率收益；仅构建修复不触发设计改版、素材可访问不等于可分发。六项未发现与预期边界冲突。这是文本判读，不是宿主加载、自动选择或独立行为实验。
- 独立复核：独立执行者复核 15 文件全部增量、59 文件候选清单、六项文字边界与双语发布草稿，并独立读取五个固定来源文件；核对 S01–S24 保留、历史证据哈希与三份核心文件一致，重跑结构和暂存差异检查通过。已审补丁 SHA-256 为 `9e71f5a78365063e56f10dfbfe198958a21904a93b49e4227f89e176e8350878`，不是提交 SHA。仓库内容无阻断发现；唯一 P3 是 PR 草稿的证据相对链接，提交后须换为实际完整提交 SHA 的链接。此后仅补充本段复核事实、证据对应说明及实际台账链接，不改变技能方法。独立执行者没有重新查看 14 张截图、运行浏览器或验证宿主与真实用户效果；不能将本次文档复核当作产品验收或合并批准。

- Document integration: `python3 -B tools/check_docs.py` passed with 59 expected files, 49 Markdown files, 390 internal links, and 26 sources. `git diff --cached --check` and the `design-direction-review` skill-format `quick_validate.py` check passed. All candidate files decode as UTF-8; no binaries, designs, screenshots, or fonts were added. Local skill links stay inside the package, with its name, trigger description, interface metadata, and CC BY 4.0 attribution/license retained.
- References and versions: S01–S24 match main entry by entry. New S25/S26 ownership, pinned SHAs, prose, notices, and inventories agree. The repository stays at draft.3, the visual-skill candidate is draft.3, and the adaptive skill stays at draft.2.
- Author text-boundary recheck: compare the current skill with the six inputs below. Approved-brand refinements, dense workspaces, and mixed-language text retain project constraints; absent visuals do not justify invented observations; preference votes do not establish efficiency; build-only fixes do not trigger redesign, and asset access does not grant redistribution rights. No conflict with these expected boundaries was found. This is textual judgment, not host loading, automatic selection, or an independent behavioral experiment.
- Independent review: a separate reviewer examined the entire 15-file increment, 59-file candidate inventory, six textual boundaries, and bilingual publication drafts, and independently read five pinned source files. They checked preservation of S01–S24, historical evidence hashes, and the three core files, and reran structure and staged-diff checks successfully. The reviewed patch SHA-256 is `9e71f5a78365063e56f10dfbfe198958a21904a93b49e4227f89e176e8350878`, not a commit SHA. No blocking repository finding remained; the sole P3 concerned relative evidence links in the PR draft, which must use the actual full commit SHA after committing. Subsequent packaging only adds this review record, evidence correspondence, and actual task links without changing skill methods. The reviewer did not re-inspect the 14 screenshots, rerun the browser, or verify host behavior or real-user effects. This document review is neither product acceptance nor merge approval.

## 中文

日期：2026-11-06。基线：`de153e4258c187a7983f7d2da6c74320f6c07cf7`。范围：本地候选；不提交、不推送、不安装第三方技能。仓库版本与发布状态保持不变，`design-direction-review` 的候选元数据单独更新至 `0.1.0-draft.3`。

### 改动与来源

- 原审阅技能保留触发范围、授权、设计真相源与证据边界，增加按需读取的排版、产品密度和局部润色方法，以及同条件对照的判读方式。
- 增加可选 [视觉方向记录](../templates/visual-direction-record.md)，由主 brief 和 02 章接入；不另设设计真相源，不强制小修填全表。
- 定向采用 [S24](../references/sources.md#s25)、[S25](../references/sources.md#s26) 的方法层思路。固定提交与实际读取范围已登记；没有引入字体/素材、引擎、检测器、固定像素或风格禁令。同步双语入口、第三方说明和检查器清单。

### 同一 brief 的可运行样例

另存本地合成阅读列表，未加入本规范仓库。两种样式由同一作者制作，使用同一 HTML、内容和行为脚本；候选仅追加 CSS。它不是历史产品改版、旧新技能各自生成的独立模型实验或随机用户研究，不能据此声称新增技能具有因果效果。

共同任务：找到上次阅读条目，从第 4 节打开并返回原列表。保留完整文案、顺序、进度、系统字体、蓝色操作含义与搜索/返回行为。Chrome `156.0.8078.80`，宽屏 `1280×900`、窄屏 `390×844`；检查常规内容、混排长标题、根文字尺寸 200%、空搜索结果、打开/返回、指针与键盘。

| 证据 | 结果与边界 |
| --- | --- |
| 自动运行 | 44 项断言通过、0 失败：内容相同、可见条目、文档与所选元素无横向溢出（1 CSS px 容差）、搜索恢复、章节起点、焦点及键盘路径；运行阶段未捕获页面/控制台错误。所选元素为 h1、h2、p、input、button，不覆盖垂直裁切。打开/返回先搜索“复杂”筛到一条，键盘从指针返回后的恢复焦点开始；只证明这些起始条件下的合成路径，不证明人的任务效率 |
| 截图复核 | 14 张视口截图覆盖两种样式的宽/窄、长标题、文字压力上下区域、空态与阅读页。首次整页截图出现重复绘制区域，弃用后等待绘制并改采视口；不以坏截图判断产品缺陷 |
| 可见差异 | 候选提高上次阅读标题与标记的权重，其余操作改为描边，卡片改为列表分隔；内容没有删减。这是具体方向选择，不是通用优劣结论 |
| 代价与发现 | 混排长标题时，候选窄屏总文档高 1194 CSS px、原样式 1181 CSS px，候选整组 CSS 变化有空间代价，不能单独归因于字号；200% 根文字尺寸时，两版收藏数量均挤压介绍文字，首屏未露出列表。无溢出并不代表密度合适，后续可比较把次要数量移到下一行 |
| 人的偏好、理解、速度 | `NOT_RUN`；无参与者，不给审美分或效率提升百分比，不把自动点击当理解测试 |
| 无障碍与平台 | 根文字尺寸压力不是浏览器缩放或完整 WCAG 验收；未测真实移动设备、原生平台与自定义字体交付。原 F09/B06 读屏安排继续 `DEFERRED`，实际读屏 `NOT_RUN` |

原始 HTML/CSS/JS、共同 brief、44 项结果、截图采集记录和截图单独保存在本地任务资料，供当前审阅使用；不把含本机路径的运行材料直接加入公共仓库。是否公开样例另行决定。

### 作者边界走查（文字推演）

| 输入 | 当前处理判断 |
| --- | --- |
| 已批准中文品牌，仅检查标题与进度主次 | 保留品牌、字体、行为，检查相邻角色和同条件画面，不要求全站重做 |
| 只有 brief，没有截图 | 可记录方向假设；不声称看到裁切、对比度或排版问题 |
| 高密度工作台要求更多信息同屏 | 依据比较任务与操作频率讨论密度，不套用阅读样例的间距与卡片选择 |
| 长中英混排标题与字体回退未知 | 检查实际换行，回退保留未验证，不套固定拉丁字符数 |
| 要把“更漂亮”的投票当任务更快 | 分列偏好、理解与任务证据，拒绝没有观察支持的因果结论 |
| 只修编译错误或要求打包付费字体 | 不把该技能设为工程入口，不由审阅建议授予素材分发权 |

以上为作者推演，未验证客户端自动选择或跨客户端加载；不重写旧版九个案例的历史结果。

### 自检与独立复核

- 自检通过：`python3 -B tools/check_docs.py`（55 文件、45 Markdown、296 内部链接、25 来源）、`git diff --check`、技能格式 quick_validate。结构/格式通过不等于事实、审美或产品验收。
- 独立执行者先仅依据候选技能、共同 brief 和画面给出审阅，再读报告与运行材料。实际查看 14 张图、相关 diff/新文件、样例源码/结果，并独立核对 S24–S25 固定来源；未重跑浏览器，不称独立运行复测。请求配置为 GPT-6.1 Sol / medium，未取得运行时独立回读，不能把请求参数当实际模型证明。
- 独立复核无阻塞项；三项低优先级表述已由作者按建议修正并核对：限定横向检查的选择器、容差与路径起点；把页面高度差归于整组 CSS。同步英文可选记录边界。其视觉建议是保留候选续读主次，继续评议宽屏动作与内容的距离、长标题和大字布局；不作为改版批准。
- 本轮没有真实参与者、客户端技能安装/触发或完整无障碍测试。技能已读取并用于本次审阅，与自动加载和稳定效果是不同证据。
- 已关闭本任务隔离浏览器及回环服务，删除本任务冗余 CLI 回包和日志/快照；保留源文件、brief、解析后原始结果、14 张有效截图及采集记录，直至本轮审阅与归档决定。未触碰共享工具缓存。

## English

Date: 2026-11-06. Baseline: `de153e4258c187a7983f7d2da6c74320f6c07cf7`. Local candidate only, without commits, pushes, or third-party skill installation. Repository version and release status stay unchanged; only `design-direction-review` candidate metadata advances to `0.1.0-draft.3`.

Add optional typography, product-density, and local-refinement guidance while preserving scope, authorization, design authority, and evidence boundaries. Add a visual-direction record linked from the main brief and chapter 02, without creating a parallel design authority or requiring small fixes to fill the entire record. Selectively synthesize methods from pinned S24–S25; import no assets, engines, detectors, fixed dimensions, or style bans. Align bilingual entry points, notices, and checker inventories.

A separate local synthetic reading-list specimen shares HTML, content, and JavaScript across two CSS conditions. Both were made by one author. This is neither a historical product redesign, independently generated old/new skill experiment, nor randomized user study; it establishes no causal skill benefit. The shared task is to resume the previous item at section 4 and return, preserving wording, order, progress, system fonts, blue action semantics, and search/return behavior.

Chrome `156.0.8078.80` exercised `1280×900` and `390×844`, normal and long mixed-language content, 200% root text size, empty search, pointer and keyboard navigation. All 44 assertions passed with no failures or captured runtime page/console errors. Checks cover shared text, row visibility, document and selected-element horizontal overflow (1 CSS px tolerance), search restoration, reading position, focus, and keyboard paths; they do not measure human efficiency. Selected elements are h1, h2, p, input, and button; vertical clipping is not checked. Open/return follows a search for “复杂” that leaves one result, and the keyboard path starts from focus restored after pointer return, not an arbitrary initial state.

Fourteen viewport screenshots cover both conditions, including upper/lower text-stress regions. Initial full-page captures contained repeated painted regions and were discarded in favor of captures after rendering at viewport size; those artifacts are not product-defect evidence. The candidate emphasizes the previous title and marker, outlines secondary actions, and uses list dividers instead of cards without removing content. These are directional choices, not universal quality judgments.

Tradeoffs remain: the narrow long-title document is 1194 CSS px high versus 1181 in the baseline. This is a tradeoff of the combined candidate CSS, not an isolated font-size effect. At 200% root text size, the count crowds introduction text in both conditions and the list is below the first viewport. A later iteration could move the secondary count to another row. Passing overflow checks does not establish appropriate density. Preference, comprehension, and human speed are `NOT_RUN`. Root text scaling is not browser-zoom or WCAG acceptance; real mobile devices, native platforms, and custom-font delivery were not tested. Existing F09/B06 screen-reader work remains `DEFERRED`, with actual screen-reader execution `NOT_RUN`.

Original specimen sources, brief, results, capture records, and screenshots remain separate local review evidence; machine-specific runtime material is not added to this public repository. Publishing the specimen requires a separate decision. Six author-only text walkthroughs cover frozen design, absent screenshots, dense tools, mixed text/fallback uncertainty, unsupported preference-to-efficiency claims, and unrelated build/licensing requests. They establish no automatic-selection or cross-client-loading result and do not rewrite historical cases.

Self-checks passed: check_docs (55 files, 45 Markdown files, 296 internal links, 25 sources), git diff --check, and skill quick_validate. These structural/format checks do not establish factual, aesthetic, or product acceptance.

An independent executor first reviewed the candidate skill, shared brief, and images before reading the report/results. The executor viewed all 14 captures, reviewed related diffs/new files and specimen sources/results, and independently checked pinned S24–S25 sources. The browser was not rerun; this was independent review, not an independent runtime retest. Requested configuration was GPT-6.1 Sol / medium, without independent runtime readback; request parameters do not prove the effective model.

No blocking findings remained. Three low-priority wording findings were corrected and checked by the author: horizontal-check selectors, tolerance, and path starting conditions; and attribution of height differences to combined CSS. Optional-record boundaries were aligned in English. Visual suggestions preserve the candidate's continuation hierarchy while leaving wide-screen action distance, long titles, and large-text layout for further judgment; they grant no redesign approval. No human-participant, client-installation/selection, or complete accessibility test was performed. Reading and using the skill in this review is separate from automatic loading or stable effectiveness.

The task-owned browser and loopback service are closed. Redundant CLI responses and task logs/snapshots were removed; sources, brief, parsed original results, 14 valid screenshots, and capture records remain until the review/archive decision. Shared tool caches were not touched.
