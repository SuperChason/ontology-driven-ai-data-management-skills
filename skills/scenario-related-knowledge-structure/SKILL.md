---
name: scenario-related-knowledge-structure
description: |
  用于场景范围和数据需求已经明确，需要盘点完成Agent任务所需的制度、文档、数据、案例、专家和已有知识资产，并建立来源、证据、责任和缺口结构，用户出现“梳理这个场景相关的知识结构”“这些知识从哪里来”或 scenario knowledge structure, evidence landscape 等信号时调用。不适用于定义对象、关系、约束和规则的正式业务语义。
metadata:
  tags: "knowledge-structure, source-evidence, expert, case, reusable-assets, knowledge-gap, enterprise-ai, ontology-driven"
  related-skills: "business-scenario-deep-analysis:depends-on, scenario-data-requirements-readiness:depends-on, twenty-nine-sentence-knowledge-extraction:feeds-into, scenario-related-semantic-modeling:feeds-into"
---

# 场景相关的知识结构

## 方法骨架

- 围绕已确认的 Agent 任务，组织完成任务所需的知识领域、来源、证据、责任和复用资产。
- 制度、流程、数据、模型、案例和专家经验分别登记权威级别、版本、适用范围和可访问性。
- 本阶段可以发现候选对象、关系、规则和例外，正式定义统一进入场景语义模型。
- 同一业务结论存在多个来源时，保留差异并建立裁决责任，不自动合并成确定规则。
- 通过知识缺口判断哪些任务可继续、哪些只能样本验证、哪些需要暂停。

需要详细产物字段时读取 [知识结构契约](references/knowledge-structure-contract.md)。

## 执行步骤

1. **按任务建立知识需求**
   - 动作：为每项 Agent 判断和动作列出需要的定义、规则、流程、案例、权限和证据。
   - 完成标准：知识需求能够追溯到具体任务。

2. **盘点知识来源**
   - 动作：登记制度、文档、表单、数据、接口说明、规则模型、历史案例、专家和已有语义资产。
   - 完成标准：每项来源有版本、责任、适用范围和访问状态。

3. **组织知识领域与依赖**
   - 动作：按当前场景划分知识主题、上下游依赖和公共/领域/场景资产引用。
   - 完成标准：能够判断哪些直接使用、哪些复用、哪些需要新建。

4. **建立证据链**
   - 动作：把候选知识条目连接到具体来源位置、真实案例或专家确认记录。
   - 完成标准：关键结论有证据或明确待确认状态。

5. **处理冲突与缺口**
   - 动作：识别版本冲突、同名异义、口径差异、失效知识和没有责任人的空白。
   - 完成标准：每个冲突有裁决人，每个缺口有任务影响和处理建议。

6. **交付知识提取输入**
   - 动作：确定可进入 29 类知识提取的材料、专家和问题清单。
   - 完成标准：提取范围、来源和确认机制明确。

## 固定输出

- 场景知识领域地图
- Agent 任务—知识需求矩阵
- 制度、文档、数据、模型、案例和专家来源台账
- 来源权威级别、版本、适用范围和责任人
- 公共、领域和场景资产复用清单
- 候选知识条目与证据索引
- 知识冲突、缺口、失效和待裁决清单
- 29 类知识提取的材料与访谈计划

## 使用边界

- 对象、术语、关系、约束、规则、状态、权限、动作和目标的权威定义由场景语义模型管理。
- 表字段物理位置由数据需求与准备度阶段管理；本阶段只引用其作为知识来源。
- 只有来源清单时不能声称知识已经正确提取或业务专家已经确认。
- 通用企业知识只按当前场景需要引用，验证出稳定复用价值后再向领域或公共层沉淀。

## 相关 Skills

- `depends-on` → `business-scenario-deep-analysis` 与 `scenario-data-requirements-readiness`。
- `feeds-into` → `twenty-nine-sentence-knowledge-extraction` 和 `scenario-related-semantic-modeling`。

## 审计信息

- **首次公开版本**：2026-08-31
- **来源说明**：面向场景知识准备和证据治理独立整理。
