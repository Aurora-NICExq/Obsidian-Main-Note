---
aliases: [时钟, 时钟树, RCC, HSI, HSE, LSI, LSE, PLL, SYSCLK, AHB, APB1, APB2]
tags: [stm32, 硬件原理]
up: "[[STM32 MOC]]"
related: "[[Timers|定时器]], [[GPIO Principles|GPIO 原理]], [[ADC Analog-to-Digital Converter|ADC]]"
---
# Clocks

> [!summary] 核心结论
> 时钟决定片上外设的工作速度。时钟树由三种基本器件搭成：**分频器**（除法）、**锁相环 PLL**（乘法）、**复用器 Mux**（选择）。四个时钟源中 **HSE 8MHz 经 PLL ×9 得到 72MHz SYSCLK** 是最常用配置。SYSCLK 经 AHB 分频器得 HCLK，再分给 APB1（≤36MHz）和 APB2（≤72MHz）。上电后启动文件先调用 `SystemInit` 完成整套配置，所以 `main()` 里什么都不写系统就已跑在 72MHz。提速前必须先设 Flash 等待周期。

---

## 1. 时钟树

### 1.1 时钟的作用

1. 时钟用于控制片上外设的工作
2. 时钟信号的频率决定了片上外设的工作速度

### 1.2 时钟树总图

![[Gemini_Generated_Image_dn26ngdn26ngdn26.jpg]]

### 1.3 分频器、锁相环和复用器

1. **分频器 (Prescaler)**
   - **作用**：**对频率做除法**。
   - **对应时钟树**：对应时钟树图中写着 `/1, /2 ... /512` 的白色方框。它的作用是把高速时钟（如 72MHz）降频，供给那些不需要跑太快的外设（比如低速总线 APB1）。

2. **锁相环 (PLL - Phase Locked Loop)**
   - **作用**：**对频率做乘法**。
   - **对应时钟树**：对应图中写着 `x2, x3 ... x16` 的灰色方框。STM32 的外部晶振通常只有 8MHz，为了达到 72MHz 的主频，必须靠锁相环把它放大 9 倍 (8MHz * 9 = 72MHz)。

3. **复用器 (Multiplexer / Mux)**
   - **作用**：**对频率做选择**。
   - **对应时钟树**：对应图中那些**梯形**的符号。它就像一个多路开关，决定了最终的时钟源是来自 HSI（内部高速时钟）、HSE（外部高速时钟）还是 PLL。

---

## 2. 时钟源

### 2.1 高速时钟（用于驱动 CPU 和主要外设）

这组时钟决定了单片机跑得快不快（性能）。

1. **HSI (High Speed Internal) - 高速内部时钟**
   - **频率**：**8MHz**。
   - **特点**：它是芯片内部的一个 RC 振荡器。
   - **优点**：**成本低**，不需要外部晶振，上电就能用（STM32 上电复位后默认使用它）。
   - **缺点**：**精度较差**，容易受温度影响而漂移。
2. **HSE (High Speed External) - 高速外部时钟**
   - **频率**：支持 **4 ~ 16MHz** 的外部晶振（开发板上通常接 8MHz）。
   - **特点**：需要你在芯片外部接一个石英晶振（OSC_IN / OSC_OUT）。
   - **作用**：它是**最常用**的时钟源。通常我们使用 HSE 接入**锁相环 (PLL)**，将 8MHz 倍频到 **72MHz** 来作为系统主频 (SYSCLK)。
   - **优点**：**精度极高**，非常稳定。

### 2.2 低速时钟（用于看门狗和 RTC）

这组时钟决定了单片机在睡眠或低功耗下的计时功能。

1. **LSE (Low Speed External) - 低速外部时钟**
   - **频率**：**32.768kHz**。
   - **特点**：外接一个圆柱形的小晶振（像手表里用的那种）。
   - **作用**：专门主要用于驱动 **RTC (实时时钟)**。
   - **为什么是 32.768k？** 因为 $2^{15} = 32768$，这个频率经过 15 次二分频后，刚好能得到 **1Hz**（也就是 1 秒），非常适合走时。
