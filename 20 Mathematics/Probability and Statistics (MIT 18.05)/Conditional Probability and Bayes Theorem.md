---
aliases:
  - 条件概率与贝叶斯定理
  - Conditional Probability
  - Bayes Theorem
  - Independence
  - Reading 2 Conditional Probability
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Counting and Probability Basics]]"
  - "[[Discrete Random Variables]]"
  - "[[Continuous Random Variables]]"
down:
  - "[[Discrete Random Variables]]"
---
# 条件概率与贝叶斯定理

> [!summary] 核心结论
> 条件概率 $P(A\mid B)=P(A\cap B)/P(B)$ 是把样本空间缩到 $B$ 后的规范化概率。链法则、全概率公式、Bayes 定理是同一枚硬币的三面：正向分解、按划分展开、反向更新信念。独立性是“条件不改概率”；医学检验等例子说明——忽视基础率（base rate）会把“检出阳性”误读成“几乎患病”。

> 底本：MIT 18.05 Reading 2–3（Jeremy Orloff / Jennifer French Kamrin, Spring 2022）。

---
## 1. 条件概率

当 $P(B)>0$ 时定义
$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$
几何图像：在 $B$ 内看 $A\cap B$ 所占比例。等可能有限模型中
$$
P(A\mid B)=\frac{|A\cap B|}{|B|}.
$$

立刻有 $P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A)$。

> [!example] 两枚公平骰子，已知和为 7
> 条件空间有 6 个结果；其中第一枚为 1 的只有 $(1,6)$，故 $P(\text{第一枚}=1\mid\text{和}=7)=1/6$。

> [!example] 端到端：袋中抽球（无放回）
> 袋中 3 红 2 蓝。依次抽两球。求 $P(\text{第二球红})$ 与 $P(\text{第一蓝}\mid\text{第二红})$。
>
> 全概率：
> $$
> P(R_2)=P(R_2\mid R_1)P(R_1)+P(R_2\mid B_1)P(B_1)
> =\frac{2}{4}\cdot\frac{3}{5}+\frac{3}{4}\cdot\frac{2}{5}
> =\frac{6}{20}+\frac{6}{20}=\frac{3}{5}.
> $$
> （对称性：无放回时每一位置边缘同分布，也得 $3/5$。）
> $$
> P(B_1\mid R_2)=\frac{P(R_2\mid B_1)P(B_1)}{P(R_2)}
> =\frac{(3/4)(2/5)}{3/5}=\frac{1}{2}.
> $$

---
## 2. 链法则

对多个事件：
$$
\begin{aligned}
P(A\cap B)&=P(A)P(B\mid A),\\
P(A\cap B\cap C)&=P(A)P(B\mid A)P(C\mid A\cap B),
\end{aligned}
$$
一般地
$$
P(A_1\cap\cdots\cap A_n)
=P(A_1)P(A_2\mid A_1)\cdots P(A_n\mid A_1\cap\cdots\cap A_{n-1}).
$$
树状图每条路径的概率 = 沿途条件概率之积；同一叶集合的路径相加。

![[ps-bayes-tree.svg]]

---
## 3. 独立性

事件 $A,B$ **独立**当且仅当
$$
P(A\cap B)=P(A)P(B).
$$
在 $P(B)>0$ 时等价于 $P(A\mid B)=P(A)$（知道 $B$ 不改变 $A$ 的概率）。两两独立 $\neq$ 相互独立（三个以上需对所有子集交概率分解）。

> [!warning] 互斥 vs 独立
> 若 $P(A),P(B)>0$ 且互斥，则 $P(A\cap B)=0\neq P(A)P(B)$，故**不独立**。互斥是“不能一起发生”；独立是“信息互不相关”。

独立试验（有放回抽样、重复抛币）是建模时最常用的独立性来源。

---
## 4. 全概率公式

设 $B_1,\ldots,B_n$ 构成 $\Omega$ 的划分（两两互斥且并集为 $\Omega$），且 $P(B_i)>0$，则对任意事件 $A$：
$$
P(A)=\sum_{i=1}^n P(A\mid B_i)P(B_i).
$$
连续版把求和换成积分；思想相同——先按“原因 / 场景”展开，再边缘化。

---
## 5. Bayes 定理

由 $P(B_i\mid A)P(A)=P(A\mid B_i)P(B_i)$ 得
$$
P(B_i\mid A)=\frac{P(A\mid B_i)P(B_i)}{P(A)}
=\frac{P(A\mid B_i)P(B_i)}{\sum_j P(A\mid B_j)P(B_j)}.
$$

