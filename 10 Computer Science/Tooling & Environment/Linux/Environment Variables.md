---
aliases: [环境变量, Environment Variables, PATH, export, bashrc]
tags: [linux, shell]
up: "[[Linux MOC]]"
related: "[[Shell Shortcuts and History|快捷键与历史]], [[Text Processing, Pipes, and Redirection|文本处理与管道]], [[Users, Groups, and Permissions|用户与权限]], [[File Operations|文件操作]]"
down: ""
---
# Environment Variables

> [!summary] 核心结论
> 环境变量是操作系统运行时记录的一批 **Key=Value** 关键信息（`env` 查看），用 `$名字` 取值。最重要的是 `PATH`（命令搜索路径）。自定义变量：`export 名=值` 临时生效；写入 `~/.bashrc`（当前用户）或 `/etc/profile`（所有用户）并 `source` 后永久生效。

前置知识：[[Text Processing, Pipes, and Redirection|echo 与 shell]]。

---

## 1. What Environment Variables Are (环境变量是什么)

Environment variables are key pieces of information the OS records at runtime to support
its own operation. They are a **Key=Value** structure (a name and a value). List the
current ones with:

```bash
env
```

## 2. Reading a Variable with `$` (用 $ 取值)

In the shell, `$` retrieves a variable's value:

```
$<variable-name>
```

```bash
echo $PATH        # print the PATH variable
```

`PATH` is the list of directories the shell searches for executables — it is why you can
type `ls` instead of `/usr/bin/ls`.

> [!tip]
> When a variable name sits next to other text, wrap it in braces to mark its boundary:
> `${VAR}_suffix` (without braces, `$VAR_suffix` would look up a variable named
> `VAR_suffix`).

## 3. Setting Variables (自行设置环境变量)

### Temporary (临时设置)

Effective only in the current shell session:

```bash
export <name>=<value>
```

### Permanent (永久生效)

Write the `export` line into a startup file:

| Scope | File |
| ----- | ---- |
| Current user only | `~/.bashrc` |
| All users | `/etc/profile` |

Then reload the file so changes take effect immediately (without re-login):

```bash
source <config-file>      # e.g. source ~/.bashrc
```

Example — adding a directory to `PATH` permanently for the current user:

```bash
echo 'export PATH=$PATH:/opt/myapp/bin' >> ~/.bashrc
source ~/.bashrc
```

---

> [!important] 一句话总结
> "`env` 看变量、`$名` 取值、`export` 设变量；想永久就写进 `~/.bashrc` 或 `/etc/profile` 再 `source`"。`PATH` 是其中最该理解的一个。
