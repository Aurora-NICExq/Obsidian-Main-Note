---
aliases:
  - 组合逻辑
  - Combinational Logic
  - Boolean Algebra
  - Mux Decoder ALU
  - Propagation Delay
  - L03 Combinational Logic
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Bits Digital Abstraction and Number Systems]]"
  - "[[Sequential Logic and Finite State Machines]]"
down:
  - "[[Sequential Logic and Finite State Machines]]"
---
# 组合逻辑

> [!summary] 核心结论
> **组合逻辑**的输出只由**当前输入**决定：$Y=f(A,B,\ldots)$，电路内**无状态**。功能用真值表 / 布尔代数 / 门网描述；MUX、译码器、加法器乃至 ALU 都是同一抽象上的积木。时序上至少给出传播延迟 $t_{\mathrm{PD}}$：输入合法稳定后，输出在 $t_{\mathrm{PD}}$ 内必回到合法数字值。数字抽象（合法电平）+ 功能规格 + $t_{\mathrm{PD}}$ 三者齐备，才叫一个合格的组合器件。

> 底本：MIT 6.004 *Computation Structures* 组合器件与 CMOS/门电路单元（接 L02 Digital Abstraction）；见 computationstructures.org。

---
## 1. 组合器件的定义

一个器件若同时满足：

1. **数字输入 / 输出**（服从 [[Bits Digital Abstraction and Number Systems]] 的电平约定）；
2. **功能规格**：每个合法输入组合对应确定的合法输出；
3. **时序规格**：至少给出传播延迟上界 $t_{\mathrm{PD}}$；

则称为**组合器件**（combinational device）。关键：输出不依赖“历史”，只依赖当前输入（在延迟之后）。

![[coa-combinational.svg]]

> [!tip] 与数电笔记
> 门级展开、卡诺图化简、加法器内部细节，可对照 `Digital Electronics` 中的 [[Basic Formulas and Theorems]]、[[Half Adder and Full Adder]] 等；本节站在计算机结构视角：把组合块当作可组合的黑盒。

---
## 2. 真值表与布尔代数

$n$ 输入布尔函数有 $2^n$ 行真值表。标准型：

- **SOP（积之和）**：对每个输出为 1 的小项取 OR；
- **POS（和之积）**：对每个输出为 0 的大项取 AND。

常用等式（便于手推与门级替换）：

$$
\begin{aligned}
&A+0=A,\quad A\cdot 1=A,\quad A+\bar A=1,\quad A\cdot\bar A=0,\\
&A+A=A,\quad A\cdot A=A,\quad \overline{A+B}=\bar A\cdot\bar B,\quad \overline{A\cdot B}=\bar A+\bar B,\\
&A+AB=A,\quad A+\bar A B=A+B.
\end{aligned}
$$

最后一行是吸收 / 共识类化简的常用形态。

> [!example] XOR
> $Y=A\oplus B=\bar A B+A\bar B$。真值表：同为 0、同为 1 时 $Y=0$，否则 $Y=1$。加法器的“本位和”就是 XOR（再加进位逻辑）。

---
## 3. 基本门与万能集

| 门 | 记号 | 备注 |
|----|------|------|
| NOT | $\bar A$ | 反相 |
| AND | $AB$ | 全 1 才 1 |
| OR | $A+B$ | 有 1 即 1 |
| NAND | $\overline{AB}$ |  alone 万能 |
| NOR | $\overline{A+B}$ | alone 万能 |
| XOR | $A\oplus B$ | 奇偶 / 半加 |

NAND（或 NOR）可实现任意布尔函数——CMOS 标准单元库里 NAND/NOR/反相器特别常见。

---
## 4. 常用积木：MUX、译码器、ALU 思想

### 4.1 多路选择器（MUX）

$2^k$ 路数据输入 + $k$ bit 选择端，输出等于被选中的那一路：
$$
Y=\sum_{i=0}^{2^k-1} S_i\,D_i,\quad
\text{（独热选择 $S_i$，或由二进制选择码译码得到）}.
$$
用途：数据通路里选操作数、选下一 PC、旁路等。

### 4.2 译码器（Decoder）

$k$ bit 输入 → $2^k$ 条独热输出（通常还有使能）。用途：寄存器堆写使能、指令操作码局部译码、存储器片选。

### 4.3 从加法器到 ALU

全加器：$(A,B,C_{\mathrm{in}})\mapsto(S,C_{\mathrm{out}})$。$N$ 位级联得行波加法器；补码下同一电路做加减（$B$ 按位取反并置 $C_{\mathrm{in}}=1$ 即减）。

**ALU**（算术逻辑单元）= 加法/逻辑/移位等运算核 + 操作选择（内部 MUX 或使能）。对程序员，ALU 是 ISA 里 `ADD/AND/OR/XOR/SLT…` 的硬件对应物；对微架构，它是组合数据通路上的关键延迟源之一。

