---
aliases:
  - wait queue
  - 等待队列
  - workqueue
  - 睡眠与唤醒
  - deferred work
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Processes Scheduling and Context]]"
  - "[[Character Device Drivers]]"
  - "[[Interrupt Management]]"
down:
  - "[[Interrupt Management]]"
---
# 睡眠、等待与延迟工作

> [!summary] 核心结论
> 进程上下文可在 **wait queue** 上睡眠：`wait_event*` 查条件 → 睡 → 事件方 `wake_up*`。原子上下文不可睡。耗时工作从硬中断推迟到 **threaded IRQ / workqueue**（可再睡）或 softirq（不可睡）。条件更新与唤醒的顺序必须正确，否则丢唤醒。

> 底本：Bootlin — Sleeping / Deferred work。

![[lk-waitqueue.svg]]

---
## 1. 等待队列模式

```c
/* 消费者 */
wait_event_interruptible(wq, READ_ONCE(ready));

/* 生产者（常在 IRQ/另一线程） */
WRITE_ONCE(ready, true);
wake_up_interruptible(&wq);
```

> [!example] 丢唤醒（经典 bug）
> 错误顺序：先 `wake_up` 再置 `ready=true`，或检查条件与睡眠之间无正确屏障/锁保护 → 消费者看到 `ready==false` 睡过去，唤醒已错过 → **永久阻塞**。应在同一锁内更新条件并唤醒，或用 `wait_event` 宏保证的模式（它会循环检查）。

- `interruptible`：信号 → `-ERESTARTSYS`。
- `wait_event_timeout`：避免永久卡住。
- `completion`：一对一“等做完”：`wait_for_completion*` / `complete`。

---
## 2. 延迟执行选项

| 机制 | 能否睡眠 | 典型用途 |
|---|---|---|
| softirq | 否 | 网络/块等高频 |
| tasklet | 否 | 老式短 BH（新代码少用） |
| threaded IRQ | 线程部分可以 | 现代驱动首选之一 |
| workqueue | 是 | 设备后处理、延迟复位 |
| timer | 回调原子 | 超时；重活再 `queue_work` |

口诀：**硬中断最短 → 能睡的工作放到能睡的上下文**。

---
## 3. workqueue

```c
INIT_WORK(&priv->work, my_work_fn);
schedule_work(&priv->work);

static void my_work_fn(struct work_struct *w)
{
	struct priv *p = container_of(w, struct priv, work);
	mutex_lock(&p->lock);
	/* 可 GFP_KERNEL、可睡 */
	mutex_unlock(&p->lock);
}
```

> [!warning] 取消与自死锁
> `cancel_work_sync` 会等 work 跑完。若在 work 里同锁顺序下又等 `cancel`，或 `remove` 路径锁顺序反了 → 死锁。`remove`：先 `cancel_work_sync`，再拆其它资源。

---
## 4. 与 `poll`

`poll`/`epoll`：`poll_wait(file, &wq, wait)` 注册；事件到时 `wake_up` 同一队列。只 `wake_up` 却忘记在 `poll` 里 `poll_wait` → 用户态卡死。

> [!example] `poll` + 读 最小逻辑
> ```c
> static __poll_t my_poll(struct file *f, poll_table *wait)
> {
> 	struct priv *p = f->private_data;
> 	__poll_t mask = 0;
>
> 	poll_wait(f, &p->wq, wait);
> 	if (p->have_data)
> 		mask |= EPOLLIN | EPOLLRDNORM;
> 	return mask;
> }
> ```
> ISR 置 `have_data` 后必须 `wake_up_interruptible(&p->wq)`，否则 `epoll_wait` 永不返回。

---
## 5. 选型速查

| 你在… | 下一步想… | 用 |
|---|---|---|
| hardirq | 睡、拷用户、拿 mutex | `IRQ_WAKE_THREAD` / `schedule_work` |
| hardirq | 仅再跑一小段原子代码 | softirq/tasklet（新代码慎用后者） |
| 进程 | 等硬件事件 | `wait_event_*` / `completion` |
| 进程 | 延迟 10ms 再复位芯片 | `schedule_delayed_work` |

---
## 6. 自检

1. 硬中断里 `mutex_lock` 会怎样？
2. 为何通常先改条件再 `wake_up`（并保证可见性）？
3. 何时选 threaded IRQ 而非手写 workqueue？

> [!success]- 参考答案
> 1. 非法睡眠 → 警告/oops/死锁。
> 2. 否则等待方可能在置位前被唤醒、再次检查仍为假后睡死；或看不见写入。
> 3. 中断后处理与该 IRQ 强绑定、希望内核自动处理 wake/oneshot 屏蔽时；通用延迟任务用 WQ 更灵活。
