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
│   ├── scenario-card.md
│   ├── agent-role-and-task.md
│   ├── scenario-specification.md
│   └── goals-risks-acceptance.md
├── 02_data_requirements/
│   ├── task-data-requirement-matrix.csv
│   ├── source-system-table-field-register.csv
│   ├── cross-system-linking-requirements.csv
│   └── data-readiness-and-gaps.md
├── 03_knowledge_structure/
│   ├── knowledge-domain-map.md
│   ├── source-evidence-register.csv
│   ├── cases-experts-assets-register.csv
│   └── knowledge-conflicts-and-gaps.md
├── 04_semantic_model/
│   ├── business-glossary.csv
│   ├── concept-object-attribute-catalog.csv
│   ├── classification-and-inheritance.csv
│   ├── relationship-constraint-rule-catalog.csv
│   ├── event-state-permission-action-catalog.csv
│   └── goals-completion-evaluation.md
├── 05_conceptual_model/
│   ├── concept-and-class-view.md
│   ├── relationship-and-state-view.md
│   ├── rule-decision-table.csv
│   └── action-permission-goal-view.md
├── 06_logical_ontology/
│   ├── ontology.ttl
│   ├── vocabulary.ttl
│   ├── shapes.ttl
│   ├── model-metadata.yaml
│   ├── rules/
│   └── queries/
├── 07_ontology_mapping/
│   ├── record-to-class-mapping.csv
│   ├── field-to-property-mapping.csv
│   ├── relation-and-code-mapping.csv
│   ├── identity-and-instance-rules.yaml
│   └── sample-instances.ttl
├── 08_validation/
│   ├── technical-validation-report.md
│   ├── expert-review.md
│   ├── golden-cases.yaml
│   └── regression-report.md
└── 09_delivery_operations/
    ├── release-notes.md
    ├── service-contract.yaml
    ├── version-dependency-lock.yaml
    └── monitoring-feedback-rollback.md
```

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

## 跨平台降级

- 可以写文件：生成目录和分文件成果。
- 只能返回文本：按目录顺序输出带文件名的 Markdown、CSV 或 YAML 代码块。
- 无法执行脚本：输出待执行校验项，并把验证状态写为未执行。
- 缺少源数据或权限：保留映射要求和缺口，不生成虚构实例。
