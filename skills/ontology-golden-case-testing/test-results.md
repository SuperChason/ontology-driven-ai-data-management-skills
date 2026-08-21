# ontology-golden-case-testing — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **可见信息**：16 个 Skill 的 name + description、用户 prompt
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `ontology-golden-case-testing` | PASS | 应选择 ontology-golden-case-testing 并给出执行动作 |
| should-trigger-02 | should_trigger | `ontology-golden-case-testing` | PASS | 应选择 ontology-golden-case-testing 并给出执行动作 |
| should-trigger-03 | should_trigger | `ontology-golden-case-testing` | PASS | 应选择 ontology-golden-case-testing 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `ontology-model-multilayer-quality-gate` | PASS | 应选择兄弟 Skill ontology-model-multilayer-quality-gate |
| edge-01 | edge_case | `none` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：帮我设计本体测试用例？请结合一个企业业务场景给我可执行结果。
- 理由：用户明确要求设计本体测试用例并落到企业场景，直接命中黄金用例测试。
- 计划动作：从真实业务问题提炼黄金用例，定义输入、期望答案、证据、覆盖规则、异常场景和验收阈值。

### should-trigger-02 — PASS

- Prompt：我现在本体规则或版本变化后要做回归，怎么做黄金问题集？
- 理由：本体规则或版本变化后的回归与黄金问题集是该 Skill 的典型使用场景。
- 计划动作：建立基线黄金问题集和版本回归矩阵，比较答案、推理路径、证据和动作结果的变化。

### should-trigger-03 — PASS

- Prompt：Please help with golden cases and provide a concrete enterprise checklist.
- 理由：golden cases 和企业级检查清单明确指向本体业务验收与回归测试。
- 计划动作：输出黄金用例建设清单，覆盖问题分层、标准答案、证据来源、覆盖度、执行和回归管理。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：这是一项简短术语查询，没有业务验收、黄金问题或回归测试需求。
- 计划动作：直接提供术语全称和简短释义。

### should-not-trigger-02 — PASS

- Prompt：帮我做本体质量审查？请直接按那个方法给出步骤。
- 理由：用户明确要求本体质量审查，应先按模型质量门检查形式、语义和业务质量。
- 计划动作：执行多层模型审查，输出缺陷、证据、整改建议和生产准入结论。

### edge-01 — PASS

- Prompt：当前情况是：没有稳定业务预期或专家无法确认答案。我还能直接用这个方法吗？
- 理由：黄金用例依赖稳定业务预期和可确认的标准答案，当前两个前提均缺失。
- 计划动作：先明确业务预期并找到有权专家确认答案，再构建黄金问题集和回归基线。
