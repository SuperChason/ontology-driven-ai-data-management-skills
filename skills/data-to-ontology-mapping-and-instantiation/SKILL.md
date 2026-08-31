---
name: data-to-ontology-mapping-and-instantiation
description: |
  用于逻辑本体和数据语义已经确认，需要说明数据记录如何对应本体类、字段如何对应属性、关联如何对应对象关系，并生成可追溯实例，用户出现“把数据映射到本体类和属性”“生成本体实例”或 data-to-ontology mapping, ontology instantiation 等信号时调用。不适用于首次寻找真实系统中的表、字段和接口。
metadata:
  tags: "data-ontology-mapping, class-mapping, property-mapping, entity-identity, instance-generation, provenance, enterprise-ai, ontology-driven"
  related-skills: "scenario-data-requirements-readiness:depends-on, scenario-related-semantic-modeling:depends-on, ontology-logical-model-generation:depends-on, ontology-model-multilayer-quality-gate:feeds-into"
---

# 数据到本体映射与实例构建

## 方法骨架

- 使用前序阶段已经确认的数据来源、字段位置、业务语义和逻辑本体，建立数据到类、属性、关系、概念和实例的映射。
- 数据记录映射为类实例，字段映射为数据属性，关联键或推导结果映射为对象关系，代码值映射为术语概念或受控值。
- 跨系统实体先确定统一标识和消歧规则，再生成 URI 和关系实例。
- 每个实例保留来源系统、记录标识、时间、版本、转换和授权信息。
- 本阶段直接引用已定位的系统、表、字段和接口，不重新承担物理数据源发现。

需要详细映射字段和实例规则时读取 [数据到本体映射契约](references/mapping-contract.md)。

## 执行步骤

1. **检查前置输入**
   - 动作：确认逻辑本体版本、数据语义、物理来源、样本、权限和质量状态一致。
   - 完成标准：未定位来源或未确认语义单列为阻断，不进入正式实例生成。

2. **建立记录到类映射**
   - 动作：定义哪类数据记录生成哪个本体类实例，以及筛选、合并和排除条件。
   - 完成标准：每个实例类有数据粒度、来源和生成条件。

3. **建立字段到属性映射**
   - 动作：映射数据属性、类型、单位、时间、空值、枚举和转换规则。
   - 完成标准：每个必需属性有来源、转换和缺失处理。

4. **建立关系与概念映射**
   - 动作：把外键、映射表、事件关联或推导结果转换为对象关系，把代码值转换为受控概念或状态。
   - 完成标准：关系方向、证据、有效期和冲突处理明确。

5. **设计实体标识与版本**
   - 动作：定义业务键、跨源实体合并、URI、版本实例、历史保留和删除策略。
   - 完成标准：同一业务实体稳定识别，版本变化不会覆盖必要历史。

6. **生成并校验样例实例**
   - 动作：使用真实或脱敏样本生成实例，执行数据类型、必填、关系和来源校验。
   - 完成标准：样例实例满足逻辑本体和 SHACL 约束，问题可回溯前序阶段。

7. **定义增量实例维护**
   - 动作：设计新增、更新、删除、失效、重放和异常恢复规则。
   - 完成标准：运行时数据变化能够安全反映到实例层并保留审计。

## 固定输出

- 数据记录—本体类映射表
- 数据字段—本体属性映射表
- 外键/关联—对象关系映射表
- 编码值—术语概念或状态映射表
- 业务事件—事件类映射表
- 实体统一标识和 URI 规则
- 类型、单位、时间和空值转换规则
- 实例与关系生成规则
- 样例实例和来源证明
- 增量更新、失效、删除和异常处理规则
- 实例校验报告与上游问题清单

## 使用边界

- 查找来源系统、表、字段和接口由 `scenario-data-requirements-readiness` 完成。
- 字段在业务上表示什么由 `scenario-related-semantic-modeling` 完成。
- 本 Skill 只把已完成来源定位和语义定义的数据映射到逻辑本体。
- 来源缺失、权限未授权或语义冲突时，不生成生产实例。
- 推导关系必须标记规则、版本和证据，不能伪装成源系统直接事实。

## 相关 Skills

- `depends-on` → `scenario-data-requirements-readiness`、`scenario-related-semantic-modeling` 和 `ontology-logical-model-generation`。
- `feeds-into` → `ontology-model-multilayer-quality-gate` 与 `ontology-golden-case-testing`。

## 审计信息

- **首次公开版本**：2026-08-31
- **来源说明**：面向企业数据本体化和实例治理独立整理。
