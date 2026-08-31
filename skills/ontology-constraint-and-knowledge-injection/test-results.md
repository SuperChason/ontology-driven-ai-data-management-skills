# ontology-constraint-and-knowledge-injection — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.3.0 已扩展为 25 个 Skill，需重新执行跨平台行为抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `ontology-constraint-and-knowledge-injection` | PASS | 应选择 ontology-constraint-and-knowledge-injection 并给出执行动作 |
| should-trigger-02 | should_trigger | `ontology-constraint-and-knowledge-injection` | PASS | 应选择 ontology-constraint-and-knowledge-injection 并给出执行动作 |
| should-trigger-03 | should_trigger | `ontology-constraint-and-knowledge-injection` | PASS | 应选择 ontology-constraint-and-knowledge-injection 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `intent-driven-minimal-ontology-loading` | PASS | 应选择兄弟 Skill intent-driven-minimal-ontology-loading |
| edge-01 | edge_case | `ontology-constraint-and-knowledge-injection` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：Prompt RAG 微调怎么选？请结合一个企业业务场景给我可执行结果。
- 理由：Prompt、RAG、微调的选择正是本体知识注入路线的核心决策。
- 计划动作：根据知识稳定性、实时性、规则约束、可解释性和更新成本选择注入方式并给出组合方案。

### should-trigger-02 — PASS

- Prompt：我现在规则型任务需要提高可解释性和一致性，本体怎么注入大模型？
- 理由：规则型任务需要提升可解释性和一致性，明确符合本体约束与知识注入场景。
- 计划动作：定义最小知识范围，并设计 Prompt 约束、RAG 检索或微调的组合、证据返回和一致性验证。

### should-trigger-03 — PASS

- Prompt：Please help with knowledge injection and provide a concrete enterprise checklist.
- 理由：提示明确要求 knowledge injection 的企业级实施清单。
- 计划动作：输出知识范围、注入路线、来源与版本、检索约束、评测、更新和回退的检查清单。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：基础术语全称与释义无需进行知识注入路线设计。
- 计划动作：不激活 Skill，直接给出简短定义。

### should-not-trigger-02 — PASS

- Prompt：只加载当前需要的本体？请直接按那个方法给出步骤。
- 理由：“只加载当前需要的本体”直接命中意图驱动的最小本体加载场景。
- 计划动作：澄清意图并设计子本体路由、最小加载范围、检索策略和无法确定意图时的处理。

### edge-01 — PASS

- Prompt：当前情况是：把微调当作实时事实更新机制。我还能直接用这个方法吗？
- 理由：把微调用于实时事实更新属于知识注入路线选型错误，适合用该 Skill 纠正并重新分配注入方式。
- 计划动作：将实时事实改由受版本控制的检索或运行时服务提供，把微调限定在相对稳定的能力与模式学习，并设计更新和回退机制。
