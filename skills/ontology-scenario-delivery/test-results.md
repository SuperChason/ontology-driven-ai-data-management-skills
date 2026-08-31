# ontology-scenario-delivery — 路由测试记录

- **测试范围**：2 条正向、2 条反向、1 条低成熟度边界用例
- **检查方式**：人工路由复核与仓库结构校验
- **结果**：5/5 设计预期明确
- **独立行为盲测**：待下一轮跨平台抽样执行

| Case | 预期路由 | 关键检查 |
|---|---|---|
| should-trigger-01 | ontology-scenario-delivery | 编排全链路和建设包 |
| should-trigger-02 | ontology-scenario-delivery | 输出缺口与追溯 |
| should-not-trigger-01 | scenario-agent-role-design | 避免总控吞掉单阶段任务 |
| should-not-trigger-02 | none | 术语问答直接回答 |
| edge-01 | ontology-scenario-delivery | 候选状态和资料缺口 |

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
