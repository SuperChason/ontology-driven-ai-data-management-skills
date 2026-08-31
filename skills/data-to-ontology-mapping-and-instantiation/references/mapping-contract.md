# 数据到本体映射契约

## 映射层次

| 映射 | 示例 |
|---|---|
| 数据记录 → 本体类 | 一条工程活动记录生成 `EngineeringActivity` 实例 |
| 数据字段 → 数据属性 | 实际完成日期映射到 `actualFinishDate` |
| 关联键 → 对象关系 | 项目标识形成 `belongsToProject` 关系 |
| 代码值 → 受控概念 | 状态代码映射到统一状态概念 |
| 事件记录 → 事件类 | 变更记录生成 `ChangeEvent` 实例 |
| 业务键 → URI | 稳定业务标识生成可追溯实例 URI |

## 映射条目字段

- mapping_id
- source_dataset / record_type / element
- source_semantic_id
- target_ontology_version
- target_class / property / concept
- selection_condition
- transformation_rule
- identity_or_join_rule
- effective_time_and_version
- provenance_rule
- missing_or_conflict_handling
- status / owner / test_case

物理来源字段来自数据准备度阶段，本契约只引用，不重新发现。

## 实例来源

每个实例至少保留：

- 来源系统和记录标识
- 抽取或事件时间
- 数据版本和映射版本
- 生成规则及其版本
- 原始值和转换后的值，按安全要求保留
- 授权范围和敏感等级
- 直接事实、推导事实或人工确认标记

## 增量维护

- 新增：创建实例及必要关系。
- 更新：区分同一实体属性变化与新业务版本。
- 删除：按业务和合规要求选择删除、失效或保留历史。
- 迟到数据：按事件时间和处理时间决定重算范围。
- 映射规则变化：做影响分析并决定是否重建历史实例。
- 失败恢复：记录批次、幂等键、重试和人工处理。
