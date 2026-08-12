---
aliases:
  - 中断与外设
  - Interrupts
  - MMIO
  - DMA
  - 异常与中断
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Virtual Memory]]"
  - "[[Parallel Processing and Concurrency]]"
  - "[[Single-Cycle Processor Datapath]]"
  - "[[STM32 MOC]]"
down:
  - "[[Parallel Processing and Concurrency]]"
---
# 中断、外设与 I/O

> [!summary] 核心结论
> CPU 通过 **MMIO**（或端口 I/O）读写设备寄存器；大块数据常用 **DMA** 让设备直接搬主存，避免 CPU 字节搬运。设备完成或出错时用 **中断** 异步通知，相对 **轮询** 更省 CPU。**异常（exception）** 来自指令执行内部（缺页、非法操作码等），**中断（interrupt）** 来自外部/异步事件——二者都走保存现场 → 向量/处理器 → 返回的路径，但是否“重启同一条指令”、能否屏蔽，语义不同。嵌入式实践见 [[STM32 MOC]]。

> 底本：[Computation Structures](https://computationstructures.org/) / MIT 6.004（Devices, interrupts, exceptions）。

---
## 1. 谁在跟内存对话

处理器核心只“懂” load/store（及特权配置）。外设出现在物理地址空间的两张面孔：

1. **普通 DRAM**：指令与数据。
2. **设备寄存器窗口**：同样用 load/store 访问，但落到总线外设——即 **MMIO（Memory-Mapped I/O）**。

另有历史方案 **port-mapped I/O**（独立 I/O 指令与地址空间）；6.004 以 MMIO 模型为主。

![[coa-interrupt.svg]]

---
## 2. MMIO 要点

- 某 PA 范围被译码到 UART / Timer / GPIO / 磁盘控制器等。
- 读“状态寄存器”、写“数据/控制寄存器”即与设备通信。
- 这些地址通常标为 **uncacheable** 或强序：否则 Cache 可能返回陈旧状态，或合并/重排破坏设备协议（与 [[Virtual Memory]] 页属性相关）。

> [!example] 轮询发送一字
> `while (!(STATUS & TX_READY)); DATA = c;` —— CPU 空转等待就绪位。简单，但忙等浪费周期。

---
## 3. DMA（Direct Memory Access）简述

大块传输（磁盘扇区、网卡包、ADC 缓冲）若逐字节由 CPU 搬，CPI 与能耗都差。

**DMA 控制器**（或设备自带 DMA 引擎）：

1. CPU 配置：源/目的地址、长度、方向、完成后是否中断。
2. 引擎在总线上发起读/写，数据在设备 ↔ 主存间流动。
3. 完成（或出错）拉中断；CPU 再做上层协议。

注意：DMA 写主存后，CPU Cache 中可能仍是旧副本 → 需 **cache clean/invalidate** 或非缓存缓冲（嵌入式高频坑）。

---
## 4. 轮询 vs 中断

| | 轮询（Polling） | 中断（Interrupt） |
|--|-----------------|-------------------|
| 机制 | 软件反复读状态 | 设备断言 IRQ，CPU 异步陷入 |
| 延迟 | 取决于轮询频率 | 响应快（在未屏蔽、优先级允许时） |
| CPU 占用 | 高（忙等）或周期性开销 | 空闲可做别的 / 休眠 |
| 复杂度 | 低 | 需控制器、优先级、可重入注意 |

高速、事件稀、或实时环内，仍可能用轮询；通用 OS 与多数驱动以中断 + 底半部为主。

---
## 5. 异常 vs 中断

课内常用区分：

### 5.1 异常（Exception / Trap / Fault）

由**当前指令流**触发：未定义指令、除零、系统调用（有意 trap）、**page fault**、对齐错误等。

- 同步于指令边界（精确异常：可见状态对应某条指令之前/之时）。
- Fault 类常在处理完后 **重启** 故障指令（缺页是典型）；Trap 类（syscall）常从**下一条**返回。

### 5.2 中断（Interrupt）

由**外部事件**触发：定时器滴答、UART RX、DMA 完成、I2C 错误——与“哪条用户指令”无直接关系。

- 异步（可在指令间采样）。
- 通常可 **屏蔽（mask）**；不可屏蔽中断（NMI）用于严重错误。
- 处理后返回到被打断的下一条（或同一精确点），继续用户程序。

> [!warning] 术语混用
> 有的教材把中断当异常的子集，或把 syscall 叫 software interrupt。抓住：**是否异步于指令、是否可屏蔽、返回时是否重启同一条** 三点即可。

---
## 6. Handler 流程（概念）

无论异常还是中断，硬件 + 软件协作的典型路径：

1. **识别**：锁存原因码 / 哪条 IRQ；可能自动关中断或抬优先级。
2. **保存现场**：PC（或返回地址）、状态寄存器（PSW / CPSR / mstatus…）、必要时通用寄存器（硬件压栈或软件在入口汇编里存）。
3. **向量**：用中断向量表 / 异常表跳到对应 **ISR / handler**（或统一入口再分发）。
4. **处理**：清设备挂起位、拷数据、调度线程、处理缺页等。
5. **恢复**：弹回寄存器与 PC，执行 **return-from-exception** 类指令，回到被打断上下文。

流水线 CPU 还需冲刷未提交指令、保证精确异常——与 [[Pipelining the Processor]]、[[Single-Cycle Processor Datapath]] 的控制流扩展相关。

> [!tip] 精确异常与流水线
> 精确异常要求：提交点之前的指令效果全部可见，之后全部不可见。流水线需在异常点冲刷后续阶段，再写异常 PC——这是单周期机没有的额外控制负担。

---
## 7. 优先级、嵌套与临界区

- 多设备 → 优先级；高优先级可抢占低优先级 ISR（嵌套）。
- 共享数据（驱动缓冲、内核队列）需在关中断或用锁保护，否则与 [[Parallel Processing and Concurrency]] 同类竞态。
- 顶半部（快、禁嵌套或短）vs 底半部 / 延迟过程（长工作移出 ISR）是 OS 工程套路。

---
## 8. 与系统结构的位置

```
应用 / 驱动
    ↕ syscall / MMIO API
OS：调度、缺页、驱动
    ↕ 异常/中断入口
CPU + MMU + 中断控制器
    ↕ 总线
DRAM · DMA · 设备
```

没有中断与异常，虚拟内存缺页与设备完成都无法高效并入指令流。

---
## 9. 中断控制器直觉

多设备 IRQ 线汇入 **中断控制器**（如 APIC / GIC / NVIC）：屏蔽、挂起、优先级、向 CPU 投递向量号。CPU 每次只看到“当前最高优先级待处理事件”。软件在 ISR 末尾写 **EOI / clear pending**，否则同一中断会反复进入。嵌套深度、尾链（tail-chaining）等是实现优化，课内抓住“控制器仲裁 + 向量分发”即可。

---
## 10. 工作例：轮询 / 中断 / DMA 时间线

> [!example] 场景
> 设备每次就绪可提供 1 字；共传 $N=1000$ 字。CPU 时钟 1 cycle；一次“检查状态或进 ISR 固定开销”用粗粒度计数。

| 方式 | 概念时间线（每字） | CPU 忙碌直觉 |
|------|-------------------|--------------|
| **轮询** | `loop: 读 STATUS` → 未就绪则重复 → 就绪则 `读/写 DATA` | 等待期间 **100% 忙等**；若平均等 $W$ cycle/字，总 CPU $\approx N(W+c)$ |
| **中断** | CPU 做别的事 → IRQ → 存现场 (~$S$ cycle) → 搬 1 字 → EOI → 返回 (~$R$) | 每字固定开销 $S+c+R$；空闲可计算/休眠。若 $W$ 很大，省下 $N\cdot W$ |
| **DMA** | CPU 配描述符一次 (~$C_{\mathrm{setup}}$) → 引擎搬 $N$ 字 → **一次**完成中断 | CPU $\approx C_{\mathrm{setup}}+S'+R'$；中间可干别的；注意 Cache 一致性 |

数值素描：设 $W=50$，$c=5$，$S+R=40$，$C_{\mathrm{setup}}=80$，完成中断开销 $40$。

- 轮询 CPU cycle $\approx 1000\times(50+5)=55000$
- 中断（设备每字一 IRQ）$\approx 1000\times(40+5)=45000$（若中间还能干别的，墙钟可重叠；此处只计 CPU 为 I/O 花的周期）
- DMA $\approx 80+40=120$ CPU cycle 量级（传输本身不占 CPU）

> [!example] 自检
> （1）何时轮询反而比中断更合适？
> （2）DMA 完成后 CPU 读缓冲前通常还要多想哪一步（与 Cache 有关）？
> （3）若中断每字一次、$S+R$ 很大而 $N$ 极大，应转向什么？

> [!success]- 参考答案
> （1）事件极频繁、等待短、或硬实时环里开销确定：轮询开销可预测，且避免频繁进出 ISR。
> （2）若缓冲可缓存：对 DMA 写入区做 **invalidate**（或用非缓存区），否则可能读到旧 Cache 行。
> （3）**DMA / 批量中断**（凑满一缓冲再 IRQ），把每字中断开销摊薄。

---
## 11. 本节清单

1. 对比 MMIO 与“普通内存”访问，并说明为何设备区常不可缓存。
2. 用几句话说明 DMA 的配置—传输—完成中断模型及 Cache 一致性风险。
3. 能对比 polling 与 interrupt 的利弊。
4. 区分 exception 与 interrupt：同步/异步、屏蔽、是否重启指令。
5. 默写 handler 五步：识别 → 存现场 → 向量 → 处理 → 恢复返回。
6. 知道中断控制器负责屏蔽/优先级/向量，以及 ISR 需清除挂起源。
7. 能用粗周期数比较轮询 / 中断 / DMA 的 CPU 占用。

## 参考

- MIT 6.004 *Computation Structures*：I/O, interrupts, exceptions（[computationstructures.org](https://computationstructures.org/)）
- MIT OCW 6.004：[Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/)
- 片上实践对照：[[STM32 MOC]]（NVIC、外设 IRQ、DMA）