2. **LSI (Low Speed Internal) - 低速内部时钟**
   - **频率**：约为 **40kHz**。
   - **特点**：芯片内部的低功耗 RC 振荡器。
   - **作用**：
     1. 驱动 **IWDG (独立看门狗)**。
     2. 也可以作为 RTC 的备用时钟（如果为了省钱不接 LSE 的话）。
   - **缺点**：精度非常差（波动范围很大）。

![[截屏2026-02-04 上午10.25.07.png]]

### 2.3 系统时钟（SYSCLK）

1. **SYSCLK 来自 HSI (内部高速时钟)**
   - **特点**：精度低。
   - **频率**：固定为 **8MHz**。
   - **场景**：通常作为备用，或者用于对成本敏感、对时钟精度要求不高的场合。
2. **SYSCLK 来自 锁相环 (PLL)**
   - **特点**：灵活。
   - **频率**：**SYSCLK 可变**。
   - **场景**：**最常用的模式**。通过 PLL 倍频，可以让 STM32 跑在最高的 72MHz 频率下，发挥最大性能。
3. **SYSCLK 来自 HSE (外部高速时钟)**
   - **特点**：精度高。
   - **频率**：直接等于 **HSE 频率**（取决于外部接的晶振，如 8MHz）。
   - **场景**：不经过 PLL 直接使用外部晶振频率，适用于不需要很高主频但需要极高稳定性的场合。

### 2.4 总线

- **AHB (Advanced High-Speed Bus)**：**高级高速总线**。
- **APB1 (Advanced Peripheral Bus 1)**：**高级外设总线 1**。
- **APB2 (Advanced Peripheral Bus 2)**：**高级外设总线 2**。

### 2.5 定时器倍频器

1. 如果 APB2 分频系数 = 1，`TIM_CLK = PCLK2`，否则 `TIM_CLK = PCLK2 * 2`
2. 如果 APB1 分频系数 = 1，`TIM_CLK = PCLK1`，否则 `TIM_CLK = PCLK1 * 2`

---

## 3. 时钟树编程

### 3.1 时钟树的初始状态

1. 时钟源来自 HSI
2. 三个分频器的分频系数都是 1

### 3.2 标准库的启动代码

```asm
LDR R0, =SystemInit  ; 把 SystemInit 函数的地址加载到 R0 寄存器
BLX R0               ; 跳转执行 R0 指向的地址（即调用 SystemInit 函数）
```

1. **SystemInit**
   - 一个 C 语言函数，通常定义在 `system_stm32f10x.c` 文件中。
   - 它的核心任务就是**配置 RCC**：开启 HSI，设置 PLL，配置 AHB/APB 分频器，最终把系统时钟 (SYSCLK) 设置为 **72MHz**。
2. **这段汇编的意义**
   - 在单片机复位后，首先执行的是启动文件（Startup file）。
   - 这段代码证明了：**在程序跳转到 C 语言的 `main` 函数之前，时钟系统就已经被 `SystemInit` 配置好了。**
   - 这就是为什么在 `main()` 里什么都不用写，系统就已经跑在 72MHz 下的原因。

### 3.3 时钟树的编程接口

1. **RCC = Reset And Clock Controller**
2. **中文名：复位和时钟控制器**

