# v0.1 审阅记录

状态：`REVIEW_CANDIDATE`，不是正式发布、项目采用或产品验收结论。

2026-11-04 许可状态更新：本版本原创文档采用 CC BY 4.0、原创代码采用 MIT，范围和贡献条件见 [许可说明](LICENSE-NOTICE.md)。以下各日期的“许可待定”均保留为历史快照；许可变更不补认全库审阅或产品验收。

## 2026-11-09：自适应保真与回归增补 / Adaptive fidelity and regression increment

基于 `9dfe4618e58fc2d84f97b19f38f52d0928b96bff` 的文档候选，范围为 03、04、05、08 章、现有验收模板、[合成案例](examples/adaptive-fidelity-regression.md)及相关入口/文件清单。只增加原创团队方法与合成项目选择；未增加或重新认证平台官方事实，没有引用私有项目材料或具体尺寸。

This documentation candidate is based on `9dfe4618e58fc2d84f97b19f38f52d0928b96bff`, covering chapters 03, 04, 05, and 08, the existing verification template, a [synthetic example](examples/adaptive-fidelity-regression.md), and related entry points/inventory. It adds original team methods and synthetic project choices only, without adding or recertifying official platform facts or referencing private project material or concrete dimensions.

- 作者检查：结构校验通过（52 个预期文件、42 份 Markdown、295 个内部链接、23 条来源）；`git diff --check` 通过。已通读完整增量及合成案例，核对双语入口和声明范围。对完整候选文本树做定向公开性检查，未发现所检项目标识、私有链接/路径或新增具体尺寸；这不构成全面隐私或事实认证。
- 适用边界走查：未知素材比例不推定通过；允许经批准的等比裁剪与排版变化；无溢出时不制造内容；留白不自动判错；共享页面可保留不同状态；背景延展与操作遮挡分开；历史隐藏层不自动清理；原稿更新保护无冲突的已批准修正。以上为作者对条款的内容走查，不是独立模型评测或产品测试。
- 独立文档审阅：`NOT_RUN`，待安排；历史全库复核不覆盖本次增量。
- 产品验证：合成案例八项检查全部 `NOT_RUN`；没有 Figma 实操、原型拖动、辅助技术、模拟器或真机证据，不声称方法效果或产品验收通过。
- 采用与发布：上述结果是提交前的本地自检快照；用户随后授权将候选提交并推送至功能分支。该授权不代表独立审阅、合并、正式发布或消费项目采用已完成。

- Author checks: structural validation passed (52 expected files, 42 Markdown files, 295 internal links, and 23 source entries); `git diff --check` passed. The full increment and synthetic example were read, including bilingual entry points and claim scope. Targeted inspection of the complete candidate text tree found none of the checked project identifiers, private links/paths, or newly added concrete dimensions. This is not comprehensive privacy or factual certification.
- Applicability walkthrough: unknown source proportions do not establish a pass; approved proportional cropping and typography changes remain allowed; no overflow does not justify invented content; whitespace is not automatically a defect; shared pages may preserve distinct states; background extension and obstructed controls are assessed separately; hidden historical layers are not automatically cleaned up; source updates preserve nonconflicting approved fixes. These are author content checks, not independent model evaluations or product tests.
- Independent document review: `NOT_RUN`, unassigned; historical repository-wide review does not cover this increment.
- Product validation: all eight synthetic checks remain `NOT_RUN`. There is no Figma execution, prototype-dragging, assistive-technology, simulator, or physical-device evidence, and no claim of proven effectiveness or product acceptance.
- Adoption and publication: the results above are a local pre-commit self-check snapshot. The user subsequently authorized committing and pushing the candidate to a feature branch. That authorization does not establish completion of independent review, merge, formal release, or consumer adoption.

## 内容范围

十个主题已形成正文，另有来源登记、三个模板和六个匿名合成案例。`0.1.0-draft.2` 新增两个原创审阅技能、能力目录与九个技能边界案例；`0.1.0-draft.3` 补充 03 章的 Figma 画布边界、空间组织和整理验证。已纳入 main、尚未正式发布的表单增补扩展 02、04、07、08 章及两个现有模板，新增完整表单合成示例及分步往返示例。官方资料仅以公开链接及短摘要引用；没有复刻设计资源或原样复制第三方文档。

