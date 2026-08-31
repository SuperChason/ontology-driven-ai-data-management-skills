# scenario-agent-role-design — 路由测试记录

- **测试范围**：Agent 作用、三方分工、相邻 Action 与建模请求
- **检查方式**：人工路由复核与仓库结构校验
- **结果**：5/5 设计预期明确
- **独立行为盲测**：待下一轮跨平台抽样执行

| Case | 预期路由 | 关键检查 |
|---|---|---|
| should-trigger-01 | scenario-agent-role-design | 作用、任务和边界 |
| should-trigger-02 | scenario-agent-role-design | 人工接管点 |
| should-not-trigger-01 | action-contract-execution-feedback-loop | 具体执行契约 |
| should-not-trigger-02 | ontology-logical-model-generation | 逻辑模型生成 |
| edge-01 | scenario-agent-role-design | 候选状态 |
