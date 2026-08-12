---
aliases:
  - 计数与概率基础
  - Counting
  - Sample Space
  - Probability Axioms
  - Reading 1 Counting and Probability
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Conditional Probability and Bayes Theorem]]"
  - "[[Discrete Random Variables]]"
down:
  - "[[Conditional Probability and Bayes Theorem]]"
---
# 计数与概率基础

> [!summary] 核心结论
> 概率从**样本空间** $\Omega$ 与**事件**（子集）出发：Kolmogorov 公理把 $P$ 变成规范化、可加的测度。有限等可能时，$P(A)=|A|/|\Omega|$，于是计数（乘法原理、排列、组合）直接变成算概率。容斥给重叠事件纠偏；下一讲的条件概率在此基础上加“缩小样本空间”的操作。

> 底本：MIT 18.05 Reading 1（Jeremy Orloff / Jennifer French Kamrin, Spring 2022）。

---
## 1. 样本空间与事件

一次随机试验的全部可能结果记为样本空间 $\Omega$。**结果**（outcome）是 $\Omega$ 的元素；**事件**（event）是 $\Omega$ 的子集。

常用集合运算：

| 符号 | 含义 |
|------|------|
| $A\cup B$ | $A$ 或 $B$ 发生 |
| $A\cap B$ | $A$ 与 $B$ 同时发生 |
| $A^c$ | $A$ 的补（不发生） |
| $A\setminus B$ | $A$ 发生且 $B$ 不发生 |
| $\emptyset$ | 不可能事件 |
| $\Omega$ | 必然事件 |

互斥（disjoint）：$A\cap B=\emptyset$。两两互斥的事件族可像“分块”一样处理。

![[ps-venn-events.svg]]

> [!tip] 工科习惯
> 先画 $\Omega$，再标事件；问“求什么概率”之前先写清事件用集合语言是什么。

---
## 2. 计数三板斧

### 2.1 乘法原理

若一过程分 $k$ 步，第 $i$ 步有 $n_i$ 种选择（且选择数不依赖前面具体取值时），则总方式数
$$
n_1 n_2\cdots n_k.
$$
有依赖时：按树状图分层乘，或用条件计数（下一讲链法则的离散版）。

### 2.2 排列（permutation）

从 $n$ 个不同物体中**有序**取 $k$ 个：
$$
P(n,k)=n(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}.
$$
全排列：$P(n,n)=n!$。

### 2.3 组合（combination）

从 $n$ 个中**无序**取 $k$ 个：
$$
\binom{n}{k}=\frac{n!}{k!(n-k)!}=\frac{P(n,k)}{k!}.
$$
恒等式：$\binom{n}{k}=\binom{n}{n-k}$，$\displaystyle\binom{n}{0}+\cdots+\binom{n}{n}=2^n$。

> [!example] 扑克牌手牌
> 52 张牌发 5 张：$\binom{52}{5}$。指定花色同花：$\binom{13}{5}$（再乘 4 种花色，若问“同花且非同花顺”需再减）。

---
## 3. 概率公理

映射 $P:\{\text{事件}\}\to[0,1]$ 满足：

1. **非负**：$P(A)\ge 0$
2. **规范化**：$P(\Omega)=1$
3. **可数可加**：若 $A_1,A_2,\ldots$ 两两互斥，则
$$
P\!\left(\bigcup_{i=1}^\infty A_i\right)=\sum_{i=1}^\infty P(A_i).
$$

有限互斥可加是特殊情形。立刻得到：

$$
P(\emptyset)=0,\qquad P(A^c)=1-P(A),\qquad A\subset B\Rightarrow P(A)\le P(B).
$$

对任意 $A,B$（不必互斥）：
$$
P(A\cup B)=P(A)+P(B)-P(A\cap B).
$$

---
## 4. 等可能结果（classical probability）

若 $\Omega$ 有限且每个结果等可能，则
$$
P(A)=\frac{|A|}{|\Omega|}.
$$
此时“算概率”=“数分子与分母”。陷阱：结果必须**真正等可能**——例如两枚硬币用 $\{HH,HT,TH,TT\}$ 而不是 $\{0\text{ 正面},1\text{ 正面},2\text{ 正面}\}$（后者不等可能）。

