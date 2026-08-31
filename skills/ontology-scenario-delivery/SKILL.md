---
name: ontology-scenario-delivery
description: |
  用于用户拿到一个企业业务场景，希望从本体适配、智能体作用、场景梳理、数据需求、知识结构和语义模型一路推进到逻辑本体、实例、验证与发布，用户出现“按这个场景生成完整本体建设包”“直接指导这个本体怎么落地”或 scenario-to-ontology delivery, ontology work package 等信号时调用。不适用于只询问某个本体术语或只需要单阶段专项产物。
metadata:
  tags: "orchestration, scenario-delivery, ontology-work-package, artifact-chain, traceability, enterprise-ai, ontology-driven"
  related-skills: "ontology-ai-scenario-fit-and-spike:depends-on, scenario-agent-role-design:orchestrates, business-scenario-deep-analysis:orchestrates, scenario-data-requirements-readiness:orchestrates, scenario-related-knowledge-structure:orchestrates, scenario-related-semantic-modeling:orchestrates, ontology-conceptual-model-design:orchestrates, ontology-logical-model-generation:orchestrates, data-to-ontology-mapping-and-instantiation:orchestrates"
---

# 场景驱动的本体建设交付

## 方法骨架

- 以一个可验证的业务场景为入口，先判断本体是否必要，再确定智能体在场景中的作用。
- 在正式建模前完成场景深描、数据需求与准备度判断，避免根据一段场景描述直接生成生产本体。
- 场景相关的知识结构负责知识来源、证据、责任和复用资产；场景相关的语义模型负责统一对象、术语、关系、约束、规则、状态、权限、动作和目标。
- 概念模型用于业务审查，逻辑本体用于机器处理，数据到本体的映射用于把已确认语义的数据生成类实例、属性值和关系实例。
- 全程维护“来源—知识条目—语义元素—模型元素—实例—测试—运行结果”的追溯链。
- 资料不足时生成候选成果和补充清单，状态保持为候选或受阻，不补造企业事实。

## 路由方式

先读取 [端到端建设链路](references/end-to-end-workflow.md)。需要生成完整交付目录或检查缺失产物时，再读取 [场景本体建设包](references/deliverable-package.md)。需要理解各阶段怎样连续交接时，可以读取 [通用示例：进度变化与预算影响](references/example-progress-budget.md)。

### 单阶段请求

用户只要求一个环节时，路由到对应专业 Skill，不强制执行整条链路。

### 全链路请求

用户希望从场景一路形成可交付本体时，本 Skill 负责阶段判断、专业 Skill 调用、产物索引、状态管理和追溯汇总。

## 执行步骤

1. **建立建设清单**
   - 动作：记录场景、目标、材料、系统、样本、已有模型和期望交付，标记已确认、候选、缺失与受阻。
   - 完成标准：形成输入清单、当前成熟度和下一阶段判断。

2. **通过场景与智能体决策门**
   - 动作：调用本体适配 Skill 初判路线，随后识别智能体任务、系统能力和人工责任。
   - 完成标准：明确本体支撑哪些智能体任务以及首个闭环范围。
   - 判停条件：场景可由简单查询、固定规则或普通工作流低成本完成时，输出轻量替代路线。

3. **完成建模前准备**
   - 动作：依次完成场景深描、业务/财务/IT 数据需求与准备度、知识来源与证据盘点。
   - 完成标准：每项关键判断都有所需数据、知识来源、责任人和缺口状态。

4. **建设语义与模型**
   - 动作：先统一场景语义，再形成概念模型和逻辑本体；未经确认的语义保持候选状态。
   - 完成标准：智能体任务所需的对象、关系、约束、规则、权限、动作和完成条件均有模型表达。

5. **连接数据并验证**
   - 动作：把已完成语义定义的数据映射到本体类、属性、关系和实例，随后执行技术验证和黄金用例。
   - 完成标准：真实样本能够形成有效实例并得到可解释、可复核的预期结果。

6. **发布与回流**
   - 动作：完成资产登记、版本、服务、Agent 绑定、灰度和回滚；把运行缺口送回对应建设阶段。
   - 完成标准：生产版本可唯一定位，运行反馈能追溯并触发回归验证。

## 固定输出

- 建设清单与产物索引
- 当前阶段和准入结论
- 已完成产物、缺失产物与阻断项
- 场景本体建设包或可复制的分文件内容
- 端到端追溯矩阵
- 下一阶段调用顺序和完成标准

每个关键条目至少包含唯一编号、场景/任务、定义、来源、证据、状态、责任人、适用范围和版本。状态统一使用：候选、有证据、已确认、已验证、受阻、已废弃。

## 使用边界

- 只有场景描述时，交付场景卡、候选框架和资料缺口，不声称逻辑模型可发布。
- 真实系统表字段的定位在数据需求与准备度阶段完成；数据到本体映射阶段直接复用该成果。
- 模型语法通过只代表技术可解析，生产准入还需要业务专家和真实用例验证。
- 高风险动作需要权限、前置条件、人工授权、失败处理和审计记录。

## 相关 Skills

- `depends-on` → `ontology-ai-scenario-fit-and-spike`。
- `orchestrates` → 八个施工型 Skill；具体顺序和返回条件见端到端建设链路。
- 模型完成后组合 `ontology-model-multilayer-quality-gate`、`ontology-golden-case-testing` 和 `ontology-runtime-service-and-version-operations`。

## 审计信息

- **首次公开版本**：2026-08-31
- **来源说明**：方法框架受《本体驱动的 AI 数据管理》启发，并结合场景化本体工程实践独立整理；仓库不包含原书正文。
