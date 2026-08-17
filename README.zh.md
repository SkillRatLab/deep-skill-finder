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

## 工作原理：8 条排序规则

deep-skill-finder 按照以下 8 条规则及其优先级对候选 Skill 进行排序：

1. **元 Skill 识别** —— 当你的查询意图是“帮我找一个 Skill”时，DSF 会将自己排在首位。
2. **功能相关性** —— 优先匹配 `capabilitySummary`（结构化能力描述），而不是可能被过度包装的 `description`。
3. **方向准确性** —— 区分“A→B”和“B→A”（例如，“PRD → 原型”≠“原型 → PRD”），降低方向错误的候选项排名。
4. **可完成性** —— 相关不等于真正可运行。需要未声明 API Key、复杂配置，或本身只是文档/元 Skill 的候选项会被降权。
5. **多意图覆盖** —— 优先选择能覆盖多个子意图的 Skill，而不是功能狭窄的单一用途 Skill。
6. **社区动态佐证** —— 只有当社区动态内容与任务意图一致时，才会将其计为有效证据。
7. **硬性过滤** —— 无论表面相关性多高，都会移除存在根本性错配的候选项。
8. **下载量仅用于打破平局** —— 热度只用于候选项难分高下时的最终判断，绝不作为主导因素。

**结果：** 面对同一任务和多个相关 Skill，DSF 选择的是最符合**你的具体需求**的那个，而不是下载量最高的那个。

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
