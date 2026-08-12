---
aliases: [计算机组成, 计算机体系结构, Computer Organization, Computer Architecture, MIT 6.004, 组成原理]
tags: [cs, computer_architecture, MOC]
up: "[[Computer Science MOC]]"
related:
  - "[[STM32 MOC]]"
  - "[[C_DataStruct MOC]]"
  - "[[Deep Learning MOC]]"
down:
  - "[[Bits Digital Abstraction and Number Systems]]"
  - "[[Combinational Logic]]"
  - "[[Sequential Logic and Finite State Machines]]"
  - "[[Performance and Design Tradeoffs]]"
  - "[[Instruction Set Architecture]]"
  - "[[Assembly Language Procedures and Stacks]]"
  - "[[Single-Cycle Processor Datapath]]"
  - "[[Pipelining the Processor]]"
  - "[[Memory Hierarchy and Caches]]"
  - "[[Virtual Memory]]"
  - "[[Interrupts Devices and IO]]"
  - "[[Parallel Processing and Concurrency]]"
---
# Computer Organization and Architecture (MIT 6.004) MOC

> 课程底本：[Computation Structures](https://computationstructures.org/)（MIT 6.004）。从比特与数字抽象 → 组合/时序逻辑 → ISA 与汇编 → 单周期/流水线处理器 → 存储层次、虚拟内存、中断 I/O → 并行与同步。OCW：[6.004 Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/)。

> 相关硬件课：`30 Electrical & Computer Engineering/Digital Electronics/`（门电路与时序）、[[STM32 MOC]]（外设 / NVIC / DMA 实践）。本库无独立 Digital Electronics / Embedded Systems MOC。

![[coa-moc-roadmap.svg]]

## 01 数字抽象与逻辑
- [[Bits Digital Abstraction and Number Systems]]：比特、电压抽象、无符号 / 补码、十六进制
- [[Combinational Logic]]：真值表、布尔代数、门、MUX/译码/ALU 直觉、传播延迟
- [[Sequential Logic and Finite State Machines]]：锁存/触发器、寄存器、时钟、Moore/Mealy、状态编码
- [[Performance and Design Tradeoffs]]：延迟/吞吐、$\mathrm{IC}\times\mathrm{CPI}\times T_{\mathrm{clk}}$、Amdahl、面积/功耗

## 02 ISA 与处理器
- [[Instruction Set Architecture]]：指令格式、寻址、RISC 风格（Beta 直觉）
- [[Assembly Language Procedures and Stacks]]：调用约定、栈帧、过程联动
- [[Single-Cycle Processor Datapath]]：单周期数据通路与控制
- [[Pipelining the Processor]]：五级流水、冒险、转发/停顿

## 03 存储、I/O 与并行
- [[Memory Hierarchy and Caches]]：局部性、行、映射、写策略、AMAT
- [[Virtual Memory]]：VA/PA、页表、TLB、缺页、保护隔离
- [[Interrupts Devices and IO]]：MMIO、DMA、中断 vs 轮询、异常 vs 中断
- [[Parallel Processing and Concurrency]]：多核共享内存、锁/原子、通信、扩展界限

## 插图（预生成 SVG）

嵌入 `90 Assets/diagrams/computer-architecture/`（文件名形如 `coa-….svg`）。重新生成：

```bash
cd "90 Assets/scripts/computer_architecture"
.venv/bin/python generate_all.py
```
