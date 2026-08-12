---
aliases:
  - 流水线
  - Pipelining
  - Pipelining the Processor
  - 流水线冒险
  - Hazard
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Single-Cycle Processor Datapath]]"
  - "[[Instruction Set Architecture]]"
down: []
---
# 处理器流水线

> [!summary] 核心结论
> 把单周期长组合路径切成 **IF / ID / EX / MEM / WB** 五级，使不同指令重叠执行：理想情况下时钟近似最慢一级延迟，吞吐接近每拍一条。实际加速受 **结构 / 数据 / 控制冒险** 限制。数据冒险用 **转发（forwarding）** 与 **气泡（stall）** 解决；控制冒险带来分支惩罚，靠预测或延迟槽缓解。流水线不改 ISA 语义，只改微架构时序。

> 底本：MIT 6.004 Computation Structures（pipelining / hazards），OCW。

---
## 1. 从单周期到流水

[[Single-Cycle Processor Datapath]] 中一条指令独占全部硬件一拍。流水线把路径切段，段间插入流水寄存器，使：

- 指令 $i$ 在 EX 时，指令 $i+1$ 在 ID，指令 $i+2$ 在 IF……
- 吞吐由「每拍完成的指令数」衡量，而非单条延迟。

![[coa-pipeline.svg]]

---
## 2. 五级含义

| 级 | 名称 | 主要工作 |
|----|------|----------|
| **IF** | Instruction Fetch | PC → I-Mem；PC+4 |
| **ID** | Instruction Decode | 译码；读 RegFile；符号扩展 |
| **EX** | Execute | ALU 运算 / 地址 / 比较 |
| **MEM** | Memory | LD/ST 访问 D-Mem；其它指令旁路 |
| **WB** | Write Back | 结果写入 RegFile |

每级边界有流水寄存器保存：指令字段、控制信号副本、中间结果、传递中的 PC+4 等，以免下一级覆盖本级还需的数据。

---
## 3. 理想加速比

设单周期时钟 $T_{\mathrm{sc}}$（≈ 五段延迟之和），流水线时钟

$$
T_{\mathrm{pipe}} \approx \max_k t_k + t_{\mathrm{overhead}}
$$

其中 $t_k$ 为第 $k$ 级组合延迟，$t_{\mathrm{overhead}}$ 为流水寄存器建立/传播开销。对大量指令 $N$，忽略填充：

$$
\mathrm{Speedup} \approx \frac{N\cdot T_{\mathrm{sc}}}{N\cdot T_{\mathrm{pipe}}} \approx \frac{T_{\mathrm{sc}}}{T_{\mathrm{pipe}}} \le 5
$$

理想 IPC≈1。平衡各级延迟很重要：某一级特别长会变成瓶颈（例如 MEM 接慢缓存）。

> [!tip] 延迟 vs 吞吐
> 单条指令的 **延迟** 仍约 5 拍；变快的是 **吞吐**。交互式「一条指令从进到出」并不变成 1 拍。

---
## 4. 三类冒险（Hazard）

### 4.1 结构冒险（Structural）

硬件资源不够并行：例如单一存储器既要 IF 取指又要 MEM 访数。

**对策**：指令/数据分离（I-Mem / D-Mem 或分离缓存）；多端口寄存器堆；复制功能单元。

### 4.2 数据冒险（Data）

指令间存在寄存器依赖，后指令在数据就绪前就需要它。最常见 **RAW**（read after write）：

![[coa-hazard.svg]]

```text
ADD R1, R2, R3    ; WB 才写入 R1
SUB R4, R1, R5    ; EX 就需要 R1
```

还有 WAR / WAW（在乱序与多写口时更突出；经典五级顺序流水线主要操心 RAW）。

### 4.3 控制冒险（Control）

分支 / 跳转在 EX（或更晚）才知道下一 PC，但 IF 每拍都要取下一条——取错则需作废。

---
## 5. 转发（Forwarding / Bypassing）

不必等 WB 写寄存器堆：把 EX/MEM 或 MEM/WB 流水寄存器中的结果 **旁路** 回 EX 的 ALU 输入。

检测（示意）：若 EX 源寄存器编号 = 前一条的目的寄存器，且前一条会写寄存器，则选转发多路器：

