---
aliases: [STM32 导航, STM32 MOC, STM32 Index, 单片机导航]
tags: [stm32, MOC]
up: ""
related: "[[FreeRTOS Overview|FreeRTOS]], [[Basic Circuit Theory MOC|电路理论 MOC]], [[Signals and Systems MOC|信号与系统 MOC]]"
down: "[[Clocks|时钟树]], [[GPIO Principles|GPIO 原理]], [[Hardware Circuits|硬件电路]], [[Timers|定时器]], [[ADC Analog-to-Digital Converter|ADC]], [[ADC Programming Interface|ADC 编程接口]], [[UART Serial Port|串口]], [[I2C]], [[SPI]], [[MPU6050]], [[W25Q64 Module|W25Q64]], [[OLED Display|OLED 显示器]], [[Pins|HAL 引脚]]"
---
# STM32 MOC

> [!summary] 学习主线
> 以 **STM32F103C8T6（Cortex-M3, LQFP48）标准库** 为主线：先搞清**时钟**（一切外设的前提）和 **GPIO**（一切引脚行为的前提），再看挂在 IO 上的**外围电路**；然后是两大内置外设——**定时器**（时间维度）与 **ADC**（模拟量维度）；接着是三种**通信协议** UART / I2C / SPI；最后用这些协议去驱动实际**外接模块**。HAL 库单列。

---

## 一、时钟：一切外设的前提

- [[Clocks|Clocks 时钟树]]：HSI/HSE/LSI/LSE 四个时钟源、PLL 倍频、AHB/APB 分频、`RCC` 编程接口、Flash 等待周期

> [!tip]
> 任何外设不工作，第一件事是检查 `RCC_APBxPeriphClockCmd` 有没有开对应时钟。

## 二、GPIO 与外围电路

- [[GPIO Principles|GPIO Principles]]：位结构、保护二极管、施密特触发器、P/N-MOS 输出级、**八种工作模式**
- [[Hardware Circuits|Hardware Circuits]]：LED 限流、三极管驱动蜂鸣器、传感器模块分压与 LM393 二值化

## 三、定时器：时间维度

- [[Timers|Timers]]：时基单元（PSC/CNT/ARR/RCR）、寄存器预加载、**输出比较与 PWM**、**输入捕获**、从模式控制器、编码器接口

## 四、ADC：模拟量维度

- [[ADC Analog-to-Digital Converter|ADC 模数转换器]]：逐次逼近原理、多路复用、常规序列与注入序列、采样时间与信号源内阻
- [[ADC Programming Interface|ADC 编程接口]]：标准库 22 个 ADC 函数速查表

## 五、通信协议

| 协议 | 线数 | 拓扑 | 同步 | 位序 |
| --- | --- | --- | --- | --- |
| UART | 2（TX / RX） | 一对一 | 异步 | 低位先行 |
| I2C | 2（SCL / SDA） | 一主多从 | 同步 | 高位先行 |
| SPI | 4（MOSI / MISO / SCK / NSS） | 一主多从 | 同步 | 可选 |

- [[UART Serial Port|UART Serial Port]]：数据帧格式、波特率、`TxE`/`TC`/`RxNE`、错误标志位
- [[I2C|I2C]]：逻辑线与、起始/停止位、寻址与 ACK、读写时序封装、软件 I2C
- [[SPI|SPI]]：CPOL/CPHA 四种模式、全双工同时收发、`TXE`/`RXNE`/`BSY`

## 六、外接模块

- [[MPU6050|MPU6050]]（走 [[I2C]]）：六轴 IMU、寄存器读写、解算欧拉角、**互补滤波**
- [[W25Q64 Module|W25Q64 Module]]（走 [[SPI]]）：Flash 存储、写使能 → 擦除 → 页编程、读数据 `0x03`
- [[OLED Display|OLED Display]]（走 [[I2C]]）：初始化接口与 i2c 写回调

## 七、HAL 库

- [[Pins|Pins]]：引脚分布、Serial Wire 调试口、`HAL_GPIO_WritePin` / `HAL_GPIO_ReadPin` / `HAL_Delay`

---

## 推荐学习顺序

![[d2-stm32-moc-01.svg]]

---

## 延伸方向

- **实时系统**：[[FreeRTOS Overview|FreeRTOS 概览]]、[[Task Management|任务管理]]、[[Task States|任务状态]]、[[Preemptive and Cooperative Scheduling|调度策略]]、[[Heap Memory Management|堆内存管理]]
- **控制算法**：[[PID_Algorithms|PID]]、[[LQR_Algorithms|LQR]]、[[MPC Model Predictive Control|MPC]]
- **底层理论**：[[Basic Formulas and Theorems|数字信号的表示]]、[[Counters|计数器原理]]、[[Shift Registers|移位寄存器]]、[[Capacitors and Their Properties|电容特性]]

---

## 目录实况（Dataview 自动生成）

上面的分组是手工编排的**学习顺序**；下面这张表由 Dataview 实时扫描目录生成，用来**核对有没有漏收的笔记**：

```dataview
TABLE file.folder AS 所在目录
FROM "30 Electrical & Computer Engineering/Embedded Systems/stm32"
WHERE file.name != this.file.name
SORT file.folder ASC, file.name ASC
```

本篇待补充的主题：

```dataview
LIST
FROM "30 Electrical & Computer Engineering/Embedded Systems/stm32"
WHERE contains(file.tags, "#待补充") OR contains(file.tags, "#待补充的实验") OR contains(file.tags, "#NVIC知识点") OR contains(file.tags, "#实验补充")
```

---

> [!todo] 尚未成篇
> **外部中断 EXTI / NVIC**（`Timers.md` 中留有 `#NVIC知识点` 标记，`attachments/` 下存有 ST 官方图19 框图待用）、**DMA**、**RTC**、**看门狗**。
