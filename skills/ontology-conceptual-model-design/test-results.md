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

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