$$
ALU_{in} \leftarrow
\begin{cases}
\mathrm{EX/MEM.ALUOut} & \text{前一条已算出} \\
\mathrm{MEM/WB.WD} & \text{再前一条} \\
\mathrm{RegFile} & \text{无依赖}
\end{cases}
$$

多数 ALU→ALU 的 RAW 可零气泡消除。

---
## 6. 必须停顿的情况（Stall）

**Load-use hazard**：前一条是 `LD`，数据要到 MEM 结束才从 D-Mem 出来，下一条若在 EX 就要用：

```text
LD  R1, 0(R2)
SUB R4, R1, R5   ; 即使转发，也得等 load 数据
```

对策：

1. **插入气泡（bubble）**：对后续指令暂停 PC/IF/ID，向 EX 灌入 `nop` 控制；
2. 编译器 **指令调度**：在 `LD` 与使用之间塞入无关指令，减少实际气泡。

转发 + 必要时 1 拍 stall，是经典五级流水的标准配方。

---
## 7. 控制流与分支惩罚

简化假设：分支条件在 EX 末可知，目标地址同时算完。则已错误取入的 IF/ID 指令需 **flush**。

**分支惩罚（branch penalty）** $p$：每条已决分支平均浪费的拍数。若分支频率为 $b$、预测错误率 $m$，则粗略

$$
\mathrm{IPC} \approx \frac{1}{1+b\cdot m\cdot p}
$$

缓解手段：

| 技术 | 思想 |
|------|------|
| 尽早判断 | 把比较挪到 ID（需更多前移硬件） |
| 静态预测 | 总预测不跳 / 向后跳向前不跳 |
| 动态预测 | BHT / BTB 记历史 |
| 延迟槽 | 架构规定分支后一条总执行（软件填充） |
| 条件移动 | 减少短分支 |

6.004 先掌握「未预测时的惩罚从何而来」，再谈预测器。

---
## 8. 流水线控制

控制信号在 ID 产生后，必须 **随指令流动**：ID/EX、EX/MEM、MEM/WB 各带一份，以免后级串台。Stall 时：

- 冻结 PC 与 IF/ID；
- 将 ID/EX 控制域清零（插入 nop）；
- 已在后面的指令继续流走。

Flush 分支错误路径时，把相应流水寄存器控制位置成安全 nop。

---
## 9. 性能小结

$$
T_{\mathrm{exec}} \approx N\cdot \mathrm{CPI}\cdot T_{\mathrm{clk}}
$$

流水线目标：缩小 $T_{\mathrm{clk}}$，并尽量让 $\mathrm{CPI}\to 1$。冒险使 $\mathrm{CPI}>1$：

$$
\mathrm{CPI} = 1 + \mathrm{stalls/instr} + \mathrm{flushes/instr}+\cdots
$$

与单周期比：即使 CPI 略大于 1，只要 $T_{\mathrm{clk}}$ 显著下降，总时间仍可更好。深度更深的流水线进一步降 $T_{\mathrm{clk}}$，但冒险惩罚与转发复杂度上升——收益递减。

---
## 10. 工作例：7 指令时间线（转发 / stall / flush）

> [!example] 序列与假设
> 经典五级、**有转发**、load-use 需 **1 拍 stall**；分支在 EX 末决、错误路径 **flush IF/ID**（惩罚约 2 拍已取指令作废）。无分支预测（总预测“不跳”）。指令：
> ```text
> I1  ADD  R1, R2, R3     ; R1 ← R2+R3
> I2  SUB  R4, R1, R5     ; RAW on R1 → 转发消掉
> I3  LD   R6, 0(R4)      ; RAW on R4 → 转发
> I4  AND  R7, R6, R8     ; load-use on R6 → 1 stall
> I5  BEQ  R7, L1         ; 假设 R7≠0，不跳（预测正确）
> I6  OR   R9, R2, R3
> I7  XOR  R10, R9, R1
> ```
> 表中单元格为该拍所在流水级；`*` = 气泡；`†` = 被 flush（本例预测正确，无 †）。

