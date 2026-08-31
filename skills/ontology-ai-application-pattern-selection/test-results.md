# ontology-ai-application-pattern-selection — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.4.0 已增加明确输出契约；既有路由盲测结论保留，跨平台行为继续按版本抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `ontology-ai-application-pattern-selection` | PASS | 应选择 ontology-ai-application-pattern-selection 并给出执行动作 |
| should-trigger-02 | should_trigger | `ontology-ai-application-pattern-selection` | PASS | 应选择 ontology-ai-application-pattern-selection 并给出执行动作 |
| should-trigger-03 | should_trigger | `ontology-ai-application-pattern-selection` | PASS | 应选择 ontology-ai-application-pattern-selection 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `ontology-ai-scenario-fit-and-spike` | PASS | 应选择兄弟 Skill ontology-ai-scenario-fit-and-spike |
| edge-01 | edge_case | `none` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：这个场景属于哪种应用模式？请结合一个企业业务场景给我可执行结果。
- 理由：明确询问场景所属应用模式，并要求结合企业场景形成可执行结果。
- 计划动作：确认场景已具备本体适用性后，对照应用模式选择架构并给出实施与验收建议。

### should-trigger-02 — PASS

- Prompt：我现在问答、审核、协同、决策和PDCA方案混在一起，六类模式怎么选？
- 理由：问答、审核、协同、决策和 PDCA 方案混杂，正需用应用模式选择方法完成归类取舍。
- 计划动作：按业务目标、闭环深度、动作权限和反馈机制比较六类模式，确定主模式及组合边界。

### should-trigger-03 — PASS

- Prompt：Please help with application pattern and provide a concrete enterprise checklist.
- 理由：提示明确要求 application pattern 的企业级选择清单。
- 计划动作：输出模式选择所需的前置条件、判定维度、架构选择、风险和验收清单。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：仅需 RDF、OWL、SPARQL 的基础术语释义，不涉及应用模式选择。
- 计划动作：不激活 Skill，直接简短回答术语全称和含义。

### should-not-trigger-02 — PASS

- Prompt：这个场景适合做本体吗？请直接按那个方法给出步骤。
- 理由：问题处于判断场景是否适合本体的前置阶段，应先做场景适配和小切口选择。
- 计划动作：评估业务复杂度、语义关系、推理与行动需求、现有能力替代性，并给出 go/no-go 和首个切口。

### edge-01 — PASS

- Prompt：当前情况是：纯信息问答可由普通检索满足。我还能直接用这个方法吗？
- 理由：纯信息问答已可由普通检索满足，缺少引入本体及选择本体应用模式的必要性。
- 计划动作：不激活 Skill，优先沿用普通检索；需求出现复杂语义、规则推理或行动闭环后再评估本体。

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
