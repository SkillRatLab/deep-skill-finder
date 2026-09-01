<div align="center">

# deep-skill-finder

**只需安装一次。让你的 Agent 选择真正能运行的 Skill，而不是排名靠前的那个。**

*一个 Agentic Skill 发现引擎。让你的 Claude Code / Codex / OpenClaw / Cursor 从 50k+ Skill 生态中，针对每项任务自动发现最合适的 Skill。*

![deep-skill-finder](assets/background.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Live in 40+ Agents](https://img.shields.io/badge/live%20in-40%2B%20AI%20Agents-8A2BE2.svg)](#生态支持情况)
[![Skills](https://img.shields.io/badge/skills-50k%2B-brightgreen.svg)](https://www.meyo.life/skill)

[English](README.md) | 中文

</div>

---

## 🚀 在你的 Agent 中安装（30 秒）

复制下面的提示词，发送给你的 Agent（Claude Code / Codex / OpenClaw / Cursor / 其他 40+ 已支持的 Agent）：

```
请安装 deep-skill-finder Skill：从
https://www.meyo.life/api/v1/skill-finder 下载安装包，解压到本地 Skills
目录并启用。
```

就是这么简单。安装通常只需 15～30 秒。如果不喜欢，随时可以用一条命令[卸载](#脚本参考)。下次你的 Agent 需要 Skill 时，DSF 会自动寻找候选项，并在安装前征得你的确认。

---

## 为什么选择 deep-skill-finder

使用 Agent 往往需要安装 Skills。但究竟哪个 Skill 能真正解决**你的具体任务**？

**每位 Agent 用户都会遇到两个问题：**

- **找不到真正需要的 Skill。** 为了出现在更多搜索结果中，创作者往往会写宽泛、抽象的描述。你的具体需求就这样被淹没在噪声里。
- **无法信任找到的 Skill。** 下载量和 Star 数无法证明一个 Skill 能否正确运行。你安装一个，它在你的任务上报错；卸载后再试另一个。20 分钟过去，你还在寻找。

**deep-skill-finder 同时解决这两个问题。** 只需安装一次，你的 Agent 就能自主完成 Skill 的发现、评估和安装；排序依据是真实的社区运行记录以及与任务的匹配度，而不是下载量。

*下方是 3 个真实案例 ↓*

---

## 实际效果：3 个真实案例

**案例 1：GitHub Actions CI/CD**
> 其他工具找到：`github-actions-gen` —— 文档简略，运行时存在 Bug
> DSF 找到：`cicd-pipeline-generator` —— 文档详细，提供可直接复制的示例，运行顺利

**案例 2：股票市场数据（龙虎榜）**
> 其他工具找到：`pywencaistock` —— 所有数据接口均已失效
> DSF 找到：`lhb-api` —— 专为该数据源构建，3 个 API 调用全部通过

**案例 3：博客翻译（GPT-4o → 中文）**
> 其他工具找到：`translation-pro` —— 翻译准确，但表达生硬，不够通俗易懂
> DSF 找到：`blog-polish-zhcn` —— 翻译、润色并保留术语，175 秒完成

---

## 工作原理 · 8 层智能排序

deep-skill-finder 不止进行关键词匹配。它会从八个层面对每个候选 Skill 进行综合判断，优先关注真实能力与任务适配度，而不是表面的文本相似性。

1. **元意图识别** — 当用户寻找的就是“用于发现 Skill 的工具”时，deep-skill-finder 能识别这一元意图，并优先推荐正确的技能发现工具。
2. **真实能力优先** — 优先依据结构化能力信息判断 Skill 实际能做什么，避免被夸大的宣传描述或表面关键词误导。
3. **意图方向推理** — 准确区分“A → B”和“B → A”等方向相反的工作流，避免看似相关、实际能力方向错误的 Skill 排在前面。
4. **执行就绪度评估** — 对依赖隐含凭证、复杂配置、特殊环境，或仅提供方法文档而缺乏实际执行能力的 Skill 进行降权。
5. **多意图覆盖分析** — 面对复杂任务，优先推荐能够覆盖更多子目标和端到端流程的 Skill，而不是只能完成单一步骤的工具。
6. **社区证据验证** — 只有与用户真实意图一致的社区内容才会被视为有效佐证，避免无关热度干扰排序。
7. **根本冲突过滤** — 即使候选 Skill 与查询共享相似关键词，只要其能力与用户目标存在根本性冲突，就会被过滤。
8. **让热度回归正确位置** — 下载量只用于区分能力与匹配度接近的候选，绝不会凌驾于真实能力、意图方向和任务适配度之上。

**最终智能汇聚** — 由推理驱动的最终排序层将所有信号整合为完整、统一的判断，输出最多 5 个高置信度推荐，并为每个结果提供清晰、可直接辅助决策的推荐理由。

---

## 生态支持情况

deep-skill-finder 开箱即用地支持 **40+ Agent 运行环境**。无论你使用哪种 Agent，都能轻松接入：

- Claude Code · Codex · Cursor · Windsurf · Cline
- WorkBuddy · OpenClaw · CatDesk · Hermes
- Copilot · Gemini · Antigravity · Amp
- 以及另外 28+ 种 Agent

**近 30 天活跃数据** *（2026-08 · 每月更新）*：
- 40+ 种不同的 `agentType` 客户端调用过 DSF
- **真实用户通过 DSF 安装次数最多的 Skills**（每个均经 10+ 个不同客户端安装验证）：
  - `desktop-pet`（116 个客户端）· `ppt-maker`（115）· `product-compare`（102）· `business-plan`（81）· `amazon-a-plus-content`（78）

---

## 快速开始

### 前置条件
- 一个正在运行的 Agent（Claude Code / Codex / Cursor / 任意一种已支持的 40+ 客户端）

### 在你的 Agent 中安装

将下面的提示词直接发送给你的 Agent：

```
请安装 deep-skill-finder Skill：从
https://www.meyo.life/api/v1/skill-finder 下载安装包，解压到本地 Skills
目录并启用。
```

Agent 会自动完成下载、解压和启用。

### 使用方法

像平常一样自然地与 Agent 对话。当任务需要外部 Skill 时，DSF 会自动触发：

```
“帮我找一个能根据 CSV 构建交互式仪表盘的 Skill”
“有没有可以获取股票市场数据的 Skill？”
“推荐一个能把技术文档翻译成通俗英文的 Skill”
“搭建一套在每次 PR 时运行的 CI/CD 流水线”
```

DSF 会返回带有推荐理由的 TOP 5 排名。确认序号后，安装将自动完成。

---

## 架构

```
用户用自然语言描述任务
            │
            ▼
         意图理解
    （改写 → 语义查询）
            │
            ▼
         多渠道召回
  ┌─────────┬──────────────┐
  │ Skill   │   社区测试   │
  │ 画像    │     帖子     │
  └────┬────┴──────┬───────┘
       └─────┬─────┘
             ▼
     8 条规则语义排序
    → 带理由的 TOP 5
             │
             ▼
 确认序号 → 自动安装 → 运行 → 反馈闭环
```

安装完成后，整个闭环会自主运行：**识别 → 召回 → 确认 → 执行 → 反馈**。每一次匹配都会让后续结果更加准确。

---

## 项目结构

```
├── SKILL.md                  # Skill 定义（供 Agent 读取）
└── scripts/
    ├── deep_skill_search.py  # 通过 Meyo 检索服务进行语义搜索
    └── deep_skill_install.py # 下载并在本地安装 Skills
```

## 脚本参考

通常你不需要直接调用这些脚本，Agent 会代为执行。不过，你也可以独立运行它们：

**搜索：**
```bash
python3 scripts/deep_skill_search.py "你的任务描述" [--agent-type openclaw]
```

**安装 / 卸载 / 列出：**
```bash
# 安装
python3 scripts/deep_skill_install.py <skill-name> --dir ~/.catpaw/skills

# 卸载
python3 scripts/deep_skill_install.py <skill-name> --dir ~/.catpaw/skills --uninstall

# 列出已安装的 Skills
python3 scripts/deep_skill_install.py --dir ~/.catpaw/skills --list
```

---

## 常见问题

**问：下载量和 Star 数难道不是足够好的指标吗？**
答：下载量和 Star 数只能说明什么更*流行*，不能说明什么能在*你的具体任务*上正常运行。DSF 根据能力匹配度和真实社区运行记录进行排序。排序规则第 8 条明确规定：下载量只能用于打破平局，绝不能作为主要信号。

**问：“一个安装其他 Skills 的 Skill”——这算递归吗？安全吗？**
答：不算。DSF 只负责*推荐* Skills。在你的设备上执行任何安装前，都必须获得你的明确确认。每个推荐给你的 Skill 都会先通过安全审计和质量检查。

**问：如果我已经在使用 SkillHub / ClawHub / Vercel find-skills 呢？**
答：DSF 可以与它们协同使用，并不冲突。它会从所有主流 Skill 来源进行多渠道召回，包括 SkillHub、ClawHub、GitHub 和社区测试帖。安装 DSF，用一个任务试试效果，再决定是否继续使用。

**问：我需要注册账号吗？**
答：不需要。DSF 可以独立运行，无需注册或提供邮箱。除用于跨会话保持状态的匿名本地 UUID 外，不收集任何遥测数据。

**问：它支持哪些 Agent？**
答：支持 40+ Agent 运行环境，包括 Claude Code、Codex、OpenClaw、Cursor、Windsurf、Cline、WorkBuddy、Hermes、CatDesk、Copilot 等。

---

## 参与贡献

欢迎提交 Issue 和 Pull Request。

### 如果你是用户
- 如果某个 Skill 的排名过高或过低，其底层信号来自 [Meyo Community](https://www.meyo.life/community/home)。在那里留下真实运行记录，是改善未来排序结果最直接的方式。
- 通过 [Issues](https://github.com/wheelry/deep-skill-finder/issues) 报告问题，或申请覆盖特定任务/领域。

### 如果你是 Skill 创作者
- 我们索引全网 Skills，致力于构建最全面的 Skill 发现层。如果你的 Skill 没有出现在 DSF 的结果中，请[提交 Issue](https://github.com/wheelry/deep-skill-finder/issues) 并附上 Skill URL，我们会进行排查。
- 有兴趣合作发布一篇“为什么我把自己的 Skill 放到 DSF 上”的文章？欢迎通过 Issues 联系我们。

---

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=wheelry/deep-skill-finder&type=Date)](https://star-history.com/#wheelry/deep-skill-finder&Date)

---

## 觉得有帮助？

- ⭐ **[给本仓库点个 Star](../../stargazers)** —— 帮助更多 Agent 用户发现 DSF
- 💬 **[发起讨论](../../discussions)** —— 分享你的使用场景或提出问题
- 🐛 **[报告问题](../../issues)** —— 如果推荐结果看起来不准确，请告诉我们
- 📖 **[立即体验 DSF](#-在你的-agent-中安装30-秒)** —— 只需 30 秒即可安装

---

## 许可证

本项目采用 MIT 许可证，可在保留署名的前提下自由使用、修改和分发。详情请参阅 [LICENSE](LICENSE)。

---

## 相关链接

- **产品主页：** https://www.meyo.life/skill
- **社区：** https://www.meyo.life/community/skills
- **SkillHub 页面：** https://skillhub.cn/skills/deep-skill-finder
- **ClawHub 页面：** https://clawhub.ai/lintong123/skills/deep-skill-finder
