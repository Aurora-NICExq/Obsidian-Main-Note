---
aliases: [主机状态监控, System Monitoring, top df iostat sar]
tags: [linux, monitoring]
up: "[[Linux MOC]]"
related: "[[Processes and Scheduling|进程与调度]], [[Networking Basics|网络基础]], [[Archiving and Compression|压缩与解压]]"
down: "[[Processes and Scheduling|进程与调度]]"
---
# System Monitoring

> [!summary] 核心结论
> 查看主机资源占用的四个命令：`top` 实时看 CPU/内存（类似任务管理器）、`df -h` 看磁盘使用、`iostat` 看 CPU 与磁盘 I/O、`sar -n DEV` 看网络流量。进程级别的深入（状态、调度）见 [[Processes and Scheduling]]。

前置知识：[[Text Processing, Pipes, and Redirection|管道与过滤]]、[[Processes and Scheduling|进程概念]]。

---

## 1. `top` — Live Resource Monitor (实时资源监控)

`top` shows CPU and memory usage in real time, similar to the Windows Task Manager, and
**refreshes every 5 seconds** by default.

```bash
top
```

| Option | Function |
| ------ | -------- |
| `-p`   | Show only a specific process (by PID) |
| `-d`   | Set the refresh interval (default 5 s) |
| `-c`   | Show the full command that started each process, not just its name |
| `-n`   | Refresh a fixed number of times, then exit (e.g. `top -n 3`) |
| `-b`   | Batch/non-interactive mode; combine with `-n` and redirect, e.g. `top -b -n 3 > /tmp/top.tmp` |
| `-i`   | Hide idle or zombie processes |
| `-u`   | Show only a specific user's processes |

## 2. `df` — Disk Usage (磁盘使用情况)

```
df [-h]
```

- **`-h`** — human-readable units (KB/MB/GB instead of raw blocks).

## 3. `iostat` — CPU and Disk I/O (CPU 与磁盘信息)

```
iostat [-x] [interval] [count]
```

- **`-x`** — show extended (more detailed) statistics.
- **interval** — seconds between refreshes; **count** — how many times to refresh.

## 4. `sar` — Network Statistics (网络状态监控)

`sar` is a powerful (and complex) system activity reporter; here it is used simply to watch
network throughput.

```
sar -n DEV <interval> <count>
```

- **`-n DEV`** — report network **interface** statistics.
- **interval** — refresh interval (omit to report once); **count** — number of reports
  (omit for unlimited).

---

> [!important] 一句话总结
> "CPU/内存看 `top`，磁盘空间看 `df -h`，磁盘 I/O 看 `iostat`，网络流量看 `sar -n DEV`"。这四个命令组合起来就是一台主机的体检表。
