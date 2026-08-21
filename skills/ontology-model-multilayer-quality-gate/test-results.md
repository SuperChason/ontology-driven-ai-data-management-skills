# ontology-model-multilayer-quality-gate — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **可见信息**：16 个 Skill 的 name + description、用户 prompt
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `ontology-model-multilayer-quality-gate` | PASS | 应选择 ontology-model-multilayer-quality-gate 并给出执行动作 |
| should-trigger-02 | should_trigger | `ontology-model-multilayer-quality-gate` | PASS | 应选择 ontology-model-multilayer-quality-gate 并给出执行动作 |
| should-trigger-03 | should_trigger | `ontology-model-multilayer-quality-gate` | PASS | 应选择 ontology-model-multilayer-quality-gate 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `ontology-golden-case-testing` | PASS | 应选择兄弟 Skill ontology-golden-case-testing |
| edge-01 | edge_case | `none` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：帮我做本体质量审查？请结合一个企业业务场景给我可执行结果。
- 理由：用户明确提出本体质量审查，并要求结合企业场景给出可执行结果。
- 计划动作：建立分层质量门，对模型的形式正确性、语义一致性、业务有效性和生产可用性进行审查。

### should-trigger-02 — PASS

- Prompt：我现在准备评审本体模型质量和生产准入，双模型怎么校验？
- 理由：模型质量评审、生产准入和双模型校验均是该 Skill 的核心触发信号。
- 计划动作：设计生成模型与独立审核模型的职责分离、检查维度、证据记录、人工裁决和准入阈值。

### should-trigger-03 — PASS

- Prompt：Please help with ontology quality gate and provide a concrete enterprise checklist.
- 理由：ontology quality gate 与企业级检查清单直接对应本体模型多层质量审查。
- 计划动作：输出可执行的本体质量门清单，包含审查项、证据、责任人、缺陷等级和放行标准。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：用户只要术语释义，没有模型审查、语义校验或生产准入需求。
- 计划动作：直接简要解释三个术语，不启动专门工作流。

### should-not-trigger-02 — PASS

- Prompt：帮我设计本体测试用例？请直接按那个方法给出步骤。
- 理由：用户要设计本体测试用例，任务重心是真实业务问题验收与用例矩阵。
- 计划动作：建立黄金问题集、期望答案、事实与规则覆盖、版本回归矩阵和通过标准。

### edge-01 — PASS

- Prompt：当前情况是：输入知识来源不明或业务冲突尚未裁决。我还能直接用这个方法吗？
- 理由：知识来源不明且业务冲突尚未裁决，模型质量审查缺少可信依据，现阶段无法直接应用质量门。
- 计划动作：先补齐来源、责任人和证据，完成业务冲突裁决；条件具备后再进行独立质量审查。
