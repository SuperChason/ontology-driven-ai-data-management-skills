---
name: ontology-runtime-service-and-version-operations
description: |
  用于本体已建成，需要以服务方式供多个Agent调用、业务规则存在多版本并行和灰度发布，用户出现“怎么做本体即服务”“本体版本如何灰度和回滚”或 ontology as a service, semantic versioning, runtime governance 等信号时调用。不适用于本体仍处于草稿或没有通过质量与用例验收。
metadata:
  tags: "ontology-as-a-service, runtime, versioning, access-control, sub-ontology, enterprise-ai, ontology-driven"
  related-skills: "ontology-model-multilayer-quality-gate:depends-on, ontology-golden-case-testing:depends-on, intent-driven-minimal-ontology-loading:composes-with, action-contract-execution-feedback-loop:composes-with"
---

# 本体运行时服务与版本运营

## 方法骨架

- 把本体从静态文件转成可查询、可授权、可组合的运行时服务。
- 服务按意图提供子本体、版本、适用范围和依赖，屏蔽底层存储差异。
- 动态事实与Action通过稳定接口接入，模型和Agent按需消费。
- 发布支持灰度、并行版本、回滚和上下文选版，避免全局瞬时切换。
- 访问控制结合角色、任务和知识敏感级别，调用记录可审计。
- 运行反馈进入变更评审、回归测试和建用优复运营闭环。

## 触发场景

### 用户会在什么情境下需要这个 Skill

1. 本体已建成，需要以服务方式供多个Agent调用
2. 业务规则存在多版本并行和灰度发布
3. 需要设计本体注册、权限、回滚和运行监控

### 语言信号

- “怎么做本体即服务”
- “本体版本如何灰度和回滚”
- “多个Agent怎样安全调用本体”
- 英文信号：ontology as a service, semantic versioning, runtime governance

### 与相邻 Skill 的区分

- 与 `intent-driven-minimal-ontology-loading`：本 skill 提供可版本化的运行时资源；最小加载 skill 决定每次任务取哪些资源。
- 与 `five-ring-ontology-engineering-lifecycle`：五环覆盖建设全流程；本 skill 聚焦上线后的服务与运营。

## 执行步骤

Skill 激活后按以下顺序执行：

1. **建立注册表**
   - 动作：登记本体标识、版本、领域、适用范围、来源、责任人、依赖和状态。
   - 完成标准：每个生产本体可唯一定位并追溯。

2. **定义服务接口**
   - 动作：提供查询、片段加载、规则解释、版本选择和健康检查接口。
   - 完成标准：调用方无需感知底层存储，响应包含版本和证据。

3. **配置权限隔离**
   - 动作：按角色、任务、项目和敏感级别授权，记录调用与拒绝。
   - 完成标准：越权用例被阻断，授权变更可审计。

4. **设计发布策略**
   - 动作：设置语义版本、兼容性、灰度范围、并行期、回滚点和迁移规则。
   - 完成标准：新旧版本各有适用上下文，回滚经过演练。

5. **运营与反馈**
   - 动作：监控命中、延迟、失败、规则冲突和业务修正，触发评审与回归。
   - 完成标准：问题能够分流到数据、语义、服务或应用责任人。

## 固定输出

- 本体资产注册表：资产编号、命名空间、领域、适用范围、来源、责任人、版本、依赖、质量结论和状态
- 运行时服务目录：服务编号、用途、输入输出、查询或加载范围、版本选择、证据、错误和健康检查
- 角色—任务—资产权限矩阵：授权、拒绝、敏感级别、适用范围和审计要求
- 版本与依赖锁定表：语义版本、兼容范围、依赖版本、Agent 绑定、数据映射版本和用例版本
- 发布、灰度、并行与回滚方案：范围、流量或对象、生效条件、观察指标、回滚点和迁移规则
- 运行监控与调用审计表：命中、延迟、失败、拒绝、规则冲突、业务修正和调用版本
- 运行反馈、问题分流、变更评审和回归状态台账

只登记通过质量门和业务用例验收的生产版本，每次服务响应都返回资产版本、适用范围和证据信息。

## 使用边界

### 不要在以下情况使用

- 本体仍处于草稿或没有通过质量与用例验收
- 直接另建一套身份权限体系
- 只需要离线交付一次性模型文件

### 常见失败模式

- **本体静态交付后缺少版本和反馈运营**：业务变化与本体发布脱节，运行异常也无法回流建模端，旧版本继续影响Agent决策。
- **新本体与存量数据和系统形成新孤岛**：语义层与事实源、既有知识资产及执行系统没有稳定映射，模型无法随真实业务同步。

### 使用折扣与复核要求

- 本体服务依赖企业已有的身份、配置、可观测和发布基础设施，当前方法未给出完整产品实现。
- 大模型生成形式结构无法直接证明业务语义正确，生产使用需保留专家确认、工具校验、真实用例和审计记录。

## 相关 Skills

- `depends-on` → `ontology-model-multilayer-quality-gate` 与 `ontology-golden-case-testing`；技术和业务验证通过后才登记生产版本。
- `composes-with` → `intent-driven-minimal-ontology-loading`；本 skill 提供可版本化的运行时资源；最小加载 skill 决定每次任务取哪些资源。
- `composes-with` → `action-contract-execution-feedback-loop`。

## 审计信息

- **历史验证**：v0.1.0 路由测试 6/6；v0.4.0 已通过输出契约结构校验，跨平台行为继续按版本抽样
- **首次公开版本**：2026-08-21
- **来源说明**：方法框架受《本体驱动的 AI 数据管理》启发；仓库不包含原书正文。
