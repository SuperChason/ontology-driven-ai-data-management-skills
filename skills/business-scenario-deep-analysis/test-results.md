# business-scenario-deep-analysis — 路由测试记录

- **测试范围**：完整场景规格、前置适配、数据专项和证据边界
- **检查方式**：人工路由复核与仓库结构校验
- **结果**：5/5 设计预期明确
- **独立行为盲测**：待下一轮跨平台抽样执行

| Case | 预期路由 | 关键检查 |
|---|---|---|
| should-trigger-01 | business-scenario-deep-analysis | 端到端场景规格 |
| should-trigger-02 | business-scenario-deep-analysis | 判断、状态和异常 |
| should-not-trigger-01 | ontology-ai-scenario-fit-and-spike | 适配初判 |
| should-not-trigger-02 | scenario-data-requirements-readiness | 数据需求专项 |
| edge-01 | business-scenario-deep-analysis | 假设与证据状态 |
