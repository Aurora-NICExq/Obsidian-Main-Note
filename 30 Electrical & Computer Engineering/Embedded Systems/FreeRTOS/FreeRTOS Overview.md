---
aliases: [FreeRTOS总图, FreeRTOS Overview, FreeRTOS 架构, 调度器总览]
tags: [FreeRTOS, embedded, rtos]
up: ""
related: ["[[Installing Interrupt Handlers]]", "[[Task Management]]", "[[Task States]]", "[[Preemptive and Cooperative Scheduling]]", "[[Time Slicing]]", "[[Heap Memory Management]]", "[[GPIO Principles|GPIO]]", "[[Timers|定时器]]", "[[Clocks|时钟]]"]
---
# FreeRTOS Overview

> [!summary] 核心结论
> FreeRTOS 的核心是**调度器**：在多个任务之间切换 CPU。任务分用户创建与调度器启动时自动创建（**空闲任务**、**定时器任务**）。Cortex-M 上靠 **SVC**（启动首个任务）、**PendSV**（后续切换）、**SysTick**（节拍 / 时间片）驱动调度。队列、信号量、互斥锁等是**内核对象**，动态创建时落在堆上，一般用 `heap_1`～`heap_5`，而不是标准库 `malloc`/`free`。

---

## 1. 总览（架构地图）

![[d2-freertos-overview-01.svg]]

调度器可选策略（配置项）——细节见 [[Preemptive and Cooperative Scheduling]]：

| 模式 | 含义（直观） |
| ---- | ------------ |
| 带时间片的抢占式 | 高优先级可抢占；同优先级按 SysTick 轮转（[[Time Slicing|详解]]） |
| 不带时间片的抢占式 | 高优先级可抢占；同优先级一直跑到阻塞/让出 |
| 协作式 | 任务主动让出或阻塞时才切换 |

调度算法 = 调度器在切换任务时所采用的策略。

---

## 2. 调度器如何“看起来并行”

单核上同一时刻只跑一个任务；调度器不断切换，形成交错执行：

![[d2-freertos-overview-02.svg]]

![[tikz-freertos-overview-01.svg]]

---

## 3. 任务从哪来

| 来源 | 例子 |
| ---- | ---- |
| **用户创建** | `xTaskCreate` / `xTaskCreateStatic` 建的应用任务（细节见 [[Task Management]]） |
| **调度器启动时自动创建** | **空闲任务（Idle）**、**定时器服务任务（Timer）** |

典型启动顺序：先做板级 / 外设初始化 → 创建用户任务 → 再 `vTaskStartScheduler()`。

```c
int main(void)
{
    /* 底层初始化：时钟、GPIO、外设… */

    xTaskCreate(vTask1, "Task1", /* ... */);
    xTaskCreate(vTask2, "Task2", /* ... */);

    vTaskStartScheduler(); /* 正常情况不会返回 */

    /* 只有空闲任务或定时器任务创建失败时才会走到这里 */
    while (1) { }
}
```

> [!note] `vTaskStartScheduler()`
> 成功后不会退出主循环意义上的“返回”；CPU 交给调度器与各个任务。若因创建空闲 / 定时器任务失败而返回，才可能执行后面的 `while (1)`。

### 3.1 空闲任务的作用

空闲任务**随时可运行**，优先级最低。当其它任务都阻塞（例如在 `vTaskDelay` 里延时）时，调度器选中空闲任务，避免“无任务可切”。

### 3.2 最小例子：一个 LED 任务

只创建一个用户任务时，它一调用 `vTaskDelay()` 进入延时，就绪队列里往往只剩空闲任务——于是调度器跑空闲任务，延时结束后再切回 LED 任务。

