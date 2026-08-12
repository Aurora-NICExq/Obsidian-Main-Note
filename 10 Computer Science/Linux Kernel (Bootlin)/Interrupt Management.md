---
aliases:
  - 中断管理
  - request_irq
  - 上下半部
  - softirq
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Sleeping Waiting and Deferred Work]]"
  - "[[IO Memory and DMA]]"
  - "[[Interrupts Devices and IO]]"
  - "[[STM32 MOC]]"
down:
  - "[[Locking Concurrency and Debugging]]"
---
# 中断管理

> [!summary] 核心结论
> 用 **`devm_request_irq` / `devm_request_threaded_irq`** 挂接：硬中断 **top half** 短小不可睡；繁重工作放 **threaded handler / workqueue / softirq**。共享 IRQ 必须能识别“是否我”，否则返回 `IRQ_NONE`。未清中断源 → 风暴；错锁变体 → 死锁或丢数据。

> 底本：Bootlin — Interrupt management。组成：[[Interrupts Devices and IO]]。

![[lk-irq.svg]]

---
## 1. 注册

```c
ret = devm_request_threaded_irq(dev, irq,
	demo_hard, demo_thread,
	IRQF_ONESHOT, "demo", priv);
```

| API | 含义 |
|---|---|
| `devm_request_irq` | 仅 hard handler |
| `devm_request_threaded_irq` | hard + 可睡的 thread；常配 `IRQF_ONESHOT` |
| `IRQF_SHARED` | 多驱动同线；handler 必须验“是我” |

---
## 2. 上下半部与时间线

> [!example] UART RX 时间线
> 1. 字节到达 → 控制器拉 IRQ。
> 2. **hard**：读状态、清中断标志、把字节推进环形缓冲（或标记有数据）、`wake_up` / `IRQ_WAKE_THREAD`。
> 3. **thread/WQ**（可选）：协议解析、再唤醒读者。
> 4. 用户 `read`：进程上下文 `copy_to_user`。
>
> hard 里 **禁止** `copy_to_user`、`mutex`、`kmalloc(GFP_KERNEL)`。

| 返回值 | 含义 |
|---|---|
| `IRQ_HANDLED` | 已处理 |
| `IRQ_NONE` | 不是我的（共享线） |
| `IRQ_WAKE_THREAD` | 唤醒 threaded 部分 |

---
## 3. 共享 IRQ

```c
static irqreturn_t demo_isr(int irq, void *dev_id)
{
	struct priv *p = dev_id;
	u32 st = readl(p->base + REG_IRQ);

	if (!(st & MY_BITS))
		return IRQ_NONE;
	writel(st & MY_BITS, p->base + REG_IRQ); /* 清自己的位 */
	/* … */
	return IRQ_HANDLED;
}
```

> [!warning] 中断风暴
> 未写清除寄存器 / 清错位 → 退出 handler 后线仍断言 → CPU 空转在中断。`/proc/interrupts` 计数狂飙是信号。

---
## 4. 禁止与卸载

- `disable_irq`：等正在跑的 handler 结束（可睡）。
- `disable_irq_nosync`：不等。
- `remove`/`rmmod`：先 `free_irq`（或依赖 `devm`）并 `cancel_work_sync`，确保无飞驰回调。

---
## 5. 与锁

进程 ↔ 硬中断共享数据：进程侧 `spin_lock_irqsave`，IRQ 侧 `spin_lock`。详见 [[Locking Concurrency and Debugging]]。

---
## 6. 自检

1. 共享 IRQ 为何必须能返回 `IRQ_NONE`？
2. `IRQF_ONESHOT` 作用？
3. top half 里 `copy_to_user` 合法吗？

> [!success]- 参考答案
> 1. 否则抢答别人的中断，清错状态或拖慢真正属主；共享模型要求“不是我”就快速放行。
> 2. 硬中断返回后保持屏蔽直到 threaded handler 跑完，避免重入淹没线程。
> 3. 不合法：可能睡、且无正确用户地址空间上下文。
