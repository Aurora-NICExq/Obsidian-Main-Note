---
aliases: [Linux用户与权限, Users Groups and Permissions, 用户与权限, chmod chown, sudo, rwx]
tags: [linux, permissions]
up: "[[Linux MOC]]"
related: "[[File Operations|文件操作]], [[Processes and Scheduling|进程与调度]], [[Systemd Service Management|systemd 服务管理]], [[The Vi Editor|vi 编辑器]]"
down: ""
---
# Users, Groups, and Permissions

> [!summary] 核心结论
> Linux 是多用户系统：`root` 是超级用户，普通用户出了自己的 HOME 大多只有读/执行权限。`su`/`sudo` 用于切换用户或临时提权。权限管控分**用户、用户组、其它**三档，每档用 `rwx` 三位表示；`chmod` 改权限（数字 4/2/1）、`chown` 改归属。

前置知识：[[File Operations|文件操作]]（文件/目录概念）。

---

## 1. The `root` User (root 超级用户)

- A normal user generally has full control **inside their own HOME directory**.
- Outside HOME, in most places a normal user has only **read and execute** permission — no
  write. `root` (the superuser) bypasses these restrictions.

### `su` and `sudo` (账户切换与提权)

`su` (**Switch User**) changes the current account:

```
su [-] [username]
```

- **`-`** — load the target user's environment after switching (recommended).
- **username** — the user to switch to; omit it to switch to `root`.
- Return to the previous user with `exit` or `Ctrl + D`.

`sudo` runs a **single command** temporarily as `root`:

```
sudo <command>
```

Not every user may use `sudo`; a normal user must first be granted `sudo` authorization.

#### Granting a User `sudo` Access (配置 sudo 认证)

1. As `root`, run `visudo`, which opens `/etc/sudoers` in the [[The Vi Editor|vi editor]].
2. Add a line at the end:

```text
itheima ALL=(ALL) NOPASSWD: ALL
```

- The trailing `NOPASSWD: ALL` means `sudo` will **not prompt for a password**.

3. Save with `:wq`, switch back to the normal user — its `sudo` commands now run as `root`.

## 2. Users and Groups (用户与用户组)

Linux supports multiple users and multiple groups; a user can belong to several groups.
Permissions are controlled at **two levels**: per-user and per-group.

### Group Management (用户组管理)

```bash
groupadd <group>      # create a group
groupdel <group>      # delete a group
```

### User Management (用户管理)

```bash
useradd [-g -d] <username>     # create a user
userdel [-r] <username>        # delete a user
id [username]                  # show a user's groups (self if omitted)
usermod -aG <group> <username> # add a user to a group
```

- **`useradd -g`** — set the user's group. Without `-g`, a same-named group is created and
  the user joined to it; with `-g`, the group must already exist.
- **`useradd -d`** — set the HOME path (default `/home/<username>`).
- **`userdel -r`** — also delete the user's HOME directory; without `-r`, HOME is kept.

## 3. Reading Permissions — `rwx` (权限信息)

| Symbol | On a file | On a directory |
| ------ | --------- | -------------- |
| `r` (read)    | view file content | list contents (`ls`) |
| `w` (write)   | modify the file | create / delete / rename inside it |
| `x` (execute) | run it as a program | `cd` into it |

A long listing (`ls -l`) shows a 10-character permission string: 1 type slot + three
`rwx` triples for **owner**, **group**, and **other**.

![[tikz-users-groups-and-permissions-01.svg]]

## 4. Changing Permissions — `chmod` (修改权限)

`chmod` changes a file's/directory's permissions. Only the **owner** or `root` may do so.

```
chmod [-R] <permissions> <file-or-dir>
```

- **`-R`** — apply recursively to everything inside a directory.

### Octal Notation (权限的数字序号)

Permissions can be written as **three digits** — owner, group, other. Within each digit:
`r = 4`, `w = 2`, `x = 1`, summed together.

- `7` = `4+2+1` = `rwx`
- `6` = `4+2` = `rw-`
- `5` = `4+1` = `r-x`

So `chmod 755 file` gives the owner `rwx` and group/other `r-x`.

## 5. Changing Ownership — `chown` (修改归属)

`chown` changes the owning user and/or group. A normal user cannot reassign ownership to
others, so this is effectively a `root`-only command.

```
chown [-R] [user][:][group] <file-or-dir>
```

- **`-R`** — recursive, like `chmod`.
- **user** — new owning user; **group** — new owning group; **`:`** separates the two
  (e.g. `chown itheima:devs file`).

---

> [!important] 一句话总结
> "权限分 用户/组/其它 三档，每档 `rwx`；`chmod` 用 4/2/1 改权限，`chown` 改归属，`-R` 递归"。提权记 `sudo`，切换用户记 `su -`。
