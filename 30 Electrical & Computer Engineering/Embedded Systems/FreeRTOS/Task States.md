---
aliases: [任务的4种状态, 任务状态, Running Ready Blocked Suspended, 阻塞与挂起]
tags: [FreeRTOS, embedded, rtos]
up: "[[FreeRTOS Overview]]"
related: ["[[Task Management]]", "[[Preemptive and Cooperative Scheduling]]", "[[Installing Interrupt Handlers]]"]
---
# Task States

> [!summary] 核心结论
> 单核上任一时刻只有一个任务处于 **Running**；其余都是非运行。非运行再分成 **Ready**（等 CPU）、**Blocked**（等超时 / 事件，主动放弃执行权）、**Suspended**（被 `vTaskSuspend` 踢出调度，直到 `vTaskResume`）。`vTaskDelay` 走的是 Blocked，不是 Suspended。

---

## 1. 先粗分，再四分

粗分（是否占用 CPU）：

| 大类 | 英文 | 含义 |
| ---- | ---- | ---- |
| 运行 | Running | 调度器选中，CPU 正在执行其任务代码 |
| 非运行 | Not-Running | 当前没有在跑 |

非运行再拆成三种，合起来就是常用的 **4 种状态**：

| 状态 | 英文 | 含义 |
| ---- | ---- | ---- |
| 运行 | Running | 正在执行 |
| 就绪 | Ready | 具备运行条件，在等被调度 |
| 阻塞 | Blocked | 等待超时或事件，**主动**放弃执行权 |
| 暂停 | Suspended | 调用 `vTaskSuspend` 后，调度器**不会**选中它 |

![[d2-task-states-01.svg]]

> [!note] Blocked vs Suspended
> - **Blocked**：自己等条件（延时、收队列、拿信号量…），条件满足后自动回 Ready。
> - **Suspended**：别人（或自己）调用 `vTaskSuspend`；**不会**因超时自行醒来，必须 `vTaskResume`。

API 细节见 [[Task Management#5. pxCreatedTask：任务句柄]]。

---

## 2. 例：`vTaskDelay` 让任务进入 Blocked

闪灯任务反复：翻转 GPIO → 延时 100 ms。

```c
static void prvLED1Task(void *pvParameters)
{
    (void)pvParameters;
    for (;;) {
        HAL_GPIO_TogglePin(LED1_GPIO_Port, LED1_Pin);
        vTaskDelay(pdMS_TO_TICKS(100)); /* 进入 Blocked，约 100 ms */
    }
}

xTaskCreate(prvLED1Task, "LED1", 128, NULL, 1, NULL);
```

状态怎么走（只有这一个用户任务时）：

1. 创建后进入 **Ready**；调度器选中 → **Running**，执行 `TogglePin`
2. `vTaskDelay` → **Blocked**；就绪队列往往只剩空闲任务 → 空闲任务 **Running**
3. 延时到 → LED 任务 **Ready** → 再被选中 **Running**
4. 循环往复：`Running ⇄ Blocked`（中间短暂经 Ready）

这就是 Overview 里“延时期间跑空闲任务”的状态版解释，见 [[FreeRTOS Overview#3.2 最小例子：一个 LED 任务]]。

---

## 3. 例：Suspended — Task1 暂停 / 恢复 LED 任务

承接 [[Task Management#5.1 例：Task1 控制 LED 闪灯任务的生命周期]]：

```c
static void prvLED1Task(void *pvParameters)
{
    (void)pvParameters;
    for (;;) {
        HAL_GPIO_TogglePin(LED1_GPIO_Port, LED1_Pin);
        vTaskDelay(pdMS_TO_TICKS(100));
    }
}

static void prvTask1(void *pvParameters)
{
    (void)pvParameters;

    vTaskDelay(pdMS_TO_TICKS(1000));
    vTaskSuspend(xLED1TaskHandle); /* LED1 → Suspended，灯停闪 */

    vTaskDelay(pdMS_TO_TICKS(1000));
    vTaskResume(xLED1TaskHandle);  /* LED1 → Ready，随后可再 Running */

    vTaskDelay(pdMS_TO_TICKS(1000));
    vTaskDelete(xLED1TaskHandle);
    vTaskDelete(NULL);
}
```

要点：

- `vTaskSuspend` 之前，LED1 在 **Running / Ready / Blocked** 之间正常闪
- 挂起后进入 **Suspended**：即使延时到了也不会被调度，灯停住
- `vTaskResume` 回到 **Ready**，再参与调度
- 这与 `vTaskDelay` 的 **Blocked** 不同：挂起不会“自己醒”

---

## 4. 记忆对照

| 现象 | 多半是什么状态 |
| ---- | -------------- |
| CPU 正在跑这段任务代码 | Running |
| 能跑、但有更高优先级在跑 / 同优先级轮不到 | Ready |
| `vTaskDelay`、等队列 / 信号量 / 通知 | Blocked |
| `vTaskSuspend`，必须 `vTaskResume` 才回来 | Suspended |
