# intent-driven-minimal-ontology-loading — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.4.0 已增加明确输出契约；既有路由盲测结论保留，跨平台行为继续按版本抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `intent-driven-minimal-ontology-loading` | PASS | 应选择 intent-driven-minimal-ontology-loading 并给出执行动作 |
| should-trigger-02 | should_trigger | `intent-driven-minimal-ontology-loading` | PASS | 应选择 intent-driven-minimal-ontology-loading 并给出执行动作 |
| should-trigger-03 | should_trigger | `intent-driven-minimal-ontology-loading` | PASS | 应选择 intent-driven-minimal-ontology-loading 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `ontology-constraint-and-knowledge-injection` | PASS | 应选择兄弟 Skill ontology-constraint-and-knowledge-injection |
| edge-01 | edge_case | `none` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：只加载当前需要的本体？请结合一个企业业务场景给我可执行结果。
- 理由：用户明确要求只加载当前任务所需本体，直接命中最小本体加载场景。
- 计划动作：识别业务意图，确定应加载的最小子本体、检索范围、路由条件和兜底机制，并给出企业场景执行清单。

### should-trigger-02 — PASS

- Prompt：我现在同一问法可能对应不同业务意图，这个意图该路由到哪个子本体？
- 理由：同一问法对应多个业务意图，且需要路由到子本体，正是意图驱动加载问题。
- 计划动作：先澄清和判定意图，再设计子本体路由规则、置信度阈值、冲突处理和人工确认点。

### should-trigger-03 — PASS

- Prompt：Please help with minimal ontology and provide a concrete enterprise checklist.
- 理由：minimal ontology 是该 Skill 的直接触发信号，且用户要求企业级可执行清单。
- 计划动作：输出意图识别、最小知识范围、混合检索、上下文装载、路由校验和监控指标清单。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：用户只询问三个技术术语的英文全称和简短释义，不涉及意图路由或本体加载。
- 计划动作：直接给出 RDF、OWL、SPARQL 的英文全称和一句话释义。

### should-not-trigger-02 — PASS

- Prompt：Prompt RAG 微调怎么选？请直接按那个方法给出步骤。
- 理由：问题核心是 Prompt、RAG 与微调的知识注入方式选择，直接命中知识注入 Skill。
- 计划动作：按知识稳定性、更新频率、规则强度、可解释性和成本比较三种方式，并给出选型步骤。

### edge-01 — PASS

- Prompt：当前情况是：任务需要全域审计或全局一致性检查。我还能直接用这个方法吗？
- 理由：全域审计和全局一致性检查通常需要完整覆盖，单凭该描述无法确定具体审查对象，也不适合直接采用最小本体加载。
- 计划动作：先澄清审计对象、覆盖范围和一致性标准，再判断是否需要完整本体或专门的质量审查流程。

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