2026-11-04，已对 `4102b2bf8ce2bd29a69c0cde5436aa8fba64f322` 完成首轮全库独立内容复核；结论和局限见 [全库复核记录](reviews/2026-11-04-repository-review.md)。该结论只覆盖所列版本、来源与文字证据；下列旧轮次仍保留各自时点和范围。

2026-11-05，本地追加 Figma 变量与主题示例、落地页 brief 附页及相关入口。增量范围、文字走查、独立复核与未执行项见 [本轮验证记录](reviews/2026-11-05-figma-landing.md)。它不重写旧轮次成绩，也不表示实际 Figma 或产品检查通过。

On 2026-11-05, local additions introduce a Figma variable/theme example, an optional landing-page brief appendix, and related entry points. See the [verification record](reviews/2026-11-05-figma-landing.md) for the incremental scope, document walkthrough, independent review, and unexecuted checks. This does not rewrite earlier scores or establish actual Figma or product acceptance.

## 自检记录

2026-10-26，作者对候选内容完成下列自检；它不是独立复核。

### 0.1.0-draft.1

- 结构检查：24 个预期文件，22 份 Markdown，47 个内部链接，15 条来源登记，检查通过。
- 公开性定向检查：未发现所检查的内部项目标识、主机个人路径、私有设计/笔记链接或节点格式；文件清单只有正文、版本文件和原创检查脚本。此类扫描不能证明所有隐私风险均不存在，仍需人工复核。
- 范围审阅：固定语言数、品牌数值、Cloud-only、整数尺寸、重试次数和 ImageGen 均未作为无条件通用要求；官方建议、条件性规范要求与项目选择分开。
- 来源审阅：正文采用登记的读取范围；动态网页不假称已固定 SHA，WCAG 与 WCAG2ICT 的适用地位分开。
- 许可检查：未添加统一开源许可证，未携带第三方正文、设计资源或 SDK 导出文件。

上述结果针对候选内容。实际提交历史、元数据、远端分支与 PR 身份在发布交接中单独核对；本文件不以自引用 SHA 冒充该核验。

### 0.1.0-draft.2

- 结构检查通过：31 个预期文件、27 份 Markdown、54 个内部链接、16 条来源登记；`git diff --check` 通过。
- 两个技能完整文件夹分别复制到隔离临时目录，使用系统 Ruby 的 YAML 安全解析器检查 frontmatter、名称、描述、界面字段及调用名称；本地引用均留在各自技能包内。没有读取私人笔记或依赖仓库外的本地文件。
- 宿主自带 `quick_validate.py` 因所用 Python 缺少 PyYAML 未能运行完成；没有安装依赖。上项是替代结构核对，不冒称该校验器通过，也不代表其他客户端运行已验证。
- 在隔离副本注入两个合成错误：技能越界引用、界面元数据中的示例私人路径；文档检查器均报告失败，恢复正常副本后重新通过。测试材料未进入公共文件树。
- 九个合成请求完成作者手工走查，具体处理记录在技能目录；没有运行独立 Agent、自动选择评估或真实设备测试，不据此声称审美效果提升。
- 新内容是原创短工作流；所见第三方技能仅作能力与许可边界索引，未复制其文件。原有十章正文、已安装技能与消费项目均未改动。

这些结果不延伸此前候选的审阅结论；新增技能与检查脚本变化仍需独立复核。

### 0.1.0-draft.3

2026-11-02，本轮仅增加通用 Figma 方法与来源，不重新认证旧版的全部官方资料或技能效果。

