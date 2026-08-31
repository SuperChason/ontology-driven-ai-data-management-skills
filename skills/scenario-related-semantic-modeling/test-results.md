# scenario-related-semantic-modeling — 路由测试记录

- **测试范围**：完整语义、知识来源、逻辑模型和关系类型边界
- **检查方式**：人工路由复核与仓库结构校验
- **结果**：5/5 设计预期明确
- **独立行为盲测**：待下一轮跨平台抽样执行

| Case | 预期路由 | 关键检查 |
|---|---|---|
| should-trigger-01 | scenario-related-semantic-modeling | 对象到目标完整语义 |
| should-trigger-02 | scenario-related-semantic-modeling | 数据业务行动语义 |
| should-not-trigger-01 | scenario-related-knowledge-structure | 来源证据台账 |
| should-not-trigger-02 | ontology-logical-model-generation | RDF/OWL/SHACL |
| edge-01 | scenario-related-semantic-modeling | 组成关系与继承区分 |
