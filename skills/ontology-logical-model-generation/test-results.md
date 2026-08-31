# ontology-logical-model-generation — 路由测试记录

- **测试范围**：形式化生成、语义前置、独立质量审查和候选隔离
- **检查方式**：人工路由复核与仓库结构校验
- **结果**：5/5 设计预期明确
- **独立行为盲测**：待下一轮跨平台抽样执行

| Case | 预期路由 | 关键检查 |
|---|---|---|
| should-trigger-01 | ontology-logical-model-generation | TTL、SHACL和查询 |
| should-trigger-02 | ontology-logical-model-generation | 形式化与追溯 |
| should-not-trigger-01 | scenario-related-semantic-modeling | 业务语义裁决 |
| should-not-trigger-02 | ontology-model-multilayer-quality-gate | 独立审查 |
| edge-01 | ontology-logical-model-generation | 候选隔离 |
