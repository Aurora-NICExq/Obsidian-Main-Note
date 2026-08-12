---
aliases: [抢占式调度和协作式调度, 抢占式调度, 协作式调度, Preemptive Scheduling, Cooperative Scheduling]
tags: [FreeRTOS, embedded, rtos]
up: "[[FreeRTOS Overview]]"
related: ["[[Time Slicing]]", "[[Task Management]]", "[[Task States]]", "[[Installing Interrupt Handlers]]"]
---
# Preemptive and Cooperative Scheduling

> [!summary] 核心结论
> FreeRTOS 调度策略由 `configUSE_PREEMPTION`（以及同优先级时的 `configUSE_TIME_SLICING`）决定。**抢占式**：更高优先级一旦就绪，立刻打断当前任务。**协作式**：仍偏好高优先级，但只有当前任务主动让出（阻塞 / `taskYIELD`）才会切换。同优先级是否按 SysTick 轮转，决定“带 / 不带时间片”。

---

## 1. FreeRTOS 里有哪些调度算法

![[d2-preemptive-and-cooperative-scheduling-01.svg]]

| 模式 | 高优先级就绪时 | 同优先级多个任务 |
| ---- | -------------- | ---------------- |
| 带时间片的抢占式 | 立刻抢占 | 每个 tick 可轮转（时间片）→ [[Time Slicing]] |
| 不带时间片的抢占式 | 立刻抢占 | 一直跑到阻塞 / 主动让出 |
| 协作式 | **不**立刻抢占 | 当前任务让出后，再选最高优先级就绪任务 |

与 Overview 总表对应：[[FreeRTOS Overview#1. 总览（架构地图）]]。

---

## 2. 抢占式 vs 协作式（定义）

**抢占式（Preemptive Scheduling）**  
调度器总是选更高优先级的就绪任务；高优先级任务一就绪，当前任务**立刻**被抢占（经 PendSV 等切走）。

**协作式（Cooperative Scheduling）**  
调度器同样优先高优先级，但**只有**当前任务主动放弃执行权时才切换——例如 `vTaskDelay`、等队列、或显式 `taskYIELD()`。高优先级就绪了，也不会打断正在跑的低优先级任务，直到后者让出。

![[d2-preemptive-and-cooperative-scheduling-02.svg]]

状态侧：被抢占时 Running → Ready；主动延时则 Running → Blocked。见 [[Task States]]。

---

## 3. 配置项（`FreeRTOSConfig.h`）

路径一般在工程的 `FreeRTOS/Inc/FreeRTOSConfig.h`（或 CubeMX 生成位置）：

```c
/* 1 = 抢占式；0 = 协作式 */
#define configUSE_PREEMPTION 1

/* 抢占式下：1 = 同优先级按 tick 时间片轮转；0 = 不轮转 */
#define configUSE_TIME_SLICING 1
```

| 想要的行为 | 典型配置 |
| ---------- | -------- |
| 带时间片的抢占式 | `PREEMPTION=1`，`TIME_SLICING=1` |
| 不带时间片的抢占式 | `PREEMPTION=1`，`TIME_SLICING=0` |
| 协作式 | `PREEMPTION=0` |

---

## 4. 例：抢占如何打断串口打印

`configUSE_PREEMPTION = 1`。两个任务都往 USART1 打字符串；Task2 优先级更高，并带随机短延时。

```c
/* 未保护整串时：逐字节轮询发送，发送过程中可被抢占 */
void PrintString(const char *Str)
{
    uint16_t i;
    uint16_t len = (uint16_t)strlen(Str);
    for (i = 0; i < len; i++) {
        while ((USART1->SR & USART_SR_TXE_Msk) == 0) { }
        USART1->DR = Str[i];
    }
}

void vTask1(void *pvParameters) /* 优先级 1：狂打 Hello world */
{
    (void)pvParameters;
    for (;;) {
        PrintString("Hello world");
    }
}

void vTask2(void *pvParameters) /* 优先级 2：偶尔打 0123 */
{
    (void)pvParameters;
    for (;;) {
        vTaskDelay(pdMS_TO_TICKS((rand() % 100) + 1));
        PrintString("0123");
    }
}

xTaskCreate(vTask1, "Task1", 128, NULL, 1, NULL);
xTaskCreate(vTask2, "Task2", 128, NULL, 2, NULL);
```

**现象（抢占式）**  
Task1 正在发 `"Hello world"` 的中途，Task2 延时结束进入 Ready → **立刻抢占** → 串口上出现字符交错，例如 `He0123llo world`。

**若改成协作式（`configUSE_PREEMPTION 0`）**  
Task1 的死循环里既不延时也不 `taskYIELD`，则可能**长期不让出**，Task2 很难插进来（或表现与抢占式截然不同）。协作式依赖“主动让出”，不适合这种只忙等、不阻塞的任务模型。

**整串原子发送（暂停调度器）**：

```c
void PrintString(const char *Str)
{
    uint16_t i;
    uint16_t len = (uint16_t)strlen(Str);

    vTaskSuspendAll(); /* 暂停调度：其它任务先别抢 */
    for (i = 0; i < len; i++) {
        while ((USART1->SR & USART_SR_TXE_Msk) == 0) { }
        USART1->DR = Str[i];
    }
    xTaskResumeAll();  /* 恢复；若有更高优先级已就绪，可能在此之后切换 */
}
```

注意：若把 `vTaskSuspendAll` / `xTaskResumeAll` 包在**每一个字节**内外（循环内一停一开），字节与字节之间仍可能被抢占，整串照样会被插花。要保护的是**整次打印**这一临界区。

---

## 5. 怎么选（实用记忆）

| 场景 | 更合适 |
| ---- | ------ |
| 硬实时、高优先级必须马上响应 | 抢占式 |
| 同优先级要“轮着跑”、避免某个任务长期独占 | 抢占 + 时间片 |
| 同优先级希望跑完关键逻辑再切、减少无谓切换 | 抢占、关时间片 |
| 演示 / 特殊模型、自己控制切换点 | 协作式（少用于一般应用） |

Cortex-M 上真正完成切换仍靠 SVC / PendSV / SysTick，见 [[Installing Interrupt Handlers]]。
