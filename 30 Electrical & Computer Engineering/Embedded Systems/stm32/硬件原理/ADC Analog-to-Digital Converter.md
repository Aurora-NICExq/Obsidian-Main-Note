---
aliases: [ADC, 模数转换器, 逐次逼近, SAR, 常规序列, 注入序列, 采样保持]
tags: [stm32, 标准库]
up: "[[STM32 MOC]]"
related: "[[ADC Programming Interface|ADC 编程接口]], [[Clocks|时钟树]], [[Timers|定时器]], [[GPIO Principles|GPIO 原理]]"
---
# ADC Analog-to-Digital Converter

> [!summary] 核心结论
> STM32F103C8T6 有 ADC1/ADC2 共 10 个外部通道，**12 位逐次逼近型**，输入 0~3.3V 对应结果 0~4095。一个 ADC 靠**多路复用**轮流转换多个通道，顺序由**常规序列**（16 通道，共用一个 DR）或**注入序列**（4 通道，各有 JDRx，优先级更高）决定。ADC 时钟不得超过 **14MHz**，PCLK2 六分频后为 12MHz，此时转换耗时约 **1.04us**。总时间 = 采样时间 + 转换时间，信号源内阻越大所需采样时间越长。

---

## 1. 逐次逼近型 ADC

### 1.1 简介

