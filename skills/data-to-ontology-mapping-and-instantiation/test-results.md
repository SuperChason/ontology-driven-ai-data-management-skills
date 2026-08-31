# data-to-ontology-mapping-and-instantiation — 路由测试记录

- **测试范围**：类属性映射、来源定位、语义定义和生产实例边界
- **检查方式**：人工路由复核与仓库结构校验
- **结果**：5/5 设计预期明确
- **独立行为盲测**：待下一轮跨平台抽样执行

| Case | 预期路由 | 关键检查 |
|---|---|---|
| should-trigger-01 | data-to-ontology-mapping-and-instantiation | 数据到类和属性 |
| should-trigger-02 | data-to-ontology-mapping-and-instantiation | 实例来源和版本 |
| should-not-trigger-01 | scenario-data-requirements-readiness | 需求和表字段定位 |
| should-not-trigger-02 | scenario-related-semantic-modeling | 业务语义定义 |
| edge-01 | data-to-ontology-mapping-and-instantiation | 禁止无来源实例 |
