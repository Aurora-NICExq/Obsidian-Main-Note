---
aliases: [W25Q64, Flash存储, 扇区擦除, 页编程, 写使能]
tags: [stm32, 硬件原理]
up: "[[STM32 MOC]]"
related: "[[SPI]], [[GPIO Principles|GPIO 原理]]"
---
# W25Q64 Module

> [!summary] 核心结论
> W25Q64 是通过 [[SPI]] 通信的 Flash 存储器，**掉电不丢失**。写数据必须走两轮「写使能 → 操作 → 等待空闲」：先 **擦除**（`0x20` 扇区擦除，扇区是最小可擦除单位），再 **页编程**（`0x02`）。读数据用 `0x03` + 24 位地址，不需要写使能。每一帧通信都由 NSS 拉低开始、拉高结束。

---

## 1. W25Q64 存储结构

### 1.1 编程接口

```c
void App_W25Q64_SaveByte(uint8_t Byte);    // 使用W25Q64保存一个字节

uint8_t App_W25Q64_LoadByte(void);         // 把保存的字节读出来
```

### 1.2 模块结构图

![[截屏2026-03-03 下午2.44.19.png]]

W25Q64 可用于存储数据，且掉电不丢失

---

## 2. 使用 W25Q64 存储数据

### 2.1 写入流程

![[d2-w25q64-module-01.svg]]

1. 扇区是最小可擦除单位

### 2.2 写使能（0x06）

写使能指令：主机发送 `0x06`

```c
uint8_t buffer[10];   // 声明一个数组

// #1. 写使能

buffer[0] = 0x06;

GPIO_WriteBit(GPIOA, GPIO_Pin_12, Bit_RESET);  // NSS=0

App_SPI_MasterTransmitReceive(SPI1, buffer, buffer, 1);

GPIO_WriteBit(GPIOA, GPIO_Pin_12, Bit_SET);    // NSS=1
```

原理：

![[截屏2026-03-03 下午3.58.12.png]]

### 2.3 扇区擦除（0x20）

扇区擦除：主机发送 `0x20` + 24 位地址

```c
// #2. 扇区擦除

buffer[0] = 0x20;
buffer[1] = 0x00;
buffer[2] = 0x00;
buffer[3] = 0x00;

GPIO_WriteBit(GPIOA, GPIO_Pin_12, Bit_RESET);  // NSS=0

App_SPI_MasterTransmitReceive(SPI1, buffer, buffer, 4);

GPIO_WriteBit(GPIOA, GPIO_Pin_12, Bit_SET);    // NSS=1
```

### 2.4 其余指令

- 等待空闲：主机先发 `0x05`，然后再收一个字节
- 页编程：主机发 `0x02` + 24 位地址 + 要写的数据

---

## 3. 使用 W25Q64 读取数据

读数据：主机发 `0x03` + 24 位地址，然后接收数据

```c
buffer[0] = 0x03;
buffer[1] = 0x00;
buffer[2] = 0x00;
buffer[3] = 0x00;

GPIO_WriteBit(GPIOA, GPIO_Pin_12, Bit_RESET);  // NSS=0

App_SPI_MasterTransmitReceive(SPI1, buffer, buffer, 4);  // 发0x03+24位地址

App_SPI_MasterTransmitReceive(SPI1, buffer, buffer, 1);  // 收一个字节

GPIO_WriteBit(GPIOA, GPIO_Pin_12, Bit_SET);  // NSS=1

return buffer[0];
```

---

## 4. 配套实验：按钮的初始化

```c
#include "button.h"

Button_TypeDef button;  // 声明一个按钮

void App_Button_Init(void);

int main(void){
    App_Button_Init();  // 初始化

    while(1){
        My_Button_Proc(&button);  // 进程
    }
}

void App_Button_Init(void){
    Button_InitTypeDef Button_InitStruct = {0};

    Button_InitStruct.GPIOx = GPIOA;
    Button_InitStruct.GPIO_Pin = GPIO_Pin_0;

    My_Button_Init(&button, &Button_InitStruct);
}
```
