---
aliases:
  - 单周期处理器
  - Single-Cycle Datapath
  - Single-Cycle Processor Datapath
  - 数据通路
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Instruction Set Architecture]]"
  - "[[Assembly Language Procedures and Stacks]]"
  - "[[Pipelining the Processor]]"
down:
  - "[[Pipelining the Processor]]"
---
# 单周期处理器数据通路

> [!summary] 核心结论
> 单周期 CPU 在 **一个时钟周期内** 完成取指–译码–执行–访存–写回。数据通路由 PC、指令存储器（I-Mem）、寄存器堆、ALU、数据存储器（D-Mem）与延伸逻辑（符号扩展、多路选择器）组成；**控制单元**根据 opcode 拉高/拉低一排控制信号，选通正确路径。正确且简单，但时钟必须迁就 **最慢指令** 的长组合路径，因此频率低——这正是流水线要解决的问题。

> 底本：MIT 6.004 Computation Structures（single-cycle processor），OCW。

---
## 1. 指令周期：Fetch–Decode–Execute

冯·诺依曼机器重复：

1. **Fetch**：用 PC 从 I-Mem 取 32 bit 指令。
2. **Decode**：拆字段（opcode, Ra, Rb, Rc, literal）；读寄存器；生成控制信号。
3. **Execute**：ALU 运算 / 地址计算 / 比较；可能访 D-Mem；写回寄存器；更新 PC。

单周期实现把上述步骤 **全部塞进同一拍** 的组合逻辑（寄存器/存储器在边沿采样）。

---
## 2. 顶层数据通路

![[coa-single-cycle.svg]]

主数据流（左 → 右）：

$$
\mathrm{PC}\ \to\ \mathrm{I\text{-}Mem}\ \to\ \mathrm{RegFile}\ \to\ \mathrm{ALU}\ \to\ \mathrm{D\text{-}Mem}\ \to\ \text{写回总线}
$$

控制单元俯视全图，向多路器、MemWrite、RegWrite 等送控制线。

---
## 3. 各部件职责

### 3.1 PC（程序计数器）

保存下一条（或当前）指令地址。每周期末更新为下列之一：

- $PC+4$（顺序执行；字寻址时也可能是 $+1$ 字，以实现为准）
- 分支目标 $PC+4+4\cdot\mathrm{sext}(literal)$（条件成立时）
- 跳转目标（来自寄存器，如 `JMP`）

PC 本身是寄存器：时钟边沿写入「下一 PC」多路器选出的值。

### 3.2 I-Mem（指令存储器）

组合读：地址 ← PC，输出 ← 指令字。单周期模型常假定 I-Mem 只读、与 D-Mem **物理分离**（哈佛视角），以免一拍内同时取指又访数冲突。

### 3.3 RegFile（寄存器堆）

- 两读口：地址 Ra、Rb → 数据 $RD1, RD2$
- 一写口：地址 Rw、数据 WD、使能 RegWrite
- $R31$ 硬连线为 0

写在时钟边沿生效，故同一拍内可读旧值、边沿写新值（与后续流水线「先写后读」约定相关）。

### 3.4 ALU

$$
\mathrm{Result} = RD1\ \mathrm{op}\ B,\quad B\in\{RD2,\ \mathrm{sext}(literal)\}
$$

`op` 由 ALUOp / 子控制决定：加、减、与、或、移位、比较置位等。分支是否成立可用 ALU 零标志或专用比较。

### 3.5 D-Mem（数据存储器）

- 地址通常来自 ALU（基址+偏移）
- `LD`：MemRead，数据 → 写回通路
- `ST`：MemWrite，数据来自 RD2（要存的寄存器）
- 其它指令不写 D-Mem

---
## 4. 关键路径与多路器

单周期正确性 = 为每类指令接通对的路径。关键多路器包括：

