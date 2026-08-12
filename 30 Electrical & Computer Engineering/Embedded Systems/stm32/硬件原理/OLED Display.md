---
aliases: [OLED, OLED显示器, OLED_Init, OLED_InitTypeDef]
tags: [stm32, 硬件原理]
up: "[[STM32 MOC]]"
related: "[[I2C]]"
---
# OLED Display

> [!summary] 核心结论
> OLED 屏通过 [[I2C]] 总线驱动。初始化接口 `OLED_Init` 接收一个 `OLED_InitTypeDef`，其中最关键的成员是 **i2c 写数据回调函数** —— 把具体的 I2C 发送实现从驱动里解耦出去，驱动本身不关心底层是硬件 I2C 还是软件模拟 I2C。

---

## 1. 屏幕初始化

### 1.1 编程接口

```c
int OLED_Init(OLED_TypeDef *OLED,               // 所使用的OLED的名称
              OLED_InitTypeDef *OLED_InitStruct); // OLED的初始化参数
```

### 1.2 初始化参数

```c
struct OLED_InitTypeDef{
    // i2c写数据回调函数
    int (*i2c_write_cb)(uint8_t addr, const uint8_t *pdata, uint16_t size); //从机地址、数据与数据量
}
```

#待补充