```c
void vLED1Task(void *pvParameters)
{
    (void)pvParameters;
    for (;;) {
        HAL_GPIO_WritePin(LED1_GPIO_Port, LED1_Pin, GPIO_PIN_SET);
        vTaskDelay(pdMS_TO_TICKS(100));
        HAL_GPIO_WritePin(LED1_GPIO_Port, LED1_Pin, GPIO_PIN_RESET);
        vTaskDelay(pdMS_TO_TICKS(100));
    }
}

int main(void)
{
    /* ... 初始化 ... */
    xTaskCreate(vLED1Task, "LED1", 128, NULL, 1, NULL);
    vTaskStartScheduler();
    while (1) { }
}
```

`pdMS_TO_TICKS(100)` 把毫秒换成 tick 数，具体取决于 `configTICK_RATE_HZ`。

---

## 4. 三种中断：SVC、PendSV、SysTick

在 Cortex-M 移植里，它们驱动调度器：

| 中断 | 典型用途 | 优先级（相对） |
| ---- | -------- | -------------- |
| **SVC** | 启动**第一个**任务（从启动路径切入任务上下文） | 最高（在这三者中） |
| **PendSV** | **后续**任务切换（上下文保存 / 恢复） | 最低 |
| **SysTick** | 系统节拍：延时、超时、可选的**时间片**轮转；也可用来感知“当前时间”（tick 计数） | 最低 |

PendSV / SysTick 故意放在很低优先级，让普通中断先跑完，再在合适时机做上下文切换，减少开关中断的干扰。

落地步骤（向量表映射、与 HAL SysTick 冲突）见 [[Installing Interrupt Handlers]]。

---

## 5. 内核对象

地位类似于片上外设之于裸机：任务之间通过它们**同步 / 通信**。任务本身也算内核对象。

常见类别（总图右侧那一列）：

- **队列**（邮箱）、**队列集**
- **事件组**
- **软件定时器**（经**定时器命令队列**交给定时器任务处理）
- **二进制 / 计数信号量**、**互斥锁**、**递归互斥锁**
- **临界区**
- **任务通知**
- **消息缓冲区**、**流缓冲区**

---

## 6. 堆内存管理（heap_1 ～ heap_5）

动态创建的任务控制块、栈、队列等对象，存放在 MCU 的**堆**里。细节与选型见 [[Heap Memory Management]]。

标准库 `malloc` / `free` 一般不适合硬实时内核：

| 问题 | 说明 |
| ---- | ---- |
| 不可重入 | 多任务 / 中断里不安全（除非自带锁，又引入不确定性） |
| 碎片化 | 反复申请释放后可能无法再分配到足够大的块 |
| 时间不确定 | 最坏执行时间难保证 |

FreeRTOS 提供五种堆实现，按需求二选一（或组合场景选 `heap_5`）：

| 方案 | 特点（记忆用） |
| ---- | -------------- |
| `heap_1` | 只能分配、不能释放；最简单、确定 |
| `heap_2` | 可释放，最佳适配，可能碎片 |
| `heap_3` | 包装标准库 `malloc`/`free`（仍受其缺点影响） |
| `heap_4` | 可释放，合并相邻空闲块，减轻碎片 |
| `heap_5` | 类似 `heap_4`，支持**多块不连续**内存区 |

![[tikz-freertos-overview-02.svg]]

---

## 7. 一张图串起来（阅读顺序）

1. `main` 里初始化硬件 → `xTaskCreate` 用户任务  
2. `vTaskStartScheduler` → 建空闲 / 定时器任务 → **SVC** 跑起第一个任务  
3. 运行中：阻塞、延时、抢占 → **PendSV** 切任务；节拍到 → **SysTick** 更新时间 / 时间片  
4. 任务间通信靠**内核对象**；动态对象来自**堆方案**

后续可按对象拆笔记：[[Task Management|任务管理]]、[[Task States|任务状态]]、[[Preemptive and Cooperative Scheduling|抢占/协作调度]]、[[Time Slicing|时间片]]、[[Heap Memory Management|内存管理]]、队列 API、中断与临界区、`FreeRTOSConfig.h` 配置项等。
