---
aliases:
  - I/O 内存
  - ioremap
  - DMA API
  - MMIO 驱动
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Kernel Memory Management]]"
  - "[[Interrupts Devices and IO]]"
  - "[[Interrupt Management]]"
  - "[[STM32 MOC]]"
down:
  - "[[Processes Scheduling and Context]]"
---
# I/O 内存与 DMA

> [!summary] 核心结论
> 设备寄存器是 **物理 MMIO**：`ioremap`/`devm_ioremap_resource` 后用 `readl`/`writel` 访问。大块数据走 **DMA API**（coherent 或 streaming），处理 IOMMU/缓存一致性；完成常配中断。组成直觉：[[Interrupts Devices and IO]]。

> 底本：Bootlin — I/O memory / DMA。

![[lk-dma.svg]]

---
## 1. MMIO 映射

```c
base = devm_platform_ioremap_resource(pdev, 0);
if (IS_ERR(base))
	return PTR_ERR(base);
val = readl(base + REG_STATUS);
writel(BIT(0), base + REG_CTRL);
```

> [!warning] 为何不能当普通指针乱写
> - 读有副作用（弹 FIFO）。
> - 编译器合并/重排会破坏设备协议。
> - 必须用访问器保证宽度与内存序；`readl_relaxed` 屏障更弱，懂序才用。

---
## 2. DMA 两类

| 类型 | API | 场景 |
|---|---|---|
| Coherent | `dma_alloc_coherent` | 描述符环；CPU↔设备需一致视图 |
| Streaming | `dma_map_single`/`sg` + `unmap` | 临时传输；注意方向 |

```c
/* streaming 示意 */
dma = dma_map_single(dev, buf, len, DMA_FROM_DEVICE);
if (dma_mapping_error(dev, dma))
	return -ENOMEM;
/* 门铃踢硬件；ISR 里： */
dma_unmap_single(dev, dma, len, DMA_FROM_DEVICE);
```

> [!example] streaming 所有权规则
> `dma_map(..., DMA_FROM_DEVICE)` 之后到 `unmap`/`sync_for_cpu` 之前：**CPU 不应读该缓冲**（cache 可能旧）。`DMA_TO_DEVICE` 则 map 前写好，map 后到 sync 前勿再改。

还需：`dma_set_mask_and_coherent(dev, DMA_BIT_MASK(32或64))`；IOMMU 下 DMA 地址 ≠ 物理地址——走 API，勿手拼。

---
## 3. 完整一次 RX DMA（心智演练）

> [!example] 网卡/串口 DMA 收一包
> | 步骤 | 谁 | 动作 |
> |---|---|---|
> | 0 | probe | `dma_alloc_coherent` 描述符环；`kmalloc`/pages 做数据缓冲 |
> | 1 | 进程/NAPI | `dma_map_single(..., FROM_DEVICE)` 填描述符，门铃启动 |
> | 2 | 设备 | 写 DRAM；完成后断言 IRQ |
> | 3 | hardirq | 读状态、清 IRQ；标记描述符完成；调度 NAPI/thread |
> | 4 | softirq/thread | `dma_unmap` 或 `dma_sync_for_cpu`；把数据送协议栈/`copy_to_user` |
> | 5 | 同上 | 重新 map/填描述符，维持环不满 |
>
> 任一步漏 unmap/漏清中断 → 泄漏或风暴。

---
## 4. 与中断协作要点

- 硬中断只做短活；重活放 threaded IRQ / workqueue（[[Sleeping Waiting and Deferred Work]]）。
- MMIO 门铃写往往需要保证“描述符已写完再踢硬件”→ 用 `writel`（带屏障）而非盲目 `writel_relaxed`。

> [!example] 缓存翻车（嵌入式高频）
> 设备 DMA 写入 DRAM 后，CPU 若仍命中旧 cache line → 读到脏数据。coherent 分配或正确 `dma_sync_*` / 非缓存映射可避免。对照 [[STM32 MOC]] 的 cache clean/invalidate。

> [!warning] 栈上缓冲勿 DMA
> 局部数组地址做 `dma_map_single`：栈可迁移、且生命周期在返回后结束 → 用堆/页/`dma_alloc_*`。

---
## 5. 自检

1. `readl` 与直接解引用差在哪？
2. streaming map 之后 CPU 还能写同一缓冲吗？
3. 为何需要 `dma_set_mask`？

> [!success]- 参考答案
> 1. 访问器保证宽度、端序、防止错误优化，并体现 device 内存语义。
> 2. 在对应方向下通常不能；需先 `dma_sync_for_cpu` / unmap，再碰缓冲。
> 3. 声明设备可寻址范围；否则映射可能失败或落在设备够不着的高位地址。
