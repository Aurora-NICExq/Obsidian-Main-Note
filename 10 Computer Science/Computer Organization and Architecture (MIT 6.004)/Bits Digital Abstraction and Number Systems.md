---
aliases:
  - 比特数字抽象与数制
  - Bits and Digital Abstraction
  - Number Systems
  - Two's Complement
  - L01 Basics of Information
  - L02 Digital Abstraction
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Combinational Logic]]"
down:
  - "[[Combinational Logic]]"
---
# 比特、数字抽象与数制

> [!summary] 核心结论
> 信息用**比特**编码；物理世界是连续电压，靠**数字抽象**（合法电平区间 + 噪声容限）把模拟噪声挡在门外。定长 $N$ bit 无符号整数取值 $[0,2^N-1]$；有符号常用**补码**（最高位权为 $-2^{N-1}$），加减可共用同一加法器。十六进制是 4 bit 一组的紧凑写法。抽象分层（应用 → ISA → 数据通路 → 门 → 电压）让每一层只看见离散符号。

> 底本：MIT 6.004 *Computation Structures* L01（Basics of Information）与 L02（The Digital Abstraction）；见 computationstructures.org。

---
## 1. 信息与比特

一次选择若有 $M$ 个等可能结果，信息量约为
$$
\log_2 M \quad\text{（单位：bit）}.
$$
把符号集映射到 $\{0,1\}^*$ 的规则叫**编码**。定长编码：等可能或“先保证可解码”时常用；变长编码（Huffman 等）把短码分给高频符号，平均长度逼近熵——本课后续信息论只点到为止。

> [!tip] 工科习惯
> 先问“有多少种可能 / 需要几 bit”，再谈电路与指令。$N$ bit 最多区分 $2^N$ 个互异消息。

---
## 2. 抽象分层

数字系统靠分层把问题切开：上层只看见离散接口，下层负责电压与时序。

![[coa-abstraction-layers.svg]]

| 层 | 典型对象 |
|----|----------|
| 应用 / OS | 程序、文件、进程 |
| ISA / 汇编 | 指令、寄存器名、寻址 |
| 数据通路 / 控制 | ALU、MUX、控制器 FSM |
| 门 / 触发器 | AND/OR/NOT、DFF、寄存器 |
| CMOS / 电压 | $V_{\mathrm{OL}}$、$V_{\mathrm{OH}}$、噪声容限 |

上层的“正确”依赖下层满足**数字纪律**（合法电平、足够噪声裕量、时序约束）。

---
## 3. 数字抽象：用电压表示 0/1

连续电压不能直接当无限精度实数用——误差会沿级联累积。数字抽象的做法：只区分两个符号，并对发送端 / 接收端规定**不同**的电压区间。

常用阈值（示意）：

| 符号 | 含义 |
|------|------|
| $V_{\mathrm{OL}}$ | 输出“0”的最高允许电压 |
| $V_{\mathrm{OH}}$ | 输出“1”的最低允许电压 |
| $V_{\mathrm{IL}}$ | 输入仍判为“0”的最高电压 |
| $V_{\mathrm{IH}}$ | 输入判为“1”的最低电压 |

噪声容限（noise margins）：
$$
\mathrm{NM}_L = V_{\mathrm{IL}}-V_{\mathrm{OL}},\qquad
\mathrm{NM}_H = V_{\mathrm{OH}}-V_{\mathrm{IH}}.
$$
要求 $\mathrm{NM}_L,\mathrm{NM}_H>0$，即输出驱动得比输入判决更“干净”，中间留下禁区吸收噪声与工艺偏差。

> [!warning] 禁止区
> 落在 $(V_{\mathrm{IL}},V_{\mathrm{IH}})$ 的电压**不是**合法数字值；组合逻辑保证：合法输入稳定足够久后，输出必回到合法区间（见 [[Combinational Logic]] 的 $t_{\mathrm{PD}}$）。

---
## 4. 无符号整数

$N$ bit 串 $b_{N-1}\cdots b_0$，无符号解释：
$$
X = \sum_{i=0}^{N-1} b_i\,2^i,\qquad
X\in\{0,1,\ldots,2^N-1\}.
$$

> [!example] 8 bit
> $1100\,1001_2 = 2^7+2^6+2^3+2^0 = 128+64+8+1=201$。
> 范围：$0\sim 255=2^8-1$。

