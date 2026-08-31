# ontology-runtime-service-and-version-operations — Stage 4 压力测试结果

- **评测方式**：独立 sub-agent 盲测
- **历史可见信息**：v0.1.0 的 16 个 Skill name + description、用户 prompt
- **当前状态**：v0.4.0 已增加明确输出契约；既有路由盲测结论保留，跨平台行为继续按版本抽样
- **隐藏信息**：case 类型、预期行为、备注和通过标准
- **通过率**：6/6（100%）
- **诱饵测试**：全部通过
- **结论**：接受

| Case | 类型 | 盲测选择 | 结果 | 判定标准 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | `ontology-runtime-service-and-version-operations` | PASS | 应选择 ontology-runtime-service-and-version-operations 并给出执行动作 |
| should-trigger-02 | should_trigger | `ontology-runtime-service-and-version-operations` | PASS | 应选择 ontology-runtime-service-and-version-operations 并给出执行动作 |
| should-trigger-03 | should_trigger | `ontology-runtime-service-and-version-operations` | PASS | 应选择 ontology-runtime-service-and-version-operations 并给出执行动作 |
| should-not-trigger-01 | should_not_trigger | `none` | PASS | 纯信息诱饵应选择 none |
| should-not-trigger-02 | should_not_trigger | `intent-driven-minimal-ontology-loading` | PASS | 应选择兄弟 Skill intent-driven-minimal-ontology-loading |
| edge-01 | edge_case | `none` | PASS | 应识别边界；可选择目标Skill做边界判定，也可路由兄弟Skill或none，禁止直接执行完整流程 |

## 盲测理由与动作

### should-trigger-01 — PASS

- Prompt：怎么做本体即服务？请结合一个企业业务场景给我可执行结果。
- 理由：明确要求设计“本体即服务”，与该 Skill 的服务化供给场景直接匹配。
- 计划动作：结合企业场景给出服务边界、调用接口、权限、版本治理、监控和验收清单。

### should-trigger-02 — PASS

- Prompt：我现在业务规则存在多版本并行和灰度发布，本体版本如何灰度和回滚？
- 理由：业务规则多版本并行、灰度发布及回滚正是本体运行时版本治理问题。
- 计划动作：设计版本标识、兼容策略、灰度范围、回滚条件、审计记录和发布流程。

### should-trigger-03 — PASS

- Prompt：Please help with ontology as a service and provide a concrete enterprise checklist.
- 理由：提示明确提出 ontology as a service，并要求企业级落地清单。
- 计划动作：输出从准入条件、服务封装、调用治理到版本运维的企业检查清单。

### should-not-trigger-01 — PASS

- Prompt：请告诉我 RDF、OWL 和 SPARQL 的英文全称，只需要简短释义。
- 理由：仅查询 RDF、OWL、SPARQL 的英文全称和简短释义，属于术语信息查询。
- 计划动作：不激活 Skill，直接给出三个术语的全称与一句话释义。

### should-not-trigger-02 — PASS

- Prompt：只加载当前需要的本体？请直接按那个方法给出步骤。
- 理由：“只加载当前需要的本体”直接对应按意图路由并最小化加载本体。
- 计划动作：先澄清业务意图，再定义子本体路由、最小知识包、混合检索和路由失败处理。

### edge-01 — PASS

- Prompt：当前情况是：直接另建一套身份权限体系。我还能直接用这个方法吗？
- 理由：提示只说明另建身份权限体系，且“这个方法”指代不明，缺少本体已验收、服务化或版本治理信息。
- 计划动作：不激活 Skill；先澄清所指方法，并评估复用现有身份权限体系及其集成边界。

## v0.4.0 输出契约校验

- **固定输出章节**：PASS，唯一二级章节
- **明确交付物**：PASS，至少 3 项具名成果
- **泛化输出占位**：PASS，未保留通用占位句
- **本地引用解析**：PASS
- **测试版本**：0.4.0
