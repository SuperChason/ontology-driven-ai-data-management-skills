# Ontology-Driven AI Data Management Skills

[![Validate skills](https://github.com/SuperChason/ontology-driven-ai-data-management-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/SuperChason/ontology-driven-ai-data-management-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

面向企业本体工程、AI 数据治理与 Agent 行动闭环的 16 个可复用 Skill。

这套 Skill 受《本体驱动的 AI 数据管理》启发，将场景选择、知识提取、语义建模、质量验证、推理决策、行动控制和运行治理整理成可执行工作流。仓库只收录独立编写的 Skill 指令、测试材料和维护脚本，不包含原书 PDF、页面图片、逐字引文及案例正文。详细边界见 [NOTICE](NOTICE)。

## 怎么使用

在 Codex 中有两种调用方式：

- 显式调用：输入 `$` 后选择 Skill，或直接在提示词中写 `$skill-name`。
- 自动匹配：直接描述任务，Codex 会根据每个 Skill 的 `description` 选择合适的工作流。

建议一次使用 1～4 个 Skill。复杂任务可以按依赖顺序分阶段执行，每个阶段先检查中间产物和继续条件。

### 示例

```text
$ontology-ai-scenario-fit-and-spike

帮我判断“工程进度变化影响预算”是否适合采用本体增强 AI。
请输出场景适配度、数据条件、首个穿刺场景、继续或停止标准，以及待确认问题。
```

```text
$action-contract-execution-feedback-loop

为“创建预算调整建议单”设计 Action 契约。
补齐输入、输出、权限、前置校验、幂等、失败重试、人工降级、执行回执和审计信息。
```

## Skill 导航

### 场景规划与规模化落地

| Skill | 适用任务 |
|---|---|
| [`ontology-ai-scenario-fit-and-spike`](skills/ontology-ai-scenario-fit-and-spike/SKILL.md) | 判断场景是否适合本体，设计首个小切口和穿刺验证 |
| [`ontology-ai-application-pattern-selection`](skills/ontology-ai-application-pattern-selection/SKILL.md) | 在问答、审核、协同、决策和 PDCA 等应用模式中选型 |
| [`five-ring-ontology-engineering-lifecycle`](skills/five-ring-ontology-engineering-lifecycle/SKILL.md) | 规划从知识采集到上线运营的本体工程生命周期 |
| [`point-line-plane-ontology-scaling`](skills/point-line-plane-ontology-scaling/SKILL.md) | 从单点场景扩展到业务线和企业级复用 |

### 知识提取、语义建模与质量验证

| Skill | 适用任务 |
|---|---|
| [`fact-reason-action-business-loop`](skills/fact-reason-action-business-loop/SKILL.md) | 用事实、事理、行动建立可追溯业务闭环 |
| [`twenty-nine-sentence-knowledge-extraction`](skills/twenty-nine-sentence-knowledge-extraction/SKILL.md) | 从制度、材料和专家访谈中提取结构化业务知识 |
| [`seven-plus-one-semantic-mapping`](skills/seven-plus-one-semantic-mapping/SKILL.md) | 检查术语、规则、权限、动作和目标评估是否完整 |
| [`ontology-model-multilayer-quality-gate`](skills/ontology-model-multilayer-quality-gate/SKILL.md) | 从语法、结构、语义和业务层审查本体质量 |
| [`ontology-golden-case-testing`](skills/ontology-golden-case-testing/SKILL.md) | 用黄金问题集、边界用例和回归矩阵验收本体 |

### Agent 推理、知识注入与行动闭环

| Skill | 适用任务 |
|---|---|
| [`intent-driven-minimal-ontology-loading`](skills/intent-driven-minimal-ontology-loading/SKILL.md) | 按用户意图加载最小必要本体和知识上下文 |
| [`ontology-constraint-and-knowledge-injection`](skills/ontology-constraint-and-knowledge-injection/SKILL.md) | 选择 Prompt、RAG、微调及混合知识注入策略 |
| [`fact-reason-goal-explainable-decision`](skills/fact-reason-goal-explainable-decision/SKILL.md) | 综合事实、规则和目标形成可解释决策 |
| [`risk-based-agent-action-modes`](skills/risk-based-agent-action-modes/SKILL.md) | 按风险选择自动执行、人工审批或协同控制 |
| [`action-contract-execution-feedback-loop`](skills/action-contract-execution-feedback-loop/SKILL.md) | 定义 Action 契约、执行校验、重试降级和结果回写 |

### 数据资产与运行治理

| Skill | 适用任务 |
|---|---|
| [`ai-training-inference-data-asset-governance`](skills/ai-training-inference-data-asset-governance/SKILL.md) | 治理训练数据、实时事实、规则模型和推理结果 |
| [`ontology-runtime-service-and-version-operations`](skills/ontology-runtime-service-and-version-operations/SKILL.md) | 建设本体运行时服务，处理版本、灰度、回滚和审计 |

## 推荐组合

### 从场景到首个验证

```text
ontology-ai-scenario-fit-and-spike
→ ontology-ai-application-pattern-selection
```

### 从业务材料到可验收本体

```text
twenty-nine-sentence-knowledge-extraction
→ fact-reason-action-business-loop
→ seven-plus-one-semantic-mapping
→ ontology-model-multilayer-quality-gate
→ ontology-golden-case-testing
```

### 从 Agent 判断到受控执行

```text
intent-driven-minimal-ontology-loading
→ fact-reason-goal-explainable-decision
→ risk-based-agent-action-modes
→ action-contract-execution-feedback-loop
```

### 从试点到生产运营

```text
five-ring-ontology-engineering-lifecycle
→ point-line-plane-ontology-scaling
→ ai-training-inference-data-asset-governance
→ ontology-runtime-service-and-version-operations
```

## 安装

### 安装全部 Skill

```bash
git clone https://github.com/SuperChason/ontology-driven-ai-data-management-skills.git
cd ontology-driven-ai-data-management-skills
./scripts/install.sh
```

脚本默认复制到 `~/.agents/skills`。可以通过环境变量指定其他目录：

```bash
CODEX_SKILLS_DIR="$HOME/.codex/skills" ./scripts/install.sh
```

已有同名 Skill 时脚本会跳过。确认需要覆盖后使用 `./scripts/install.sh --force`。

### 只安装一个 Skill

```bash
mkdir -p "$HOME/.agents/skills"
cp -R skills/ontology-ai-scenario-fit-and-spike "$HOME/.agents/skills/"
```

安装后重新打开 Codex；部分版本可以自动发现新增 Skill。

## 质量检查

每个 Skill 都包含：

- `SKILL.md`：触发边界、执行步骤、固定输出和失败模式。
- `agents/openai.yaml`：展示名称、简介和默认提示词。
- `test-prompts.json`：正向、反向和边界触发测试。
- `test-results.md`：当前测试记录。

本地验证：

```bash
python3 scripts/validate_skills.py
```

## 贡献

欢迎提交 Issue 和 Pull Request。新增或修改 Skill 时，请同步维护触发测试，并遵守 [CONTRIBUTING.md](CONTRIBUTING.md) 中的来源与隐私要求。

## License

仓库原创代码与文本采用 [MIT License](LICENSE)。原书内容及相关权利归原作者和出版方所有，MIT License 不扩展至原书内容。详见 [NOTICE](NOTICE)。
