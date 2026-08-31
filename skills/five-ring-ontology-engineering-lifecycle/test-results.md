# five-ring-ontology-engineering-lifecycle — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.3.0 已扩展为 25 个 Skill，需重新执行跨平台行为抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `five-ring-ontology-engineering-lifecycle` | PASS | 应选择 five-ring-ontology-engineering-lifecycle 并给出执行动作 |
| should-trigger-02 | should_trigger | `five-ring-ontology-engineering-lifecycle` | PASS | 应选择 five-ring-ontology-engineering-lifecycle 并给出执行动作 |
| should-trigger-03 | should_trigger | `five-ring-ontology-engineering-lifecycle` | PASS | 应选择 five-ring-ontology-engineering-lifecycle 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `ontology-model-multilayer-quality-gate` | PASS | 应选择兄弟 Skill ontology-model-multilayer-quality-gate |
| edge-01 | edge_case | `ontology-ai-scenario-fit-and-spike` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：按五环规划实施？请结合一个企业业务场景给我可执行结果。
- 理由：用户明确要求按五环规划企业本体建设，并需要可执行结果，直接命中该 Skill 的实施规划场景。
- 计划动作：围绕具体企业场景输出五个阶段的目标、关键任务、责任角色、阶段产出、质量门和运营机制。

### should-trigger-02 — PASS

- Prompt：我现在已有模型原型但缺少上线和运营路径，本体项目需要哪些阶段和产出？
- 理由：已有模型原型、需要补齐上线与运营路径，正是从原型走向生产的全生命周期规划问题。
- 计划动作：评估原型现状，规划建模、验证、服务化上线和持续运营阶段，并列出每阶段交付物与准入条件。

### should-trigger-03 — PASS

- Prompt：Please help with ontology lifecycle and provide a concrete enterprise checklist.
- 理由：ontology lifecycle 与企业检查清单明确对应本体工程生命周期 Skill。
- 计划动作：生成企业级本体生命周期检查清单，覆盖阶段活动、产物、角色、质量门和生产就绪要求。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：请求只涉及三个技术术语的英文全称和简短释义，不需要本体工程规划类工作流。
- 计划动作：直接给出 RDF、OWL、SPARQL 的英文全称及一句话释义。

### should-not-trigger-02 — PASS

- Prompt：帮我做本体质量审查？请直接按那个方法给出步骤。
- 理由：核心任务是本体模型质量审查，明确命中多层质量门，而非生命周期规划。
- 计划动作：按语法、结构、语义、业务一致性和生产准入维度审查模型，并给出问题等级与整改结论。

### edge-01 — PASS

- Prompt：当前情况是：没有明确业务场景却先建设大而全平台。我还能直接用这个方法吗？
- 理由：当前缺少明确业务场景且平台范围过大，应先判断本体适配性并收敛首个小切口。
- 计划动作：暂停大而全建设，开展场景适配评估，选择可验证的垂直切片并设定 go/no-go 标准。
