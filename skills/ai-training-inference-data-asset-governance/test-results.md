# ai-training-inference-data-asset-governance — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.3.0 已扩展为 25 个 Skill，需重新执行跨平台行为抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `ai-training-inference-data-asset-governance` | PASS | 应选择 ai-training-inference-data-asset-governance 并给出执行动作 |
| should-trigger-02 | should_trigger | `ai-training-inference-data-asset-governance` | PASS | 应选择 ai-training-inference-data-asset-governance 并给出执行动作 |
| should-trigger-03 | should_trigger | `ai-training-inference-data-asset-governance` | PASS | 应选择 ai-training-inference-data-asset-governance 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `seven-plus-one-semantic-mapping` | PASS | 应选择兄弟 Skill seven-plus-one-semantic-mapping |
| edge-01 | edge_case | `ai-training-inference-data-asset-governance` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：AI数据资产怎么分类？请结合一个企业业务场景给我可执行结果。
- 理由：明确询问 AI 数据资产分类及企业场景落地，直接符合该 Skill。
- 计划动作：按资产类型、来源、用途、责任人、血缘、质量和生命周期给出分类方案与执行清单。

### should-trigger-02 — PASS

- Prompt：我现在训练数据、实时事实、规则和推理结果混在一起，训练和推理数据怎么分？
- 理由：训练数据、实时事实、规则和推理结果混杂，正需进行训练与推理数据资产分治和溯源治理。
- 计划动作：划分训练资产、运行时事实、规则知识和推理产物，并定义血缘、版本、访问和留存要求。

### should-trigger-03 — PASS

- Prompt：Please help with AI data assets and provide a concrete enterprise checklist.
- 理由：提示明确要求 AI data assets 的企业级检查清单。
- 计划动作：输出覆盖分类目录、来源证明、责任归属、质量、安全、版本和消费管理的清单。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：仅需本体技术术语的全称和简短释义，不涉及 AI 数据资产分类或治理。
- 计划动作：不激活 Skill，直接完成术语释义。

### should-not-trigger-02 — PASS

- Prompt：按7+1映射一下？请直接按那个方法给出步骤。
- 理由：用户明确要求按 7+1 方法映射，直接命中 7+1 语义映射 Skill。
- 计划动作：按 7+1 维度映射场景语义，并标注缺失的知识、规则、权限、动作及责任信息。

### edge-01 — PASS

- Prompt：当前情况是：资产消费者和责任人尚未明确。我还能直接用这个方法吗？
- 理由：资产消费者和责任人未明确是 AI 数据资产治理的关键缺口，适合用该 Skill 先补齐治理前提。
- 计划动作：先识别资产消费者、生产者和责任人，再开展分类、目录、血缘、权限及生命周期治理。