| 拍 | I1 | I2 | I3 | I4 | I5 | I6 | I7 | 备注 |
|----|----|----|----|----|----|----|----|------|
| 1 | IF | | | | | | | |
| 2 | ID | IF | | | | | | |
| 3 | EX | ID | IF | | | | | EX←Reg；I2 将靠转发 |
| 4 | MEM | EX | ID | IF | | | | I2 用 EX/MEM 转发 R1 |
| 5 | WB | MEM | EX | ID | IF | | | I3 用转发得 R4 |
| 6 | | WB | MEM | *ID* | IF | | | load-use：冻结 I4，插气泡 |
| 7 | | | WB | EX | ID | IF | | I4 用 MEM/WB（或旁路）得 R6 |
| 8 | | | | MEM | EX | ID | IF | I5 在 EX 知“不跳” |
| 9 | | | | WB | MEM | EX | ID | 预测正确，无 flush |
| 10 | | | | | WB | MEM | EX | |
| 11 | | | | | | WB | MEM | |
| 12 | | | | | | | WB | I7 完成 |

> [!example] 自检
> （1）若把 I5 改成**会跳到 L1**且 L1 处是另一条 `ADD`，表中哪几格变 `†`？分支惩罚大约几拍？
> （2）本序列从 I1 进入到 I7 离开共 12 拍、完成 7 条指令：粗算 $\mathrm{CPI}\approx$？相对理想 CPI=1，多余周期从哪来？
> （3）若**没有转发**，I2 相对 I1 至少还要再等几拍才安全进 EX？

> [!success]- 参考答案
> （1）拍 8 时 I5 在 EX 决出“跳”：已在 IF/ID 的 I6（及再取的错误路径）需 flush；下一拍从 L1 重取。未提前判断时惩罚约 **2** 拍（作废 IF+ID）。表中 I6 的 ID/IF 格标 `†`，随后改填目标指令。
> （2）$\mathrm{CPI}\approx 12/7\approx 1.71$。多余来自：**1** 拍 load-use stall + 流水线填充（前几拍未满）+ 排空。稳态若只有这一处 stall，长期 stalls/instr $\approx 1/7$。
> （3）无转发时须等 I1 的 WB 写完 RegFile 后 I2 才能在 ID 读到新 R1（或至少等 WB 与 ID 同拍的旁路约定）。相对“有转发、I2 紧跟 I1 的 EX”，通常再插 **2** 拍气泡（经典五级 RAW 无转发惩罚约 2）。

粗算本例有效吞吐：有转发时仅 1 次 stall →
$$
\mathrm{CPI}_{\mathrm{approx}} \approx 1 + \frac{1}{7}\approx 1.14
$$
（忽略填充；上表 12/7 含填充，短序列会偏悲观。）若每 7 条还有 1 次错误预测、惩罚 $p=2$：
$$
\mathrm{CPI}\approx 1+\frac{1}{7}+\frac{2}{7}\approx 1.43.
$$

---
## 11. 与前后知识点的衔接

- ISA 不变：汇编程序员仍写 `ADD`/`LD`；冒险由硬件（+编译器调度）消化。
- 单周期图上的部件，在流水线中 **时间复用**：同一 ALU 不同拍服务不同指令。
- 缓存未命中、多周期外设会把「MEM 一拍」变成可变延迟，引出更复杂的停顿与记分牌/乱序——超出本课核心，但动机相同：保持流水充满。

---
## 12. 本节清单

1. 默写五级 IF–ID–EX–MEM–WB 各做什么。
2. 会估算理想加速比上界 ≈ 级数，并指出开销与不平衡的影响。
3. 区分结构 / 数据 / 控制冒险，并各举一例。
4. 说明转发能消哪些 RAW，以及 load-use 为何仍要 stall。
5. 会解释分支惩罚与 flush；知道预测如何提高有效 IPC。
6. 能根据短指令序列画出含 stall/转发/flush 的时间线，并估算 CPI。

## 参考

- MIT 6.004 *Computation Structures*, pipelined Beta / hazards (OCW)
- Patterson & Hennessy, *COD*：pipelining 与 hazard 章
- Hennessy & Patterson, *Computer Architecture: A Quantitative Approach*（进阶：预测与 CPI 分析）