- 已读取 S17 指定正文，近似坐标范围和跨页操作描述作为产品能力事实；团队排布与保护建议没有标作 `OFFICIAL_REQUIREMENT`。
- 结构检查通过：31 个预期文件、27 份 Markdown、56 个内部链接、17 条来源登记；`git diff --check` 通过。检查器仅将来源编号上限同步到 S17，其余逻辑未变。
- 使用内存替换输入检查来源登记：正常 S17 通过，缺少 S17、重复 S17、意外 S18 均按预期失败；没有改写真实来源文件或安装依赖。
- 已人工通读完整候选树，并定向扫描候选文本和既有可达历史，未发现本轮发布的隐私或凭据阻碍；扫描不是全面安全认证。最终待公开提交、署名及 PR 文案在提交后另行核对，准确 SHA 和结果留在 PR 交接中；独立复核尚待完成，不预先记作通过。
- 没有访问或修改设计文件，没有操作真实节点或验证极限坐标、跨页依赖、账户功能与性能；这些项目运行证据仍为 `UNVERIFIED`。
- 没有更改许可、安装工具、启用技能、构建或修改消费项目。本轮独立复核只针对明确候选与差异，不替代全仓库正式发布决定。

### 未发布：表单提交与纠错

2026-11-03，基于 `0.1.0-draft.3` / `fd2c9f030fe350e57ddd3508294ef93525b69b34` 完成本地文档增补；记录当时未提交、推送或更改版本号，本记录不代表正式发布或消费项目升级。

- 作者自检：四章分别负责模式选择、组件/token、操作可访问性及验收；完整示例维护一份状态定义，两个模板沿用原有字段与案例。
- 来源：登记 S18–S21 的读取范围、固定提交或动态页面身份、采用与不采用部分；补读同一固定 WCAG 版本的所列条款，不重新认证旧来源的全部内容。
- 结构检查通过：32 个预期文件、28 份 Markdown、85 个内部链接、21 条来源登记；`git diff --check` 通过。
- 检查器在隔离临时副本完成 7 项检查：正常候选通过；缺少 S21、重复 S21、意外 S22、使用未登记的 GitHub 分支或文件、缺少完整示例均按预期失败。测试输入未进入仓库，没有放宽到任意 GitHub 路径。
- 内容与范围：示例输入为原创合成数据；未知提交结果不直接归入可重试失败，原始工具结果与人工判断分开。11 项产品验收全部为 `NOT_RUN`，没有运行产品、服务查询、读屏或自动无障碍扫描。
- 独立文档初审发现两项：查询确认字段拒绝时需要回到纠错状态；重复操作验收需要分别验证客户端拦截与服务端防重复。作者已修订状态表及 F03、F06、F08；独立审阅者完成定向再审，确认两项已解决，未发现新增需修正问题。
- 独立审阅者另核对 S12、S18–S21 的本次相关正文；S18 外链图像与其 LICENSE 未由审阅者重读。复核只覆盖本次文档增补，不追认旧版整库审阅、许可证或任何项目的产品验收；本条为作者对审阅结果的记录，不是审阅者的发布批准。

### 未发布：案例验证后的定向修订

2026-11-03，在上述本地增补后进行案例验证并按发现修订；前节的数量与结论保留为当时快照。该阶段仍为本地候选，当时未提交、推送或更改版本号。

- 前轮对相同 12 个合成文字案例做新旧版对照；独立审阅者依据匿名回答评判，评判时未知版本映射。旧版 11 项完整、1 项部分，新版 10 项完整、2 项部分，两组没有预定义危险建议。单轮结果不证明新版更好或更差，也不属于产品验收。
- 本轮补齐分步往返的草稿、有效字段、依赖步骤与确认关系及具体焦点；增加不可重试整单拒绝的直接/查询路径；把纠错重提后的业务结果核对写入模板和示例。08 章已有原则沿用，未重复追加；并发编辑恢复示例留待后续。
- 作者按原案例与验收条件定向走查上述三类问题，同时检查正常成功、仅回看不修改和结果已知但恢复条件不明的边界；这是文档覆盖检查，没有重新进行一轮模型效果对照。焦点落点及状态名仍为合成项目选择，未改变官方要求或扩大来源采用范围。
- 结构检查通过：33 个预期文件、29 份 Markdown、97 个内部链接、21 条来源登记；`git diff --check` 通过。检查器仅增加分步示例的预期文件入口；原来源与 GitHub 路径限制保留。
- 独立初审指出四处验收表述缺口：整单拒绝查询前后的状态时序、自取分支的实际提交证据、使用非默认排序检验保留、模板中的查询触发动作。作者已逐项修订；独立审阅者完成定向再审，确认四项已解决，未发现新的行为矛盾。本条为作者对该范围审阅结果的记录，不代表发布批准。
- 创建示例 F01–F12、分步示例 B01–B06 共 18 项产品检查全部为 `NOT_RUN`；没有运行产品、服务请求、读屏或自动无障碍扫描。独立文档复核与产品、整库及发布验收分别记录。

