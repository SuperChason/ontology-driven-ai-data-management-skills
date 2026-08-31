# 场景语义模型契约

## 输出组织原则

- 用户只要某一类语义资产时，只输出对应表和必要的缺口，不强制生成全套模型。
- 生成完整场景语义模型时，按“术语→对象→属性→分类与继承→关系→规则→事件与状态→角色权限与动作→目标与指标→追溯与缺口”的顺序交付。
- 已确认、候选和受阻条目分开表达，不用编造内容填满空表。
- 对象、属性、关系和规则使用稳定编号串联，避免仅靠名称做跨表引用。

## 核心语义条目字段

- 唯一编号、名称和定义
- 所属场景和 Agent 任务
- 语义类型：术语、对象、属性、分类、关系、约束、规则、事件、状态、权限、动作、目标或指标
- 来源、证据位置和适用范围
- 候选、有证据、已确认、已验证、受阻或已废弃状态
- 责任人、确认角色和版本
- 正例、反例、边界和例外
- 上下游语义与后续模型元素

## 通用输出模板

### 1. 业务术语表

| 字段 | 填写要求 |
|---|---|
| term_id | 当前建设包内唯一的术语编号 |
| standard_term / definition | 标准术语和可判定定义 |
| synonyms / english_name | 同义词、口语、旧称和英文名称 |
| context / domain | 适用语境和所属领域 |
| source / evidence | 来源及可定位证据 |
| owner / confirmer / status / version | 责任、确认、状态和版本 |

### 2. 业务对象清单

| 字段 | 填写要求 |
|---|---|
| object_id / name / definition | 对象编号、名称和边界清晰的定义 |
| object_type / domain | 业务对象、交易事件或参考信息，以及所属领域 |
| identity / granularity | 唯一标识和一个实例代表什么 |
| lifecycle / key_states | 从创建到失效的生命周期和关键状态 |
| source_system | 权威来源系统或业务来源 |
| shared_asset_relation | 引用公共资产、引用后扩展或场景自建 |
| source / evidence / owner / confirmer / status / version | 追溯和治理字段 |

### 3. 对象属性定义表

| 字段 | 填写要求 |
|---|---|
| attribute_id / object_id | 属性编号和所属对象编号 |
| name / definition | 属性名称和业务定义 |
| data_type / unit / format | 数据类型、单位和格式 |
| required / cardinality | 是否必填以及可出现的数量 |
| value_range / code_set | 值域、编码集和默认值 |
| constraint / example / exception | 可执行约束、正反例和例外 |
| inherited_from | 继承来源；无继承时留空 |
| source / evidence / owner / status / version | 追溯和治理字段 |

### 4. 分类与继承定义表

| 字段 | 填写要求 |
|---|---|
| scheme_id / dimension / purpose | 分类方案、分类维度和用途 |
| category_id / name / condition | 分类项、名称和可判断条件 |
| parent_concept / child_concept | 仅记录稳定 `is-a` 继承 |
| inherited_elements / specific_elements | 继承和子概念特有的属性、约束或规则 |
| examples / exclusions / evidence | 包含、排除、边界样例和证据 |
| owner / confirmer / status / version | 责任、确认、状态和版本 |

### 5. 对象关系定义表

| 字段 | 填写要求 |
|---|---|
| relation_id / name / definition | 关系编号、名称和业务含义 |
| subject_object_id / target_object_id | 主对象和目标对象编号 |
| relation_type / direction | 继承、组成、影响、依赖、责任、来源、状态等类型及方向 |
| cardinality | `1:1`、`1:N`、`N:1` 或 `N:M` |
| valid_condition / temporal_scope | 成立条件和时间范围 |
| inverse_relation / exception | 反向关系和例外 |
| source / evidence / owner / status / version | 追溯和治理字段 |

### 6. 业务规则定义表

