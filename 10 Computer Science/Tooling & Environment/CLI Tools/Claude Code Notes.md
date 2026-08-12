---
tags:
  - cli
  - tooling
---
# Claude Code 使用笔记

---

## 一、CLAUDE.md 文件

### 是什么

CLAUDE.md 是 Claude Code 自动读取的特殊配置文件，每次启动会话时会自动加载到上下文中，相当于给 Claude 的"项目说明书"，让它快速理解你的项目规范和工作方式。

### 三级配置层级（优先级从高到低）

| 层级 | 路径 | 用途 |
|------|------|------|
| 项目本地（个人） | `.claude/CLAUDE.md` | 个人私有偏好，加入 `.gitignore` |
| 项目级（团队共享） | `项目根目录/CLAUDE.md` | 提交到 git，团队共享规范 |
| 全局用户级 | `~/.claude/CLAUDE.md` | 跨所有项目的个人偏好 |

### 快速生成

在项目目录启动 Claude Code 后执行 `/init`，Claude 会自动分析项目结构、代码风格、配置文件，生成一份初始 CLAUDE.md，再手动补充调整。

### 推荐内容结构

```markdown
## 项目说明
[简要描述项目是什么、做什么]

## 技术栈
[使用的语言、框架、主要依赖]

## 常用命令
- 启动：`npm run dev`
- 测试：`npm test`
- 构建：`npm run build`

## Platform Rules（针对内容创作类项目）
- LinkedIn：[格式、长度、CTA 风格]
- X：[格式、话题标签规则、帖子串规则]
- Instagram：[说明文字长度、话题标签数量、语气]

## 编码规范
[代码风格、命名约定、注释语言等]

## Gotchas（易踩坑的地方）
- [项目中反直觉的设定]
- [需要避免的遗留代码]
- [Claude 可能误判的受众假设]

## Workflow（工作流约定）
- [每次输出几个变体]
- [文件命名规范]
- [哪些操作必须经过你审批]
```

### 导入其他文件

CLAUDE.md 支持用 `@路径` 语法导入其他文件：

```markdown
查看 @README 了解项目概述，查看 @package.json 了解可用命令。

# Git 工作流

@docs/git-instructions.md
```

---

## 二、上下文管理

### 上下文衰减（Context Rot）

官方文档明确指出：**上下文窗口是 Claude Code 最重要的资源**。随着对话越来越长，模型需要处理全部历史内容，性能会逐渐下降，这称为"上下文衰减"（context rot）。

### `/compact` — 手动压缩上下文

将长对话历史压缩为精简摘要，让会话可以继续进行而不丢失核心信息。

```bash
/compact                        # 直接压缩
/compact 保留认证模块的完整讨论   # 指定压缩时重点保留的内容
```

**注意事项：**
- 压缩是**有损操作**，细节会丢失
- Claude Code 在上下文约 75% 时会自动触发压缩
- **建议在 60~70% 时主动触发**，避免在关键任务中间被打断
- 压缩时可以通过指令控制保留哪些内容，比自动压缩更精准

**绕过自动压缩的场景：** 当你担心自动压缩丢失重要背景（如正在进行的复杂架构讨论），可以在接近阈值前先手动 `/compact` 并明确指定保留内容。

### `/clear` — 清空上下文

彻底清空当前会话的所有上下文，从零开始。适合切换到完全不同的任务时使用。

```bash
/clear
```

### `/context` — 查看上下文占用

查看当前上下文的占用情况，并给出优化建议，例如：
- 上下文已满 80% 以上 → 建议运行 `/compact`
- 某次工具调用返回内容过大 → 建议缩小查询范围
- CLAUDE.md 文件过大 → 建议精简

---

## 三、Plan 规划模式

### 是什么

在 Plan Mode 下，Claude 只进行分析和规划，**不会执行任何实际操作**（不读写文件、不运行命令）。相当于先让 Claude 出一份详细方案，你审批后再执行。

### 如何开启

**方式一：会话中切换（推荐）**

按 `Shift + Tab` 在以下模式间循环切换：

```
normal → ⏵⏵ accept edits on → ⏸ plan mode on → normal
```

**方式二：启动时指定**

```bash
claude --permission-mode plan
```

### 使用流程

1. 按 `Shift + Tab` 进入 Plan Mode
2. 输入详细需求（`Shift + Enter` 换行）
3. Claude 生成执行计划
4. 选择：执行并进入自动模式 / 执行但保持询问模式 / 继续修改计划

