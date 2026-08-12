---
aliases: [串口, UART, USART, 波特率, TxE, TC, RxNE, 数据帧, 奇偶校验]
tags: [stm32, 硬件原理]
up: "[[STM32 MOC]]"
related: "[[GPIO Principles|GPIO 原理]], [[I2C]], [[SPI]], [[Clocks|时钟树]]"
---
# UART Serial Port

> [!summary] 核心结论
> 串口靠约定好的**数据帧格式**在一根线上传数据：空闲高电平 → 起始位（低）→ 8~9 位数据（**低位先行**）→ 可选校验位 → 停止位（高）。USART 模块内部是一对**移位寄存器**做串并转换，波特率由波特率控制器设置分频系数决定。发送查 `TxE`（能不能写下一个）和 `TC`（是不是全发完了），接收查 `RxNE`。RX 引脚要配成上拉输入，保证空闲时是高电平。

---

## 1. 通信协议

- 串口是一种通信接口，用于传输数据
- 串口想要在导线上传输数据，需要遵从一定的数据格式。
- 数据传输的格式，就是串口的通信协议。

![[tikz-uart-serial-port-01.svg]]

- **Tx**（Transmit）：数据发送引脚
- **Rx**（Receive）：数据接收引脚
- 两台设备**交叉连接** —— 一端的 Tx 接对端的 Rx

