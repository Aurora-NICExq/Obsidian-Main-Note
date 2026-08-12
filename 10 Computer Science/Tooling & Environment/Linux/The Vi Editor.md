---
aliases: [vi编辑器, The Vi Editor, vim]
tags: [linux, editor]
up: "[[Linux MOC]]"
related: "[[Text Processing, Pipes, and Redirection|文本处理与管道]], [[File Operations|文件操作]], [[Users, Groups, and Permissions|用户与权限]]"
down: ""
---
# The Vi Editor

> [!summary] 核心结论
> `vi`/`vim` 是 Linux 上几乎必装的终端文本编辑器，核心是三种模式：**命令模式 (Command)** 解释按键为命令、**输入模式 (Insert)** 自由编辑文本、**底线命令模式 (Last-line)** 以 `:` 开头执行保存/退出。三者之间靠 `i a o`（进入输入）、`ESC`（回命令）、`:`（进底线）切换。

前置知识：[[File Operations|文件操作]]（创建与查看文件）。

---

## 1. Opening a File (打开文件)

```bash
vi <file-path>
vim <file-path>
```

- If the file **does not exist**, this starts editing a **new** file (saved on first write).
- If the file **exists**, it opens for editing.

## 2. The Three Modes (三种工作模式)

- **Command mode (命令模式)** — the mode you start in. Keystrokes are interpreted as
  **commands**, not text; you cannot type content freely here.
- **Insert mode (输入模式 / 编辑模式)** — free text editing. Entered from command mode with
  `i`, `a`, `o`, etc.
- **Last-line mode (底线命令模式)** — begins with `:`; used for saving, quitting, search,
  and other file-level operations (e.g. `:wq` to write and quit, `:q!` to quit without
  saving).

## 3. Switching Between Modes (模式切换)

![[tikz-the-vi-editor-01.svg]]

## 4. Entering Insert Mode (进入输入模式的按键)

From **command mode**, these keys switch to insert mode at different positions:

| Mode    | Key   | Description |
| ------- | ----- | ----------- |
| Command | `i`   | Insert **at** the current cursor position |
| Command | `a`   | Insert **after** the current cursor position |
| Command | `I`   | Insert at the **beginning of the line** |
| Command | `A`   | Insert at the **end of the line** |
| Command | `o`   | Open a new line **below** and insert |
| Command | `O`   | Open a new line **above** and insert |
| Insert  | `ESC` | Return to command mode (works from any state) |

---

> [!important] 一句话总结
> 记住一条回路：`ESC` 永远回到命令模式，命令模式用 `i/a/o` 去编辑、用 `:wq` 去保存退出。卡住时先按 `ESC`，再决定下一步。
