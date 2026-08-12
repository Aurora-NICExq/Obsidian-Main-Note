---
aliases:
  - 进程与调度
  - task_struct
  - 调度器
  - 上下文切换
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Sleeping Waiting and Deferred Work]]"
  - "[[Locking Concurrency and Debugging]]"
  - "[[Parallel Processing and Concurrency]]"
down:
  - "[[Sleeping Waiting and Deferred Work]]"
---
# 进程、调度与上下文

> [!summary] 核心结论
> 调度实体主要是 **`task_struct`（线程）**。**进程上下文**（syscall、内核线程）可睡眠、可用 `current`；**原子上下文**（硬/软中断、持 spinlock）不能调度。驱动作者很少改调度器，但必须分清代码跑在哪类上下文——选错锁/GFP 是头号内核 bug。

> 底本：Bootlin — Processes / Scheduling。

![[lk-process-states.svg]]

---
## 1. `current` 与两类上下文

| 上下文 | 例子 | 可睡眠？ | `current` 含义 |
|---|---|---|---|
| 进程 | syscall、`kthread`、work | 是 | 正在执行的任务 |
| 原子 | hardirq、softirq、持 spinlock | 否 | 可能是“碰巧被打断的任务”，**不是**打开设备的那个进程 |

> [!example] 典型误用
> 在 IRQ handler 里 `mutex_lock` 或 `copy_to_user` 到“当前用户缓冲”——用户缓冲属于 **当时发起 I/O 的进程**，不是 `current`。应把数据放环形缓冲，在进程上下文的 `read` 里 `copy_to_user`。

---
## 2. 状态（简化）

| 状态 | 含义 |
|---|---|
| `TASK_RUNNING` | 可运行（含正在跑） |
| `TASK_INTERRUPTIBLE` | 睡眠，信号可唤醒 |
| `TASK_UNINTERRUPTIBLE` | 等 I/O 等；信号不打断（滥用会成 D 状态难点） |
| 停止/踪迹/僵尸 | 调试与退出 |

---
## 3. 调度触发

- 主动：睡眠路径内部 `schedule()`。
- 抢占：时钟、唤醒更高优先级、抢占点（配置相关）。
- 实时策略与 CFS 并存；驱动一般 `wake_up*` 即可。

> [!tip] 内核线程 vs workqueue
> `kthread_run` 适合长期循环工人；多数驱动后处理用 **workqueue** 更省事（生命周期与取消 API 成熟）。见 [[Sleeping Waiting and Deferred Work]]。

---
## 4. 上下文切换直觉

一次切换大致：保存当前寄存器/栈指针 → 选下一 `task_struct` → 恢复其寄存器 →（若 mm 不同）切地址空间 → 返回下一段内核/用户代码。驱动不直接调用切换，但 **睡眠 = 自愿让出 CPU**，会走到调度器。

> [!example] 系统调用里阻塞读的上下文变化
> 1. 用户线程 A 调 `read` → 陷入，`current = A`（进程上下文）。
> 2. 无数据 → `wait_event` → `schedule()`，A 变为可中断睡眠。
> 3. CPU 跑别的任务；设备 IRQ 到 → hardirq（原子）把数据放入缓冲并 `wake_up`。
> 4. A 被标为可运行；稍后再次被调度，从 `wait_event` 返回，继续 `copy_to_user`。
>
> 全程：**IRQ 从不替 A 做 `copy_to_user`**；只有 A 回到进程上下文才碰用户缓冲。

---
## 5. 与锁、抢占

- 持 **spinlock** → 关本地抢占，不能睡。
- **mutex** → 可睡，仅进程上下文。
- 抢占点：即使没主动 `schedule`，内核也可能在安全点抢占（配置相关）；原子上下文关闭抢占。
- 详见 [[Locking Concurrency and Debugging]]。

> [!warning] `in_interrupt()` / `in_atomic()` 自检习惯
> 新写可能睡眠的路径前，想清楚：若 `in_atomic()` 为真却调用了 `mutex`/`msleep`/`vmalloc`，就是 bug。宁肯 `queue_work` 也别赌。

---
## 6. 自检

1. 系统调用里 `printk` 时 `current` 是谁？硬中断里呢？
2. 为何 spinlock 临界区调用可能睡眠的函数是 bug？
3. 用户进程两个 `pthread` 对应几个 `task_struct`？

> [!success]- 参考答案
> 1. syscall：就是该用户线程对应的 task；hardirq：是被打断的那个 task（通常与本次设备 I/O 发起者无关）。
> 2. 睡眠会调度出去，但 spinlock 假设临界区不可切换；其它核可能空转死等，或触发 lockdep/`scheduling while atomic`。
> 3. 两个（每个线程一个 `task_struct`，同属一个线程组）。