| 名称 | 符号 | 含义 |
|------|------|------|
| 先验 | $P(B_i)$ | 见到数据前对“原因”的信念 |
| 似然 | $P(A\mid B_i)$ | 该原因下数据出现的机会 |
| 后验 | $P(B_i\mid A)$ | 见到数据后更新的信念 |
| 证据 | $P(A)$ | 边缘概率（归一化常数） |

口语：**后验 $\propto$ 似然 × 先验**。

> [!tip] 计算顺序
> 1）画划分树；2）填先验与似然；3）算各叶 $P(A\cap B_i)$；4）求和得 $P(A)$；5）用 Bayes 得后验。

---
## 6. 医学检验与基础率谬误

设病患率（先验）$P(D)=0.001$，健康 $P(D^c)=0.999$。试剂：
$$
P(+ \mid D)=0.99,\qquad P(+ \mid D^c)=0.05
$$
（灵敏度 99%，误报率 5%）。问：检出阳性后真正患病的概率 $P(D\mid +)$？

$$
\begin{aligned}
P(+)
&=P(+\mid D)P(D)+P(+\mid D^c)P(D^c)\\
&=0.99\cdot 0.001+0.05\cdot 0.999=0.05094,\\[4pt]
P(D\mid +)
&=\frac{0.99\cdot 0.001}{0.05094}\approx 0.0194.
\end{aligned}
$$
约 **2%**，远不是“99% 准就几乎确诊”。

> [!example] 频率直觉（100000 人）
> 约 100 人患病，其中约 99 人检出；约 99900 健康人中约 4995 人误报阳性。阳性人群里真患者占比 $99/(99+4995)\approx 1.9\%$。

**基础率谬误（base-rate fallacy）**：只盯着灵敏度 / “准确率”，忽略疾病稀有（先验极小），导致后验被高估。

> [!warning] “99% 准确”不等于后验 99%
> 灵敏度高只说明 $P(+\mid D)$ 大；后验 $P(D\mid +)$ 还被先验 $P(D)$ 与假阳性率压着。稀有病 + 哪怕不大的误报率 → 阳性人群里真患者仍可能是少数。

同类陷阱：垃圾邮件过滤、稀有故障报警、法庭上 DNA “匹配概率”话术——一律先写清先验与划分，再 Bayes。

---
## 7. 多假设与连续更新

若划分有多个 $B_i$，Bayes 对每个 $i$ 算一次后验；也可只比后验比（odds）：
$$
\frac{P(B_1\mid A)}{P(B_2\mid A)}=\frac{P(A\mid B_1)}{P(A\mid B_2)}\cdot\frac{P(B_1)}{P(B_2)}.
$$
似然比 × 先验比 = 后验比。顺序来的独立数据可把上一轮后验当作下一轮先验（序贯更新）。

---
## 8. 与随机变量的衔接

条件概率对事件陈述；引入随机变量 $X,Y$ 后写成
$$
P(X=x\mid Y=y),\qquad f_{X\mid Y}(x\mid y)
$$
等（离散 PMF / 连续条件密度）。全概率与 Bayes 的形状不变，只是求和 / 积分对象换成分布。

---
## 9. 自检与参考答案

1. 会用定义算 $P(A\mid B)$；会画概率树并写链法则。
2. 分清独立与互斥；会检验 $P(A\cap B)=P(A)P(B)$。
3. 会用全概率公式与 Bayes；能填先验 / 似然 / 后验表。
4. 会算医学检验类后验，并解释为何基础率不可忽略。

> [!success]- 参考答案
> 1. $P(A\mid B)=P(A\cap B)/P(B)$；树路径乘条件概率，同叶相加。
> 2. 独立：$P(A\cap B)=P(A)P(B)$。互斥且正概率 $\Rightarrow$ **不**独立。
> 3. $P(A)=\sum P(A\mid B_i)P(B_i)$；后验 $\propto$ 似然 × 先验。
> 4. 医学例中先验小 → 即使灵敏度高，后验也可很低；必须用全概率归一化。

> [!example] 练习：两厂家芯片
> 厂 A 产 70%，次品率 2%；厂 B 产 30%，次品率 5%。随机抽一片为次品，求来自 B 的概率。

> [!success]- 练习参考答案
> $P(D)=0.02\cdot 0.7+0.05\cdot 0.3=0.029$。
> $P(B\mid D)=(0.05\cdot 0.3)/0.029=0.015/0.029\approx 0.517$。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, Reading 2–3 (Conditional Probability / Bayes), MIT OCW Spring 2022
- 课程主页：https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
