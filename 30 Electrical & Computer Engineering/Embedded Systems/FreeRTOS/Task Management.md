---
aliases: [任务管理, 创建任务, xTaskCreate, 任务句柄, 任务优先级]
tags: [FreeRTOS, embedded, rtos]
up: "[[FreeRTOS Overview]]"
related: ["[[Task States]]", "[[Preemptive and Cooperative Scheduling]]", "[[Installing Interrupt Handlers]]"]
---
# Task Management

> [!summary] 核心结论
> 用户任务用 `xTaskCreate`（堆上动态分配）或 `xTaskCreateStatic`（用户提供内存）创建。同一段任务函数可通过 `pvParameters` 跑出多个实例；`uxPriority` 决定谁先跑；`pxCreatedTask` 返回句柄，后续的挂起 / 恢复 / 删除都靠它。

---

## 1. 两种创建方式

| API | 方式 | 内存从哪来 |
| --- | ---- | ---------- |
| `xTaskCreate` | 动态（默认） | FreeRTOS 堆（`heap_1`～`heap_5`） |
| `xTaskCreateStatic` | 静态（高级） | 用户手动提供 TCB / 栈缓冲区 |

堆方案背景见 [[Heap Memory Management]]。

---

## 2. `xTaskCreate` 参数

```c
BaseType_t xTaskCreate(
    TaskFunction_t pxTaskCode,                 /* 任务函数 */
    const char * const pcName,                 /* 调试用名字 */
    const configSTACK_DEPTH_TYPE uxStackDepth, /* 栈深度（字，不是字节） */
    void * const pvParameters,                 /* 传给任务的参数 */
    UBaseType_t uxPriority,                    /* 优先级 */
    TaskHandle_t * const pxCreatedTask         /* 输出：任务句柄 */
);
```

返回 `pdPASS` 表示创建成功。

---

## 3. `pvParameters`：一段代码，多个实例

任务函数签名是 `void (*)(void *pvParameters)`。典型用法：同一函数、不同参数，创建多个任务。

### 3.1 例：LED1 / LED3 共用闪灯任务

目标：只写一段任务代码；LED1 周期 1000 ms，LED3 周期 200 ms。

**① 用结构体打包“闪谁、多快”：**

```c
typedef struct {
    GPIO_TypeDef *LED_GPIOx; /* GPIO 端口 */
    uint16_t      LED_Pin;   /* 引脚 */
    uint32_t      Period;    /* 闪灯周期 (ms) */
} LEDBlinkInfoTypeDef;
```

**② 两个常量实例：**

```c
/* LED1：PC3，1000 ms */
static const LEDBlinkInfoTypeDef led1BlinkInfo = {
    .LED_GPIOx = GPIOC,
    .LED_Pin   = GPIO_PIN_3,
    .Period    = 1000
};

/* LED3：PC2，200 ms */
static const LEDBlinkInfoTypeDef led3BlinkInfo = {
    .LED_GPIOx = GPIOC,
    .LED_Pin   = GPIO_PIN_2,
    .Period    = 200
};
```

**③ 创建时把地址塞进 `pvParameters`：**

```c
xTaskCreate(prvLEDTask, "LED1", 128, (void *)&led1BlinkInfo, 1, NULL);
xTaskCreate(prvLEDTask, "LED3", 128, (void *)&led3BlinkInfo, 1, NULL);
```

任务函数里把 `pvParameters` 转回结构体指针即可读端口 / 引脚 / 周期。常量须在任务存活期内一直有效（`static` / 全局），不要传栈上临时变量的地址。

---

## 4. `uxPriority`：优先级

- 调度器**总是**选就绪队列里优先级最高的任务执行。
- 合法范围：`0` ～ `configMAX_PRIORITIES - 1`；**`0` 最低**（空闲任务也在这一档）。
- 例：`#define configMAX_PRIORITIES 5` → 可用优先级为 `0`～`4`。

同优先级时是否时间片轮转，取决于调度配置（见 [[FreeRTOS Overview#1. 总览（架构地图）]]）。

---

## 5. `pxCreatedTask`：任务句柄

创建成功后，句柄经这个**输出参数**交还给你。之后凡是“针对某个任务”的操作都要用它：

| API | 作用 | `NULL` 的含义 |
| --- | ---- | ------------- |
| `vTaskSuspend(xTaskToSuspend)` | 暂停任务 | 暂停**自身** |
| `vTaskResume(xTaskToResume)` | 恢复已暂停的任务 | （不适用，需有效句柄） |
| `vTaskDelete(xTaskToDelete)` | 删除任务 | 删除**自身** |

不需要后续操作时，最后一个参数可填 `NULL`。

### 5.1 例：Task1 控制 LED 闪灯任务的生命周期

先保存 LED 任务句柄，再创建控制任务：

```c
static TaskHandle_t xLED1TaskHandle;

static void prvTask1(void *pvParameters)
{
    (void)pvParameters;

    vTaskDelay(pdMS_TO_TICKS(1000));
    vTaskSuspend(xLED1TaskHandle);   /* 暂停 LED1 */

    vTaskDelay(pdMS_TO_TICKS(1000));
    vTaskResume(xLED1TaskHandle);    /* 恢复 LED1 */

    vTaskDelay(pdMS_TO_TICKS(1000));
    vTaskDelete(xLED1TaskHandle);    /* 删掉 LED1 */

    vTaskDelete(NULL);               /* 删掉自身 */
}

/* main 里： */
xTaskCreate(prvLED1Task, "LED1", 128, NULL, 1, &xLED1TaskHandle);
xTaskCreate(prvTask1,    "Task1", 128, NULL, 1, NULL);
```

> [!note] 删除与内存
> 动态创建的任务被 `vTaskDelete` 后，TCB / 栈由**空闲任务**回收。若空闲任务长期跑不到，内存可能迟迟不释放。

---

## 6. 与 Overview 的衔接

1. `main` 初始化硬件 → `xTaskCreate`（可带参数 / 句柄）→ `vTaskStartScheduler`
2. 调度行为由优先级 + 阻塞（如 `vTaskDelay`）驱动；中断侧见 [[Installing Interrupt Handlers]]
