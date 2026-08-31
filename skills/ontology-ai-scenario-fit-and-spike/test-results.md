# ontology-ai-scenario-fit-and-spike — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.3.0 已扩展为 25 个 Skill，需重新执行跨平台行为抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `ontology-ai-scenario-fit-and-spike` | PASS | 应选择 ontology-ai-scenario-fit-and-spike 并给出执行动作 |
| should-trigger-02 | should_trigger | `ontology-ai-scenario-fit-and-spike` | PASS | 应选择 ontology-ai-scenario-fit-and-spike 并给出执行动作 |
| should-trigger-03 | should_trigger | `ontology-ai-scenario-fit-and-spike` | PASS | 应选择 ontology-ai-scenario-fit-and-spike 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `ontology-ai-application-pattern-selection` | PASS | 应选择兄弟 Skill ontology-ai-application-pattern-selection |
| edge-01 | edge_case | `ontology-ai-scenario-fit-and-spike` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：这个场景适合做本体吗？请结合一个企业业务场景给我可执行结果。
- 理由：请求直接判断企业业务场景是否适合采用本体，并要求形成可执行结果，符合场景适配评估的触发条件。
- 计划动作：评估本体必要性、数据与规则条件、预期价值和风险，给出 go/no-go 判断及首个验证切口。

### should-trigger-02 — PASS

- Prompt：我现在项目范围很大，需要确定首个小切口，先做哪个小切口？
- 理由：项目范围过大且需要选择首个小切口，正是该 Skill 的 vertical slice 规划场景。
- 计划动作：比较候选切口的业务价值、复杂度、数据可得性和验证成本，确定首个最小闭环。

### should-trigger-03 — PASS

- Prompt：Please help with ontology fit and provide a concrete enterprise checklist.
- 理由：明确提出 ontology fit，并要求企业级检查清单，与该 Skill 的核心用途完全一致。
- 计划动作：输出企业场景本体适配检查清单，并据此给出可执行的适配结论和验证建议。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：仅查询 RDF、OWL 和 SPARQL 的英文全称及简短释义，属于基础信息查询，无需本体场景评估。
- 计划动作：不激活 Skill，直接提供三个术语的全称和简短释义。

### should-not-trigger-02 — PASS

- Prompt：这个场景属于哪种应用模式？请直接按那个方法给出步骤。
- 理由：请求已经进入本体应用模式分类与步骤选择阶段，最匹配六类应用模式选型 Skill。
- 计划动作：识别该场景对应的本体 AI 应用模式，并按所选模式给出实施步骤。

### edge-01 — PASS

- Prompt：当前情况是：规则和目标持续剧烈变化，建模速度无法跟上。我还能直接用这个方法吗？
- 理由：规则、目标剧烈变化且建模跟不上，直接影响本体路线的可行性，需先做 go/no-go 与最小试点判断。
- 计划动作：评估变化频率、建模维护成本和可稳定语义范围，判断是否暂停、缩小切口或改用更轻量方案。
