---
name: scenario-agent-role-design
description: |
  用于业务场景已初步明确，需要判断智能体能帮助哪一部分、在场景中发挥什么作用，并划分Agent、确定性系统和人工职责，用户出现“这个场景智能体能做什么”“先识别Agent的作用”或 agent role in scenario, human-system-agent boundary 等信号时调用。不适用于已经确定Agent任务、只需设计具体Action契约。
metadata:
  tags: "agent-role, task-identification, value-positioning, responsibility-boundary, human-in-the-loop, enterprise-ai, ontology-driven"
  related-skills: "ontology-ai-scenario-fit-and-spike:depends-on, business-scenario-deep-analysis:feeds-into, risk-based-agent-action-modes:composes-with"
---

# 识别场景中的智能体作用与任务

## 方法骨架

- 从场景目标、当前工作和关键困难出发，识别智能体可以承担的理解、检索、关联、判断、生成、协调与受控执行任务。
- 对每项任务分别判断智能体价值、确定性系统能力和人工责任，不因使用本体而预设必须建设 Agent。
- 智能体任务应落到明确用户、触发、输入、输出、完成条件和失败处理。
- 数据计算、固定校验和事务控制优先交给确定性系统；高风险决定和责任承担保留人工确认。
- 输出的知识与数据需求作为后续场景深描、数据需求和本体范围的输入。

## 执行步骤

1. **建立场景最小认识**
   - 动作：确认用户、问题、目标结果、现有过程和已知系统。
   - 完成标准：能够描述谁在什么情况下需要什么帮助。

2. **拆解工作与判断**
   - 动作：列出当前人工任务、信息处理、判断节点、系统操作、异常和协同环节。
   - 完成标准：每项工作有执行者、输入、输出和主要困难。

3. **识别 Agent 候选任务**
   - 动作：判断智能体能否承担信息提取、意图识别、知识检索、跨源关联、规则解释、方案生成、任务协调或工具调用。
   - 完成标准：每个候选任务写清价值、所需能力、数据与知识依赖。

4. **划分三方边界**
   - 动作：明确 Agent、确定性系统和人工分别负责什么，以及交接条件。
   - 完成标准：计算、判断、审批、执行和责任归属无重叠空白。

5. **确定风险和成功条件**
   - 动作：评估错误后果、可逆性、权限和人工接管，定义任务完成条件和效果指标。
   - 完成标准：每项 Agent 任务有自动化等级、人工介入点和验收方式。

6. **形成后续建模输入**
   - 动作：汇总 Agent 任务需要的数据、知识、语义、规则、权限和Action。
   - 完成标准：能够交给场景深描和数据需求分析继续细化。

## 固定输出

- 智能体作用说明
- Agent 候选任务清单与优先级
- 用户、Agent、确定性系统和人工责任矩阵
- 每项任务的触发、输入、输出、完成条件和失败处理
- 自动化等级、权限、人工介入和风险清单
- 数据、知识、本体与工具能力需求
- 保留、缩小或取消 Agent 化的判断

## 使用边界

- 场景信息不足时先给候选任务和澄清清单，避免直接确定自动执行。
- 固定公式、精确计算、状态事务和硬约束由确定性能力承接，并通过工具供 Agent 调用。
- 智能体只做简单查询且无需关系、规则和追溯时，本体范围可以收缩或取消。
- 具体动作的重试、降级和结果回写交给 `action-contract-execution-feedback-loop`。

## 相关 Skills

- `depends-on` → `ontology-ai-scenario-fit-and-spike`；先完成本体适配初判。
- `feeds-into` → `business-scenario-deep-analysis`；把候选任务放回完整业务过程验证。
- `composes-with` → `risk-based-agent-action-modes`；高风险任务继续确定行动模式。

## 审计信息

- **首次公开版本**：2026-08-31
- **来源说明**：面向企业智能体场景设计独立整理。
