---
aliases: [命令入门, File System and Navigation, Linux Filesystem, ls cd pwd]
tags: [linux, filesystem]
up: "[[Linux MOC]]"
related: "[[File Operations|文件操作]], [[Text Processing, Pipes, and Redirection|文本处理与管道]], [[Users, Groups, and Permissions|用户与权限]], [[Environment Variables|环境变量]]"
down: "[[File Operations|文件操作]]"
---
# File System and Navigation

> [!summary] 核心结论
> Linux 没有盘符 (drive letter)，所有文件都挂在唯一的根目录 `/` 下，构成一棵单一的目录树。导航的三个基础命令是 `ls`（列目录）、`cd`（切换目录）、`pwd`（打印当前目录）。终端启动后默认位于当前用户的 **HOME 目录**，而不是根目录。

---

## 1. The Single Directory Tree (单一目录树)

Unlike Windows, Linux has **no drive letters** (`C:`, `D:`). Everything hangs under one
root directory, written `/`. Every file and device is reachable as a path starting from `/`.

When a terminal starts, the **current working directory** is the logged-in user's **HOME
directory**, not the root. A user's HOME directory follows the pattern:

```
/home/<username>
```

For example, the user `itheima` has the HOME directory `/home/itheima`. This is why a bare
`ls` right after opening a terminal lists the HOME directory's contents, not `/`.

## 2. General Command Format (命令的通用格式)

Every command, regardless of purpose, follows the same shape:

```
command [-options] [parameter]
```

- **command** — the command itself (e.g. `ls`).
- **-options** — optional flags that tune the command's behaviour.
- **parameter** — optional argument, usually the target the command acts on.

The `[]` in syntax descriptions marks a part as **optional**.

## 3. `ls` — List Directory Contents (列出目录内容)

```
ls [-a -l -h] [path]
```

With no options or path, `ls` prints the contents of the current working directory in a
flat layout. Common options (which **combine freely**, e.g. `ls -lh`):

| Option | Meaning |
| ------ | ------- |
| `-a`   | Show **all** files, including hidden ones (names starting with `.`) |
| `-l`   | **Long** format: permissions, owner, size, modification time, name |
| `-h`   | **Human-readable** sizes (KB/MB/GB); only meaningful together with `-l` |

> [!tip]
> `ls -lh` is the everyday combination — a detailed listing with readable file sizes.

## 4. `cd` — Change Directory (切换工作目录)

`cd` (**Change Directory**) moves the shell to another directory.

```
cd [path]
```

- `cd` takes **no options**; it is driven purely by its path argument.
- A bare `cd` with no argument returns to the **current user's HOME directory**.

## 5. `pwd` — Print Working Directory (查看当前目录)

`pwd` (**Print Working Directory**) prints the full absolute path of where you currently
are.

```
pwd
```

It takes no options and no parameters. Note the difference from `ls`: `ls` lists *what is
inside* a directory, while `pwd` answers *where you are*.

## 6. Absolute vs Relative Paths (绝对路径与相对路径)

- **Absolute path** — described from the **root** `/`; always begins with `/`
  (e.g. `/home/itheima/test`).
- **Relative path** — described from the **current directory**; does **not** begin with `/`
  (e.g. `test`, `./test`).

### Special Path Symbols (特殊路径符)

| Symbol | Meaning |
| ------ | ------- |
| `.`    | The **current** working directory |
| `..`   | The **parent** directory (one level up) |
| `~`    | The **current user's HOME** directory |

Example: from `/home/itheima/docs`, `cd ..` moves to `/home/itheima`, and `cd ~` jumps
straight to `/home/itheima` from anywhere.

---

> [!important] 一句话总结
> 一切从 `/` 开始，用 `pwd` 知道"我在哪"，用 `ls` 知道"这里有什么"，用 `cd` + 路径（绝对或相对，配合 `.` `..` `~`）决定"去哪里"。下一步是对文件本身的操作，见 [[File Operations]]。
