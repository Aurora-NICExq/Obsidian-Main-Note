---
aliases: [Linux进程、调度, Processes and Scheduling, 进程与调度, task_struct, fork CFS, scheduler]
tags: [linux, process]
up: "[[Linux MOC]]"
related: "[[System Monitoring|系统监控]], [[Users, Groups, and Permissions|用户与权限]], [[Text Processing, Pipes, and Redirection|管道与过滤]], [[Time Slicing|FreeRTOS 时间片]]"
down: ""
---
# Processes and Scheduling

> [!summary] 核心结论
> 进程是操作系统管理程序运行的基本对象，内核中由 `task_struct` 描述。本笔记从**进程管理命令**（`ps`/`kill`/`top`）到**生命周期与状态**（就绪/运行/阻塞、僵尸、深浅睡眠），再到**创建机制**（`fork`/`vfork`/`clone` + 写时复制 copy-on-write），最后到**调度器**（CFS、nice、实时策略）与**多核负载均衡**（affinity、`taskset`）。

前置知识：[[System Monitoring|系统监控]]（top / ps 的基础用法）。

---

Every process is visible to users by its **PID** (process ID), used to distinguish and
manage it. In the Linux kernel, both processes and threads are schedulable **tasks**,
described by the core structure `task_struct`.

## 1. Processes and `task_struct` (进程与 task_struct)

`task_struct` holds the core information a process needs to run, for example:

- PID / TGID
- process state
- scheduling information
- memory mapping
- file descriptors
- signal-handling information
- parent/child relationships

The kernel manages these tasks with several data structures — linked lists, trees, hash
tables, and so on.

## 2. Common Process Commands (常用进程管理命令)

```bash
ps -ef                 # list all processes
ps -ef | grep <name>   # filter processes by name
kill PID               # ask a process to terminate
kill -9 PID            # force-kill a process
top                    # view system resources and process state
top -p PID             # view a single process
```

See [[System Monitoring]] for the full `top`/`ps` option tables.

## 3. The Fork Bomb (fork 炸弹)

A fork bomb endlessly spawns child processes, rapidly exhausting system resources. It is
shown only to understand the mechanism — **never actually run it**.

```bash
:(){ :|:& };:
```

## 4. Process Lifecycle (进程生命周期)

### Basic States (基础状态)

| State | Meaning |
| ----- | ------- |
| Ready (就绪态)   | Runnable, waiting for the CPU to be scheduled |
| Running (运行态) | Currently executing on the CPU |
| Blocked (阻塞态) | Waiting for a resource or event, temporarily not runnable |

### Special States in Linux (Linux 中常见的特殊状态)

| State | Meaning |
| ----- | ------- |
| Zombie (僵尸态)  | Child has exited, but the parent has not yet reaped its exit status via `wait` / `wait4` |
| Stopped (停止态) | Paused, e.g. `Ctrl + Z`, a debugger breakpoint, or `SIGSTOP` |
| Sleeping (睡眠态)| Waiting for a resource/event; re-enters the runnable state when woken |

A zombie has already exited and **cannot be killed with `kill`** — it must be reaped by its
parent; if the parent exits, the zombie is adopted and reaped by `init` / `systemd`.

A stopped process can be resumed with `fg`, `bg`, or `SIGCONT`. The idea behind `cpulimit`
is to repeatedly switch a process between stopped and running to throttle its CPU usage.

## 5. `fork` Example (fork 示例)

```c
#include <stdio.h>
#include <unistd.h>

int main(void) {
    fork();                 // returns 0 in the child
    printf("hello\n");

    fork();
    printf("hello\n");

    return 0;
}
```

Run directly in a terminal, this typically prints **6** lines of `hello`:

- After the first `fork()` there are 2 processes, each printing once.
- After the second `fork()` there are 4 processes, each printing once.
- Total: 2 + 4 = 6.

If stdout is redirected, the buffer may be duplicated by `fork()`, so the line count must
be reasoned about together with the buffering behaviour.

## 6. Light vs Deep Sleep (深睡眠与浅睡眠)

Both light and deep sleep can be woken by the awaited resource or event.

| State | Characteristic |
| ----- | -------------- |
| Light sleep (浅睡眠) | Can be woken by a signal |
| Deep sleep (深睡眠)  | Usually waiting on an uninterruptible kernel-space resource; cannot be killed immediately even with `kill -9` |

Deep sleep is common when waiting on disk I/O, network file systems, device drivers, etc.

## 7. `fork`, `vfork`, `clone` (创建进程的三种方式)

### `fork`

`fork()` creates a child process. After a parent P1 forks a child P2, the child initially
inherits much of the parent's context. To avoid copying all memory immediately, Linux uses
**copy-on-write**:

