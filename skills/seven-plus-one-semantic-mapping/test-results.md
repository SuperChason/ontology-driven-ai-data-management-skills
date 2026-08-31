# seven-plus-one-semantic-mapping — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.4.0 已增加明确输出契约；既有路由盲测结论保留，跨平台行为继续按版本抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `seven-plus-one-semantic-mapping` | PASS | 应选择 seven-plus-one-semantic-mapping 并给出执行动作 |
| should-trigger-02 | should_trigger | `seven-plus-one-semantic-mapping` | PASS | 应选择 seven-plus-one-semantic-mapping 并给出执行动作 |
| should-trigger-03 | should_trigger | `seven-plus-one-semantic-mapping` | PASS | 应选择 seven-plus-one-semantic-mapping 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `twenty-nine-sentence-knowledge-extraction` | PASS | 应选择兄弟 Skill twenty-nine-sentence-knowledge-extraction |
| edge-01 | edge_case | `none` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：按7+1映射一下？请结合一个企业业务场景给我可执行结果。
- 理由：明确要求按 7+1 映射企业业务场景，直接命中该 Skill。
- 计划动作：按 7+1 框架映射业务对象、事实、规则、角色权限、动作及相关语义。

### should-trigger-02 — PASS

- Prompt：我现在要检查Agent知识、规则、权限和动作是否完整，这个场景缺哪些语义？
- 理由：需要检查 Agent 的知识、规则、权限和动作是否完整，正是 7+1 语义完整性检查场景。
- 计划动作：逐项盘点现有语义，标出缺失、冲突、来源和责任人，并形成补齐清单。

### should-trigger-03 — PASS

- Prompt：Please help with 7+1 semantic mapping and provide a concrete enterprise checklist.
- 理由：明确提出 7+1 semantic mapping 和企业检查清单，与该 Skill 完全一致。
- 计划动作：输出 7+1 语义映射检查清单，并据此完成企业场景映射。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：仅查询 RDF、OWL 和 SPARQL 的基础释义，无需进行场景语义映射。
- 计划动作：不激活 Skill，直接提供简短术语说明。

### should-not-trigger-02 — PASS

- Prompt：怎么访谈业务专家？请直接按那个方法给出步骤。
- 理由：请求重点是访谈业务专家，最适合采用结构化知识提取 Skill。
- 计划动作：设计专家访谈并用结构化句式提取、核对和确认业务知识。

### edge-01 — PASS

- Prompt：当前情况是：只做概念科普，无需机器推理或行动。我还能直接用这个方法吗？
- 理由：任务仅做概念科普，且无需机器推理或行动，缺少 7+1 语义映射的使用目标。
- 计划动作：不激活 Skill，直接按受众需要解释相关概念。

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