| 字段 | 填写要求 |
|---|---|
| rule_id / name / rule_type | 规则编号、名称与约束、推导、计算、触发或决策类型 |
| involved_elements | 涉及对象、属性、关系或事件编号 |
| trigger / condition / conclusion | 触发、条件表达式和结论 |
| priority / conflict / exception | 优先级、冲突处理和例外 |
| following_action_id | 命中后调用的动作编号；规则与动作分开定义 |
| source / evidence / owner / confirmer / status / version | 制度证据、责任和版本 |
| test_case | 正常、边界、例外或冲突用例 |

### 7. 事件与状态定义表

| 字段 | 填写要求 |
|---|---|
| event_id / name / event_type | 事件编号、名称和业务类型 |
| source / trigger / participants | 事件来源、触发条件和参与对象或角色 |
| input / output / result | 事件输入、输出和结果 |
| state_id / object_id | 状态编号和所属对象 |
| from_state / to_state / transition_condition | 起始状态、目标状态和迁移条件 |
| abnormal_state / recovery | 异常状态和恢复路径 |
| evidence / owner / status / version | 追溯和治理字段 |

### 8. 角色、权限与动作定义表

| 字段 | 填写要求 |
|---|---|
| role_id / responsibility | 角色编号和业务责任 |
| permission_id / scope / condition | 权限、授权范围和生效条件 |
| action_id / name / target | 动作编号、名称和作用对象或系统 |
| input / output | 输入、输出和错误结果 |
| precondition / effect | 前置条件和预期状态变化 |
| execution_mode / risk / human_control | 自动、需确认或禁止，以及风险和人工控制点 |
| failure / feedback / audit | 失败处理、结果回写和审计 |
| source / owner / confirmer / status / version | 追溯和治理字段 |

### 9. 目标与指标定义表

| 字段 | 填写要求 |
|---|---|
| goal_id / goal_level / definition | 场景、Agent 任务或动作结果目标 |
| metric_id / name / business_definition | 指标编号、名称和业务口径 |
| formula_or_judgement | 计算公式或判断方式 |
| data_source / dimensions / period / unit | 数据来源、统计维度、周期和单位 |
| baseline / target / threshold | 基准、目标和阈值 |
| acceptance_role / frequency | 验收角色和评价频率 |
| source / owner / status / version | 追溯和治理字段 |

### 10. 追溯、冲突与确认状态表

| 字段 | 填写要求 |
|---|---|
| semantic_id / semantic_type | 语义条目编号和类型 |
| scenario_id / task_id | 所属场景和 Agent 任务 |
| source_id / evidence_location | 来源编号和证据位置 |
| conflict_id / conflict_description | 冲突编号和差异描述 |
| impact / resolution / confirmer | 影响、裁决结果和确认角色 |
| status / version / downstream_links | 状态、版本和后续模型、映射、测试链接 |

## 分类与继承

### 业务分类方案

- 分类维度和目的
- 分类项和判断条件
- 包含、排除和边界示例
- 影响的规则、流程或权限

同一对象允许按内容、原因、影响程度、处理状态等不同维度分类。

### 概念继承关系

- 上位概念和下位概念
- 继承的属性与约束
- 子概念特有属性和规则
- 业务依据和实例

只有“下位概念属于上位概念”的稳定泛化进入继承树。

## 场景目标与评价

### 目标层次

- 场景业务目标
- Agent 任务目标
- 动作结果目标

### 评价口径

- 业务结果：覆盖、及时、合规和业务结果一致性
- Agent 任务：准确、召回、证据可追溯和人工修正
- 动作结果：成功、越权、异常、回滚和人工接管

每个指标记录定义、公式或判断方式、数据来源、统计范围、基准、目标、阈值和责任人。模型语法、SHACL 通过率等技术指标由技术验证阶段管理。

## 关系类型检查

| 问题 | 关系类型示例 |
|---|---|
| A 是否属于一种 B | 概念继承 |
| A 是否由 B 组成或包含 B | 组成/包含 |
| A 是否影响 B | 影响 |
| A 是否依赖 B 才能成立 | 依赖 |
| A 是否由角色 B 负责 | 责任 |
| A 是否从状态 B 进入 C | 状态流转 |
| A 的结论来自 B | 来源/证据 |

关系类型不同，约束、查询和推理行为也不同。
