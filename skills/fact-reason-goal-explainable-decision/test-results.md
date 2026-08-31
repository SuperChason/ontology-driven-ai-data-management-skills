# fact-reason-goal-explainable-decision — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.4.0 已增加明确输出契约；既有路由盲测结论保留，跨平台行为继续按版本抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `fact-reason-goal-explainable-decision` | PASS | 应选择 fact-reason-goal-explainable-decision 并给出执行动作 |
| should-trigger-02 | should_trigger | `fact-reason-goal-explainable-decision` | PASS | 应选择 fact-reason-goal-explainable-decision 并给出执行动作 |
| should-trigger-03 | should_trigger | `fact-reason-goal-explainable-decision` | PASS | 应选择 fact-reason-goal-explainable-decision 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `fact-reason-action-business-loop` | PASS | 应选择兄弟 Skill fact-reason-action-business-loop |
| edge-01 | edge_case | `none` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：按事实事理目标分析？请结合一个企业业务场景给我可执行结果。
- 理由：用户明确要求按事实、事理、目标进行分析，直接命中可解释决策方法。
- 计划动作：选取企业决策场景，分别整理事实、规则与约束、目标及权衡，形成可追溯的判断和行动建议。

### should-trigger-02 — PASS

- Prompt：我现在实时事实、业务规则和多个目标需要综合决策，这个决策依据是什么？
- 理由：实时事实、业务规则和多个目标的综合决策及依据解释是该 Skill 的核心适用范围。
- 计划动作：建立事实证据、规则推理、目标权重和冲突权衡链路，输出决策结论及可追溯依据。

### should-trigger-03 — PASS

- Prompt：Please help with fact-reason-goal and provide a concrete enterprise checklist.
- 理由：fact-reason-goal 是直接触发信号，用户还要求企业级具体检查清单。
- 计划动作：给出事实可信度、规则适用性、目标优先级、冲突权衡、结论解释和审计留痕清单。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：用户只要技术术语的英文全称和简短释义，不存在业务决策或目标权衡。
- 计划动作：直接给出 RDF、OWL、SPARQL 的英文全称和简要定义。

### should-not-trigger-02 — PASS

- Prompt：帮我按事实事理行动拆解？请直接按那个方法给出步骤。
- 理由：用户明确要求按事实、事理、行动拆解，应进入业务闭环建模 Skill。
- 计划动作：把业务描述拆成可验证事实、判断依据和系统行动，补充反馈与追溯关系，形成执行步骤。

### edge-01 — PASS

- Prompt：当前情况是：纯创意、审美或情感判断。我还能直接用这个方法吗？
- 理由：纯创意、审美或情感判断缺少明确事实来源、业务规则和可权衡目标，不适合直接套用该决策方法。
- 计划动作：先明确评价主体、偏好标准和期望结果；若仍属于主观创作，可直接采用创意评议方式。

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
