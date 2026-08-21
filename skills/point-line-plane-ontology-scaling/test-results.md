# point-line-plane-ontology-scaling — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **可见信息**：16 个 Skill 的 name + description、用户 prompt
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `point-line-plane-ontology-scaling` | PASS | 应选择 point-line-plane-ontology-scaling 并给出执行动作 |
| should-trigger-02 | should_trigger | `point-line-plane-ontology-scaling` | PASS | 应选择 point-line-plane-ontology-scaling 并给出执行动作 |
| should-trigger-03 | should_trigger | `point-line-plane-ontology-scaling` | PASS | 应选择 point-line-plane-ontology-scaling 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `ontology-ai-scenario-fit-and-spike` | PASS | 应选择兄弟 Skill ontology-ai-scenario-fit-and-spike |
| edge-01 | edge_case | `none` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：怎么从点扩到线和面？请结合一个企业业务场景给我可执行结果。
- 理由：用户明确提出从点扩到线和面的本体扩展问题，并要求企业场景下的执行方案。
- 计划动作：从已验证单点出发，规划场景链、共享语义层和跨域治理，明确每一级扩展的价值与准入条件。

### should-trigger-02 — PASS

- Prompt：我现在多个局部本体开始重复或冲突，这个本体怎么复用到其他场景？
- 理由：多个局部本体重复冲突和跨场景复用正是本体规模化与联邦治理问题。
- 计划动作：盘点重复概念与冲突规则，划分共享核心和领域边界，设计复用、映射、版本及治理机制。

### should-trigger-03 — PASS

- Prompt：Please help with point-line-plane and provide a concrete enterprise checklist.
- 理由：point-line-plane 与企业级清单直接指向本体从单点验证到跨场景扩展的工作流。
- 计划动作：生成点、线、面三级扩展检查清单，覆盖价值闭环、复用边界、冲突治理和联邦运营。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：请求只是基础术语释义，不涉及本体复用、冲突治理或规模化扩展。
- 计划动作：直接给出三个术语的简短释义。

### should-not-trigger-02 — PASS

- Prompt：这个场景适合做本体吗？请直接按那个方法给出步骤。
- 理由：用户首先要判断场景是否适合本体，应进行适配性评估和小切口验证，尚未进入规模化阶段。
- 计划动作：评估业务复杂度、语义复用、规则推理和可验证价值，给出适用性结论及最小验证切片。

### edge-01 — PASS

- Prompt：当前情况是：为了统一术语而统一，没有跨域任务支撑。我还能直接用这个方法吗？
- 理由：仅为统一术语且缺少跨域任务支撑，没有形成从点到面扩展所需的价值闭环和复用需求。
- 计划动作：先确认真实跨域任务、复用对象和业务价值；当前仅维护必要术语表，不启动本体规模化。
