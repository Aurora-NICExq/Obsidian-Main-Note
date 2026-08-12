---
aliases:
  - 内核内存管理
  - kmalloc
  - slab
  - 伙伴系统
  - vmalloc
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Virtual Memory]]"
  - "[[IO Memory and DMA]]"
  - "[[Locking Concurrency and Debugging]]"
down:
  - "[[IO Memory and DMA]]"
---
# 内核内存管理

> [!summary] 核心结论
> 内核堆不是 libc：`kmalloc`/`kzalloc` 走 **slab/slub**（小对象、通常物理连续）；大块用 **buddy 页分配**；只需虚拟连续时用 `vmalloc`。GFP（`GFP_KERNEL` vs `GFP_ATOMIC`）决定能否睡眠。驱动优先 `devm_kmalloc`；DMA 缓冲另有约束（[[IO Memory and DMA]]）。用户态 VA 直觉见 [[Virtual Memory]]。

> 底本：Bootlin — Memory management。

![[lk-mm.svg]]

---
## 1. 三层直觉

| API | 连续含义 | 典型用途 |
|---|---|---|
| `alloc_pages` / `__get_free_pages` | 物理页 | 自管大缓冲 |
| `kmalloc` / `kmem_cache_*` | 通常物理连续 | 描述符、小缓冲 |
| `vmalloc` | 仅虚拟连续 | 大数组、模块代码 |

配对：`kfree` / `free_pages` / `vfree`——不可混用。

---
## 2. GFP 标志（必懂）

| 标志 | 能否睡 | 场景 |
|---|---|---|
| `GFP_KERNEL` | 是 | 进程上下文常规分配 |
| `GFP_ATOMIC` | 否 | 中断 / 持 spinlock；更容易失败 |
| `GFP_NOWAIT` | 否 | 比 atomic 更“别努力回收” |

> [!example] 选错 GFP 的下场
> 在 `spin_lock_irqsave` 里 `kmalloc(..., GFP_KERNEL)` → 可能睡眠 → **`scheduling while atomic`** 或死锁。应改 `GFP_ATOMIC`，或把分配挪到锁外/工作队列。

---
## 3. slab / 尺寸与失败

- 相同大小反复分配 → `kmem_cache_create` + `kmem_cache_alloc`。
- `kmalloc` 对过大尺寸可能失败或直接走页分配——不要假设“总能成功”。
- 用户可控大小：`array_size`/`struct_size` 防溢出。

> [!example] 安全分配用户长度
> ```c
> if (n > MAX)
> 	return -EINVAL;
> buf = kmalloc_array(n, sizeof(*buf), GFP_KERNEL);
> if (!buf)
> 	return -ENOMEM;
> ```

---
## 4. 选型决策树（驱动视角）

| 需求 | 倾向 |
|---|---|
| 几十～几 KB 描述符，进程上下文 | `devm_kzalloc` / `kmalloc` + `GFP_KERNEL` |
| 同上，但在 IRQ/持 spinlock | 预分配，或 `GFP_ATOMIC`（检查失败） |
| 多页、要物理连续（老 DMA） | `dma_alloc_coherent` 或页分配 + DMA API |
| 大数组、仅 CPU 用、可睡 | `vmalloc` / `kvmalloc` |
| 同尺寸海量对象 | 私有 `kmem_cache` |

> [!example] `kvmalloc` 直觉
> 先尝试 `kmalloc`，失败再退到 `vmalloc`——方便“可能大也可能小”的缓冲；**不要**把 `kvmalloc` 结果直接拿去给设备做普通 DMA（物理连续性不保证）。

---
## 5. 与用户页、设备

- 用户缓冲：`copy_*_user`；要 pin 做 DMA 用 `pin_user_pages` 一类 API，用完必须 unpin。
- 设备 `mmap`：`remap_pfn_range` 等，注意 **缓存属性**（WC/UC）；错误属性 → 用户看见旧数据或性能极差。

---
## 6. 调试

`kmemleak`、KASAN、UBSAN（配置开启）抓泄漏/UAF/越界。开发内核尽量打开。

> [!warning] 释放后使用
> `kfree` 后再碰指针、或 `remove` 后 work 仍跑并访问 priv → KASAN 红灯。异步路径必须先取消再释放（见 [[Sleeping Waiting and Deferred Work]]）。

---
## 7. 自检

1. 硬中断里能否 `kmalloc(..., GFP_KERNEL)`？
2. `kmalloc` 与 `vmalloc` 对 DMA 友好性差在哪？
3. 为何偏好 `devm_kzalloc`？

> [!success]- 参考答案
> 1. 不能（会睡）；用 `GFP_ATOMIC` 或推迟到可睡上下文。
> 2. `kmalloc` 通常物理连续，便于 DMA；`vmalloc` 物理可不连续，需 sg/特殊处理，一般不直接给设备 DMA。
> 3. 绑定 `struct device` 生命周期，probe 失败/`remove` 时自动释放，减少泄漏。