| 选择 | 典型选项 | 用途 |
|------|----------|------|
| ALUSrc | Reg / Imm | RR vs RC / 地址计算 |
| RegDst | Rc / 其它 | 写回目标寄存器编号 |
| MemtoReg | ALU / D-Mem | `ADD` vs `LD` 写回数据来源 |
| PCSrc | PC+4 / 分支 / 跳转 | 下一 PC |
| 链接写回 | 是否把返回地址写入 $LP$ | 带链接的控制流 |

符号扩展单元把 16 bit literal 扩成 32 bit，供 ALU 与分支偏移使用。

---
## 5. 控制信号

控制单元输入：opcode（及必要时功能子域）。输出是布尔信号集合，例如：

| 信号 | 作用 |
|------|------|
| RegWrite | 允许写寄存器堆 |
| MemRead / MemWrite | 数据存储器读写 |
| ALUSrc | ALU 第二操作数来源 |
| ALUOp | ALU 运算种类 |
| MemtoReg | 写回数据来源 |
| Branch / Jump | 影响 PCSrc |
| RegDst | 写回寄存器编号来源 |

> [!example] `LD Rc, lit(Ra)`
> RegWrite=1，MemRead=1，MemWrite=0，ALUSrc=Imm（做 $R_a+\mathrm{sext}(lit)$），MemtoReg=Mem，ALUOp=Add，PCSrc=PC+4。

> [!example] `BEQ Ra, label`
> RegWrite=0，MemWrite=0；ALU 做 $R_a-0$ 或与 $R31$ 比较；若零且 Branch=1，则 PCSrc=BranchTarget。

可用真值表：每行一条 opcode，每列一个控制信号——这就是「硬连线控制」的雏形。

---
## 6. 按指令类走一遍

### 6.1 R 型运算（`ADD Rc, Ra, Rb`）

读 Ra/Rb → ALU → 经 MemtoReg 选 ALU → 边沿写 Rc；PC ← PC+4。

### 6.2 立即数运算（`ADDC`）

ALUSrc=Imm；其余类似 R 型。

### 6.3 `ST`

计算地址；RD2 → D-Mem 写口；RegWrite=0。

### 6.4 控制流

分支：比较 + 选 PC。跳转：PC ← 寄存器；若带链接，额外 RegWrite 把返回地址写入 $LP$。

所有路径必须在 **同一时钟周期结束前** 稳定到寄存器/存储器建立时间要求之内。

---
## 7. 时序：为什么单周期慢

设各段组合延迟：

| 段 | 延迟符号 |
|----|----------|
| I-Mem | $t_{\mathrm{IM}}$ |
| Reg 读 | $t_{\mathrm{REG}}$ |
| ALU | $t_{\mathrm{ALU}}$ |
| D-Mem | $t_{\mathrm{DM}}$ |
| Mux / 控制等 | $t_{\mathrm{MUX}}$ |

最坏路径往往是 **load**：

$$
T_{\mathrm{clk}} \ge t_{\mathrm{IM}}+t_{\mathrm{REG}}+t_{\mathrm{ALU}}+t_{\mathrm{DM}}+t_{\mathrm{MUX}}+\cdots
$$

而像 `ADD` 并不需要完整 $t_{\mathrm{DM}}$，像 `JMP` 更短。但 **时钟由最长路径决定**，短指令也被迫等满一拍 → 吞吐差。

$$
\mathrm{IPC}_{\mathrm{ideal}} = 1,\quad f=\frac{1}{T_{\mathrm{clk}}}
$$

性能还受存储器技术限制：一拍内完成「取指 + 可能的数据访问」要求 I-Mem/D-Mem 都很快，或采用分离存储。

> [!tip] 与 ISA 的关系
> 单周期实现直接「展开」[[Instruction Set Architecture]] 的语义：每条指令一条组合路径。换流水线后，**同一 ISA** 仍成立，只是控制与冒险处理变复杂——见 [[Pipelining the Processor]]。

---
## 8. 教学价值与局限