> [!example] 掷两枚公平骰子
> $|\Omega|=36$。和为 7：$\{(1,6),(2,5),\ldots,(6,1)\}$ 共 6 个，故 $P=6/36=1/6$。

> [!example] 至少一枚正面（两枚公平硬币）
> $|A|=3$（$HT,TH,HH$），$P=3/4$。用补集更快：$1-P(\text{全反})=1-1/4=3/4$。

---
## 5. 容斥原理（简介）

两个事件见上式。三个事件：
$$
\begin{aligned}
P(A\cup B\cup C)
&=P(A)+P(B)+P(C)\\
&\quad-P(A\cap B)-P(A\cap C)-P(B\cap C)\\
&\quad+P(A\cap B\cap C).
\end{aligned}
$$
直觉：先全部加上，两两交集加了两次要减，三重交集被减过头再加回。

> [!example] 至少抽到一张 A（从 52 张抽 5 张）
> 用补集：一张 A 都没有 $=\binom{48}{5}/\binom{52}{5}$，故
> $$
> P(\text{至少一张 A})=1-\frac{\binom{48}{5}}{\binom{52}{5}}.
> $$
> 直接容斥按“至少 $k$ 张指定花色”亦可，但补集往往更干净。

> [!example] 端到端数值：密码与容斥
> 4 位 PIN，每位 $0$–$9$，等可能。事件 $A$：至少有一位是 $7$。
> $$
> |\Omega|=10^4=10000,\qquad
> |A^c|=9^4=6561,\qquad
> P(A)=1-6561/10000=0.3439.
> $$
> 若误用“四位中选位置放 7”却不处理重叠，会重复计数含多个 7 的码；补集自动避开重叠。

一般 $n$ 个事件的容斥：交替加减所有 $k$ 重交的概率，$k=1,\ldots,n$。

---
## 6. 常用技巧与常见坑

1. **补集**：问“至少一个”时常算 $1-P(\text{一个都没有})$。
2. **分母先固定**：换分母等于换了模型；比较两个模型时不要混用 $|\Omega|$。
3. **有序 / 无序一致即可**：分子分母同用排列或同用组合；混用会错。
4. **对称性**：许多问题用“随机排列中位置 $i$ 的概率相同”可秒算，不必枚举。

> [!warning] 生日悖论预告
> $n$ 人中至少两人同生日，补集是“全不同”：
> $$
> P=1-\frac{P(365,n)}{365^n}.
> $$
> $n=23$ 时已约 $1/2$——直觉对“至少一对”严重低估。

---
## 7. 与后续章节的接口

- **条件概率**：$P(A\mid B)=P(A\cap B)/P(B)$ 把样本空间缩到 $B$。
- **离散随机变量**：给 $\Omega$ 上的函数 $X$，用 PMF 代替“逐事件”描述。
- **独立性**：下一讲定义；计数模型里常对应“有放回 / 分步独立选择”。

---
## 8. 自检与参考答案

1. 会写 $\Omega$、事件与集合运算；会读 Venn 图。
2. 熟练乘法原理、$P(n,k)$、$\binom{n}{k}$；分子分母计数口径一致。
3. 记住三条公理及 $P(A\cup B)=P(A)+P(B)-P(A\cap B)$；会用等可能公式。
4. 会用补集与简单容斥；知道生日类问题直觉会失灵。

> [!success]- 参考答案
> 1. $\Omega=$ 全部结果；事件 $=$ 子集；并/交/补对应或/且/非。
> 2. 有序用 $P(n,k)$，无序用 $\binom{n}{k}$；分子分母同口径。
> 3. 非负、归一、$P(\Omega)=1$、互斥可加；等可能时 $P(A)=|A|/|\Omega|$。
> 4. “至少一个”常算 $1-P(\text{全无})$；生日 $n=23$ 已约一半。

> [!example] 练习：两骰子点数
> 两枚公平骰子。求 $P(\text{点数之积为偶数})$。

> [!success]- 练习参考答案
> 积为奇数 $\Leftrightarrow$ 两枚都奇数。奇数面 $\{1,3,5\}$，共 $3\times 3=9$ 种，故 $P(\text{积奇})=9/36=1/4$，
> $P(\text{积偶})=1-1/4=3/4$。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, Reading 1 (Counting / Probability), MIT OCW Spring 2022
- 课程主页：https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