溢出：结果超出 $[0,2^N-1]$ 时，模 $2^N$ 回绕（硬件加法器自然如此）。

---
## 5. 补码（two's complement）

有符号整数让最高位带**负权**：
$$
X = -b_{N-1}\,2^{N-1}+\sum_{i=0}^{N-2} b_i\,2^i.
$$
范围：
$$
X\in\bigl[-2^{N-1},\,2^{N-1}-1\bigr].
$$
例如 $N=8$：$-128\sim +127$。

性质（工科最常用的几条）：

1. **取负**：按位取反再加 1（在模 $2^N$ 意义下）。
2. **加减统一**：补码加法与无符号加法电路相同；符号位参与运算即可。
3. **符号扩展**：向高位复制符号位，数值不变。

> [!example] 4 bit 补码
> $0110\to +6$；$1010\to -8+2=-6$。
> $-6$ 的编码：对 $0110$ 取反得 $1001$，再加 1 得 $1010$。

> [!warning] 非对称范围
> 最负值 $-2^{N-1}$ 没有对应的正数可表示；对它取负会溢出。

---
## 6. 十六进制与位宽习惯

$2^4=16$，故 4 bit ↔ 1 个十六进制数字：

| bin | hex | bin | hex |
|-----|-----|-----|-----|
| 0000 | 0 | 1000 | 8 |
| 0001 | 1 | 1001 | 9 |
| 0010 | 2 | 1010 | A |
| 0011 | 3 | 1011 | B |
| 0100 | 4 | 1100 | C |
| 0101 | 5 | 1101 | D |
| 0110 | 6 | 1110 | E |
| 0111 | 7 | 1111 | F |

书写习惯：`0x` 前缀或下标 $_16$。例如 `0xC9` $= 1100\,1001_2$。调试内存、指令编码、掩码时几乎总用 hex。

定宽机器常见 $N=8,16,32,64$；更大整数靠多精度或软件拆分。

---
## 7. 与后续章节的接口

- **组合逻辑**：在合法数字输入上实现布尔函数 $Y=f(A,B,\ldots)$，并给出传播延迟。
- **时序 / FSM**：用寄存器“记住”比特串作为状态。
- **ISA**：指令与立即数本身就是定宽比特模式（操作码、寄存器号、字面量）。

---
## 8. 工作例：进制、补码与噪声容限

> [!example] 综合小算
> （1）无符号 8 bit：`0xA5` 的十进制？二进制？
> （2）同一比特串若按 8 bit 补码解释，值是多少？
> （3）对 $+19$（8 bit 补码）写出编码；再求 $-19$ 的编码。
> （4）设 $V_{OL}=0.4\,\mathrm{V}$，$V_{IL}=0.8\,\mathrm{V}$，$V_{IH}=2.0\,\mathrm{V}$，$V_{OH}=2.4\,\mathrm{V}$。求 $\mathrm{NM}_L$、$\mathrm{NM}_H$。电压 $1.2\,\mathrm{V}$ 是否合法数字输入？

> [!success]- 参考答案
> （1）`0xA5`=$1010\,0101_2$=$165$。
> （2）最高位 1 → $-128+32+4+1=-91$。
> （3）$+19=0001\,0011$；取反 $1110\,1100$ +1 → $1110\,1101$ = `0xED`（即 $-19$）。
> （4）$\mathrm{NM}_L=0.8-0.4=0.4\,\mathrm{V}$；$\mathrm{NM}_H=2.4-2.0=0.4\,\mathrm{V}$。$1.2\,\mathrm{V}$ 落在 $(V_{IL},V_{IH})$ **禁区**，不是合法 0/1。

---
## 9. 本节清单

1. 会用 $\log_2 M$ 估计等可能选择所需比特数；知道定长编码容量是 $2^N$。
2. 能画出 / 口述抽象分层，并说明“上层离散、下层电压”。
3. 会写 $V_{\mathrm{OL/OH/IL/IH}}$ 与噪声容限；解释禁区为何必须存在。
4. 熟练无符号与补码的权值公式、范围、取负与符号扩展；会在 bin/hex 间互转。
5. 能独立完成补码取负与噪声容限数值题。

## 参考

- MIT 6.004 *Computation Structures*, L01 Basics of Information；L02 The Digital Abstraction — https://computationstructures.org/
- 课程笔记：https://computationstructures.org/notes/information/notes.html 、https://computationstructures.org/notes/digitalabstraction/notes.html
- MIT OCW：https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/