### 最佳实践

> Plan Mode 不是开销，是投资。先探索再编码，可以大幅减少返工。

对于复杂任务，可以结合深度思考关键词：
- `think` < `think hard` < `think harder` < `ultrathink`（依次增加思考预算，消耗更多 token）

---

## 四、权限管理

### 五种权限模式

| 模式 | 描述 | 开启方式 |
|------|------|---------|
| `normal`（默认） | 每次敏感操作都弹窗确认 | 默认 |
| `acceptEdits` | 自动批准文件编辑，其他操作仍需确认 | `Shift + Tab` 循环 |
| `plan` | 只规划不执行 | `Shift + Tab` 循环 |
| `dontAsk` | 执行常用安全操作不询问 | `claude --permission-mode dontAsk` |
| `bypassPermissions` | 绕过所有权限确认，直接执行一切操作 | `claude --dangerously-skip-permissions` |

### 推荐做法：白名单预授权

比直接用 `--dangerously-skip-permissions` 更安全的方式是在 `.claude/settings.json` 中配置白名单，预授权常用的安全操作：

```json
{
  "permissions": {
    "allow": [
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(npm test:*)"
    ],
    "defaultMode": "acceptEdits"
  }
}
```

### `--dangerously-skip-permissions` 的适用场景

适合批量低风险操作（如修复 100 个 lint 错误、全局重命名函数），不适合在重要项目上不加审查地使用。**在 root 身份下无法使用此模式。**

---

## 五、斜杠命令（Slash Commands）

### 内置常用命令

```bash
/compact          # 压缩上下文
/clear            # 清空上下文
/context          # 查看上下文占用
/init             # 自动生成 CLAUDE.md
/memory           # 编辑 CLAUDE.md 文件
/model            # 切换模型
/mcp              # 查看 MCP 服务器状态
/permissions      # 查看权限配置
/hooks            # 配置钩子
/vim              # 开启 Vim 编辑模式
/branch           # 将当前对话分支到新会话（原 /fork）
```

### 自定义斜杠命令

在 `.claude/commands/` 目录下新建 `.md` 文件即可创建项目级自定义命令；在 `~/.claude/commands/` 下创建则是全局命令。

```bash
# 创建项目级命令
mkdir -p .claude/commands
echo "分析这段代码的性能问题并给出优化建议：" > .claude/commands/optimize.md

# 创建全局命令
mkdir -p ~/.claude/commands
echo "检查这段代码的安全漏洞：" > ~/.claude/commands/security.md

# 支持参数传递
echo '按照我们的编码规范修复 issue #$ARGUMENTS' > .claude/commands/fix-issue.md
# 使用时：/fix-issue 123
```

> **注意：** 自定义斜杠命令已逐渐并入 Skills 体系（`.claude/skills/`），两种方式目前均支持，但 Skills 是推荐的新方式。

---

## 六、Skills（技能）

### 是什么

Skills 是可复用的工作流模块，存放在 `.claude/skills/` 目录下，每个 Skill 有一个 `SKILL.md` 描述文件，告诉 Claude 在什么情况下使用该技能以及如何使用。

```
.claude/
└── skills/
    └── my-skill/
        └── SKILL.md    # 技能描述和使用说明
```

### 安装方式

```bash
# 安装到当前项目（本地）
claude /plugin install frontend-design --local

# 安装为全局（所有项目可用）
claude /plugin install frontend-design
```

### 通过插件市场获取

```bash
# 添加官方插件市场
claude /plugin marketplace add anthropics/skills

# 浏览可用插件
claude /plugin

# 安装常用插件
claude /plugin install document-skills    # 文档处理
claude /plugin install frontend-design    # 前端开发
claude /plugin install git-workflow       # Git 工作流
```

---

## 七、Hooks（钩子）

### 是什么

Hooks 是在 Claude Code 会话特定节点自动触发的脚本，让你可以在 Claude 操作前后插入自定义逻辑，实现自动化检查、格式化、通知等功能。

### 配置方式

