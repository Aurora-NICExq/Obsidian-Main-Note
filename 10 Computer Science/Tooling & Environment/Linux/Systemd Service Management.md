---
aliases: [systemctl, Systemd Service Management, services, 服务管理, date 时区, ntp chrony]
tags: [linux, services]
up: "[[Linux MOC]]"
related: "[[Package Management (yum)|软件管理]], [[Networking Basics|网络基础]], [[Processes and Scheduling|进程与调度]], [[File Operations|文件操作]]"
down: ""
---
# Systemd Service Management

> [!summary] 核心结论
> 长期运行的后台程序（如网络、防火墙、SSH、时间同步）在 Linux 上称为**服务 (service)**，由 `systemctl` 统一管理启动、停止、查看状态和开机自启。本笔记同时收纳与服务相关的**系统时间**话题：`date` 看/格式化时间、修改时区、用 `ntp`/`chrony` 自动校时。

前置知识：[[Package Management (yum)|软件管理]]（很多服务由 yum 安装）。

---

## 1. `systemctl` — Controlling Services (服务控制)

Many built-in and third-party programs support management through `systemctl`. A program
manageable this way is called a **service** (or daemon).

```
systemctl start | stop | status | enable | disable <service-name>
```

| Subcommand | Effect |
| ---------- | ------ |
| `start`    | Start the service now |
| `stop`     | Stop the service now |
| `status`   | Show whether it is running, plus recent log lines |
| `enable`   | Start automatically **on boot** |
| `disable`  | Do **not** start on boot |

### Common Built-in Services (常见内置服务)

- `NetworkManager` — primary network service
- `network` — secondary network service
- `firewalld` — firewall
- `sshd` — SSH server (this is what remote login tools like FinalShell connect to)

### Third-party Services (第三方服务)

Software installed via [[Package Management (yum)|yum]] often registers a service too:

```bash
yum install -y ntp      # then control it via the 'ntpd' service name
yum install -y httpd    # then control it via the 'httpd' (Apache) service name
```

```bash
systemctl start httpd
systemctl enable httpd
```

## 2. System Time with `date` (查看与格式化时间)

```
date [-d] [+<format-string>]
```

- **`-d`** — display the date described by a given string (used for date arithmetic).
- **`+<format>`** — control the output format with `%` codes:

| Code | Meaning | Code | Meaning |
| ---- | ------- | ---- | ------- |
| `%Y` | year (4-digit) | `%H` | hour (00–23) |
| `%y` | year (last 2 digits) | `%M` | minute (00–59) |
| `%m` | month (01–12) | `%S` | second (00–60) |
| `%d` | day (01–31) | `%s` | seconds since 1970-01-01 UTC (Unix epoch) |

Example: `date "+%Y-%m-%d %H:%M:%S"`.

## 3. Fixing the Timezone (修改时区)

A wrong time often means the system timezone is not set to yours. As `root`, repoint the
`/etc/localtime` symlink (see `ln -s` in [[File Operations]]):

```bash
rm -f /etc/localtime
sudo ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

This deletes the old `localtime` and links China Standard Time (UTC+8) in its place.

## 4. Automatic Time Sync with NTP (自动校时)

`ntp` keeps the clock accurate by syncing with time servers over the network.

```bash
yum -y install ntp           # install
systemctl start ntpd         # start the daemon
systemctl enable ntpd        # start on boot
```

Once running, `ntpd` periodically corrects the system clock. You can also sync manually
(needs `root`):

```bash
ntpdate -u ntp.aliyun.com
```

> [!note]
> Modern distributions often use `chrony` (the `chronyd` service) or `systemd-timesyncd`
> instead of the classic `ntpd`; the management pattern via `systemctl` is the same.

---

> [!important] 一句话总结
> "后台程序 = 服务，服务 = `systemctl start/enable`"。时间不准时，先查时区（`/etc/localtime` 软链接），再交给 `ntpd`/`chronyd` 自动校准。
