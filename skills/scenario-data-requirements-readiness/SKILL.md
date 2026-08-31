---
name: scenario-data-requirements-readiness
description: |
  用于场景和Agent任务已经梳理，需要判断业务、财务、IT等数据分别需要什么、来自哪些系统表字段、质量权限是否满足，用户出现“这个场景需要哪些数据”“业务财务IT三类数据怎么盘点”或 scenario data requirements, data readiness 等信号时调用。不适用于把已确认数据映射为本体类、属性和实例。
metadata:
  tags: "data-requirements, business-data, finance-data, it-data, source-location, readiness, data-gap, enterprise-ai, ontology-driven"
  related-skills: "business-scenario-deep-analysis:depends-on, scenario-related-knowledge-structure:feeds-into, scenario-related-semantic-modeling:feeds-into, data-to-ontology-mapping-and-instantiation:distinguished-from"
---

# 场景数据需求与数据准备度分析

## 方法骨架

- 从 Agent 任务、业务判断和动作逐项反推所需事实，再确定数据对象、字段、粒度、时间和质量要求。
- 业务、财务和 IT 可作为数据领域标签；同时标记主数据、事实、规则配置、指标、结果、日志等数据角色。
- 在本阶段完成来源系统、数据集、表、字段和接口定位，明确责任、权限、更新和样本可得性。
- 业务与财务数据可能交叉，按业务含义和实际用途允许多标签，不用部门归属替代语义判断。
- 输出数据准备度和缺口对 Agent 任务的影响，关键数据不可得时缩小场景范围或设计样本验证。
- 数据到本体类、属性、关系和实例的对应留给后续映射阶段。

需要详细字段模板时读取 [数据需求与准备度契约](references/data-requirement-contract.md)。

## 执行步骤

1. **从任务反推数据**
   - 动作：对每项 Agent 任务列出判断、行动、所需事实和最低数据集合。
   - 完成标准：每项数据需求都有明确用途和对应任务。

2. **分类数据领域与角色**
   - 动作：标注业务、财务、IT 技术等领域，以及主数据、事实、规则配置、指标、结果、日志和审计角色。
   - 完成标准：交叉数据保留多标签，IT 技术数据和业务语义数据边界明确。

3. **明确数据要求**
   - 动作：定义对象、字段、粒度、时间范围、版本、更新频率、质量、权限和样本要求。
   - 完成标准：需求可以被数据责任人核验。

4. **定位物理来源**
   - 动作：确认来源系统、数据集、表、字段、接口、责任人和访问方式。
   - 完成标准：已定位数据可直接追溯，未定位项有责任人和计划。

5. **检查跨系统关联**
   - 动作：检查统一标识、主数据、映射表、编码、时间、版本和状态对齐条件。
   - 完成标准：每个跨系统关联有现有键、映射方案或缺口结论。

6. **评估准备度与影响**
   - 动作：将数据标为可用、需清洗、缺映射、缺权限、时效不足、只有人工记录或缺失，评估对任务的影响。
   - 完成标准：阻断项、替代数据、样本方案和首期调整明确。

## 固定输出

- Agent 任务—数据需求矩阵
- 业务、财务、IT 数据清单与数据角色
- 数据对象、字段、指标、粒度、时间、版本和质量要求
- 来源系统—数据集—表—字段—接口登记表
- 数据责任人、权限、敏感级别和使用限制
- 跨系统标识与关联需求
- 数据准备度报告
- 数据缺口、任务影响与补充方案

## 使用边界

- 项目主数据即使由 IT 部门维护，也按其业务含义归入业务数据，并增加 IT 管理标签。
- 接口定义、系统日志、调用审计、权限元数据和更新时间通常归入 IT 技术数据。
- 在本阶段记录表字段的物理位置；字段的统一业务定义进入场景语义模型。
- 在本阶段不生成本体实例；后续映射 Skill 使用已确认的物理来源和语义定义。

## 相关 Skills

- `depends-on` → `business-scenario-deep-analysis`；任务、判断和动作是数据需求的依据。
- `feeds-into` → `scenario-related-knowledge-structure` 与 `scenario-related-semantic-modeling`。
- 与 `data-to-ontology-mapping-and-instantiation` 区分：本 Skill 定位真实数据；后者把数据对应到本体模型。

## 审计信息

- **首次公开版本**：2026-08-31
- **来源说明**：面向场景驱动的企业数据准备独立整理。