### 未发布：修复后完整案例复测

2026-11-03，对原始旧版、修复前快照和修复后快照各执行一轮合成文字案例；这是规范应用的案例评估，不是产品测试。以下是可公开的验证摘要，原始手册包、完整题面/判据、回答和匿名评分保存在作者受控的本地记录中，未随本 PR 公开；本节不是可直接复跑的测试套件。

#### 输入、方法与判定

- 原始旧版为固定提交 `fd2c9f030fe350e57ddd3508294ef93525b69b34`。各组均读取十章正文、三个模板、匿名案例和来源登记；修复前另含完整表单示例，修复后再含分步往返示例。未向执行者提供历史成绩、修复报告或版本映射。
- 三个执行者分别使用独立上下文，均指定 `gpt-6.1-sol` / `high`，按同一指令与顺序各回答 16 例，共 48 份回答。每例三个必要判断及危险建议在执行前固定；另由独立上下文中的同配置模型评审，每例回答次序随机排列，评分时不提供版本映射，评分保存后再解盲。
- 原 12 例覆盖正常、异常、信息不足和原新增场景；追加 C13–C16 四项边界。C12 将过时的“当前七种状态未覆盖”改为中性要求核对所给手册是否覆盖，第三判据相应核对覆盖与项目选择边界；业务事实及危险判据不变，三组采用同一题面。其余原案例和判据保留。
- `PASS` 为三个必要判断完整满足且无危险建议；`PARTIAL` 为存在遗漏或含混但无危险建议；`FAIL` 为危险建议或实质矛盾。这些评级只针对文字回答，不映射为产品验收状态。
- 124 处手册引文均核对到各自原文与章节；48 份评分覆盖 144 项必要判断，其中 354 处证据短引逐字匹配回答字段。结构与引文检查不能替代内容判断。

下列 SHA-256 标识当时提供的 JSON 手册包，供持有原始材料的审阅者核对，不是 Git 提交 SHA，也不单独证明评估有效：

| 手册包 | 文档数 | SHA-256 |
| --- | --- | --- |
| 原始旧版 | 15 | `2d5f5f0a463330867072c50cea3d41f0e78999e8c954966c1f244e734877dfd8` |
| 修复前 | 16 | `78cada5611ba22f1067fca40b10dc8d9c4f9840ff84d9e6cf7d6fd32704d7c37` |
| 修复后 | 17 | `3f87d49c27f18641ceafae9beaea0b489be97c9338d07adba7646e94169484bb` |

#### 本轮结果

| 版本 | 原 12 例 PASS / PARTIAL | 加测 4 例 PASS / PARTIAL | 全部 PASS / PARTIAL / FAIL |
| --- | --- | --- | --- |
| 原始旧版 | 9 / 3 | 3 / 1 | 12 / 4 / 0 |
| 修复前 | 11 / 1 | 2 / 2 | 13 / 3 / 0 |
| 修复后 | 12 / 0 | 4 / 0 | 16 / 0 / 0 |

| 编号 | 合成情境 | 原始旧版 | 修复前 | 修复后 |
| --- | --- | --- | --- | --- |
| C01 | 批准方向内的小文案调整 | PASS | PASS | PASS |
| C02 | 已确认成功后的反馈与操作 | PARTIAL | PASS | PASS |
| C03 | 已批准且可追溯的 Token 覆盖 | PASS | PASS | PASS |
| C04 | 超时却准备清空并自动重提 | PASS | PASS | PASS |
| C05 | 丢失字段拒绝响应后查询、纠错并重提 | PASS | PARTIAL | PASS |
| C06 | 导出成功掩盖循环引用与未批准备用值 | PASS | PASS | PASS |
| C07 | 仅凭按钮截图签收服务端防重复 | PASS | PASS | PASS |
| C08 | 自动检查 incomplete 且人工环境受阻 | PASS | PASS | PASS |
| C09 | 查询、防重复能力和测试权限尚未确认 | PASS | PASS | PASS |
| C10 | 编辑已有记录时发生版本冲突 | PARTIAL | PASS | PASS |
| C11 | 分步表单修改前序分支 | PARTIAL | PASS | PASS |
| C12 | 当前条件下不可重试的整单拒绝 | PASS | PASS | PASS |
| C13 | 已确认未创建，但重试条件未知 | PASS | PARTIAL | PASS |
| C14 | 分步流程仅回看，没有修改选择 | PASS | PASS | PASS |
| C15 | 拒绝到达时焦点仍有效或所在控件被移除 | PASS | PASS | PASS |
| C16 | 批量 6 条成功、2 条字段拒绝、2 条未知 | PARTIAL | PARTIAL | PASS |

