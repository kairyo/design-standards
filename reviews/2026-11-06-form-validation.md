# 表单纠错与验收判据验证 / Form correction and acceptance-criteria verification

## 范围与版本 / Scope and version

2026-11-06，基于 `9dfe4618e58fc2d84f97b19f38f52d0928b96bff`，补充 [07 章](../docs/07-inclusive-design.md)、[08 章](../docs/08-implementation-acceptance.md) 和 [验收模板](../templates/verification-record.md)。三条增补仍属 `TEAM_RECOMMENDATION`；版本号、来源、许可和发布状态不变。本记录所在提交的文件树标识最终文档候选，不把下述旧版演示结果当作该候选的新运行验证。关联 [Issue #7](https://github.com/kairyo/design-standards/issues/7)，不据此关闭其余验收工作。

On 2026-11-06, add guidance to chapters 07 and 08 and the verification template, based on `9dfe4618e58fc2d84f97b19f38f52d0928b96bff`. All three additions remain `TEAM_RECOMMENDATION`; version, sources, licenses, and release status are unchanged. The tree of the commit containing this record identifies the final documentation candidate; the earlier demo results below are not a new runtime test of that candidate. Related to Issue #7; remaining acceptance work is not closed by this change.

## 历史演示依据 / Historical demo evidence

2026-11-05，作者在仓库外建立独立的合成本地演示，以真实本地 HTTP 服务与 SQLite 记录验证提交、查询、重复请求及分步往返。修复后保存的 18 项记录中，16 项在所列范围内 PASS，F09/B06 的键盘与页面语义部分通过、实际读屏未执行而记为 BLOCKED；已执行的 256 条断言通过。24 个案例运行的请求与业务记录另经 SQLite 读回核对。实现和执行者相同，不称为独立产品测试。

On 2026-11-05, the author built a separate synthetic local demo outside this repository, using an actual local HTTP service and SQLite records to check submission, queries, duplicate requests, and step navigation. Of the 18 retained post-fix records, 16 passed within their stated scope; F09/B06 passed their keyboard and page-semantics portions but remained BLOCKED because actual screen-reader checks were not executed. All 256 executed assertions passed, and requests and business records from 24 case runs were cross-checked by reading SQLite. The implementer and executor were the same person; this was not independent product testing.

环境为 macOS 27.2 (26B123)、Chrome 156.0.8078.80、Python 3.9.6、SQLite 3.54.0 和 Playwright CLI 0.1.22；检查 1280×900 与 360×800 CSS 像素视口、指针/键盘、浅深主题、200% CSS 文字尺寸与混合方向内容。该记录不覆盖真实移动设备、其他浏览器、完整本地化、真实业务服务或完整无障碍符合性。

The environment was macOS 27.2 (26B123), Chrome 156.0.8078.80, Python 3.9.6, SQLite 3.54.0, and Playwright CLI 0.1.22. Coverage included 1280×900 and 360×800 CSS-pixel viewports, pointer/keyboard input, light/dark themes, 200% CSS text sizing, and mixed-direction content. It did not cover actual mobile devices, other browsers, complete localization, real business services, or full accessibility conformance.

两处已确认的演示实现问题均已修复并复验：错误提示在失焦时消失引起布局移动，导致纠正后的第一次点击未提交；未修改字段而仅切换焦点，也错误地清除了服务端错误。这说明需补充更具体的操作判据，不足以证明规范核心状态模型错误。全页截图与实际视口的疑点未被确认为遮挡缺陷；工具输出解析和等待时点问题另记，不算产品缺陷。

Two confirmed demo implementation defects were fixed and retested: removing an error on blur shifted the layout and lost the first click after correction; moving focus without editing also incorrectly cleared a server-side error. These motivate more explicit operational criteria, not a conclusion that the specification's core state model was wrong. A full-page versus viewport screenshot discrepancy was not confirmed as an obstruction defect. Output-parsing and wait-timing issues were tracked separately from product defects.

本次整理核对了保留记录的完整性与数量，没有重跑演示。原始请求记录、截图、代码和日志保留在作者受控本地位置，不随本 PR 发布；本摘要不是公开可复跑的运行证据包，独立文档复核也没有重新执行该演示。以下 SHA-256 仅用于标识保留记录，不替代访问原始证据或独立复验：

This preparation checked the integrity and counts of retained records without rerunning the demo. Raw requests, screenshots, code, and logs remain in the author's controlled local storage and are not published in this PR. This summary is not a publicly rerunnable runtime-evidence package, and independent documentation review did not execute the demo again. These SHA-256 values identify retained records only; they do not replace access to raw evidence or independent retesting:

| 记录 / Record | SHA-256 |
| --- | --- |
| 演示报告（含暂缓更新） / Demo report including deferral update | `a695520f4745bf21aac886824515ce4b4c098f0ec91a831b70538c93911d8012` |
| SQLite 交叉核对记录 / SQLite cross-check record | `df9b3b51a13a9e6a43b5653caa0b391436be7e316975d8e1d29aac1a745dd318` |
| 读屏暂缓决定 / Screen-reader deferral decision | `2cf43333da244c737368a8c6a4d76837427f8af110fc52028ded96f1ac7fe2b4` |

## 本次文字走查 / Current document walkthrough

以下是作者和独立审阅者对条款的情景推演，结论为文字是否覆盖，不是执行产品动作后的 PASS：

The following scenarios were assessed by the author and an independent reviewer for textual coverage; these are not PASS results from executing product actions:

| 情景 / Scenario | 条款覆盖与边界 / Coverage and boundary |
| --- | --- |
| 只回看字段，没有修改 / Revisit without editing | 07 章禁止仅因焦点变化清除已确认错误。 / Chapter 07 prevents confirmed errors from disappearing solely because focus changes. |
| 实际编辑后重验 / Edit and revalidate | 记录清除或待重验条件，重提仍检查完整条件；不禁止有效重验后清除错误。 / Record clearing or revalidation triggers, and recheck full submission conditions; clearing after valid revalidation remains allowed. |
| 首次点击因布局变化落空 / Layout shift loses the first click | 08 章保留按下、失焦与抬起的连续过程，核对请求和业务结果。 / Chapter 08 retains the continuous press, blur, and release sequence and checks requests and business results. |
| 键盘通过、指针失败 / Keyboard passes, pointer fails | 分别记录；必需路径失败时，组合项不能通过。 / Record paths separately; a required-path failure prevents the composite from passing. |
| 键盘通过、读屏未执行且暂缓 / Keyboard passes, screen reader unexecuted and deferred | 保留未执行状态，另记暂缓决定及恢复条件，父项不记 PASS。 / Retain unexecuted status, separately record deferral and resumption conditions, and do not mark the parent PASS. |
| 已通过部分加必需 BLOCKED / Passed portion plus required BLOCKED | 父项不能记 PASS，保留缺少的前提。 / The parent cannot be PASS; retain missing prerequisites. |
| 子项确实不适用 / A subcheck is genuinely inapplicable | 保留范围理由；不得以暂缓冒充不适用。 / Retain the scope rationale; deferral cannot masquerade as inapplicability. |
| 全部适用必需子项通过 / All applicable required subchecks pass | 只在所列条件和实际证据范围内汇总 PASS。 / Aggregate PASS only within the stated conditions and actual evidence. |

独立初审指出模板的“不得仅因其他子项通过”仍可能被误解为允许其他理由覆盖未完成状态。作者收紧为“任一适用的必需子项仍为 FAIL、BLOCKED 或 NOT_RUN，父项不得记为 PASS”；定向独立回核确认此项已解决，其余三条增补未发现阻断问题。此结论限于文字改动及相关上下文，不是全库复核、读屏验证、维护者批准或合并放行。

Initial independent review found that “must not pass solely because other subchecks pass” could still be read as permitting other reasons to override incomplete status. The author tightened it to prohibit parent PASS whenever any applicable required subcheck remains FAIL, BLOCKED, or NOT_RUN. Targeted independent follow-up confirmed resolution, with no other blockers found in the three additions. This conclusion is limited to the text changes and relevant context; it is not a repository-wide review, screen-reader test, maintainer approval, or merge clearance.

## 检查与保留边界 / Checks and retained boundaries

三条增补的本地文档检查已通过：51 个必需文件、41 份 Markdown、272 个内部链接、23 条来源；`git diff --check` 通过。此为加入本验证记录及双语入口前的历史数量；最终提交包的检查结果在 PR 验证部分另记。检查器只增加本记录的必需文件登记，不改变检查规则或弱化公开性检查。

The local three-clause candidate passed documentation checks: 51 required files, 41 Markdown files, 272 internal links, and 23 sources; `git diff --check` also passed. These are historical counts before adding this record and bilingual entry points; the final publication-package results are recorded separately in the PR validation section. The checker only registers this record as required; its checking rules and disclosure checks are not weakened.

2026-11-06，维护者明确暂缓 F09/B06 的实际读屏子项，后续明确需要时再启动。原先因计算机操作工具超时形成的 BLOCKED 历史保留，实际读屏仍为 NOT_RUN；暂缓是安排，不是 PASS 或 NOT_APPLICABLE。不会因工具恢复而自动开启测试。恢复时重新核对版本、环境与旁白原状态，测试后恢复临时设置。

On 2026-11-06, the maintainer explicitly deferred the actual screen-reader portions of F09/B06 until explicitly requested later. The historical BLOCKED records from computer-use tool timeouts are retained, and actual screen-reader execution remains NOT_RUN. Deferral is scheduling, not PASS or NOT_APPLICABLE; tool recovery does not automatically restart testing. Resumption requires rechecking version, environment, and the original VoiceOver state, then restoring temporary settings after testing.

七项 Figma 实操、真实产品效果和技能加载继续未验证；规范示例中的产品检查仍保留未执行标记，不以仓库外的合成演示摘要改写。已授权本次整理、提交、推送与创建双语 PR，暂不合并；没有正式发布或消费项目采用授权。保留既有历史报告，不复制私人路径、账号资料、原始聊天或设备标识到公开材料。

The seven Figma execution checks, real-product effectiveness, and skill loading remain unverified. Product checks in specification examples retain their unexecuted markers; a summary of an external synthetic demo does not rewrite them. Preparation, commit, push, and a bilingual PR are authorized, but merging is not. Formal release and consumer-project adoption are not authorized. Existing historical reports remain intact; private paths, account data, raw chat, and device identifiers are not copied into public material.
