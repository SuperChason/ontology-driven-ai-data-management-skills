---
name: ontology-runtime-service-and-version-operations
description: |
  用于本体已建成，需要以服务方式供多个Agent调用、业务规则存在多版本并行和灰度发布，用户出现“怎么做本体即服务”“本体版本如何灰度和回滚”或 ontology as a service, semantic versioning, runtime governance 等信号时调用。不适用于本体仍处于草稿或没有通过质量与用例验收。
metadata:
  tags: "ontology-as-a-service, runtime, versioning, access-control, sub-ontology, enterprise-ai, ontology-driven"
  related-skills: "seven-plus-one-semantic-mapping:depends-on, intent-driven-minimal-ontology-loading:composes-with, action-contract-execution-feedback-loop:composes-with"
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

### 固定输出

最终结果至少包含：输入与假设、逐步判断、证据与来源、未决项、风险边界、建议动作、完成标准。涉及项目适配时，将方法假设与项目事实分栏表达。

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

- `depends-on` → `seven-plus-one-semantic-mapping`。
- `composes-with` → `intent-driven-minimal-ontology-loading`；本 skill 提供可版本化的运行时资源；最小加载 skill 决定每次任务取哪些资源。
- `composes-with` → `action-contract-execution-feedback-loop`。

## 审计信息

- **验证通过**：V1 ✓ / V2 ✓ / V3 ✓
- **测试通过率**：100%（6/6，独立 sub-agent 盲测；详见 test-results.md）
- **首次公开版本**：2026-08-21
- **来源说明**：方法框架受《本体驱动的 AI 数据管理》启发；仓库不包含原书正文。
