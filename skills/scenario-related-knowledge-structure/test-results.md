# scenario-related-knowledge-structure — 路由测试记录

- **测试范围**：知识来源、证据、复用、语义定义和数据物理来源边界
- **检查方式**：人工路由复核与仓库结构校验
- **结果**：5/5 设计预期明确
- **独立行为盲测**：待下一轮跨平台抽样执行

| Case | 预期路由 | 关键检查 |
|---|---|---|
| should-trigger-01 | scenario-related-knowledge-structure | 来源、责任和缺口 |
| should-trigger-02 | scenario-related-knowledge-structure | 证据台账 |
| should-not-trigger-01 | scenario-related-semantic-modeling | 对象关系约束 |
| should-not-trigger-02 | scenario-data-requirements-readiness | 系统表字段 |
| edge-01 | scenario-related-knowledge-structure | 禁止无证据确认 |

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
