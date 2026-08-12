---
aliases: [ADC编程接口, ADC标准库函数, ADC_Init, ADC_Cmd]
tags: [stm32, 标准库]
up: "[[STM32 MOC]]"
related: "[[ADC Analog-to-Digital Converter|ADC 模数转换器]], [[Clocks|时钟树]]"
---
# ADC Programming Interface

> [!summary] 核心结论
> 标准库的 ADC 接口按用途分四类：**通用**（初始化、总开关、标志位、中断、DMA）、**常规序列**、**注入序列**、**校准相关**。原理部分见 [[ADC Analog-to-Digital Converter]]。

---

## 1. 函数速查表

| 序号  | 分类   | 编程接口                                 | 作用            |
| --- | ---- | ------------------------------------ | ------------- |
| 1   | 通用   | `ADC_Init`                           | 设置 ADC 的基本参数  |
| 2   | 通用   | `ADC_Cmd`                            | 总开关           |
| 3   | 通用   | `ADC_GetFlagStatus`                  | 获取标志位的值       |
| 4   | 通用   | `ADC_ClearFlag`                      | 清除标志位         |
| 5   | 通用   | `ADC_ITConfig`                       | 配置中断          |
| 6   | 通用   | `ADC_DMACmd`                         | 配置 DMA 请求     |
| 7   | 通用   | `ADC_TempSensorVrefintCmd`           | 温度计和参考电压开关    |
| 8   | 常规序列 | `ADC_RegularChannelConfig`           | 配置常规序列的通道     |
| 9   | 常规序列 | `ADC_ExternalTrigConvCmd`            | 外部触发开关（常规）    |
| 10  | 常规序列 | `ADC_SoftwareStartConvCmd`           | 软件启动（常规）      |
| 11  | 常规序列 | `ADC_GetConversionValue`             | 读取 DR 寄存器的值   |
| 12  | 注入序列 | `ADC_InjectedSequencerLengthConfig`  | 设置注入序列的长度     |
| 13  | 注入序列 | `ADC_InjectedChannelConfig`          | 配置注入序列的通道     |
| 14  | 注入序列 | `ADC_ExternalTrigInjectedConvCmd`    | 外部触发开关（注入）    |
| 15  | 注入序列 | `ADC_ExternalTrigInjectedConvConfig` | 选择注入序列的外部触发   |
| 16  | 注入序列 | `ADC_SetInjectedOffset`              | 设置注入序列的通道偏置   |
| 17  | 注入序列 | `ADC_SoftwareStartInjectedConvCmd`   | 软件启动（注入）      |
| 18  | 注入序列 | `ADC_GetInjectedConversionValue`     | 读取 JDRx 寄存器的值 |
| 19  | 校准相关 | `ADC_ResetCalibration`               | 复位校准寄存器       |
| 20  | 校准相关 | `ADC_GetResetCalibrationStatus`      | 查询复位是否完成      |
| 21  | 校准相关 | `ADC_StartCalibration`               | 启动校准          |
| 22  | 校准相关 | `ADC_GetCalibrationStatus`           | 查询校准是否完成      |
