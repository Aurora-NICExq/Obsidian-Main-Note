---
aliases:
  - 内核锁
  - spinlock
  - mutex
  - RCU
  - 内核调试
  - oops
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Interrupt Management]]"
  - "[[Processes Scheduling and Context]]"
  - "[[Kernel Memory Management]]"
  - "[[Parallel Processing and Concurrency]]"
down: []
---
# 锁、并发与调试入口

> [!summary] 核心结论
> **原子上下文 → spinlock（及 irq/bh 变体）；可睡进程上下文 → mutex**。读多写少考虑 rwsem/RCU；计数用 `atomic`/`refcount`。禁止在 spinlock 里睡眠；固定全局锁顺序防 AB-BA。开发内核打开 **lockdep**；oops 用匹配的 `vmlinux` 解码。

> 底本：Bootlin — Locking / Concurrent access / Kernel debugging。

![[lk-locking.svg]]

---
## 1. 原语速查

| 原语 | 睡眠 | 场景 |
|---|---|---|
| `spinlock` / `*_irqsave` | 否 | 短临界区；与 IRQ 共享 |
| `mutex` | 是 | 长临界区、进程上下文 |
| `rwlock` / `rwsem` | 读规则不同 | 读多写少 |
| RCU | 读侧极轻 | 发布-订阅结构 |
| `atomic_t` / `refcount_t` | — | 计数、状态位 |

---
## 2. 场景选型（带着对象想）

> [!example] 同一链表的三种碰法
> | 并发双方 | 用锁 |
> |---|---|
> | 仅进程 A / 进程 B | `mutex` 或短 `spinlock` |
> | 进程 ↔ softirq | `spin_lock_bh` |
> | 进程 ↔ hardirq | 进程 `spin_lock_irqsave`，IRQ 里 `spin_lock` |
>
> 选错：进程用普通 `spin_lock` 而 IRQ 同锁 → IRQ 可打断进程临界区 → 死锁。

持锁时间尽量短；锁内不做冗长 I/O。

---
## 3. 死锁模式

| 模式 | 样子 |
|---|---|
| AB-BA | CPU0 持 A 等 B，CPU1 持 B 等 A |
| 重入 | 非递归 spinlock 再次 `spin_lock` |
| 睡在原子上下文 | spinlock / hardirq 里 `mutex`/`GFP_KERNEL` |
| 回调反向加锁 | `cancel_work_sync` 与 work 内锁顺序相反 |

`CONFIG_PROVE_LOCKING`（lockdep）会在可能违规时警告——**开发机务必开**。

---
## 4. 调试入口

| 手段 | 用途 |
|---|---|
| `dev_err` / `dmesg` | 第一现场 |
| oops 栈 | `decode_stacktrace.sh`、`addr2line -e vmlinux` / 模块 |
| `ftrace` / `trace-cmd` | 函数图、irq/sched 事件 |
| `perf` | 热点 |
| KASAN / kmemleak | UAF、泄漏 |
| KGDB / JTAG | 板级源码级 |

> [!example] 把 oops 对上 `.ko`
> 1. 确认 oops 来自哪一版模块（vermagic）。
> 2. `eu-addr2line -e my.ko 0x段内偏移` 或加载时记录的基址 + 偏移。
> 3. 发行版可用 `crash`/`gdb vmlinux` + `add-symbol-file`。

---
## 5. 实践清单

1. 列出并发角色：进程 / hardirq / softirq / timer / work。
2. 注释“此锁保护哪些字段”。
3. `remove`：取消异步、再释放。
4. 复现后开 lockdep/KASAN，再刷 `printk`。

---
## 6. 自检

1. softirq 与进程共享列表，用哪类 spinlock？
2. lockdep 报 possible recursive locking 为何仍当真 bug？
3. oops 的 PC 如何对上你的 `.ko`？

> [!success]- 参考答案
> 1. `spin_lock_bh`（或等价禁用 BH 的变体）。
> 2. 即使当前路径碰巧没炸，锁序/重入模型已不成立，换时序就会死锁。
> 3. 用匹配构建的模块算段内偏移，或 `gdb`/`addr2line` 对加载基址+偏移；需符号未 strip。
