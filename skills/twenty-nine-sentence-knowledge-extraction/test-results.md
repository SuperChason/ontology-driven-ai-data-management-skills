# twenty-nine-sentence-knowledge-extraction — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.4.0 已增加明确输出契约；既有路由盲测结论保留，跨平台行为继续按版本抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `twenty-nine-sentence-knowledge-extraction` | PASS | 应选择 twenty-nine-sentence-knowledge-extraction 并给出执行动作 |
| should-trigger-02 | should_trigger | `twenty-nine-sentence-knowledge-extraction` | PASS | 应选择 twenty-nine-sentence-knowledge-extraction 并给出执行动作 |
| should-trigger-03 | should_trigger | `twenty-nine-sentence-knowledge-extraction` | PASS | 应选择 twenty-nine-sentence-knowledge-extraction 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `seven-plus-one-semantic-mapping` | PASS | 应选择兄弟 Skill seven-plus-one-semantic-mapping |
| edge-01 | edge_case | `none` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：怎么访谈业务专家？请结合一个企业业务场景给我可执行结果。
- 理由：请求设计业务专家访谈并形成企业场景结果，符合结构化知识提取用途。
- 计划动作：设计专家访谈提纲，按结构化句式提取概念、关系、规则、例外和证据。

### should-trigger-02 — PASS

- Prompt：我现在专家说得很散，需要结构化访谈，用29句话提取知识？
- 理由：专家表达零散且明确要求用 29 句话提取知识，直接命中该 Skill。
- 计划动作：用 29 句话框架组织访谈，把零散经验转成可确认的本体知识候选项。

### should-trigger-03 — PASS

- Prompt：Please help with knowledge elicitation and provide a concrete enterprise checklist.
- 理由：明确提出 knowledge elicitation 和企业检查清单，属于专家知识获取与结构化任务。
- 计划动作：输出知识获取检查清单，覆盖专家选择、提问、结构化记录、证据核对和确认。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：基础术语释义无需专家访谈或知识提取流程。
- 计划动作：不激活 Skill，直接提供简短术语解释。

### should-not-trigger-02 — PASS

- Prompt：按7+1映射一下？请直接按那个方法给出步骤。
- 理由：请求明确要求按 7+1 方法映射，最匹配 7+1 语义映射 Skill。
- 计划动作：按 7+1 语义框架展开映射步骤并检查语义完整性。

### edge-01 — PASS

- Prompt：当前情况是：用户只需要普通会议纪要或文档摘要。我还能直接用这个方法吗？
- 理由：用户只需要普通会议纪要或文档摘要，不涉及本体知识提取或专家确认。
- 计划动作：不激活 Skill，按普通摘要任务提炼主题、结论和待办。

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