- ADC（Analog-Digital Converter） 模拟-数字转换器
- ADC可以将引脚上连续变化的模拟电压转换为内存中存储的数字变量[[Basic Formulas and Theorems#^b60fca|数字信号只有高低电平]]
- 12位逐次逼近型（工作模式）ADC，1us转换时间（最快转换频率）。
- 输入电压范围：0~3.3V，转换结果范围：0~4095（12位分辨率）
- STM32F103C8T6 ADC资源：ADC1、ADC2，10个外部输入通道

### 1.2 采样深度

采样深度：用多少二进制位表示转换结果，采样深度越深，误差越小

![[截屏2026-02-03 下午3.30.01-2347932.png]]

### 1.3 内部结构框图

![[截屏2026-02-03 下午3.48.06-2347947.png]]

- 采样比较器对两个输入信号进行比较。
- 正输入电压大于负输入，输出一个1，否则是0。
- 结果寄存器用于存储ADC比较之后的结果。
- 电压发生器根据结果寄存器的值输出对应电压

以 ADC0809 为例的完整芯片结构：

![[image-20260125132844758.png]]

### 1.4 采样保持电路

1. 作用：通过电路，保持采样采下的正输入电压不变（模拟信号是不断变化的）
2. 工作流程：
   - 采样：开关闭合，电容充电（电压等于模拟信号两端电压）
   - 保持：开关断开，电容电压保持不变

---

## 2. STM32 的 ADC 内部结构

### 2.1 ADC 的多路复用

只使用一个ADC，同时去转换多个模拟信号

![[截屏2026-02-03 下午4.33.47-2348107.png]]

1. 采样之后断开开关
2. 通过电路进行转换，转换的结果保存在结果寄存器中
3. C8T6中不存在通道10～13对应的引脚

### 2.2 常规序列

![[截屏2026-02-03 下午6.54.37-2348143.png]]

常规序列决定了多路复用情况下，开关闭合的先后顺序和闭合时间

1. **通道 7 (Channel 7)**：采样时间 **0.1 us**。
2. **通道 8 (Channel 8)**：采样时间 **0.2 us**。
3. **通道 9 (Channel 9)**：采样时间 **0.1 us**。

外部触发信号：输出上升沿作为启动信号

### 2.3 注入序列

- 相比于常规序列，通道更少
- 每个通道有单独的结果寄存器
- 优先级更高

![[截屏2026-02-03 下午7.20.26-2348157.png]]

---

## 3. 采样时间和转换时间

1. 采样时间：开关闭合的时间长度。
2. 转换时间：对采样点进行转换所消耗的时间。

### 3.1 ADC 的时钟频率

- ADC的输入时钟不得超过14MHz，它是由PCLK2经分频产生——RM0008数据手册
- PCLK2六分频之后，时钟频率为12MHz。

### 3.2 转换时间的计算方法

**单周期时间**：**0.083 us**。

- 计算方式：$1 / 12\text{MHz} \approx 0.083\text{us}$。

**转换时间计算**：

- **公式**：$12 \text{ cycle} + 0.5 \text{ cycle} = 12.5 \text{ cycle}$。
- **最终耗时**：$12.5 \times 0.083\text{us} \approx \mathbf{1.04\text{us}}$。

**完整的 ADC 转换总时间 ($T_{total}$)** 由两部分组成：

$$T_{total} = \text{采样时间} + \text{转换时间}$$

### 3.3 采样时间和信号源内阻

信号源内阻越大，电流越小，采样时间越长

#### 3.3.1 信号源内阻的计算方法

$$R_{AIN} < \frac{T_S}{f_{ADC} \times C_{ADC} \times \ln(2^{N+2})} - R_{ADC}$$

#### 3.3.2 采样时间的计算方法

$$T_S > (R_{AIN} + R_{ADC}) \times C_{ADC} \times \ln(2^{N+2}) \times f_{ADC}$$

**左边 $T_S$**：

- 代表需要配置的**采样周期数**（比如 1.5, 7.5, 13.5, 55.5 Cycles 等）。
- 注意：这里的 $T_S$ 单位是 **周期数 (Cycles)**，而不是时间秒。公式右边的 $f_{ADC}$ 把时间转换成了周期数。

**右边各项含义**：

- **$(R_{AIN} + R_{ADC}) \times C_{ADC}$**： **RC 时间常数 ($\tau$)**。它决定了电容充满电需要多长时间。阻值越大 ($R_{AIN}$)，充电越慢。
- **$\ln(2^{N+2})$**：这是一个与精度有关的系数。对于 12 位 ADC ($N=12$)，这个值大约是 $\ln(16384) \approx 9.7$。也就是大约需要 **10 个 RC 时间常数** 才能充得足够满。
- **$f_{ADC}$**：ADC 的时钟频率。

---

## 4. 常规单通道转换

### 4.1 初始化 IO 引脚

配置 PA0 引脚

### 4.2 配置 ADC 时钟

```c
// 设置分频器的分频系数（6分频）
RCC_ADCCLKConfig(RCC_PCLK2_Div6);

// 使能ADC1的时钟
RCC_APB2PeriphClockCmd(RCC_APB2Periph_ADC1, ENABLE);
```

ADC 需要 ENABLE 与设置分频系数

### 4.3 ADC 编程接口

参考 [[ADC Programming Interface]]

### 4.4 初始化 ADC 的基本参数

```c
ADC_InitTypeDef ADC_InitStruct = {0};

// 连续模式
ADC_InitStruct.ADC_ContinuousConvMode = ;

// 对齐方式（左/右）
ADC_InitStruct.ADC_DataAlign = ;

// 选择常规序列的外部触发信号
ADC_InitStruct.ADC_ExternalTrigConv = ;

// 双ADC模式
ADC_InitStruct.ADC_Mode = ;

// 常规序列的通道数
ADC_InitStruct.ADC_NbrOfChannel = ;

// 扫描模式
ADC_InitStruct.ADC_ScanConvMode = ;

ADC_Init(ADC1, &ADC_InitStruct);
```

#### 4.4.1 对齐方式

12 位转换结果放进 16 位数据寄存器 DR，空出的 4 位补 0：

| 对齐方式 | 15    | 14    | 13   | 12   | 11   | 10   | 9    | 8    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| -------- | ----- | ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **右对齐** | 0     | 0     | 0    | 0    | b11  | b10  | b9   | b8   | b7   | b6   | b5   | b4   | b3   | b2   | b1   | b0   |
| **左对齐** | b11   | b10   | b9   | b8   | b7   | b6   | b5   | b4   | b3   | b2   | b1   | b0   | 0    | 0    | 0    | 0    |

#待补充

---

## 5. 定时器触发

使用定时器产生 ADC 的外部触发信号的方式被称作定时器触发。

---

## 6. 注入序列的编程接口

```c
void ADC_InjectedSequencerLengthConfig(ADC_TypeDef* ADCx, uint8_t Length);
void ADC_ExternalTrigInjectedConvConfig(ADC_TypeDef* ADCx, uint32_t ADC_ExternalTrigInjecConv);
void ADC_ExternalTrigInjectedConvCmd(ADC_TypeDef* ADCx, FunctionalState NewState);
void ADC_SoftwareStartInjectedConvCmd(ADC_TypeDef* ADCx, FunctionalState NewState);
uint16_t ADC_GetInjectedConversionValue(ADC_TypeDef* ADCx, uint8_t ADC_InjectedChannel);
void ADC_SetInjectedOffset(ADC_TypeDef* ADCx, uint8_t ADC_InjectedChannel, uint16_t Offset);
void ADC_InjectedDiscModeCmd(ADC_TypeDef* ADCx, FunctionalState NewState);
```