**价值**：把指令语义画成电路；控制真值表可机械生成。

**局限**：短指令浪费时钟；真实缓存延迟难塞进一拍；硬件时间利用率低。工业界转向多周期/流水线——见 [[Pipelining the Processor]]。

---
## 9. 工作例：R 型与 Load 通路追踪

> [!example] 公共假设
> 单周期 Beta 风格；字长 32 bit；PC 当前为 `0x100`；RegFile：$R2=0x10$，$R3=0x20$，$R4=0x2000$；Mem[`0x2010`]=`0xDEADBEEF`。

### 9.1 `ADD R1, R2, R3`

| 阶段 | 数据 / 控制 |
|------|-------------|
| Fetch | I-Mem[PC] → 指令；默认下一 PC 候选 = PC+4 |
| Decode | opcode→控制；Ra=2,Rb=3,Rc=1；RD1=`0x10`，RD2=`0x20` |
| Execute | ALUSrc=**Reg**；ALUOp=**Add**；ALUOut=`0x30` |
| Mem | MemRead=0，MemWrite=0（旁路） |
| WB | MemtoReg=**ALU**；RegDst=**Rc**；RegWrite=**1** → 边沿写 $R1\leftarrow 0x30$ |
| PC | PCSrc=**PC+4** → `0x104` |

关键控制一排：RegWrite=1，ALUSrc=0(Reg)，ALUOp=Add，MemtoReg=0(ALU)，MemWrite=0，Branch=0。

### 9.2 `LD R5, 0x10(R4)`

有效地址 $EA=R4+\mathrm{sext}(0x10)=0x2000+0x10=0x2010$。

| 阶段 | 数据 / 控制 |
|------|-------------|
| Fetch | 取 `LD` 指令 |
| Decode | Ra=4，literal=0x10，目的 Rc=5；RD1=`0x2000` |
| Execute | ALUSrc=**Imm**；ALUOp=**Add**；ALUOut=`0x2010` |
| Mem | MemRead=**1**，MemWrite=0；D-Mem 出 `0xDEADBEEF` |
| WB | MemtoReg=**Mem**；RegWrite=**1** → $R5\leftarrow 0xDEADBEEF$ |
| PC | PC+4 |

关键控制一排：RegWrite=1，ALUSrc=1(Imm)，ALUOp=Add，MemRead=1，MemtoReg=1(Mem)，MemWrite=0，Branch=0。

> [!example] 自检
> （1）若改成 `ST R5, 0x10(R4)`（假设 $R5$ 已有值），哪些控制信号相对 LD **必须翻转**？写回是否发生？
> （2）为何 load 路径通常决定 $T_{\mathrm{clk}}$ 下界，而 ADD 不用 D-Mem 仍要等同一拍长？

> [!success]- 参考答案
> （1）MemRead→0，MemWrite→1，RegWrite→0；MemtoReg 无关（不写寄存器）。数据：ALU 仍算 EA，RD2（$R5$）送 D-Mem 写数据口。**无寄存器写回**。
> （2）单周期时钟由**最长组合路径**定——load 经 I-Mem→Reg→ALU→D-Mem→Mux→Reg 建立；ADD 虽较短，仍共用同一 $T_{\mathrm{clk}}$，故短指令空等。

---
## 10. 本节清单

1. 默画 PC → I-Mem → RegFile → ALU → D-Mem → 写回，并标控制单元。
2. 对 `ADD` / `LD` / `ST` / `BEQ` 各写一排关键控制信号。
3. 指出 MemtoReg、ALUSrc、PCSrc 的选项；说明 load 常决定 $T_{\mathrm{clk}}$。
4. 说明 I/D 分离如何回避一拍双访问冲突。
5. 能逐步追踪一条 R 型与一条 load 的数据与控制信号。

## 参考

- MIT 6.004 *Computation Structures*, single-cycle datapath & control (OCW)
- Patterson & Hennessy, *COD*：single-cycle processor 章