在 `.claude/settings.json` 中配置（也可在 `~/.claude/settings.json` 全局配置）：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo '即将执行 Bash 命令' >> /tmp/claude.log"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/hooks/auto_format.py"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/hooks/quality_check.py"
          }
        ]
      }
    ]
  }
}
```

### 主要事件类型

| 事件 | 触发时机 |
|------|---------|
| `PreToolUse` | Claude 调用工具**之前**，可用于拦截/阻断 |
| `PostToolUse` | Claude 调用工具**之后**，可用于自动格式化 |
| `Stop` | Claude 完成一轮回答后，可用于质量检查 |
| `SessionStart` | 会话开始时，每次会话触发一次 |
| `SessionEnd` | 会话结束时，每次会话触发一次 |
| `UserPromptSubmit` | 用户提交每条消息时 |
| `Notification` | Claude 发出通知时 |

### matcher 规则

```json
"matcher": "Bash"              // 只针对 Bash 命令
"matcher": "Write|Edit"        // 针对文件写入或编辑
"matcher": "*"                 // 针对所有工具
```

> `matcher` 只适用于 `PreToolUse` 和 `PostToolUse`，`Stop`、`SessionStart` 等事件不需要指定 matcher。

### 实用场景示例

- **`PreToolUse`**：在执行 `rm` 等危险命令前自动阻断并记录日志
- **`PostToolUse`**：文件编辑后自动运行 `black`/`prettier` 格式化
- **`Stop`**：任务完成后自动运行测试套件，或发送桌面通知

---

## 八、MCP（模型上下文协议）

### 是什么

MCP 让 Claude Code 能够连接外部工具和服务（如 GitHub、数据库、Sentry 等），将这些服务的功能变成可直接调用的能力。

### 基本命令

```bash
# 添加 MCP 服务器（HTTP 协议）
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# 查看已连接的服务器列表
claude mcp list

# 获取特定服务器信息
claude mcp get github

# 删除服务器
claude mcp remove github

# 在会话中查看服务器状态
/mcp
```

### `--scope` 参数：指定配置存储位置

| scope | 说明 |
|-------|------|
| `local`（默认） | 仅当前项目对当前用户可用 |
| `project` | 通过 `.mcp.json` 文件与项目所有成员共享 |
| `user` | 在所有项目中对当前用户可用 |

### 使用 MCP 工具

连接后，MCP 服务器的功能以斜杠命令形式出现：

```bash
/mcp__github__list_prs               # 列出 GitHub PR
/mcp__jira__create_issue "登录按钮失效" high  # 创建 Jira 问题
```

---

## 九、子代理（SubAgent）

### 为什么使用子代理

长时间在同一窗口对话会导致上下文衰减。针对不同任务使用子代理，可以**隔离上下文**，让每个子代理专注于单一任务，提高执行质量。

### 工作原理

主代理收到复杂任务后，可以 fork 出多个子代理并行处理不同子任务，各子代理拥有独立的上下文窗口，互不干扰。

### 典型场景

- 同时进行多个独立模块的开发
- 一个子代理写代码，另一个子代理写测试
- 长任务拆分为阶段性子任务，每阶段开新会话

### 会话恢复

```bash
claude --continue    # 继续上次会话
claude --resume      # 选择历史会话恢复
```

---

## 十、插件市场

插件（Plugin）是打包了 Skills、斜杠命令、Hooks、MCP 配置等的完整功能包，可以从插件市场一键安装他人共享的工作流套件。

```bash
# 添加插件市场
claude /plugin marketplace add anthropics/skills

# 浏览插件
claude /plugin

# 安装本地插件
claude plugin install ./my-plugin
```

一个典型的插件结构：

```
my-plugin/
├── plugin.json        # 插件配置
├── skills/            # Skills 目录
├── commands/          # 自定义斜杠命令
├── mcp/               # MCP 配置
├── agents/            # 子代理定义
└── hooks/             # Hook 脚本
```

---

## 十一、最重要的规划原则

> 来自 Claude Code 最佳实践

1. **验证 > 信任** — 给 Claude 验证手段，不要盲目信任输出
2. **上下文是最贵的资源** — `/clear` 是你最好的朋友，子代理是上下文防火墙
3. **具体 > 模糊** — 一次精准的指令胜过三次模糊的修正
4. **先探索再编码** — Plan Mode 不是开销，是投资
5. **配置是长期杠杆** — 在 CLAUDE.md / Hooks / Skills 上花的时间，每次会话都在回报
6. **预批准而非跳过权限** — `/permissions` 白名单 > `--dangerously-skip-permissions`
7. **犯错后更新规则** — 每个错误都是改进 CLAUDE.md 的机会
