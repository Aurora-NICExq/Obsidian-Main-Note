---
aliases: [Linux 内核, Linux Kernel, Bootlin Kernel, 内核驱动开发, 内核源码]
tags: [cs, linux_kernel, MOC]
up: "[[Computer Science MOC]]"
related:
  - "[[Linux MOC]]"
  - "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
  - "[[STM32 MOC]]"
down:
  - "[[Kernel Introduction and Source Tree]]"
  - "[[Kernel Configuration Build and Boot]]"
  - "[[Loadable Kernel Modules]]"
  - "[[Hardware Description and Device Tree]]"
  - "[[Device Driver Model and Platform Drivers]]"
  - "[[Character Device Drivers]]"
  - "[[Kernel Memory Management]]"
  - "[[IO Memory and DMA]]"
  - "[[Processes Scheduling and Context]]"
  - "[[Sleeping Waiting and Deferred Work]]"
  - "[[Interrupt Management]]"
  - "[[Locking Concurrency and Debugging]]"
---
# Linux Kernel (Bootlin) MOC

> 课程底本：[Bootlin — Linux kernel and driver development](https://bootlin.com/doc/training/linux-kernel/)（CC BY-SA；slides / labs 可离线下载）。辅读结构可参考 [linux-kernel-labs](https://linux-kernel-labs.github.io/)。本夹面向 **内核源码与驱动**；用户态运维（shell / systemd / yum）见 [[Linux MOC]]。

> 相关：[[Computer Organization and Architecture (MIT 6.004) MOC|组成/体系]]（中断、MMIO、DMA、VM 直觉）；嵌入式板级实践 [[STM32 MOC]]。

![[lk-moc-roadmap.svg]]

## 01 源码、构建与模块
- [[Kernel Introduction and Source Tree]]：内核角色、许可、源码树与阅读入口
- [[Kernel Configuration Build and Boot]]：Kconfig、`make`、镜像与启动链
- [[Loadable Kernel Modules]]：`.ko`、参数、符号与生命周期

## 02 硬件描述与驱动模型
- [[Hardware Description and Device Tree]]：DTB / bindings、平台数据来源
- [[Device Driver Model and Platform Drivers]]：bus/device/driver、`probe`/`remove`
- [[Character Device Drivers]]：`cdev`、`file_operations`、用户态接口

## 03 内存、I/O 与 DMA
- [[Kernel Memory Management]]：页分配、slab、`kmalloc`/`vmalloc`
- [[IO Memory and DMA]]：`ioremap`、寄存器访问、DMA API

## 04 进程、睡眠、中断与并发
- [[Processes Scheduling and Context]]：task、调度、上下文
- [[Sleeping Waiting and Deferred Work]]：wait queue、workqueue、延迟工作
- [[Interrupt Management]]：上下半部、共享 IRQ、软中断路径
- [[Locking Concurrency and Debugging]]：锁原语选择、常见陷阱与调试入口

## 插图（预生成 SVG）

嵌入 `90 Assets/diagrams/linux-kernel/`（文件名形如 `lk-….svg`）。重新生成：

```bash
cd "90 Assets/scripts/linux_kernel"
MPLCONFIGDIR="$(pwd)/.mplconfig" .venv/bin/python generate_all.py
```
