---
aliases: [SPI, 串行外设接口, MOSI, MISO, SCK, NSS, CPOL, CPHA, 全双工]
tags: [stm32, 硬件原理]
up: "[[STM32 MOC]]"
related: "[[W25Q64 Module|W25Q64 模块]], [[I2C]], [[UART Serial Port|串口]], [[GPIO Principles|GPIO 原理]]"
---
# SPI

> [!summary] 核心结论
> SPI 是**同步全双工**串行总线，4 根线：MOSI / MISO / SCK / NSS（低电平选中）。**每发送 1 字节必然同时接收 1 字节**——这是所有 SPI 代码结构的根源。时钟极性 **CPOL** 与相位 **CPHA** 组合出 4 种模式，主从必须一致。收发的核心节奏是：等 `TXE` 再写 `DR`、等 `RXNE` 再读 `DR`，收尾等 `BSY=0` 再拉高片选。

---

## 1. 电路结构和通信协议

### 1.1 SPI 总线的电路结构

![[截屏2026-02-06 下午3.21.47.png]]

SPI（Serial Peripheral Interface）是同步串行通信，总线通常有 4 根线：

1. MOSI - Master Output Slave Input - 主发从收
2. MISO - Master Input Slave Output - 主收从发
3. SCK - Serial Clock - 串行时钟
4. NSS - Negative Slave Select - 从机选择（低电压有效）

### 1.2 通信流程

1. 确定通信参数
2. GPIO和时钟初始化
3. 配置SPI外设寄存器
4. 片选拉低，开始一帧通信
5. 按状态位完成收发
6. 片选拉高，结束通信

### 1.3 波形图

![[tikz-spi-01.svg]]

- NSS1存在低电压，其余保持高电压（选中NSS1进行通信）
- 主机通过SCK发送时钟信号
- 时钟信号频率决定通信速度
- SPI 是“全双工同步移位”：每发送 1 字节，同时也会接收 1 字节。

### 1.4 参数一：时钟信号的极性和相位

低极性：空闲状态下，SCK线上的时钟信号处于低电压，高极性相反

边沿：上升沿或者下降沿，空闲状态后，第一个边沿就是第1边沿

低极性下，所有上升沿都是第1边沿

![[tikz-spi-02.svg]]

### 1.5 SPI 的 4 种模式

| SPI模式 | CPOL（时钟极性） | CPHA（时钟相位） | SCK空闲电平 | 第一个边沿用于   | 第二个边沿用于   |
| ------- | ---------------- | ---------------- | ----------- | ---------------- | ---------------- |
| Mode 0  | 0                | 0                | 低电平      | 采样（采集数据） | 发送（数据变化） |
| Mode 1  | 0                | 1                | 低电平      | 发送（数据变化） | 采样（采集数据） |
| Mode 2  | 1                | 0                | 高电平      | 采样（采集数据） | 发送（数据变化） |
| Mode 3  | 1                | 1                | 高电平      | 发送（数据变化） | 采样（采集数据） |

### 1.6 参数二：传输顺序

| 传输顺序  | 全称                        | 先发送的位     | 后发送的位     | 例：发送 `0x96`（二进制 `1001 0110`）时的顺序 |
| --------- | --------------------------- | -------------- | -------------- | --------------------------------------------- |
| MSB First | Most Significant Bit First  | 最高位（bit7） | 最低位（bit0） | `1 → 0 → 0 → 1 → 0 → 1 → 1 → 0`               |
| LSB First | Least Significant Bit First | 最低位（bit0） | 最高位（bit7） | `0 → 1 → 1 → 0 → 1 → 0 → 0 → 1`               |

### 1.7 参数三：数据宽度

数据宽度指的是：**一次按帧（frame）传输多少位**。

可以选择 8bit 或者 16bit

---

## 2. IO 引脚初始化

### 2.1 W25Q64 简介

1. 断电不丢失数据
2. SPI接口通信

详见 [[W25Q64 Module]]。

### 2.2 引脚分布

- VCC - 接电源+
- GND - 接地
- DI(Slave Data Input MOSI) - 接主机的MOSI
- DO(Slave Data Output MISO) - 接主机的MISO
- CLK(Serial Clock SCK) - 接主机的SCK

### 2.3 SPI 的引脚位置

> 表49　SPI1 重映像

| 复用功能    | `SPI1_REMAP = 0` | `SPI1_REMAP = 1` |
| ----------- | ---------------- | ---------------- |
| `SPI1_NSS`  | PA4              | PA15             |
| `SPI1_SCK`  | PA5              | PB3              |
| `SPI1_MISO` | PA6              | PB4              |
| `SPI1_MOSI` | PA7              | PB5              |