```c
// 1. 外部高速时钟 (HSE) 配置
void RCC_HSEConfig(uint32_t RCC_HSE);        // HSE开关 (ON/OFF/Bypass)

// 2. 内部高速时钟 (HSI) 控制
void RCC_HSICmd(FunctionalState NewState);   // HSI开关 (ENABLE/DISABLE)

// 3. 锁相环 (PLL) 配置与控制
// 配置PLL输入源和倍频系数 (如: RCC_PLLSource_HSE_Div1, RCC_PLLMul_9)
void RCC_PLLConfig(uint32_t RCC_PLLSource, uint32_t RCC_PLLMul); 
void RCC_PLLCmd(FunctionalState NewState);   // PLL开关 (ENABLE/DISABLE)

// 4. 系统时钟 (SYSCLK) 选择
// 选择谁作为系统主时钟 (HSI, HSE, PLL)
void RCC_SYSCLKConfig(uint32_t RCC_SYSCLKSource); 

// 5. 总线分频器配置
void RCC_HCLKConfig(uint32_t RCC_SYSCLK);    // 配置AHB总线时钟 (HCLK)
void RCC_PCLK1Config(uint32_t RCC_HCLK);     // 配置APB1低速总线 (PCLK1)
void RCC_PCLK2Config(uint32_t RCC_HCLK);     // 配置APB2高速总线 (PCLK2)

// 6. 状态检查
// 检查标志位 (如: RCC_FLAG_HSERDY 检查外部晶振是否起振稳定)
FlagStatus RCC_GetFlagStatus(uint8_t RCC_FLAG); 

// 获取当前系统时钟来源 (00:HSI, 0x04:HSE, 0x08:PLL)
uint8_t RCC_GetSYSCLKSource(void);
```

### 3.4 配置锁相环

```c
// 配置锁相环的参数
// @参数 RCC_PLLSource 选择锁相环的输入 RCC_PLLSource_HSE_Div1 - HSE
//                                      RCC_PLLSource_HSE_Div2 - HSE/2
//                                      RCC_PLLSource_HSI_Div2 - HSI/2
void RCC_PLLConfig(uint32_t RCC_PLLSource, uint32_t RCC_PLLMul);

// 控制锁相环的开关
void RCC_PLLCmd(FunctionalState NewState);   // ENABLE - 开 DISABLE - 关

// 获取RCC的状态
// @参数 RCC_FLAG  RCC_FLAG_PLLRDY - PLL就绪
FlagStatus RCC_GetFlagStatus(uint8_t RCC_FLAG);
```

### 3.5 配置 Flash 指令预取

```c
// @注意 需在SYSCLK <= 8MHz时进行

// 开启Flash指令预取
FLASH_PrefetchBufferCmd(ENABLE);

// 设置Flash访问延迟
FLASH_SetLatency(FLASH_Latency_2);
```

**速度差问题**：

- STM32 的 Cortex-M3 **内核**跑得非常快（最高 72MHz）。
- 但是片上的 **Flash 存储器**读取速度相对较慢（通常只有 24MHz 左右）。

**加入等待 (Latency)**：

- 当内核加速到 72MHz 时，它发出的取指请求太快了，Flash 来不及给数据。
- 所以必须设置 `FLASH_SetLatency(FLASH_Latency_2)`，告诉内核：“每次读 Flash，请多等 2 个周期。”。
- 如果不设置延迟直接把频率超到 72M，CPU 读到的指令就会是乱码，程序直接崩溃。

**时机选择**：

- 注意代码第一行的注释：**“需在 SYSCLK <= 8MHz 时进行”**。
- 这意味着必须在系统还运行在低速状态（刚启动时的 HSI 或 HSE）时就先把这个“安全带”系好，然后再去开启 PLL 提速。

### 3.6 片上外设开关和复位

```c
// 开启/关闭AHB总线上的片上外设的时钟
// (例如: DMA, CRC等)
void RCC_AHBPeriphClockCmd(uint32_t RCC_AHBPeriph, FunctionalState NewState);

// 开启/关闭APB2总线上的片上外设的时钟
// (重点: GPIO, ADC, USART1, SPI1等高速外设)
void RCC_APB2PeriphClockCmd(uint32_t RCC_APB2Periph, FunctionalState NewState);

// 开启/关闭APB1总线上的片上外设的时钟
// (重点: I2C, CAN, USART2/3, SPI2/3等低速外设)
void RCC_APB1PeriphClockCmd(uint32_t RCC_APB1Periph, FunctionalState NewState);

// 复位APB2总线上的片上外设
// (相当于给某个具体的外设按一下重启键)
void RCC_APB2PeriphResetCmd(uint32_t RCC_APB2Periph, FunctionalState NewState);

// 复位APB1总线上的片上外设
void RCC_APB1PeriphResetCmd(uint32_t RCC_APB1Periph, FunctionalState NewState);
```
