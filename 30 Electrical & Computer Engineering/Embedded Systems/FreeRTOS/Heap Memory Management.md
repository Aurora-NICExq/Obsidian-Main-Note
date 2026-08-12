---
aliases: [内存管理方案, 堆内存管理, heap_1, heap_2, heap_3, heap_4, heap_5, pvPortMalloc]
tags: [FreeRTOS, embedded, rtos]
up: "[[FreeRTOS Overview]]"
related: ["[[Task Management]]", "[[FreeRTOS Overview#6. 堆内存管理（heap_1 ～ heap_5）]]"]
---
# Heap Memory Management

> [!summary] 核心结论
> 动态创建的任务 / 队列等走 FreeRTOS 堆 API：`pvPortMalloc` / `vPortFree`（用法像 `malloc` / `free`）。工程里**五选一**链接 `heap_1.c`～`heap_5.c`。标准 C 库堆通常不可重入、易碎片、耗时不确定，不适合当硬实时内核的默认分配器。

---

## 1. API：跟 `malloc` 很像

```c
void *pvPortMalloc(size_t xSize); /* 分配 */
void  vPortFree(void *pv);        /* 释放（有的方案为空操作） */
```

`xTaskCreate`、队列等动态创建，底层都进这两个函数。静态 API（如 `xTaskCreateStatic`）不走堆，见 [[Task Management#1. 两种创建方式]]。

总览图：[[FreeRTOS Overview#6. 堆内存管理（heap_1 ～ heap_5）]]。

---

## 2. 为什么不用裸的 `malloc` / `free`

| 问题 | 含义 |
| ---- | ---- |
| **不可重入** | 标准库堆内部常有全局元数据；任务 A 分到一半被切换，任务 B 再 `malloc`，可能把堆结构弄坏。中断里调用更危险。 |
| **碎片** | 反复申请/释放后，空闲块东一块西一块，总空闲够大却凑不出连续大块。 |
| **时间不确定** | 最坏耗时难保证，硬实时难用。 |

> [!note] 什么叫不可重入？
> 函数执行到一半被打断（任务切换 / 中断），同一函数（或共享同一全局状态的路径）再次进入，结果会错——就叫**不可重入**。可重入函数不依赖未保护的共享可变状态，或进出时加了合适互斥。`heap_3` 的做法是：在调 C 库 `malloc`/`free` **期间暂停调度器**，避免别的任务重入同一堆。

---

## 3. 五选一：`heap_1`～`heap_5`

按需在工程里只编进**一个** `heap_x.c`（每个都以各自算法实现 `pvPortMalloc` / `vPortFree`）。

| 方案 | 能释放？ | 特点 | 典型场景 |
| ---- | -------- | ---- | -------- |
| `heap_1` | 否 | 只往前切，最简单、确定 | 启动时创建对象，运行期从不删 |
| `heap_2` | 是 | 最佳适配；**不**合并相邻空闲块，易碎片 | 可删对象，但要接受碎片风险 |
| `heap_3` | 是 | 包装标准库 `malloc`/`free`，分配时 `vTaskSuspendAll` | 已依赖 C 库堆、对确定性要求不极端 |
| `heap_4` | 是 | 可释放，**合并**相邻空闲块，减碎片 | 最常用的“能建能删”方案 |
| `heap_5` | 是 | 算法近 `heap_4`，支持**多块不连续**内存 | 多片 SRAM / 外扩 RAM 拼成一个堆 |

![[d2-heap-memory-management-01.svg]]

---

## 4. `heap_1`：只能切，不能拼

调用 `pvPortMalloc` 像**切面包**：从堆里依次切下一块；`vPortFree` **做不到**把面包拼回去（实现里通常是空函数）。

![[tikz-heap-memory-management-01.svg]]

**适用**：只创建内核对象、不销毁（不 `vTaskDelete`、不删队列）的程序——内存确定性最好。

---

## 5. `heap_2` / `heap_4`：能释放，碎片策略不同

- **`heap_2`**：空闲块按大小找较合适的一块（最佳适配思路）；释放后**不**把相邻空闲块合并 → 长期建删容易碎。
- **`heap_4`**：释放时**合并**地址相邻的空闲块 → 同样能建能删，碎片通常好于 `heap_2`，嵌入式里很常见。

需要“删任务 / 删队列”时，优先考虑 `heap_4` 而不是 `heap_1`。

---

## 6. `heap_3`：给 C 库堆加“暂停调度”

```text
pvPortMalloc  →  vTaskSuspendAll()  →  malloc()  →  xTaskResumeAll()
vPortFree     →  vTaskSuspendAll()  →  free()    →  xTaskResumeAll()
```

这样别的任务不会在 `malloc` 执行中途插进来，缓解**不可重入**。但仍继承 C 库堆的碎片与耗时不确定性；中断里照样不该乱调。

---

## 7. `heap_5`：不连续的多块内存

更复杂的板子可能有多片 SRAM（或内部 + 外扩），物理地址**不连续**。`heap_5` 允许把多段区域注册进同一个堆来管理（算法近似 `heap_4`）。

![[d2-heap-memory-management-02.svg]]

---

## 8. 怎么选（记忆）

| 你的程序 | 倾向 |
| -------- | ---- |
| 启动建完对象，永不删 | `heap_1` |
| 要删对象，单片连续 RAM | `heap_4`（一般优于 `heap_2`） |
| 必须用 C 库堆 / newlib 等 | `heap_3`（清楚代价） |
| 多片不连续 RAM 拼堆 | `heap_5` |

动态创建失败时 `xTaskCreate` 等会返回失败；堆太小或碎片严重时表现为创建失败或异常——调 `configTOTAL_HEAP_SIZE`（`heap_1/2/4`）或检查 `heap_5` 区域表。
