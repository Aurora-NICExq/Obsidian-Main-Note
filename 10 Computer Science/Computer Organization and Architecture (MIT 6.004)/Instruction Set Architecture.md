---
aliases:
  - ISA
  - 指令集架构
  - Instruction Set Architecture
  - Beta ISA
  - RISC
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Assembly Language Procedures and Stacks]]"
  - "[[Single-Cycle Processor Datapath]]"
down:
  - "[[Assembly Language Procedures and Stacks]]"
---
# 指令集架构（ISA）

> [!summary] 核心结论
> **ISA** 是硬件与软件之间的契约：规定寄存器、指令编码、寻址与异常语义；编译器只面向 ISA，不必关心流水线细节。6.004 的 **Beta** 是典型 **RISC / 寄存器–寄存器** 模型：固定字长指令、少量格式、load/store 访存。理解 opcode / 寄存器域 / literal，就能把汇编译成机器字，并为后续单周期与流水线数据通路定接口。

> 底本：MIT 6.004 Computation Structures（ISA / Beta），OCW。

---
## 1. ISA 作为软硬件契约

抽象层次上，ISA 夹在「高级语言 / 操作系统」与「数据通路 / 控制」之间：

- **对软件可见**：指令集合、寄存器文件、内存模型、调用约定、异常/中断入口。
- **对硬件约束**：译码器必须识别编码；数据通路必须实现约定好的语义（如 `ADD` 写回哪个寄存器）。
- **对实现隐藏**：是否单周期、是否流水、是否乱序——只要对外行为符合 ISA，都是合法微架构。

因此「换 CPU 实现、不换二进制」的前提，是 ISA 稳定。课程用 Beta 练手，思想与 MIPS / RISC-V 同族。

---
## 2. RISC 与 CISC（速览）

| 维度 | RISC（精简） | CISC（复杂） |
|------|--------------|--------------|
| 指令长度 | 常固定（如 32 bit） | 可变长 |
| 访存 | **load/store**：运算只在寄存器 | 运算可直接访存 |
| 指令数 / 语义 | 少、规整、易流水 | 多、微码友好 |
| 编码 | 少量固定格式 | 多种前缀 / 模态 |

现代 x86 对外仍像 CISC，内部常译成类 RISC 微操作。6.004 选 RISC，是为了让 **一条指令 ≈ 一条清晰数据通路路径**。

---
## 3. Beta 寄存器–存储器模型

### 3.1 寄存器文件

Beta 有 **32 个 32 位通用寄存器** $R0,\ldots,R31$：

- $R31$ **恒为 0**（读出为 0；写入被忽略）——便于合成「立即数 / 比较结果写废」等惯用法。
- 软件约定（非硬连线，但 ABI 常用）：
  - $LP=R28$：linkage pointer（返回地址）
  - $SP=R29$：栈指针
  - $BP=R27$：帧指针（可选）
  - $XP=R30$：异常时保存 PC

运算指令的源与目的几乎都是寄存器；**内存只通过 LD / ST（及 LDR）触及**。

### 3.2 存储器

字节寻址、字（32 bit）对齐访问是常见假定。栈向下增长：`push` 减小 $SP$，`pop` 增大 $SP$。过程调用细节见 [[Assembly Language Procedures and Stacks]]。

---
## 4. 指令格式

Beta 指令统一 **32 bit**，主要两类版式（与图中字段对应）：

![[coa-isa-format.svg]]

### 4.1 寄存器–寄存器（RR）操作类

典型域划分（高位 → 低位）：

| 域 | 约略位宽 | 含义 |
|----|----------|------|
| opcode | 6 | 操作种类 |
| Rc | 5 | 目的寄存器 |
| Ra | 5 | 源寄存器 A |
| Rb | 5 | 源寄存器 B |
| unused | 11 | 保留 / 忽略 |

语义示例：
$$
R_c \leftarrow R_a\ \mathrm{op}\ R_b
$$
如 `ADD Rc, Ra, Rb`、`AND`、`CMPEQ`、移位等。

### 4.2 带立即数（RC / 其它）格式

| 域 | 约略位宽 | 含义 |
|----|----------|------|
| opcode | 6 | 操作种类 |
| Rc | 5 | 目的（或分支不用） |
| Ra | 5 | 基址 / 比较源 |
| literal | 16 | 有符号立即数 |

用于：

- 运算立即数：`ADDC Rc, Ra, literal` → $R_c\leftarrow R_a+\mathrm{sext}(\mathrm{literal})$
- 访存：`LD Rc, literal(Ra)` → $R_c\leftarrow \mathrm{Mem}[R_a+\mathrm{sext}(\mathrm{literal})]$
- 分支：`BEQ Ra, label` → 若 $R_a=0$ 则 PC 相对跳转

16 位 literal 经 **符号扩展（sext）** 到 32 位，再与寄存器相加或并入 PC。

---
## 5. 寻址方式

Beta / 典型 RISC 的寻址可归纳为：

