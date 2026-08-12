---
aliases: [IP地址 域名解析 端口, Networking Basics, IP DNS ping, ports, netstat nmap]
tags: [linux, networking]
up: "[[Linux MOC]]"
related: "[[File Transfer (wget, curl)|文件下载]], [[Systemd Service Management|systemd 服务管理]], [[System Monitoring|系统监控]], [[Package Management (yum)|软件管理]]"
down: "[[File Transfer (wget, curl)|文件下载]]"
---
# Networking Basics

> [!summary] 核心结论
> 网络基础四件套：**IP 地址**唯一标识一台联网主机（`ifconfig` 查看），**主机名/DNS** 把名字解析成 IP（先查本机 `hosts`，再问 DNS 服务器），`ping` 测试连通性，**端口**则在一台主机内部锁定具体程序（`netstat`/`nmap` 查看占用）。

---

## 1. IP Addresses (IP 地址)

Every networked machine has an **IP address** used to communicate with others. Two
versions exist: **IPv4** and **IPv6**.

- IPv4 format: `a.b.c.d`, where each of `a b c d` is `0–255` — e.g. `192.168.88.101`.
- View the local machine's IP with `ifconfig`. If unavailable, install net-tools:

```bash
yum -y install net-tools
```

### Special IP Addresses (特殊 IP 地址)

| Address     | Meaning |
| ----------- | ------- |
| `127.0.0.1` | Loopback — refers to **this machine** (localhost) |
| `0.0.0.0`   | "Any/all" — refers to this machine, used in port binding, and in access rules means **all IPs allowed** |

## 2. Hostname and DNS Resolution (主机名与域名解析)

Besides an IP, a machine can have a **hostname**. Turning a name like `www.baidu.com` into
an IP is **DNS resolution**, which proceeds in two steps:

1. Check the local "address book" first:
   - Windows: `C:\Windows\System32\drivers\etc\hosts`
   - Linux: `/etc/hosts`
2. If not found locally, query a **DNS server** (e.g. `114.114.114.114`, `8.8.8.8`).

![[d2-networking-basics-01.svg]]

## 3. `ping` — Test Connectivity (测试连通性)

```
ping [-c num] <ip-or-hostname>
```

- **`-c`** — how many times to check; **without `-c`, ping runs forever** (stop with
  `Ctrl+C`).
- The argument is the target server's IP or hostname.

## 4. Ports (端口)

An IP locates a *machine*; a **port** locates a specific *program* on it, so programs can
talk to each other unambiguously. Ports are **physical** (visible connectors like USB,
RJ45) or **virtual** (software ports used by the OS). Linux supports **65535** virtual
ports, split into three ranges:

| Range | Name | Usage |
| ----- | ---- | ----- |
| `1–1023` | Well-known ports (公认端口) | Reserved for system/known services (SSH `22`, HTTPS `443`). Don't occupy without reason |
| `1024–49151` | Registered ports (注册端口) | Freely usable, loosely bound to programs/services |
| `49152–65535` | Dynamic ports (动态端口) | Temporary, used on the fly when a program makes outbound connections |

### Checking Port Usage (查看端口占用)

```bash
yum -y install nmap         # install nmap first
nmap <ip-address>           # scan which ports are open on a host
```

```bash
netstat -anp | grep <port>  # see which process occupies a given port
```

- `netstat` flags: `-a` all connections, `-n` numeric addresses, `-p` show the owning
  program; piping through `grep` filters to the port of interest.

---

> [!important] 一句话总结
> "IP 找主机，端口找程序，DNS 把名字变 IP，`ping` 看通不通"。排查网络问题时，按这条链路从 IP → DNS → 端口逐层定位。下载文件见 [[File Transfer (wget, curl)]]。
