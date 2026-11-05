# 最小文字案例包 / Minimal text-case suite

## 中文

本包用于检查规范能否支持有边界的文字判断，包含正常、异常、信息不足、补充场景和符合性边界。它不是产品测试、自动评分器或技能效果认证。题面是原创合成材料，不含真实用户、项目或设备数据。

这是可选的维护材料：当变更涉及授权、证据、交接或适用边界时，可选择相关题目复跑；不要求每次文档修改重跑全部案例，不以单轮分数作为发布门槛。保留原答和评分是为了追溯判断，不把它们加入设计正文。

- [inputs.json](inputs.json)：共同执行指令、明确列出的规范输入文件及六个题面。
- [rubric.json](rubric.json)：逐题必要判断、失败条件与评级定义，只给评审者。
- [首轮运行记录](2026-11-04-run.md)：输入身份、原始回答、作者评判及限制。

### 复跑步骤

1. 选择固定完整 commit SHA。在本地未提交候选上运行时，记录基线 SHA 与每个实际输入文件的 SHA-256；基线 SHA 不能冒充含本地修改的版本。保存题面、判据和执行指令的身份。
2. 执行者使用新上下文，只接收 `inputs.json` 及其 `specification_files` 列出的文件；不要提供本说明、判据、历史报告或参考回答。只按文件中的 `instruction` 回答全部题目，不顺着链接扩展材料，不启动产品、服务、设计工具或设备。
3. 冻结原始回答后，评审者再读取 `rubric.json`，逐项给出回答证据、遗漏与 `PASS` / `PARTIAL` / `FAIL`。按行为与证据判断，不靠出现特定词语判通过；没有回答或执行中断标 `NOT_RUN`，不能计为通过。
4. 记录日期、输入文件及哈希、执行方式、已知模型配置、执行与评审是否独立、实际读取范围、原始回答和逐题结论。不要润色原答复后仍称原始回答；补答和重试单列。上下文分离不等于系统级隔离，也不自动构成盲评。
5. 如比较两个版本，固定题面、判据与执行配置，保存两组实际输入；先评判匿名回答再解盲。规范引用仍可能暴露版本线索。不同轮次的单次成绩不能直接解释成稳定提升。

本包不要求某个模型、账户或工具；执行时沿用任务授权。文字案例评级与[产品验收记录](../../templates/verification-record.md)中的实际运行状态分开，不能用文字 `PASS` 替代产品 `NOT_RUN`。公开题面会被后续作者看到，不能当作从未见过的留出集；变更行为时应补有针对性的场景。

运行 `python3 -B tools/check_docs.py` 可检查文件、链接及案例 JSON 的基本对应关系；它不会执行模型或评判答案。旧的 16 例比较仍以 [REVIEW](../../REVIEW.md) 中的历史方法与限制为准，本包不声称复现了那一轮。

详细题面、回答和证据允许保留原始语言；本入口与结果摘要保持中英等义。文件许可沿用[许可说明](../../LICENSE-NOTICE.md)，案例数据不是可执行代码。没有新增安装、发布或产品操作授权。

## English

This suite checks whether the guidance supports bounded textual judgments across normal, abnormal, insufficient-information, supplemental, and conformance-boundary scenarios. It is not a product test, automatic grader, or certification of skill effectiveness. The original synthetic prompts contain no real user, project, or device data.

This is optional maintenance material: rerun relevant cases when a change affects authorization, evidence, handoff, or applicability boundaries. Do not require the entire suite for every documentation edit or use a single-run score as a release gate. Original answers and assessments support traceability; they are not design-chapter requirements.

- [inputs.json](inputs.json): shared instructions, an explicit list of guidance files, and six prompts.
- [rubric.json](rubric.json): required judgments, failure conditions, and rating definitions, for evaluators only.
- [First run record](2026-11-04-run.md): input identity, original responses, author assessment, and limitations.

### How to rerun

1. Select a full fixed commit SHA. For an uncommitted local candidate, record its base SHA and the SHA-256 of every actual input file; the base SHA does not identify local changes. Preserve the identities of prompts, criteria, and execution instructions.
2. Use a fresh executor context containing only `inputs.json` and its listed `specification_files`. Withhold this guide, the rubric, historical reports, and reference answers. Answer every prompt using the shared `instruction`; do not follow links for extra material or operate products, services, design tools, or devices.
3. Freeze original responses before the evaluator opens `rubric.json`. Record response evidence, omissions, and `PASS` / `PARTIAL` / `FAIL` for each criterion and case. Judge behavior and evidence, not keyword presence. Missing responses or interrupted execution are `NOT_RUN`, never a pass.
4. Record the date, input files and hashes, execution method, known model configuration, executor/evaluator independence, actual reading scope, original responses, and per-case conclusions. Do not polish responses while retaining an “original” label; record follow-ups and retries separately. Context separation is not system-level isolation and does not itself establish blinded evaluation.
5. For a version comparison, hold prompts, criteria, and execution configuration fixed and retain both input sets. Grade anonymous responses before revealing versions. Guidance citations may still reveal version clues. Single-run scores from different rounds do not establish a stable improvement.

No particular model, account, or tool is required; retain the active task's authorization. Text-case ratings are separate from actual runtime states in the [product verification record](../../templates/verification-record.md): a textual `PASS` cannot replace a product `NOT_RUN`. Public cases can be seen by later authors and are not an unseen holdout set. Add focused scenarios when behavior changes.

`python3 -B tools/check_docs.py` checks files, links, and basic case-JSON correspondence. It neither runs models nor grades answers. The historical 16-case comparison retains its own method and limitations in [REVIEW](../../REVIEW.md); this suite does not claim to reproduce that round.

Detailed prompts, responses, and evidence may retain their original language; this entry point and result summaries remain equivalent in Chinese and English. The [licensing notice](../../LICENSE-NOTICE.md) applies; case data is not executable code. No installation, publication, or product-operation permission is added.
