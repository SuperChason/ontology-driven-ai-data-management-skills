# scenario-data-requirements-readiness — 路由测试记录

- **测试范围**：三类数据、来源定位、准备度与本体映射边界
- **检查方式**：人工路由复核与仓库结构校验
- **结果**：5/5 设计预期明确
- **独立行为盲测**：待下一轮跨平台抽样执行

| Case | 预期路由 | 关键检查 |
|---|---|---|
| should-trigger-01 | scenario-data-requirements-readiness | 任务数据矩阵和表字段 |
| should-trigger-02 | scenario-data-requirements-readiness | 质量权限和缺口 |
| should-not-trigger-01 | data-to-ontology-mapping-and-instantiation | 类与实例映射 |
| should-not-trigger-02 | scenario-related-semantic-modeling | 业务语义定义 |
| edge-01 | scenario-data-requirements-readiness | 禁止虚报就绪 |

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
