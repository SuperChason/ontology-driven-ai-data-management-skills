# Ontology-Driven AI Data Management Skills

[![Validate skills](https://github.com/SuperChason/ontology-driven-ai-data-management-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/SuperChason/ontology-driven-ai-data-management-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue.svg)](https://agentskills.io/specification)

面向企业本体工程、AI 数据治理与 Agent 行动闭环的 16 个可复用 Skill，同时支持 Codex、Claude Code 和 WorkBuddy。

这套 Skill 受《本体驱动的 AI 数据管理》启发，将场景选择、知识提取、语义建模、质量验证、推理决策、行动控制和运行治理整理成可执行工作流。仓库只收录独立编写的 Skill 指令、测试材料和维护脚本，不包含原书 PDF、页面图片、逐字引文及案例正文。详细边界见 [NOTICE](NOTICE)。

## 平台支持

| 平台 | 使用方式 | 自动匹配 | 显式调用 | 分发形式 |
|---|---|---:|---|---|
| Codex | 安装到个人或项目 Skill 目录 | 支持 | `$skill-name` | 安装脚本、ZIP |
| Claude Code | 安装到个人或项目 Skill 目录 | 支持 | `/skill-name` | 安装脚本、ZIP |
| WorkBuddy | 在技能管理中上传并启用 | 支持 | 在对话中指定 Skill 名称 | 每个 Skill 一个 ZIP |

三端共用 `skills/` 下的核心 `SKILL.md`。构建时会按平台生成运行包：

- Codex 包保留 `agents/openai.yaml`，用于界面名称、简介和默认提示词。
- Claude Code 包使用开放 Agent Skills 结构，排除 Codex 专属元数据。
- WorkBuddy 包将每个 Skill 单独打包，压缩包根目录直接包含 `SKILL.md`。
- `test-prompts.json` 和 `test-results.md` 留在源码仓库中，运行包不携带测试材料。

## 快速下载

进入 [GitHub Releases](https://github.com/SuperChason/ontology-driven-ai-data-management-skills/releases/latest) 下载对应平台文件：

| 文件 | 用途 |
|---|---|
| `ontology-skills-codex-vX.Y.Z.zip` | Codex 离线安装包 |
| `ontology-skills-claude-code-vX.Y.Z.zip` | Claude Code 离线安装包 |
| `ontology-skills-workbuddy-vX.Y.Z.zip` | WorkBuddy 上传包合集 |
| `SHA256SUMS.txt` | 下载文件完整性校验 |

也可以克隆仓库后直接安装：

```bash
git clone https://github.com/SuperChason/ontology-driven-ai-data-management-skills.git
cd ontology-driven-ai-data-management-skills
```

## Codex

### 安装

安装到当前用户，所有项目都可以使用：

```bash
./scripts/install.sh codex
```

默认目标目录为 `~/.codex/skills`。

安装到当前项目，方便跟随项目版本管理：

```bash
./scripts/install.sh codex --target "$PWD/.agents/skills"
```

只安装一个 Skill：

```bash
./scripts/install.sh codex --skill ontology-ai-scenario-fit-and-spike
```

已有同名 Skill 时，安装脚本会保留现有版本并显示 `Skipped`。确认采用仓库版本后增加 `--force`。

### 使用

显式调用：

```text
$ontology-ai-scenario-fit-and-spike

帮我判断“工程进度变化影响预算”是否适合采用本体增强 AI。
请输出场景适配度、数据条件、首个穿刺场景、继续或停止标准，以及待确认问题。
```

自动匹配：

```text
帮我判断这个企业 AI 场景是否适合采用本体，并设计一个最小穿刺验证。
```

Codex 会根据每个 Skill 的 `description` 选择相关工作流。复杂任务建议一次启用 1～4 个 Skill，按依赖顺序检查中间结果。

### 更新

使用 Git 克隆安装时：

```bash
git pull --ff-only
python3 scripts/validate_skills.py
./scripts/install.sh codex --force
```

只更新一个 Skill：

```bash
git pull --ff-only
./scripts/install.sh codex --skill ontology-ai-scenario-fit-and-spike --force
```

使用 Release ZIP 安装时，下载新版本、解压到新目录，再运行其中的安装脚本：

```bash
./scripts/install.sh codex --force
```

更新后新建一个 Codex 任务，使用一个正向问题和一个无关问题检查触发边界。

## Claude Code

### 安装

安装到当前用户：

```bash
./scripts/install.sh claude-code
```

默认目标目录为 `~/.claude/skills`。

安装到当前项目：

```bash
./scripts/install.sh claude-code --target "$PWD/.claude/skills"
```

只安装一个 Skill：

```bash
./scripts/install.sh claude-code --skill fact-reason-action-business-loop
```

### 使用

显式调用：

```text
/fact-reason-action-business-loop

请把这段业务描述拆成事实、事理、行动和反馈闭环。
```

自动匹配：

```text
这个业务判断依据和后续系统动作混在一起了，帮我整理成可追溯闭环。
```

Claude Code 通过 `name` 和 `description` 发现 Skill。安装完成后可以输入 `/` 查看已加载的自定义 Skill；部分版本会实时发现新增文件，未出现时重新启动 Claude Code。

### 更新

使用 Git 克隆安装时：

```bash
git pull --ff-only
python3 scripts/validate_skills.py
./scripts/install.sh claude-code --force
```

使用 Release ZIP 安装时，下载并解压新版本，然后执行：

```bash
./scripts/install.sh claude-code --force
```

更新后输入 `/` 检查 Skill 名称，再用 `test-prompts.json` 中的一条 `should_trigger` 和一条 `should_not_trigger` 用例做抽样。

## WorkBuddy

### 获取上传包

推荐从 [GitHub Releases](https://github.com/SuperChason/ontology-driven-ai-data-management-skills/releases/latest) 下载：

```text
ontology-skills-workbuddy-vX.Y.Z.zip
```

解压后结构如下：

```text
ontology-skills-workbuddy-vX.Y.Z/
├── README.md
├── LICENSE
├── NOTICE
├── VERSION
└── skills/
    ├── action-contract-execution-feedback-loop-vX.Y.Z.zip
    ├── ...
    └── twenty-nine-sentence-knowledge-extraction-vX.Y.Z.zip
```

`skills/` 里的 16 个 ZIP 才是 WorkBuddy 直接上传的 Skill 包。可以按实际需要选择，不要求一次全部安装。

### 安装

1. 打开 WorkBuddy。
2. 进入左侧的“专家·技能·连接器”区域。
3. 选择添加技能或上传本地技能包。
4. 从解压后的 `skills/` 中选择一个 Skill ZIP。
5. 查看名称、说明和权限范围，确认后安装并启用。
6. 重复上述步骤，添加当前工作需要的其他 Skill。

每个上传包的根目录都直接包含 `SKILL.md`，并附带 `LICENSE`、`NOTICE` 和 `VERSION`。

### 使用

直接描述任务，WorkBuddy 会根据 Skill 描述自动匹配：

```text
帮我判断这个场景是否适合做本体，并给出最小验证切口和停止条件。
```

需要明确指定时，在任务中写出完整 Skill 名称：

```text
请使用 ontology-ai-scenario-fit-and-spike 分析下面的场景材料。
```

### 更新

1. 在 Releases 页面确认新版本号并下载新的 WorkBuddy 合集。
2. 保留上一版本 ZIP，作为出现问题时的回退包。
3. 解压新合集，找到需要更新的 Skill ZIP。
4. 在 WorkBuddy 技能管理中停用旧版本。
5. 上传新版同名 Skill；如果当前客户端不允许同名覆盖，先移除旧版本再上传。
6. 启用新版，用一条正向问题、一条相邻 Skill 问题和一条无关问题做抽样。
7. 抽样通过后再处理其余 Skill。

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

## 仓库结构

```text
.
├── skills/                         # 16 个 Skill 的唯一核心源
│   └── <skill-name>/
│       ├── SKILL.md                # 三端共用
│       ├── agents/openai.yaml      # Codex 专属界面元数据
│       ├── test-prompts.json       # 触发与路由测试
│       └── test-results.md         # 当前测试记录
├── scripts/
│   ├── install.sh                  # Codex、Claude Code 安装与更新
│   ├── validate_skills.py          # 核心源校验
│   ├── build_packages.py           # 三端打包
│   └── validate_packages.py        # 分发包校验
├── .github/workflows/
│   ├── validate.yml                # 推送和 PR 自动校验
│   └── release.yml                 # 标签触发 GitHub Release
└── VERSION                          # 当前发布版本
```

## 本地构建和验证

执行完整验证：

```bash
python3 scripts/validate_skills.py
python3 scripts/build_packages.py
python3 scripts/validate_packages.py
```

成功后 `dist/` 中会生成：

```text
dist/
├── ontology-skills-codex-vX.Y.Z.zip
├── ontology-skills-claude-code-vX.Y.Z.zip
├── ontology-skills-workbuddy-vX.Y.Z.zip
├── SHA256SUMS.txt
└── workbuddy/skills/
    └── <16 个单 Skill ZIP>
```

`dist/` 是构建产物，不提交到 Git。推送代码后，GitHub Actions 会保留一份短期构建产物；推送与 `VERSION` 一致的 `vX.Y.Z` 标签后，Release 工作流会创建正式下载版本。

## 维护和发布

修改 Skill 时：

1. 只编辑 `skills/<skill-name>/` 下的核心源。
2. 修改触发条件时，同步更新 `test-prompts.json` 和 `test-results.md`。
3. 运行三条本地构建与验证命令。
4. 检查 `git diff --check` 和实际变更范围。
5. 更新 `VERSION`。
6. 合并并推送主分支。
7. 创建与版本一致的 Git 标签，触发三端 Release。

发布后分别抽样：

- Codex：检查 `$skill-name` 显式调用和自动匹配。
- Claude Code：检查 `/skill-name`、自动匹配和 Skill 列表。
- WorkBuddy：上传一个新版 ZIP，检查启用、自动匹配和相邻 Skill 路由。

结构校验可以发现打包错误，仍需保留平台运行抽样。平台升级、权限模型变化或模型切换后，重新执行抽样。

## 质量检查

每个 Skill 都包含：

- `SKILL.md`：触发边界、执行步骤、固定输出和失败模式。
- `agents/openai.yaml`：Codex 展示名称、简介和默认提示词。
- `test-prompts.json`：正向、反向和边界触发测试。
- `test-results.md`：当前测试记录。

校验脚本会检查：

- 16 个 Skill 是否齐全。
- `name`、`description` 和字符串型 `metadata` 是否符合开放规范。
- 相邻 Skill 引用是否存在。
- 公共仓库内容是否包含客户项目、个人路径或原书摘录。
- 三端包是否只携带各自需要的运行文件。
- WorkBuddy ZIP 的根目录是否包含 `SKILL.md`。
- 发布文件 SHA-256 是否一致。

## 贡献

欢迎提交 Issue 和 Pull Request。新增或修改 Skill 时，请同步维护触发测试，并遵守 [CONTRIBUTING.md](CONTRIBUTING.md) 中的来源与隐私要求。

## License

仓库原创代码与文本采用 [MIT License](LICENSE)。原书内容及相关权利归原作者和出版方所有，MIT License 不扩展至原书内容。详见 [NOTICE](NOTICE)。
