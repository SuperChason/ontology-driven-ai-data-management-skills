---
name: ontology-conceptual-model-design
description: |
  用于场景语义已经形成，需要把术语、对象、关系、规则、状态、权限、动作和目标组织成业务专家可阅读审查的概念模型，用户出现“把语义清单画成概念模型”“给业务专家做本体模型评审”或 conceptual ontology model, business model views 等信号时调用。不适用于直接编写RDF/OWL文件或只定义单个术语。
metadata:
  tags: "conceptual-model, business-view, class-hierarchy, relationship-view, decision-table, state-model, expert-review, enterprise-ai, ontology-driven"
  related-skills: "scenario-related-semantic-modeling:depends-on, ontology-logical-model-generation:feeds-into, ontology-model-multilayer-quality-gate:feeds-into"
---

# 本体概念模型设计

## 方法骨架

- 把已确认的语义条目组织成业务人员可理解、可审查的整体模型，建立模型结构和跨视图一致性。
- 概念模型保留业务名称、定义、来源和示例，暂不绑定具体 RDF/OWL 语法。
- 分类继承、组成关系、影响关系、状态变化、规则路径和动作权限分别展示，避免用一张大图混合所有语义。
- 每个 Agent 任务都要能沿“输入事实—关系/规则—判断—权限—动作—完成条件”找到模型支撑。
- 业务专家确认后才进入逻辑本体生成。

需要视图清单和检查项时读取 [概念模型视图契约](references/conceptual-model-views.md)。

## 执行步骤

1. **确定模型模块**
   - 动作：按 Agent 任务和业务边界划分公共引用、场景对象、规则、动作和目标模块。
   - 完成标准：每个模块职责、依赖和适用范围明确。

2. **构建对象与概念视图**
   - 动作：组织核心对象、概念继承、分类方案、属性、标识和实例示例。
   - 完成标准：父子概念、组成对象和代码枚举没有混用。

3. **构建关系、规则和状态视图**
   - 动作：分别表达关系网络、规则决策表、事件触发和状态流转。
   - 完成标准：关系方向、规则条件、状态入口出口和例外可审查。

4. **构建流程、动作和权限视图**
   - 动作：关联任务、角色、权限、Action 输入输出、前置条件、效果和人工介入。
   - 完成标准：每个可执行动作有授权和失败边界。

5. **构建目标与解释路径**
   - 动作：把场景目标、任务完成条件和评价口径连接到事实、规则、判断和结果。
   - 完成标准：能够解释推荐或行动服务于什么目标。

6. **执行跨视图审查**
   - 动作：检查重名、孤立、重复、冲突、缺失和跨视图标识不一致，形成专家问题清单。
   - 完成标准：业务专家能够逐项确认或退回语义建模。

## 固定输出

- 模型模块与依赖图
- 概念关系图和类层级树
- 业务分类方案和属性详情
- 对象关系视图
- 规则决策表
- 事件与状态流转图
- 流程、Action 输入输出和权限矩阵
- 实例示例视图
- 场景目标、完成条件和解释路径
- 模型元素清单与专家评审问题

## 使用边界

- 概念模型只使用已确认语义；候选条目单独着色或分区。
- 一张图只承载一种主要审查目的，复杂场景拆成多个可组合视图。
- 图形美观不能替代语义完整性和业务确认。
- 具体命名空间、类属性声明和 SHACL 约束进入逻辑模型阶段。

## 相关 Skills

- `depends-on` → `scenario-related-semantic-modeling`。
- `feeds-into` → `ontology-logical-model-generation` 和 `ontology-model-multilayer-quality-gate`。

## 审计信息

- **首次公开版本**：2026-08-31
- **来源说明**：面向本体业务审查和工程交接独立整理。