- After fork, parent and child first **share** the physical pages.
- The shared pages are marked **read-only**.
- When either side **writes**, a page fault is triggered.
- The kernel **copies** the physical page, then restores write permission.

### copy-on-write

![[tikz-processes-and-scheduling-01.svg]]

### `vfork`

After `vfork()` creates a child, the parent **blocks** until the child either:

1. calls `exec`, or
2. calls `_exit` / `exit`.

`vfork()` does **not** copy the parent's `mm`; instead the child temporarily shares the
parent's address space. The child should therefore `exec` or exit as soon as possible and
must not modify parent-related data before returning.

### `clone`

`clone()` allows fine-grained selection of which resources to share. `pthread_create`
usually uses `clone()` under the hood to create threads. Common share flags:

- `CLONE_VM` — share the memory space
- `CLONE_FS` — share filesystem-related information
- `CLONE_FILES` — share the file-descriptor table
- `CLONE_SIGHAND` — share signal handling
- `CLONE_THREAD` — place into the same thread group

A thread shares resources but is still an independently schedulable object.

![[tikz-processes-and-scheduling-02.svg]]

## 8. PID, TID, and `getpid` (PID、TID 与 getpid)

Within the same PID namespace:

- `getpid()` returns the current process's PID, i.e. the thread-group ID (TGID).
- Multiple threads in the same process usually have the **same** `getpid()` result.
- Each thread still has its own thread ID (TID).
- `gettid()` distinguishes different threads within the same process.

With PID namespaces, the same task may see different PIDs in different namespaces.

## 9. How Sleep Is Implemented (睡眠的实现)

Process sleep is often implemented with a **wait queue**:

1. The process finds a resource unavailable.
2. The process joins that resource's wait queue.
3. The process's state switches to sleeping.
4. When the resource is ready, the kernel wakes the processes in the wait queue.
5. The process re-enters the runnable state.

## 10. The IDLE Process (IDLE 进程)

PID 0 is usually called **idle / swapper** — the idle task created early during kernel
boot. Distinguish:

- **PID 0** — idle / swapper, runs when the CPU is idle.
- **PID 1** — init / systemd, the ancestor of the user-space process tree, which also
  adopts orphan processes.

## 11. Part 2 Summary (小结)

- `task_struct` is the core structure Linux uses to manage a task.
- `fork()` creates a process; resources are copied lazily via copy-on-write.
- `vfork()` temporarily shares the parent's address space, and the parent blocks.
- `clone()` selects which resources to share; a thread is a resource-sharing, schedulable
  task.
- Zombies must be reaped by the parent; a deep-sleeping process cannot be interrupted by a
  signal immediately.
- `getpid()` is not the thread ID — threads in a process usually share `getpid()`.

---

## Part 3: The Scheduler (调度器)

The scheduler's core goal is to balance **throughput** and **responsiveness**:

- Throughput — number of processes completed per unit time.
- Responsiveness — whether interactive tasks get the CPU promptly.

The kernel's preemption behaviour can be chosen via the **preemption model**.

### Process Classification (进程分类)

I/O-bound vs CPU-bound:

- **I/O-bound** — mostly waiting on I/O, high interactivity demands, usually given higher
  priority (to stay responsive to the user).
- **CPU-bound** — mostly computing, insensitive to latency.

ARM's **big.LITTLE**: big cores handle CPU-intensive tasks, small cores handle I/O-intensive
ones.

### Priority Scheduling (优先级调度)

Priority range 0–139:

- **0–99** — real-time (RT) priorities.
- **100–139** — normal-process priorities (mapping to nice values −20 to 19).

For RT, a **larger** numeric priority means **higher** priority, and RT priorities are
always higher than any normal process. Two RT policies:

- **SCHED_FIFO** — higher-priority runs until it sleeps, then lower-priority runs; at equal
  priority it is first-in-first-out.
- **SCHED_RR** — same priority ordering, but equal-priority tasks **round-robin**.