#### 发现、修复对应与限制

- C05：修复前再次遗漏重提后的实际业务结果检查；修复后明确比对原标识未创建、新提交标识与输入快照、新记录内容。输入保留、主动定位及不抢焦点的边界同时保留。
- C11：修复后明确返回、分支切换、主动进入下一步及缺项纠错的焦点落点，并检查草稿、确认与请求一致。修复前本轮也通过，而上一轮为部分通过；不能把本例写成稳定的评分提升。
- C12：三组回答均通过。修复后已能直接引用新增整单拒绝条款；旧版和修复前依原则推导并指出覆盖缺口。这里补齐的是明确表达，不能改写成旧版曾失败。
- 修复后四项边界加测均通过。C13 的修复前回答对请求对应关系仍含混，C16 的旧版及修复前回答未明确核对纠正重提后的新业务记录；修复后均补齐。未出现任何一项低于修复前的评级，也没有预定义危险建议。
- 本轮旧版 C02、C10 的部分通过，分别来自成功反馈的焦点边界与冲突解决后数据核对不够明确。历史成绩保持原样；同一快照的单轮生成与判读存在变化，不能把不同轮次直接当作稳定效果测量。
- 案例与判据由已知文档内容的作者准备；C11/C12 已进入修复后示例，新增边界只是有限的迁移检查。版本映射虽隐藏，内容及引用仍可能暴露版本线索；上下文隔离不是操作系统级隔离证明。单轮、模型执行与模型评分不支持统计显著或普遍效果承诺。
- 结构检查通过：33 个预期文件、29 份 Markdown、97 个内部链接、21 条来源登记；`git diff --check` 通过。复测前后 33 个文件哈希、分支、HEAD、暂存区和工作区差异一致。随后仅整理本审阅记录与 CHANGELOG，所测规范正文、模板、示例和来源内容保持不变。
- 18 项产品检查继续为 `NOT_RUN`；没有真实服务、设备、辅助技术或用户试用证据。批量与并发编辑的完整产品契约仍由采用项目定义；本轮不据此扩大采用、许可、发布或合并范围。

## 独立复核重点

- 官方要求与建议分类、动态来源的时效边界、Duo 系统行为的适用条件。
- 本地化、单位、布局精度、构建方式与工具选择没有混入单个项目的绝对规则。
- 交接、真实运行证据和审阅独立性保持清晰，而不引入平行权限体系。
- 原创性、公开性、许可和实际可用性；作者检查不替代独立复核。
- 技能的触发边界、自包含性和真实使用效果；平台建议不得变成默认改配置、设备操作或委派授权。

## 待决定 / 未验证

- 首轮全库独立内容复核已完成，后续修订及复验分别记录；技能加载、实际产品效果和维护者的正式发布决定仍未完成，不创建稳定发布标签。
- 当前版本的原创文档与代码分别按 CC BY 4.0 和 MIT 提供，具体范围见许可说明；历史阶段的许可待定记录保留，第三方权利另行核对。
- 没有对任何现有项目启用规范；没有验证平台 SDK、Figma 账户功能或真实产品运行。
- 没有证据证明采用此文档能提高某个可量化的审美评分；可用性应在获准的代表性任务中评估。
- 没有安装、配置或建立自动更新机制。
- 新技能尚未完成宿主自动选择、跨客户端兼容、独立行为评估或真实项目验收；未创建插件分发包。
