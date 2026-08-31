# 场景本体建设包

## 推荐目录

```text
scenario-ontology-package/
├── 00_manifest/
│   ├── construction-manifest.yaml
│   ├── deliverable-index.md
│   ├── gap-list.md
│   └── traceability-matrix.csv
├── 01_scenario/
│   ├── 01-01-scenario-fit-card.md
│   ├── 01-02-agent-role-and-task.csv
│   ├── 01-03-human-agent-system-responsibility.csv
│   ├── 01-04-scenario-specification.md
│   └── 01-05-goals-risks-acceptance.md
├── 02_data_and_knowledge/
│   ├── task-data-requirement-matrix.csv
│   ├── source-system-table-field-register.csv
│   ├── cross-system-linking-requirements.csv
│   ├── data-readiness-and-gaps.md
│   ├── knowledge-domain-map.md
│   ├── source-evidence-register.csv
│   ├── cases-experts-assets-register.csv
│   └── knowledge-conflicts-and-gaps.md
├── 03_semantic_model/
│   ├── 03-01-business-glossary.csv
│   ├── 03-02-business-objects.csv
│   ├── 03-03-object-attributes.csv
│   ├── 03-04-classification-and-inheritance.csv
│   ├── 03-05-object-relations.csv
│   ├── 03-06-business-rules.csv
│   ├── 03-07-events-and-states.csv
│   ├── 03-08-roles-permissions-actions.csv
│   ├── 03-09-goals-and-metrics.csv
│   └── 03-10-semantic-conflicts-and-status.csv
├── 04_conceptual_model/
│   ├── concept-and-class-view.md
│   ├── relationship-and-state-view.md
│   ├── rule-decision-table.csv
│   └── action-permission-goal-view.md
├── 05_logical_ontology/
│   ├── ontology.ttl
│   ├── vocabulary.ttl
│   ├── shapes.ttl
│   ├── model-metadata.yaml
│   ├── rules/
│   └── queries/
├── 06_ontology_mapping/
│   ├── record-to-class-mapping.csv
│   ├── field-to-property-mapping.csv
│   ├── relation-and-code-mapping.csv
│   ├── identity-and-instance-rules.yaml
│   └── sample-instances.ttl
├── 07_validation/
│   ├── technical-validation-report.md
│   ├── defect-and-blocker-register.csv
│   ├── expert-review.md
│   ├── golden-cases.yaml
│   └── regression-report.md
└── 08_delivery_operations/
    ├── semantic-asset-register.csv
    ├── release-notes.md
    ├── service-contract.yaml
    ├── version-dependency-lock.yaml
    ├── cross-domain-collaboration.csv
    └── monitoring-feedback-rollback.md
```

目录是完整建设包的总索引。单阶段任务只生成当前 Skill 负责的成果及必要上游引用，不为凑目录生成空文件。

## 成果名称与交付要求

| 成果组 | 必备内容 | 主要生成 Skill |
|---|---|---|
| 场景与任务 | 适配结论、Agent 任务、三方责任、场景规格、目标风险与验收 | `ontology-ai-scenario-fit-and-spike`、`scenario-agent-role-design`、`business-scenario-deep-analysis` |
| 数据与知识准备 | 任务数据需求、物理来源、准备度、知识来源、证据、专家和缺口 | `scenario-data-requirements-readiness`、`scenario-related-knowledge-structure` |
| 场景语义模型 | 术语、对象、属性、分类继承、关系、规则、事件状态、权限动作、目标指标和冲突 | `scenario-related-semantic-modeling` |
| 模型施工 | 概念视图、逻辑元素、约束、查询、Action 引用和模型元数据 | `ontology-conceptual-model-design`、`ontology-logical-model-generation` |
| 数据映射与实例 | 记录到类、字段到属性、关联到关系、编码映射、标识规则和样例实例 | `data-to-ontology-mapping-and-instantiation` |
| 质量与验收 | 多层质量检查、缺陷阻断、黄金用例、边界异常权限用例和回归结果 | `ontology-model-multilayer-quality-gate`、`ontology-golden-case-testing` |
| 发布与运行 | 资产登记、服务契约、版本依赖、跨域协同、灰度回滚和反馈 | `ontology-runtime-service-and-version-operations` |

## 通用条目字段

| 字段 | 说明 |
|---|---|
| id | 在当前建设包内唯一 |
| scenario_id / task_id | 所属场景和 Agent 任务 |
| name / definition | 名称和可判定定义 |
| source / evidence | 来源及可定位证据 |
| status | 候选、有证据、已确认、已验证、受阻、已废弃 |
| owner / confirmer | 责任人和确认角色 |
| scope / version | 适用范围与版本 |
| downstream_links | 对应模型、实例、测试和运行结果 |

表格型成果除业务字段外，均保留上述通用字段。跨表引用使用 `id`，名称只用于阅读展示。

## 跨平台降级

- 可以写文件：生成目录和分文件成果。
- 只能返回文本：按目录顺序输出带文件名的 Markdown、CSV 或 YAML 代码块。
- 无法执行脚本：输出待执行校验项，并把验证状态写为未执行。
- 缺少源数据或权限：保留映射要求和缺口，不生成虚构实例。