> [!abstract] 与 FreeRTOS 时间片
> `SCHED_RR` 最接近 FreeRTOS 打开 `configUSE_TIME_SLICING` 后的同优先级轮转；`SCHED_FIFO` 接近关掉时间片。Linux **默认的 CFS 不是时间片轮转**。对照见 [[Time Slicing#4. 和 Linux 调度：联系与区别]]。

### RT Bandwidth Limit (RT 带宽限制)

To stop real-time processes (e.g. an infinite loop) from monopolizing the CPU and starving
normal processes, RT may run for at most `runtime` within each `period`:

- `/proc/sys/kernel/sched_rt_period_us`
- `/proc/sys/kernel/sched_rt_runtime_us`

### Nice Value (nice 值)

The nice value tunes a normal process's weight, ranging −20 to 19 (default 0). A **smaller**
nice value means higher priority, larger weight, and a larger share of CPU time. The mapping
from nice value to weight is defined by the kernel's `prio_to_weight` array.

### Dynamic Reward and Penalty (动态奖励与惩罚)

- The longer a process sleeps, the more its virtual runtime is compensated, and the more
  likely it is to be scheduled (rewarding I/O-bound processes).
- The longer it runs, the faster its `vruntime` grows, and the less likely it is to be
  scheduled (penalizing CPU-bound processes).

Linux introduced this mechanism in early 2.6 versions so that I/O-bound processes gain an
advantage when competing with CPU-bound ones.

### CFS: Completely Fair Scheduler (完全公平调度)

CFS is Linux's default scheduler for normal processes; its core idea is to let every process
fairly share CPU time.

- Introduces **vruntime** (virtual runtime); a smaller vruntime means the process "deserves"
  more CPU time.
- At each scheduling point, it picks the process with the **smallest vruntime**.
- Actual runtime is converted into a vruntime increment based on weight (from the nice
  value).

CFS organizes runnable processes in a **red-black tree**, sorted by vruntime:

> [!note] 红黑树
> Left nodes are smaller than right nodes. CFS always picks the leftmost node (smallest
> vruntime) to run.

### Scheduling-related System Calls (调度相关的系统调用)

| System Call | Description |
|---|---|
| `nice()` | Sets a process's nice value |
| `sched_setscheduler()` | Sets a process's scheduling policy |
| `sched_getscheduler()` | Gets a process's scheduling policy |
| `sched_setparam()` | Sets a process's real-time priority |
| `sched_getparam()` | Gets a process's realtime priority |
| `sched_get_priority_max()` | Gets the maximum realtime priority |
| `sched_get_priority_min()` | Gets the minimum real-time priority |
| `sched_rr_get_interval()` | Gets a process's timeslice value |
| `sched_setaffinity()` | Sets a process's processor affinity |
| `sched_getaffinity()` | Gets a process's processor affinity |
| `sched_yield()` | Temporarily yields the processor |

### Debugging Tools (调试工具)

`chrt` and `renice` adjust scheduling parameters.

Set SCHED_FIFO with RT priority 50:

```bash
# chrt -f -a -p 50 10576
```

Set the nice value:

```bash
# renice -n -5 -g 9394
# nice -n 5 ./a.out
```

### Part 3 Summary (Part3 小结)

- The scheduler balances throughput and responsiveness.
- RT policies (SCHED_FIFO / SCHED_RR) use priorities 0–99 and always outrank normal
  processes.
- RT has a bandwidth limit (`sched_rt_period_us` / `sched_rt_runtime_us`) to avoid hogging
  the CPU.
- The nice value (−20 to 19) affects a normal process's weight and CPU share; smaller means
  higher priority.
- CFS uses vruntime + a red-black tree, always running the smallest-vruntime process.
- Dynamic adjustment: sleeping is rewarded, running is penalized.
- Scheduling parameters can be changed via system calls or the `chrt`, `renice`, `nice`
  tools.

---

## Part 4: Load Balancing on Multi-core (多核下负载均衡)

### Load Balancing (负载均衡)

- **RT processes** — the N highest-priority RT tasks are spread across N cores:
  - `pull_rt_task()`
  - `push_rt_task()`
- **Normal processes**:
  - Periodic load balancing
  - Load balancing when a core goes idle
  - Load balancing on `fork` and `exec`

### CPU Task Affinity (CPU 亲和性)

Affinity binds a task to a specific set of CPUs.

```c
int pthread_attr_setaffinity_np(pthread_attr_t *, size_t, const cpu_set_t *);
int pthread_attr_getaffinity_np(pthread_attr_t *, size_t, cpu_set_t *);
int sched_setaffinity(pid_t pid, unsigned int cpusetsize, cpu_set_t *mask);
int sched_getaffinity(pid_t pid, unsigned int cpusetsize, cpu_set_t *mask);
```

### `taskset`

`taskset` sets which core(s) a thread runs on, using a CPU **bitmask** (in hex).

```bash
taskset -a -p 01 19999
taskset -a -p 02 19999
taskset -a -p 03 19999
```

Each argument:

- **`-a`** — apply to **all** threads of the process, not just the main thread.
- **`-p`** — operate on an **existing** process given by PID (rather than launching a new
  command).
- **`01` / `02` / `03`** — the CPU affinity **mask** in hexadecimal. Each bit is one core:
  `0x01` (bit 0) = CPU 0, `0x02` (bit 1) = CPU 1, `0x03` (bits 0–1) = CPUs 0 and 1.
- **`19999`** — the target **PID** (because `-p` was given).

So `taskset -a -p 01 19999` pins all threads of PID 19999 to CPU 0 only.

---

## Part 5: Control Groups (cgroup)

The nice value and RT bandwidth limit in Part 3 tune **one process at a time**. A **cgroup**
(control group) groups many processes together and controls the resources the whole group may
use — effectively a group-level knob for weight and bandwidth.

For the CPU controller two mechanisms matter:

- **`cpu.shares`** — a **relative weight** for CFS. A group with more shares gets a
  proportionally larger slice of CPU **when there is contention**; on an idle CPU a group can
  still run beyond its share.
- **`cpu.cfs_period_us` / `cpu.cfs_quota_us`** — a **hard bandwidth cap**: the group may run
  for at most `quota` microseconds within each `period`. For real-time tasks the analogous
  knobs are `cpu.rt_period_us` / `cpu.rt_runtime_us` (compare the RT bandwidth limit in Part 3).

### Android and cgroup (Android 的分群)

Android sorts processes into cgroups by interactivity, so background work cannot starve the
foreground app of CPU:

| Group | `cpu.shares` | `cpu.rt_period_us` | `cpu.rt_runtime_us` |
| ----- | -----------: | -----------------: | ------------------: |
| `apps` (foreground)              | 1024 | 1000000 | 800000 |
| `bg_non_interactive` (background) |   52 | 1000000 | 700000 |

The foreground `apps` group carries roughly **20×** the shares of `bg_non_interactive`, so
under contention it wins the great majority of CPU time. The per-group RT runtime caps
(800000 vs 700000 out of a 1000000 period) further stop either group's real-time tasks from
monopolizing the core.

### Docker and cgroup (Docker 的分群)

Docker limits a container's CPU by writing to that container's cgroup:

```bash
docker run --cpu-quota 25000 --cpu-period 10000 --cpu-shares 30 linuxep/lepvo:1
```

The container's cgroup then appears under `/sys/fs/cgroup/cpu/docker/<container-id>/`:

```bash
$ cd /sys/fs/cgroup/cpu/docker/3f39ca25d14d.../
$ ls
cgroup.clone_children  cgroup.procs          cpuacct.stat
cpuacct.usage          cpuacct.usage_percpu  cpu.cfs_period_us
cpu.cfs_quota_us       cpu.shares            cpu.stat
notify_on_release      tasks
$ cat cpu.cfs_quota_us
25000
$ cat cpu.cfs_period_us
10000
$ cat cpu.shares
30
```

Here `quota / period = 25000 / 10000 = 2.5`, so the container may use at most **2.5 cores'**
worth of CPU time, with a CFS weight of 30 relative to its siblings.

## Part 6: Hard Real-Time and PREEMPT_RT (硬实时与 PREEMPT_RT)

**Hard real-time** means the latency from an event (such as a wakeup) to the corresponding
task actually being scheduled is **bounded and predictable** — it never exceeds a deadline. A
dedicated **RTOS** guarantees this. A general-purpose Linux kernel does **not** by default:
long non-preemptible sections (spinlocks, interrupt handlers, softirqs) can delay scheduling
by an unpredictable amount.

### Kernel Preemption (内核抢占)

Successive kernel versions have grown increasingly preemptible, shrinking the windows during
which a high-priority task must wait. The **PREEMPT_RT** patch (now largely merged upstream)
pushes this further to approach hard-real-time behaviour:

- **Spinlocks → sleeping mutexes** — most `spinlock_t` become preemptible rt-mutexes; only the
  genuinely atomic `raw_spinlock_t` remain true spinlocks. These rt-mutexes implement the
  **priority-inheritance** protocol to avoid priority inversion.
- **Threaded interrupts (中断线程化)** — hardirq handlers run in schedulable kernel threads, so
  they can themselves be preempted by a higher-priority RT task.
- **Threaded softirqs (软中断线程化)** — softirqs likewise move into schedulable threads instead
  of running in an unpreemptible context.

Together these convert most previously non-preemptible sections into schedulable,
priority-ordered work, which bounds the worst-case scheduling latency.

### Part 6 Summary (Part6 小结)

- Hard real-time = bounded, predictable wakeup-to-schedule latency; an RTOS guarantees it,
  stock Linux does not.
- PREEMPT_RT turns spinlocks into priority-inheriting sleeping mutexes and threads both
  interrupts and softirqs, making the kernel far more preemptible.

---

> [!important] 一句话总结
> 进程 = 一个 `task_struct`；`fork` 靠写时复制省内存，`clone` 决定线程共享哪些资源；普通进程由 CFS 按 vruntime + 红黑树公平调度，实时进程 (0~99) 始终优先；多核上靠负载均衡和 `taskset`/affinity 决定"在哪个核上跑"；cgroup 把进程分群，用 `shares`/`quota` 控制每组的 CPU；PREEMPT_RT 把自旋锁、中断、软中断都变成可抢占的可调度对象，让 Linux 逼近硬实时。
