---
aliases:
  - 内核导论
  - 源码树
  - Linux kernel intro
  - GPL kernel
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Linux MOC]]"
  - "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
down:
  - "[[Kernel Configuration Build and Boot]]"
---
# 内核导论与源码树

> [!summary] 核心结论
> Linux **内核**在用户态与硬件之间提供进程、内存、文件系统、网络与驱动等抽象；用户程序经 **系统调用** 进入内核。源码以 **GPL-2.0**（及部分双许可驱动）为主——学习/改驱动时需注意许可与导出符号约束。阅读入口优先：`Documentation/`、`include/`、`kernel/`、`mm/`、`drivers/`、`arch/<cpu>/`；在线浏览可用 Elixir，离线则以本地树 + `rg`/`cscope` 即可。

> 底本：Bootlin *Linux kernel and driver development* — Kernel introduction / Linux kernel sources。

![[lk-kernel-layers.svg]]

---
## 1. 内核在系统中的位置

| 层 | 典型内容 |
|---|---|
| 用户态 | 应用、shell、libc；无权直接碰硬件/页表 |
| 系统调用边界 | `open`/`read`/`mmap`/`ioctl`… 陷入内核 |
| 内核子系统 | VFS、mm、scheduler、net、driver model |
| 架构相关 | `arch/*`：异常入口、页表、SMP、时钟 |
| 硬件 | CPU、总线、外设 |

与组成课 [[Interrupts Devices and IO]] 的 MMIO/中断/DMA 直觉衔接：内核驱动正是把这些机制封装成可复用 API。

> [!example] 一次 `read(fd, buf, n)` 的下落（字符设备）
> 1. libc 封装 → `svc`/`syscall` 陷入；
> 2. 通用 syscall 入口保存寄存器，按号跳到 `sys_read`；
> 3. VFS：`struct file` → `f_op->read_iter` / `read`；
> 4. 驱动：从硬件 FIFO/`wait_queue` 取数据，`copy_to_user`；
> 5. 返回字节数或负 errno → 用户态看见返回值。
>
> 同一条用户 API，块设备/套接字走不同子系统，但 **“VFS/套接字层派发到具体 `*operations`”** 的模式一致。

---
## 2. 为什么“读内核”难，但路径清晰

- 体量大、配置组合多：只跟 **你启用的选项 + 你的 arch** 相关的代码路径。
- C 语言 + 大量宏/内联/`container_of`：习惯指针与结构嵌入即可。
- 版本演进快：笔记以 **通用机制** 为准；具体函数名以你手头的树为准（Bootlin 材料常跟某一 LTS）。

> [!tip] 阅读策略
> 先跟一条完整路径（例如字符设备 `open→read`），再横向扫子系统，比“从上到下读完 `kernel/`”有效。用 `rg -n 'struct file_operations'` 或 Elixir 的引用跳转定位实现。

---
## 3. 源码树速览

![[lk-source-tree.svg]]

| 目录 | 角色 | 第一周建议读什么 |
|---|---|---|
| `arch/` | 每 CPU 架构：启动、中断、页表、syscall 表 | 你的 `arch/<cpu>/kernel/entry*`、`irq*` |
| `kernel/` | 调度、时间、IRQ 核心、locking | `sched/`、`irq/`、`locking/` 的头文件注释 |
| `mm/` | 伙伴、slab、mmap、缺页 | `slub.c` 开头、`kmalloc` 声明处 |
| `fs/` | VFS 与具体 FS | `read_write.c`、`char_dev.c` |
| `drivers/` | 按总线/类型分的驱动 | `base/`（device model）+ 你板子的驱动 |
| `include/linux/` | 核心 API 头 | `device.h`、`interrupt.h`、`mutex.h` |
| `include/uapi/` | 导出到用户态的 UAPI | ioctl 号、结构布局 |
| `init/` | `start_kernel` 一带 | `main.c` 里初始化调用顺序 |
| `Documentation/` | 文档与 bindings | `driver-api/`、`devicetree/bindings/` |

---
## 4. 许可与“能导出什么”

- 内核整体 **GPLv2**；许多头文件标明 `GPL-2.0`。
- 模块若使用仅 `EXPORT_SYMBOL_GPL` 的符号，通常被视为 **GPL 兼容** 模块。
- 专有用户态经系统调用用内核 **不受** GPL“传染”；**链进内核的模块** 不同。

> [!warning] 发行与合规
> 学习笔记里贴内核片段做理解没问题；若你对外发布改动过的内核/模块，需按 GPL 义务提供对应源码。不要把“内部树”当可闭源链接库。

---
## 5. 与本库其它笔记的边界

- [[Linux MOC]]：发行版、shell、systemd——**用户态**。
- 本夹：源码结构、模块、设备模型、mm/IRQ/锁——**内核态**。
- 板级寄存器与 RTOS：[[STM32 MOC]]（对照“裸机驱动 vs Linux 驱动模型”）。

---
## 6. 自检

1. 用户态 `read()` 最终会落到哪一类内核对象上的操作？
2. 为什么改 `drivers/` 里某驱动，不必理解整个网络栈？
3. `arch/` 与 `kernel/` 的职责如何划分？

> [!success]- 参考答案
> 1. 对打开的 `struct file` 调用其 `file_operations`（或 `file_operations` 派发到的驱动/套接字实现）。
> 2. 驱动通过稳定子系统 API（cdev、netdev、regmap…）挂接；只要接口边界清楚，不必深入无关子系统实现。
> 3. `arch/`：与 CPU/平台相关的入口、页表、中断控制器 glue；`kernel/`：尽量 arch 无关的核心策略与框架。