#待补充的实验

---

## 3. SPI 模块初始化

### 3.1 模块结构框图

![[截屏2026-02-10 下午1.27.30.png]]

### 3.2 SPI_Init

```c
void SPI_Init(SPI_TypeDef *SPIx,                 // SPI的名称，可以是SPI1或SPI2
              SPI_InitTypeDef *SPI_InitStruct);  // 用于传递初始化参数
// 作用：对SPI模块进行初始化
```

结构体参数：

```c
struct SPI_InitTypeDef{
    uint16_t SPI_Direction;          // 用来选择SPI通信的方向
    uint16_t SPI_Mode;               // 用来选择SPI的模式，SPI_Master - 主机，SPI_Slave - 从机
    uint16_t SPI_DataSize;           // 数据宽度，SPI_DataSize_8b - 8bit，SPI_DataSize_16b - 16bit
    uint16_t SPI_CPOL;               // 时钟的极性
    uint16_t SPI_CPHA;               // 时钟的相位
    uint16_t SPI_NSS;                // 软件NSS/硬件NSS
    uint16_t SPI_BaudRatePrescaler;  // 用来选择波特率分频器的分频系数
    uint16_t SPI_FirstBit;           // 比特位的传输顺序，SPI_FirstBit_MSB 从最高位到最低位，LSB 从低到高
}
```

### 3.3 选择数据通信方向

![[截屏2026-02-10 下午2.01.41.png]]

- 2线只读：从机只通过MOSI接收主机发来的数据，同时不会通过MISO向主机返回数据（用于主机向从机广播）

```c
uint16_t SPI_Direction;  // 通信的方向 - SPI_Direction_2Lines_FullDuplex  2线全双工
                         //            - SPI_Direction_2Lines_ReadOnly    2线只读
                         //            - SPI_Direction_1Line_Rx           单线接收
                         //            - SPI_Direction_1Line_Tx           单线发送
```

---

## 4. 数据收发

### 4.1 SPI 收发特点

1. SPI数据收发是双向的、同时的
2. 每发送一个比特位必然接收一个比特位

### 4.2 编程接口

```c
void App_SPI_MasterTransmitReceive(SPI_TypeDef *SPIx,      // SPI的名称
                                   const uint8_t *pDataTx, // 要发送的数据
                                   uint8_t *pDataRx,       // 接收到的数据
                                   uint16_t Size);         // 收发数据的数量
// 作用：使用SPI总线收发数据
```

### 4.3 标志位

| 标志位   | 含义           | 什么时候为1                               | 常见用途                     |
| -------- | -------------- | ----------------------------------------- | ---------------------------- |
| **TXE**  | 发送缓冲区空   | 说明可以写入下一字节/下一帧到 `DR`        | 发数据前先等 TXE=1，避免覆盖 |
| **RXNE** | 接收缓冲区非空 | 说明 `DR` 里有新收到的数据可读            | 收数据时等 RXNE=1 再读 `DR`  |
| **BSY**  | SPI 正在忙     | 正在移位传输（时钟还在跑/最后一位未完成） | 通信收尾时等 BSY=0 再拉高 CS |

### 4.4 流程图

![[d2-spi-01.svg]]

### 4.5 代码实现

```c
void App_SPI_MasterTransmitReceive(SPI_TypeDef *SPIx,
                                   const uint8_t *pDataTx, uint8_t *pDataRx, uint16_t Size)
{
    SPI_Cmd(SPIx, ENABLE);                    // #1. 闭合总开关
    SPI_I2S_SendData(SPIx, pDataTx[0]);       // #2. 发送第一个字节

    for (uint16_t i = 0; i < Size - 1; i++)
    {
        // 发送一个字节
        while (SPI_I2S_GetFlagStatus(SPIx, SPI_I2S_FLAG_TXE) == RESET);
        SPI_I2S_SendData(SPIx, pDataTx[i + 1]);

        // 接收一个字节
        while (SPI_I2S_GetFlagStatus(SPIx, SPI_I2S_FLAG_RXNE) == RESET);
        pDataRx[i] = SPI_I2S_ReceiveData(SPIx);
    }

    // #4. 读出最后一个字节
    while (SPI_I2S_GetFlagStatus(SPIx, SPI_I2S_FLAG_RXNE) == RESET);
    pDataRx[Size - 1] = SPI_I2S_ReceiveData(SPIx);

    // #5. 断开总开关
    SPI_Cmd(SPIx, DISABLE);
}
```
