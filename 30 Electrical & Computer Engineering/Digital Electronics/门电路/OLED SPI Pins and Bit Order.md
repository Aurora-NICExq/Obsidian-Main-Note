---
tags:
  - 数字电子技术
---
# OLED SPI Pins and Bit Order

- `OLED_D0` 作为时钟
- `OLED_D1` 作为数据
- `OLED_DC` 区分命令/数据
- `OLED_CS` 片选
- `OLED_RES` 复位
- `OledWriteBytes()` 里“上升沿采集”“高位先发”

对应手册主要看：

- **第 14 页**：`Table 7-1 MCU Bus Interface Pin Selection`
- **第 15 页**：`Table 8-1 MCU Interface Assignment Under Different Bus Interface Mode`
- **第 17 页**：`8.1.3 MCU Serial Interface (4-wire SPI)`、`Table 8-4`
- **第 18 页**：`Figure 8-5 Write Procedure in 4-Wire Serial Interface Mode`
- **第 52 页**：`Table 13-4 4-Wire Serial Interface Timing Characteristics`