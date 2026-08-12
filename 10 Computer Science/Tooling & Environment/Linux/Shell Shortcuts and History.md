---
aliases: [常用快捷键, Shell Shortcuts and History, history, Ctrl shortcuts]
tags: [linux, shell]
up: "[[Linux MOC]]"
related: "[[Text Processing, Pipes, and Redirection|文本处理与管道]], [[Environment Variables|环境变量]], [[The Vi Editor|vi 编辑器]]"
down: ""
---
# Shell Shortcuts and History

> [!summary] 核心结论
> 命令行高效操作的快捷键与历史功能：`Ctrl+C` 强制停止、`Ctrl+D` 退出登录、`Ctrl+L`/`clear` 清屏、`Ctrl+R` 反向搜索历史命令、`history` 查看历史、`!前缀` 重跑上一条匹配命令，以及 `Ctrl+A/E` 行首行尾跳转。

---

## 1. Stopping and Exiting (停止与退出)

| Shortcut  | Effect |
| --------- | ------ |
| `Ctrl + C` | **Force-stop** the running program, or abort the current half-typed line and start over |
| `Ctrl + D` | **Log out** of the current shell/account, or exit certain interactive programs |

## 2. Searching Command History (历史命令)

- **`history`** — list previously entered commands.
- **`Ctrl + R`** — reverse-search history: start typing and it matches the most recent
  command containing that text.
  - **Enter** runs the matched command immediately.
  - **← / →** pull the command onto the prompt **without** running it (so you can edit it).
- **`!<prefix>`** — re-run the most recent command starting with `<prefix>`
  (e.g. `!ssh` re-runs the last `ssh ...`).

## 3. Clearing the Screen (清屏)

- **`Ctrl + L`** — clear the terminal.
- **`clear`** — the command equivalent, same effect.

## 4. Moving the Cursor (光标移动)

| Shortcut    | Effect |
| ----------- | ------ |
| `Ctrl + A`  | Jump to the **beginning** of the line |
| `Ctrl + E`  | Jump to the **end** of the line |
| `Ctrl + ←`  | Move **left one word** |
| `Ctrl + →`  | Move **right one word** |

---

> [!important] 一句话总结
> `Ctrl+C` 救场、`Ctrl+R` 翻历史、`Ctrl+A/E` 跳行首尾——这几个键能显著减少在命令行里的重复敲字。
