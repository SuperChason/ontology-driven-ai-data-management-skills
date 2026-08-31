---
name: ontology-logical-model-generation
description: |
  用于概念模型和业务语义已经确认，需要生成机器可处理的类、属性、关系、词汇、约束、查询和动作接口，用户出现“生成逻辑本体模型”“把概念模型转成RDF OWL SHACL”或 logical ontology generation, TTL, SHACL shapes 等信号时调用。不适用于业务语义尚未确认或只需要审查现有模型质量。
metadata:
  tags: "logical-ontology, rdf, owl, skos, shacl, sparql, formalization, enterprise-ai, ontology-driven"
  related-skills: "ontology-conceptual-model-design:depends-on, data-to-ontology-mapping-and-instantiation:feeds-into, ontology-model-multilayer-quality-gate:feeds-into"
---

# 逻辑本体模型生成

## 方法骨架

- 把已确认的概念模型形式化为机器可解析的类、属性、关系、词汇、约束、规则接口和查询模板。
- 先选择满足场景需求的最小技术组合；RDF/OWL/SKOS/SHACL/SPARQL按实际任务使用，流程、规则和权限可映射到企业现有引擎。
- 业务语义编号和来源必须保留在逻辑元素元数据中，防止形式模型失去业务证据。
- 候选语义与生产语义分模块或分状态发布，禁止在生成过程中把未确认内容自动升级。
- 逻辑模型生成后进入独立技术与业务质量门。

需要形式化映射规则时读取 [逻辑模型契约](references/logical-model-contract.md)。

## 执行步骤

1. **确定形式化配置**
   - 动作：选择命名空间、URI、模块、版本、依赖、序列化格式和需要的标准能力。
   - 完成标准：技术选择能够支持当前查询、校验、推理和集成需求。

2. **生成类、属性和词汇**
   - 动作：把对象、概念继承、数据属性、对象关系、术语和分类转换为逻辑元素。
   - 完成标准：元素与概念模型编号一一对应，名称和定义完整。

3. **生成约束与规则接口**
   - 动作：把数量、类型、值域、时间、一致性和权限前置约束转为 SHACL 或目标引擎可执行结构。
   - 完成标准：每条关键约束有来源、严重级别和测试样本。

4. **生成查询和动作接口**
   - 动作：为 Agent 关键任务建立查询模板，并为动作保留输入、输出、前置、效果和权限契约。
   - 完成标准：每项关键任务至少有可验证的模型访问路径。

5. **生成元数据与追溯**
   - 动作：记录模型标识、版本、状态、适用范围、责任、依赖和语义来源。
   - 完成标准：逻辑元素能够回溯场景语义、概念视图和证据。

6. **执行生成后自检**
   - 动作：解析文件并检查名称、引用、孤立元素、依赖和候选隔离，生成待独立审核的问题单。
   - 完成标准：文件可解析，自检结果不冒充独立质量结论。

## 固定输出

- 本体命名空间、URI 和模块规则
- RDF/OWL 类、属性和关系模型
- SKOS 术语和分类模型
- SHACL 约束模型
- 规则或决策表的目标实现映射
- SPARQL 查询模板
- Action 契约和权限引用
- 模型元数据、版本和依赖
- 语义—逻辑元素追溯表
- 生成后自检报告与独立审核输入

## 使用边界

- 业务语义来源不明、冲突未裁决或概念模型未确认时，保持草稿并返回前置阶段。
- SWRL、OWL-S、ODRL、BPMN 等根据目标平台选择，不设为所有场景必交格式。
- SHACL 用于数据图约束，规则引擎、流程引擎和 IAM 继续承担各自运行职责。
- 自检只能发现可解析和显性结构问题，独立质量审核及黄金用例仍然必需。

## 相关 Skills

- `depends-on` → `ontology-conceptual-model-design`。
- `feeds-into` → `data-to-ontology-mapping-and-instantiation` 与 `ontology-model-multilayer-quality-gate`。

## 审计信息

- **首次公开版本**：2026-08-31
- **来源说明**：结合开放语义标准和企业本体工程实践独立整理。
