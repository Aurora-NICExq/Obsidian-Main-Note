---
aliases: [文件操作, File Operations, mkdir touch cp mv rm, find which, 软连接]
tags: [linux, filesystem]
up: "[[Linux MOC]]"
related: "[[File System and Navigation|文件系统与导航]], [[Archiving and Compression|压缩与解压]], [[Text Processing, Pipes, and Redirection|文本处理与管道]], [[Users, Groups, and Permissions|用户与权限]]"
down: "[[Archiving and Compression|压缩与解压]]"
---
# File Operations

> [!summary] 核心结论
> 文件与目录的增删改查命令：`mkdir` 建目录、`touch` 建文件、`cat`/`more` 看内容、`cp`/`mv` 复制移动、`rm` 删除。目录操作普遍用 `-r`（递归），删除用 `-f`（强制）。`find`/`which` 用于查找文件和命令，`ln -s` 创建软链接（快捷方式）。

前置知识：[[File System and Navigation|文件系统与导航]]（路径与特殊路径符）。

---

## 1. Creating Directories — `mkdir` (创建目录)

`mkdir` (**Make Directory**) creates new directories.

```
mkdir [-p] path
```

The path argument is **required** and may be relative or absolute:

```bash
mkdir demo                    # in the current directory
mkdir /home/itheima/test      # absolute path
```

- **`-p`** — create any missing **parent** directories along the way. Without it,
  `mkdir a/b/c` fails if `a` or `a/b` does not exist; with `-p` it creates the whole chain.

## 2. Creating and Viewing Files (创建与查看文件)

- **`touch path`** — create an empty file (or update an existing file's timestamp). No
  options; the path may be relative, absolute, or use special path symbols.
- **`cat path`** — dump the **entire** file content to the terminal at once.
- **`more path`** — view content **page by page** (Space = next page, `q` = quit). Better
  than `cat` for long files.

## 3. Copying and Moving — `cp`, `mv` (复制与移动)

```
cp [-r] source destination       # cp = copy
mv source destination            # mv = move
```

- **`cp -r`** — the `-r` (recursive) option is **required when copying a directory** and
  its contents.
- **`mv`** — moves a file/directory. If the destination does not exist, `mv` **renames**
  the source instead. So `mv old.txt new.txt` is how you rename a file.

## 4. Deleting — `rm` (删除)

```
rm [-r -f] path1 path2 ... pathN
```

- **`-r`** — recursive; required to delete a **directory** (same idea as `cp -r`).
- **`-f`** — force; delete without the confirmation prompt. Normal users rarely see a
  prompt anyway; `-f` mainly matters for `root`.

> [!warning]
> `rm -rf` is irreversible — there is no recycle bin. `rm -rf /` or `rm -rf ~` can wipe a
> system or home directory. Double-check the path before pressing Enter.

### Wildcards (通配符 `*`)

`rm` (and many commands) support `*`, which matches **any content, including empty**:

- `test*` — anything **starting with** `test`
- `*test` — anything **ending with** `test`
- `*test*` — anything **containing** `test`

## 5. Finding Files — `find` (查找文件)

Search the directory tree for files by name or size.

```
find <start-path> -name "<filename>"      # by name (supports * wildcard)
find <start-path> -size +|-n[kMG]         # by size
```

For `-size`: `+` means larger than, `-` means smaller than, `n` is the number, and
`k`/`M`/`G` are KB/MB/GB. Example: `find / -size +100M` finds files larger than 100 MB.

## 6. Locating Commands — `which` (查找命令位置)

Every command is really a binary executable (like a `.exe` on Windows). `which` shows
where a command's program file lives:

```bash
which ls        # e.g. /usr/bin/ls
```

## 7. Symbolic Links — `ln -s` (软链接)

A **symbolic (soft) link** points to a file or directory in another location, much like a
Windows shortcut.

```
ln -s source destination
```

- **`-s`** — create a *symbolic* link (without `-s` you get a hard link).
- **source** — the existing file/directory being linked to.
- **destination** — where the link is created.

Example — repointing the system timezone file (used in [[Systemd Service Management]]):

```bash
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

---

> [!important] 一句话总结
> 记住"目录操作加 `-r`"这条主线：`cp -r`、`rm -r`、`mkdir -p` 处理目录层级；`find`/`which` 负责"找东西"，`ln -s` 负责"建快捷方式"。打包压缩见 [[Archiving and Compression]]。
