# ontology-conceptual-model-design — 路由测试记录

- **测试范围**：专家视图、语义前置、逻辑生成和复杂图拆分
- **检查方式**：人工路由复核与仓库结构校验
- **结果**：5/5 设计预期明确
- **独立行为盲测**：待下一轮跨平台抽样执行

| Case | 预期路由 | 关键检查 |
|---|---|---|
| should-trigger-01 | ontology-conceptual-model-design | 多视图业务模型 |
| should-trigger-02 | ontology-conceptual-model-design | 跨视图一致性 |
| should-not-trigger-01 | ontology-logical-model-generation | 机器形式化 |
| should-not-trigger-02 | scenario-related-semantic-modeling | 语义定义 |
| edge-01 | ontology-conceptual-model-design | 分视图审查 |
