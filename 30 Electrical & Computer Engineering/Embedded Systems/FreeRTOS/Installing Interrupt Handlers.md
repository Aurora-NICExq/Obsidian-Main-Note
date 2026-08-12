---
aliases: [安装中断服务程序, 安装 ISR, FreeRTOS 中断向量, PendSV SysTick SVC, HAL 时间基准]
tags: [FreeRTOS, embedded, rtos, interrupt]
up: "[[FreeRTOS Overview]]"
related: ["[[Task Management]]", "[[Task States]]", "[[Timers|定时器]]", "[[Clocks|时钟]]"]
---
# Installing Interrupt Handlers

> [!summary] 核心结论
> Cortex-M 上 FreeRTOS 靠 `port.c` 里的三个 ISR 驱动调度：**SVC**（启动首个任务）、**PendSV**（后续切换）、**SysTick**（节拍）。必须把它们挂进启动文件的**中断向量表**（或用宏把 CMSIS 名映射到 FreeRTOS 名）。SysTick 被内核占用后，HAL 的 `HAL_Delay` / `HAL_GetTick` 不能再依赖默认的 `SysTick_Handler`，通常改用其它定时器（如 TIM6/TIM7）作 HAL 时间基准。

---

## 1. 要把哪三个 ISR 装进向量表

`port.c`（Cortex-M 移植层）提供：

| FreeRTOS 函数 | 属性 | 对应异常 |
| ------------- | ---- | -------- |
| `vPortSVCHandler` | `naked` | SVC |
| `xPortPendSVHandler` | `naked` | PendSV |
| `xPortSysTickHandler` | 普通 C | SysTick |

声明形如：

```c
void vPortSVCHandler(void) __attribute__((naked));
void xPortPendSVHandler(void) __attribute__((naked));
void xPortSysTickHandler(void);
```

不安装的话，调度器无法启动任务、无法切换、也无法产生 tick——FreeRTOS 跑不起来。三者分工见 [[FreeRTOS Overview#4. 三种中断：SVC、PendSV、SysTick]]。

---

## 2. 挂到中断向量表

启动汇编（如 `startup_stm32xxxx.s`）里，系统异常段大致是：

```asm
.word  SVC_Handler
.word  DebugMon_Handler
.word  PendSV_Handler
.word  SysTick_Handler
```

向量表里写的是 **CMSIS 弱符号名**（`SVC_Handler` 等），而 `port.c` 导出的是 **FreeRTOS 名**。常见做法二选一：

### 2.1 在 `FreeRTOSConfig.h` 里用宏映射（推荐）

```c
#define vPortSVCHandler     SVC_Handler
#define xPortPendSVHandler  PendSV_Handler
#define xPortSysTickHandler SysTick_Handler
```

链接后，向量表里的弱符号被 FreeRTOS 的强符号覆盖。

### 2.2 直接改向量表名字

把 `.word` 改成指向 `vPortSVCHandler` / `xPortPendSVHandler` / `xPortSysTickHandler`。不如宏映射常见，也更容易和 CubeMX 生成的启动文件打架。

![[d2-installing-interrupt-handlers-01.svg]]

---

## 3. SysTick 冲突：HAL 改用其它定时器作时间基准

裸机工程里，HAL 默认用 SysTick：

```c
uint32_t uwTick; /* HAL 系统节拍计数值 */

void SysTick_Handler(void)
{
    HAL_IncTick(); /* 每次中断递增 uwTick */
}

uint32_t HAL_GetTick(void)
{
    return uwTick;
}
```

依赖 `uwTick` 的典型 API：

| API | 用途 |
| --- | ---- |
| `HAL_Delay()` | 忙等延时 |
| `HAL_GetTick()` | 读当前毫秒时间戳 |
| `HAL_UART_Transmit(..., Timeout)` 等 | 阻塞传输的超时判断 |

上 FreeRTOS 后，**SysTick 归内核**（`xPortSysTickHandler`），不能再给 `HAL_IncTick` 用。否则要么 HAL 时间停住，要么和 FreeRTOS tick 抢同一个 ISR。

处理方式：在 CubeMX / HAL 里把 **Timebase Source** 改成其它定时器（常用基本定时器 TIM6 / TIM7），由该定时器的更新中断调用 `HAL_IncTick()`。SysTick 只留给 FreeRTOS。

> [!warning] 注意
> 改时间基准后，仍要保证该定时器中断优先级配置合理，且不要在 ISR 里调用会阻塞的 FreeRTOS API（除非走 FromISR 路径并遵守优先级上限）。

---

## 4. 装好 ISR 之后：创建任务并启动调度器

向量与时间基准就绪后，在 `main` 里创建任务并启动调度器即可（文件名：`main.c`）：

```c
int main(void)
{
    /* 板级 / 外设初始化 … */

    xTaskCreate(vLED1Task, "LED1", 128, NULL, 1, NULL);
    xTaskCreate(vLED3Task, "LED3", 128, NULL, 1, NULL);

    vTaskStartScheduler(); /* 正常不会返回 */

    while (1) {
    }
}
```

`vTaskStartScheduler()` 内部会创建空闲任务（以及可选的定时器服务任务），再经 **SVC** 切入第一个任务；之后的切换靠 **PendSV**，节拍靠 **SysTick**。

---

## 5. 检查清单

1. 三个 FreeRTOS ISR 已映射到向量表中的 CMSIS 名（或向量表已改名）
2. HAL 时间基准已从 SysTick 挪到其它定时器
3. `main` 中先 `xTaskCreate`，再 `vTaskStartScheduler`
4. `FreeRTOSConfig.h` 里 tick 频率、中断优先级上限等与芯片一致