1. **寄存器寻址**：操作数在 $R_a,R_b$。
2. **立即数寻址**：操作数是指令内 literal（符号扩展）。
3. **基址 + 偏移（displacement）**：有效地址
   $$
   EA = R_a + \mathrm{sext}(\mathrm{literal})
   $$
   用于 `LD` / `ST`。
4. **PC 相对**：分支目标
   $$
   PC_{\mathrm{new}} = PC + 4 + 4\cdot\mathrm{sext}(\mathrm{literal})
   $$
   （具体「是否含当前指令长度、literal 单位是字还是字节」以实现手册为准；思想是 **相对当前位置的偏移**。）
5. **寄存器间接跳转**：`JMP` 一类把目标放在寄存器中，用于返回（`JMP(LP)`）与间接调用。

没有 x86 式复杂「基址+变址+比例+位移」的多模式编码——这正是 RISC 译码简单的原因。

---
## 6. 指令类别速览

| 类 | 例子 | 数据通路要点 |
|----|------|----------------|
| 算术逻辑 | ADD, SUB, AND, OR, XOR, SHL… | ALU + 写回寄存器 |
| 比较 | CMPEQ, CMPLT, CMPLE | ALU 置 0/1 到 Rc |
| 访存 | LD, ST, LDR | 地址计算 + D-Mem |
| 控制 | BEQ, BNE, JMP | 改 PC；可能写 LP |
| 其它 | 系统 / 异常相关 | 进入 trap 路径 |

**LDR**（load relative）用 PC 相对地址取常量——常用于字面量池，而不靠超长立即数。

---
## 7. 从汇编到机器字

汇编是 ISA 的可读皮；机器码是同一信息的位模式。译码步骤：

1. 查助记符 → opcode。
2. 解析寄存器名 → 5 bit 编号（`R3` → `00011`）。
3. 解析 label → 相对 literal（链接/汇编两遍扫）。
4. 拼 32 bit 字，写入指令存储器。

例（示意）：`ADD R1, R2, R3` 只填 opcode + Rc=1, Ra=2, Rb=3；无内存操作数。

> [!tip] 与微架构的分界
> 「这条指令要几个周期」不是 ISA 问题；ISA 只保证：**最终寄存器与内存状态**与语义一致。单周期实现里一条指令一拍做完；流水线里同一语义被拆成 IF/ID/EX/MEM/WB。

---
## 8. 设计张力

ISA 设计在几极之间权衡：

- **编码密度 vs 译码简单**：固定 32 bit 浪费空间，但硬件规整。
- **立即数位宽**：太短则常要多指令拼常数；太长则挤占 opcode/寄存器域。
- **寄存器个数**：多则减访存，但增大上下文与编码位宽。
- **特权与异常**：用户态可见寄存器 vs 内核态额外状态。

Beta 选择「少格式、32 寄存器、16 位 literal」——足够上课实现完整 CPU，又不淹没在编码特例里。

---
## 9. 工作例：有效地址与字段拼装

> [!example] 题目
> （1）`LD R4, -4(R29)`：若 $R29=SP=0x2000$，有效地址 EA？访存的是哪个字（相对栈顶的直觉）？
> （2）`ADDC R1, R31, 42`：执行后 $R1$？为何常用 $R31$ 当“零源”？
> （3）分支示意：当前 PC=`0x0100`，`BEQ R0, L` 且 $R0=0$，literal 编码为字偏移 $+3$（按 $PC_{\mathrm{new}}=PC+4+4\cdot\mathrm{lit}$）。目标地址？
> （4）RR 格式域宽核对：opcode 6 + Rc 5 + Ra 5 + Rb 5 + unused 11 = ? bit。

> [!success]- 参考答案
> （1）$\mathrm{EA}=0x2000+\mathrm{sext}(-4)=0x1FFC$——栈顶之下一字（常见“读入参 / 保存槽”）。
> （2）$R1\leftarrow 0+42=42$。$R31$ 恒 0，免占临时寄存器清零，也便于合成比较/立即数加载类惯用序列。
> （3）$PC_{\mathrm{new}}=0x100+4+4\cdot 3=0x110$。
> （4）$6+5+5+5+11=32$，正好一字。

---
## 10. 本节清单

1. 能一句话说清：ISA = 软硬件契约；微架构可替换。
2. 会对比 RISC load/store 与 CISC 访存运算。
3. 默写 Beta 式字段：opcode / Ra / Rb / Rc / literal，并写出 $R_c\leftarrow R_a\ \mathrm{op}\ R_b$。
4. 会算基址+偏移有效地址，并解释为何 $R31=0$ 有用。
5. 能把简单汇编指令对应到后续 [[Single-Cycle Processor Datapath]] 的控制信号需求。
6. 能手算 LD/ADDC/BEQ 类有效地址或目标 PC，并核对 32 bit 域宽。

## 参考

- MIT 6.004 *Computation Structures*, ISA / Beta instruction set materials (OCW)
- Harris & Harris, *Digital Design and Computer Architecture*（RISC 章节对照）
- Patterson & Hennessy, *Computer Organization and Design*（ISA 与 MIPS/RISC-V 对照）
