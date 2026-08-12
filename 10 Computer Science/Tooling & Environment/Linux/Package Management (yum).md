---
aliases: [yum命令, Package Management, yum, RPM, 软件安装]
tags: [linux, packaging]
up: "[[Linux MOC]]"
related: "[[Systemd Service Management|systemd 服务管理]], [[Arch Build System (PKGBUILD)|Arch 构建体系]], [[Networking Basics|网络基础]]"
down: "[[Systemd Service Management|systemd 服务管理]]"
---
# Package Management (yum)

> [!summary] 核心结论
> `yum` 是基于 RPM 的软件包管理器（用于 CentOS/RHEL 等发行版），自动下载、安装、卸载软件并自动解决依赖关系。核心用法是 `yum [-y] install|remove|search 软件名`，`-y` 自动确认。Arch 系发行版的对应工具是 `pacman`，见 [[Arch Build System (PKGBUILD)]]。

---

## 1. What `yum` Does (yum 是什么)

`yum` is the **RPM package manager** used on Red Hat–family distributions (CentOS, RHEL,
Fedora's older releases). It automates installing and configuring software and, crucially,
**resolves dependencies automatically** — pulling in any other packages a program needs.

> [!note]
> `yum` requires network access to reach its software repositories, and installing system
> packages usually requires `root`/`sudo`.

## 2. Syntax (语法)

```
yum [-y] [install | remove | search] <package-name>
```

| Part | Meaning |
| ---- | ------- |
| `-y` | Auto-confirm — answer "yes" to prompts, no manual confirmation |
| `install` | Install the package |
| `remove`  | Uninstall the package |
| `search`  | Search the repositories for a package |

## 3. Examples (示例)

```bash
yum -y install ntp          # install the ntp time-sync service
yum -y install httpd        # install the Apache web server
yum -y install net-tools    # provides ifconfig, netstat, etc.
yum search nginx            # look up a package before installing
yum -y remove httpd         # uninstall
```

Several packages installed this way are managed afterward as **services** via
`systemctl` (e.g. `ntpd`, `httpd`) — see [[Systemd Service Management]].

---

> [!important] 一句话总结
> `yum -y install <pkg>` 一条命令搞定下载、安装与依赖；记住它与 Arch 的 `pacman`、Debian 的 `apt` 是同一类工具的不同实现。