> [!example] 1 bit ALU 切片（思想）
> 对 $A,B$ 同时算出 $A+B$、$A\land B$、$A\lor B$ 等，再用 `op` 选择输出；$N$ 片并联并串进位链即 $N$ bit ALU。

---
## 5. 无状态：组合 vs 时序

| | 组合 | 时序 |
|--|------|------|
| 输出依赖 | 仅当前输入 | 输入 + 内部状态 |
| 存储 | 无 | 锁存器 / 触发器 / 寄存器 |
| 时钟 | 不需要 | 通常有 |

若反馈把输出绕回输入且未用寄存器隔开，可能出现锁存、振荡或冒险——那就不再是单纯组合块。带状态的系统见 [[Sequential Logic and Finite State Machines]]。

---
## 6. 传播延迟 $t_{\mathrm{PD}}$（简述）

$t_{\mathrm{PD}}$：**上界**——从所有输入变为合法稳定值起，到所有输出保证合法稳定为止的最长时间。

对门网：
$$
t_{\mathrm{PD}}(\text{电路}) \ge \max_{\text{路径 }P}\sum_{\text{门 }g\in P}t_{\mathrm{PD}}(g)
$$
（实际取最长路径的保守上界）。行波加法器进位链是经典的 $O(N)$ 长路径例子。

> [!warning] 功能正确 ≠ 时序正确
> 真值表对了，若时钟周期短于寄存器之间组合逻辑的 $t_{\mathrm{PD}}$，采样仍会采到非法或旧值。性能权衡见 [[Performance and Design Tradeoffs]]。

可选的更细规格还有污染延迟 $t_{\mathrm{CD}}$（输出最早何时可能变）、建立/保持时间（对后续寄存器）——进入时序节再展开。

> [!example] 行波进位粗估
> 若 1 bit 全加器 $t_{\mathrm{PD,FA}}=t_0$，则 $N$ bit 行波加法器进位链约 $N t_0$。32 bit 时这常是 ALU 关键路径；加速加法（进位旁路 / 超前进位）正是在砍这条 $t_{\mathrm{PD}}$。

---
## 7. 设计小清单（工科）

1. **先功能后门级**：真值表 / 布尔式写清，再映射到 NAND/NOR 或标准单元。
2. **模块化**：大组合块拆成 MUX、加法器、比较器等有名字的部件，便于估延迟与复用。
3. **注意扇出与负载**：延迟模型随负载变；估算时别只背“理想门延迟”。
4. **避免意料外反馈**：组合云必须无环（或明确做成异步锁存并证明安全）。

---
## 8. 工作例：布尔化简、MUX 与 $t_{\mathrm{PD}}$

> [!example] 题目
> （1）化简 $F=A\bar B+AB+B\bar C$ 到较简 SOP（可用吸收 / 共识）。
> （2）用 2 选 1 MUX 实现 $Y=A\oplus B$（提示：以 $A$ 为选择端时两路数据是什么）。
> （3）门网：输入 → NOT（$t_{\mathrm{PD}}=1$）→ AND（$t_{\mathrm{PD}}=2$）与并行 OR（$t_{\mathrm{PD}}=2$）→ 再 NAND（$t_{\mathrm{PD}}=2$）。估电路 $t_{\mathrm{PD}}$ 下界（取最长路径）。

> [!success]- 参考答案
> （1）$A\bar B+AB=A$；$F=A+B\bar C$（或继续视需要展开）。检：$A=1$ 时原式为 1；$A=0$ 时原式 $=B\bar C$。
> （2）$A=0$ 时 $Y=B$；$A=1$ 时 $Y=\bar B$。故 MUX 选择=$A$，数据口 $D_0=B$，$D_1=\bar B$。
> （3）路径例：IN→NOT→AND→NAND：$1+2+2=5$；IN→OR→NAND 若 OR 直接吃输入：$2+2=4$。故 $t_{\mathrm{PD}}\ge 5$（单位与题设一致）。

---
## 9. 本节清单

1. 能陈述组合器件三要素（数字 IO、功能表、$t_{\mathrm{PD}}$），并解释“无内部状态”。
2. 会写简单函数的真值表与 SOP；会用德摩根与吸收做初级化简。
3. 说明 MUX / 译码器用途；能口述 ALU = 多运算组合核 + 选择。
4. 会用最长路径思想估算 $t_{\mathrm{PD}}$；区分功能正确与时序满足。
5. 能手推一题化简 + 一题 MUX 实现 + 一题路径延迟。

## 参考

- MIT 6.004 *Computation Structures*, Digital Abstraction / Combinational devices — https://computationstructures.org/lectures/digital/digital.html
- 课程笔记：https://computationstructures.org/notes/digitalabstraction/notes.html
- MIT OCW：https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/