1. 导线上传输高低变化的电压
2. 串口在不传输数据时是空闲状态（高电压）
3. 发送方发送低电压（起始位）表示数据传输的开始
4. 每次传输一个字节的数据，传输过程从最低位到最高位（高电压表示1[[Basic Formulas and Theorems#^b60fca|数字信号的表示]]）
5. 数据传输结束后发送高电压（停止位）
6. 数据传输过程中**低位先行**

### 1.1 数据传输示意图

![[tikz-uart-serial-port-02.svg]]

### 1.2 串口数据帧的类型

^341089

- 数据位可以有8～9位
- 检验位检验传输过程中是否出错（检验位可以不存在）
- 停止位可以设置成其它值

### 1.3 校验方式

1. 奇校验：要求数据位中有奇数个1。
2. 偶校验：要求数据位中有偶数个1。

---

## 2. USART 模块

### 2.1 简介

- USART是单片机中的串口
- USART既能发送信息，也能接收信息

### 2.2 基本用法

![[截屏2026-01-28 下午3.55.09.png]]

- 将要发送的数据写入寄存器即可发送数据（数据从TX引脚以数据帧的格式发送）
- 解析通过RX引脚接受的数据帧的波形即可接收数据到寄存器中
- 总开关控制USART模块的使能与禁止

### 2.3 移位寄存器和串并转换

上方的移位寄存器将并行数据转换为串行，下方相反（数字电路层面的实现见 [[Shift Registers|移位寄存器]]）

- 并行：多个比特位一起（发送数据时比特位同时存储在发送数据寄存器中）
- 串行：一个比特位进行操作（发送数据时比特位一个一个发送）

移位寄存器每一个周期移动一位**（数据帧传输的过程中低位先行的原因）**

### 2.4 数据帧格式的设置方法

1. 控制电路控制数据帧的格式
2. 数据帧格式用于设置参数

### 2.5 波特率设置方法

- 波特率：每秒钟最多输入多少位，发送的位越多，数据传输速度越快
- 波特率控制器用于设置分频器的分频系数

波特率寄存器 **BRR** 的位布局：高 12 位是整数部分，低 4 位是小数部分。

| 位     | M11      | M10      | M9      | M8      | M7      | M6     | M5     | M4     | M3    | M2    | M1    | M0    | F3       | F2       | F1        | F0         |
| ------ | -------- | -------- | ------- | ------- | ------- | ------ | ------ | ------ | ----- | ----- | ----- | ----- | -------- | -------- | --------- | ---------- |
| 权重   | $2^{11}$ | $2^{10}$ | $2^{9}$ | $2^{8}$ | $2^{7}$ | $2^{6}$ | $2^{5}$ | $2^{4}$ | $2^{3}$ | $2^{2}$ | $2^{1}$ | $2^{0}$ | $2^{-1}$ | $2^{-2}$ | $2^{-3}$  | $2^{-4}$   |
| 十进制 | 2048     | 1024     | 512     | 256     | 128     | 64     | 32     | 16     | 8     | 4     | 2     | 1     | 0.5      | 0.25     | 0.125     | 0.0625     |

控制器中填入的数据用来改变分频系数

### 2.6 编程接口

#### 2.6.1 串口初始化

```c
void USART_Init(USART_TypeDef *USARTx,                 //串口名称
                USART_InitTypeDef *USART_InitStruct);  //初始化的参数
```

#### 2.6.2 初始化参数结构体

```c
struct USART_InitTypeDef{

    uint32_t USART_BaudRate;    // 波特率（直接填入想要的波特率）

    uint16_t USART_WordLength;  // 数据位长度
                                // - USART_WordLength_8b
                                // - USART_WordLength_9b

    uint16_t USART_StopBits;    // 停止位长度
                                // - USART_StopBits_0_5
                                // - USART_StopBits_1
                                // - USART_StopBits_1_5
                                // - USART_StopBits_2

    uint16_t USART_Parity;      // 校验方式
                                // - USART_Parity_No
                                // - USART_Parity_Even
                                // - USART_Parity_Odd

    uint16_t USART_Mode;        // 数据收发方向  
                                // - USART_Mode_Tx
                                // - USART_Mode_Rx
                                // - USART_Mode_Tx | USART_Mode_Rx
}
```

USART_Mode 控制的是 TX 开关与 RX 开关的闭合

---

## 3. 初始化 IO 引脚

### 3.1 USART 的引脚

- 标准模块功能：TX引脚和RX引脚
- 硬件流控：CTS引脚和RTS引脚
- 同步模式：连接CK引脚用于串口的同步模式

### 3.2 引脚分布表

![[截屏2026-01-28 下午6.33.08.png]]

- PA9可以作为USART1_TX使用，PA10可以作为USART1_RX使用

### 3.3 重映射表

重映射用于默认引脚无法使用时，（可以查阅手册看对应片上外设）

### 3.4 IO 配置表

> 表21　USART

| USART 引脚    | 配置         | GPIO 配置          |
| ------------- | ------------ | ------------------ |
| `USARTx_TX`   | 全双工模式   | 推挽复用输出       |
| `USARTx_TX`   | 半双工同步模式 | 推挽复用输出     |
| `USARTx_RX`   | 全双工模式   | 浮空输入或带上拉输入 |
| `USARTx_RX`   | 半双工同步模式 | 未用，可作为通用 I/O |
| `USARTx_CK`   | 同步模式     | 推挽复用输出       |
| `USARTx_RTS`  | 硬件流量控制 | 推挽复用输出       |
| `USARTx_CTS`  | 硬件流量控制 | 浮空输入或带上拉输入 |

- 全双工：数据通信的方向完全是双向的（标准串口基础）
- 半双工：方向是双向的，但是不能同时进行（两个模块的TX引脚相互连接，共用一根线）
- 同步：在标准的串口基础上，增加了CK线（传输时钟信号，同步两个设备）
- 硬件流控：在标准的串口基础上，增加了CTS和RTS交叉连接

### 3.5 GPIO 配置

1. RX引脚选择上拉输入，保证串口数据帧处于空闲状态[[GPIO Principles#^c3df2c|默认高电平]]

---

## 4. 发送数据

### 4.1 TxE 标志位

**TxE: Transmit Data Register Empty - 发送数据寄存器空**

- 当 TDR（发送数据寄存器）空时，TxE = 1；
- 否则 TxE = 0。
- **如果不进行判断，可能会导致新写入的数据把原来的数据覆盖掉**

### 4.2 TC 标志位

**TC: Transmit Complete - 发送完成**

- 当 TDR（发送数据寄存器）空 **且** 移位寄存器空时，TC = 1；（移位寄存器中是正在被发送的数据）
- 否则 TC = 0。

### 4.3 编程接口

#### 4.3.1 开关接口

```c
void USART_Cmd(USART_TypeDef *USARTx,   // 串口名称
               FunctionalState NewState // ENABLE-使能; DISABLE-禁止
              );
```

- **作用**：控制 USART 模块的使能和禁止。
- **地位**：它是 USART 外设的 **“总开关”**。

**使用提示：** 在使用 `USART_Init` 初始化好结构体参数后，**必须**调用这个函数并传入 `ENABLE`，串口才会开始工作。如果传入 `DISABLE`，串口将停止工作，常用于低功耗处理。

#### 4.3.2 查询标志位值

```c
FlagStatus USART_GetFlagStatus(USART_TypeDef *USARTx, // 串口名称
                               uint16_t USART_FLAG    // 要查询的标志位
                              );
```

- **作用**：查询 USART 标志位的值。
- **返回值**：
  - **RESET (0)**：标志位未置位。
  - **SET (1)**：标志位已置位。
  - 使用布尔型SET进行判断（0或1可能是整型）
- 实际应用：
  - **检查是否可以发送数据**：调用此函数查询 `USART_FLAG_TXE`。如果返回 `SET`，说明 TDR 空了，可以写入新数据。
  - **检查是否发送结束**：调用此函数查询 `USART_FLAG_TC`。如果返回 `SET`，说明数据完全发完了。

#### 4.3.3 发送数据

```c
void USART_SendData(USART_TypeDef *USARTx, // 串口名称
                    uint16_t Data          // 要发送的数据,可能是9位数据位，因此使用无符号16位整型
                   );
```

- **作用**：把要发送的数据写入到发送数据寄存器 (TDR) 里。

---

## 5. 接收数据

### 5.1 RxNE 标志位

**RxNE: Receive Data Register Not Empty - 接收数据寄存器非空**

- 当 RDR（接收数据寄存器）非空时，RxNE = 1；
- 否则 RxNE = 0。

### 5.2 接收代码的编写方法

#### 5.2.1 编程接口

```c
uint16_t USART_ReceiveData(USART_TypeDef *USARTx); // 串口名称
```

#### 5.2.2 完整代码

```c
// #1. 等待接收数据寄存器非空
while(USART_GetFlagStatus(USARTx, USART_FLAG_RXNE) == RESET);  //只要标志位是 RESET (0)，说明 RDR 寄存器是空的，程序就卡在这里空转，直到数据到达。

// #2. 接收数据
uint8_t byteRcvd = USART_ReceiveData(USARTx);  //没有校验位，8位数据模式最常见

// #3. 处理数据
...
```

### 5.3 使用串口控制 LED

#这里回头做一下实验吧

### 5.4 错误标志位

**PE: Parity Error - 奇偶校验错**

- 如果接收到的数据有校验错误，则 PE = 1；
- 否则 PE = 0。

**FE: Frame Error - 帧格式错误**

- 如果接收到了无效的数据帧，则 FE = 1；
- 否则 FE = 0。
- 发生在 **硬件同步失败** 的时候。（检测不到停止位）

**NE: Noise Error - 噪声错**

- 如果在接收的数据中检测到了噪声，则 NE = 1；
- 否则 NE = 0。
- 三次采样中，有一个电平和另外两个不一样（比如 1-0-1），硬件就会判定这个信号受到了干扰。

**ORE: Overrun Error - 过载错**

- 如果由于过载造成了数据丢失，则 ORE = 1；
- 否则 ORE = 0。
- 新数据丢弃（或者覆盖旧数据）

---

## 6. 封装常用功能

### 6.1 串口发送相关函数

```c
void My_USART_SendByte(...);    // 发送一个字节
void My_USART_SendBytes(...);   // 发送多个字节
void My_USART_SendChar(...);    // 发送一个字符
void My_USART_SendString(...);  // 发送字符串
void My_USART_Printf(...);      // 发送格式化字符串
```

### 6.2 串口接收相关函数

```c
... My_USART_ReceiveByte(...);   // 接收一个字节
... My_USART_ReceiveBytes(...);  // 接收多个字节
... My_USART_ReceiveLine(...);   // 接收一行字符串
```

#这里也需要用到keil5

### 6.3 python 实现串口通信

```bash
python -m serial.tools.list_ports
python -m serial.tools.miniterm /dev/tty.usbmodemXXXX 115200
```

---

## 7. HAL 库

```c
HAL_StatusTypeDef HAL_UART_Transmit(UART_HandleTypeDef *huart,
                                    uint8_t *pData,
                                    uint16_t Size,
                                    uint32_t Timeout)
```

作用：通过串口向外发送数据
