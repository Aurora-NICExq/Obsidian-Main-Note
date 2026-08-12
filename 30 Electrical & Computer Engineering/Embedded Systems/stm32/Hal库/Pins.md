---
aliases: [引脚, Pins, HAL引脚, HAL_GPIO_WritePin, HAL_GPIO_ReadPin, Serial Wire]
tags: [stm32, HAL库]
up: "[[STM32 MOC]]"
related: "[[GPIO Principles|GPIO 原理]], [[Hardware Circuits|硬件电路]]"
---
# Pins

> [!summary] 核心结论
> STM32F103C8T6（LQFP48）可用的 GPIO 为 **GPIOA/GPIOB 各 16 个**、**PC13~PC15**、**PD0~PD1**。调试口选 **Serial Wire** 而非 JTAG，可释放更多 IO。HAL 层操作引脚只需三个函数：`HAL_GPIO_WritePin` 写、`HAL_GPIO_ReadPin` 读、`HAL_Delay` 延时。

---

## 1. 引脚分布

![[截屏2026-03-06 下午6.14.25.png]]

| GPIO 组 | 引脚范围/编号          |
| ------- | ---------------------- |
| GPIOA   | PA0、PA1、PA2、…、PA15 |
| GPIOB   | PB0、PB1、PB2、…、PB15 |
| GPIOC   | PC13、PC14、PC15       |
| GPIOD   | PD0、PD1               |

### 1.1 调试接口选择

Debug 选择：Serial Wire

作用：释放更多 IO 引脚，防止 **JTAG** 占用过多引脚。

---

## 2. 闪灯实验

```c
void HAL_GPIO_WritePin(GPIOx, GPIO_Pin, PinState)
```

作用：向 IO 写 0/1

参数 GPIOx：组编号，x 取 A..D
参数 GPIO_Pin：引脚编号，GPIO_PIN_0..15
参数 PinState：要写的值，GPIO_PIN_RESET - 0
　　　　　 GPIO_PIN_SET - 1

```c
void HAL_Delay(uint32_t Delay)
```

作用：延迟一段时间

参数 Delay：要延迟的时间长度，单位 ms

---

## 3. 按钮实验

```c
GPIO_PinState HAL_GPIO_ReadPin(GPIOx, GPIO_Pin)
```

作用：读取 IO 的当前值

参数 GPIOx：组编号，x 取 A..D
参数 GPIO_Pin：引脚编号，GPIO_PIN_0..15
