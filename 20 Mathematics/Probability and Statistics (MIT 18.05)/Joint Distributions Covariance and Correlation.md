---
aliases:
  - 联合分布与协方差
  - Joint Distributions
  - Covariance and Correlation
  - Cov Corr
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Discrete Random Variables]]"
  - "[[Continuous Random Variables]]"
  - "[[Law of Large Numbers and Central Limit Theorem]]"
  - "[[Linear Regression]]"
down:
  - "[[Law of Large Numbers and Central Limit Theorem]]"
---
# 联合分布、协方差与相关

> [!summary] 核心结论
> 联合分布给出 $(X,Y)$ 的完整概率结构；边缘分布与条件分布由联合分布积分/求和得到。独立 $\Leftrightarrow$ 联合 $=$ 边缘之积，且此时 $\operatorname{Cov}(X,Y)=0$（反之一般不成立）。协方差度量线性共变；相关系数是标准化后的协方差，且 $|\rho|\le 1$。方差加法公式 $\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}(X,Y)$ 是工科误差传播与和式方差的核心。

> 底本：MIT 18.05（Orloff / Kamrin）联合分布与相关单元。

> 关键词：joint / marginal / conditional、independence、covariance、correlation、$\operatorname{Var}(X+Y)$

---

## 1. 联合分布：离散与连续

### 1.1 离散：联合 PMF

$$
p_{X,Y}(x,y)=P(X=x,Y=y),\qquad
\sum_x\sum_y p_{X,Y}(x,y)=1.
$$

事件 $\{(X,Y)\in A\}$ 的概率是把 $A$ 上所有格点的联合质量相加。

### 1.2 连续：联合 PDF

非负函数 $f_{X,Y}$ 满足
$$
\iint_{\mathbb{R}^2}f_{X,Y}(x,y)\,dx\,dy=1,
$$
且对可测区域 $A$，
$$
P\bigl((X,Y)\in A\bigr)=\iint_A f_{X,Y}(x,y)\,dx\,dy.
$$

联合 CDF：$F_{X,Y}(a,b)=P(X\le a,Y\le b)$。在连续情形有
$$
f_{X,Y}=\frac{\partial^2 F_{X,Y}}{\partial x\,\partial y}
$$
（在密度连续点处）。

> [!tip] 读图直觉
> 散点图稠密的方向对应高概率质量；相关强弱看“云”是否拉长成斜带。

![[ps-joint-correlation.svg]]

---

## 2. 边缘分布（marginal）

从联合“积掉”另一个变量：

**离散**
$$
p_X(x)=\sum_y p_{X,Y}(x,y),\qquad
p_Y(y)=\sum_x p_{X,Y}(x,y).
$$

**连续**
$$
f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy,\qquad
f_Y(y)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx.
$$

边缘分布描述单变量行为，但**一般不能**还原联合结构（同边缘可有不同相关）。

---

## 3. 条件分布（conditional）

固定一变量后，另一变量的分布：

**离散**（$p_Y(y)>0$）
$$
p_{X\mid Y}(x\mid y)=\frac{p_{X,Y}(x,y)}{p_Y(y)}.
$$

**连续**（$f_Y(y)>0$）
$$
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}.
$$

条件期望 $\mathbb{E}[X\mid Y=y]$ 是回归思想的概率语言：给定 $Y$，对 $X$ 的最佳均方预测（在平方损失下）是条件均值。

> [!example] 离散表格速算
> 先按行/列求和得边缘，再用联合/边缘得条件；检查每一条件行（或列）是否归一化到 1。

> [!example] 端到端：$2\times 2$ 联合表
> 联合 PMF（已归一）：
>
> |  | $Y=0$ | $Y=1$ | 边缘 $X$ |
> |--|--------|--------|-----------|
> | $X=0$ | $0.10$ | $0.30$ | $0.40$ |
> | $X=1$ | $0.20$ | $0.40$ | $0.60$ |
> | 边缘 $Y$ | $0.30$ | $0.70$ | $1$ |
>
> $E[X]=0.6$，$E[Y]=0.7$，$E[XY]=1\cdot 1\cdot 0.40=0.40$。
> $$
> \mathrm{Cov}(X,Y)=0.40-0.6\cdot 0.7=0.40-0.42=-0.02.
> $$
> $\mathrm{Var}(X)=0.6\cdot 0.4=0.24$，$\mathrm{Var}(Y)=0.7\cdot 0.3=0.21$，
> $$
> \rho=\frac{-0.02}{\sqrt{0.24\cdot 0.21}}=\frac{-0.02}{\sqrt{0.0504}}\approx\frac{-0.02}{0.224}=-0.089.
> $$
> 检验独立：$p_X(0)p_Y(0)=0.4\cdot 0.3=0.12\neq 0.10=p(0,0)$ → **不独立**（尽管 $|\rho|$ 很小）。

---

## 4. 独立性

$X,Y$ **独立**当且仅当对一切（适当）集合
$$
P(X\in A,Y\in B)=P(X\in A)P(Y\in B).
$$

等价刻画（在相应设定下）：

| 类型 | 判据 |
|------|------|
| 离散 | $p_{X,Y}(x,y)=p_X(x)p_Y(y)$ 对一切 $x,y$ |
| 连续 | $f_{X,Y}(x,y)=f_X(x)f_Y(y)$ 对几乎处处 |
| 条件 | $p_{X\mid Y}=p_X$（或密度版） |

独立 $\Rightarrow$ 不相关（见下），但**不相关 $\not\Rightarrow$ 独立**。经典反例：令 $X\sim$ 对称于 0，$Y=X^2$，则 $\operatorname{Cov}(X,Y)=0$ 但 $Y$ 完全由 $X$ 决定。

> [!warning] 高斯例外要记牢
> 若 $(X,Y)$ **联合正态**，则不相关 $\Leftrightarrow$ 独立。非联合正态时不可套用。

---

## 5. 协方差与和的方差

定义（$\mu_X=\mathbb{E}X$，$\mu_Y=\mathbb{E}Y$）
$$
\operatorname{Cov}(X,Y)=\mathbb{E}\bigl[(X-\mu_X)(Y-\mu_Y)\bigr]
=\mathbb{E}[XY]-\mu_X\mu_Y.
$$

性质：$\operatorname{Cov}(X,X)=\operatorname{Var}X$；对称；双线性 $\operatorname{Cov}(aX+b,cY+d)=ac\operatorname{Cov}(X,Y)$；独立 $\Rightarrow$ $\operatorname{Cov}=0$（因独立时 $\mathbb{E}[XY]=\mathbb{E}X\,\mathbb{E}Y$）。期望线性 $\mathbb{E}[aX+bY]=a\mathbb{E}X+b\mathbb{E}Y$ **不需**独立。

核心公式：
$$
\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}(X,Y).
$$
一般和：$\operatorname{Var}(\sum_i X_i)=\sum_i\operatorname{Var}X_i+2\sum_{i<j}\operatorname{Cov}(X_i,X_j)$。独立或不相关时交叉项消失。

> [!tip] 工科用法
> 测量误差合成、投资组合方差、蒙特卡洛均值方差都回到这一条；相关误差会放大或抵消总方差。

---

## 6. 相关系数（correlation）

若 $\sigma_X,\sigma_Y>0$，
$$
\rho(X,Y)=\operatorname{Corr}(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.
$$
$|\rho|\le 1$；$|\rho|=1$ $\Leftrightarrow$ $Y=aX+b$ a.s.（$a\neq 0$）；仿射变换下 $\operatorname{Corr}(aX+b,cY+d)=\operatorname{sign}(ac)\,\rho$（$ac\neq 0$）。$\rho$ 只捕捉**线性**关系。

---

## 7. 计算流程

**离散表**：归一化 → 边缘 → $\mathbb{E}X,\mathbb{E}Y,\mathbb{E}[XY]$ → Cov → $\rho$ → 检验联合是否等于边缘乘积。  
**连续密度**：求和换积分；先画支撑（矩形 / 三角 / 圆盘）再定限。

> [!example] 均匀三角形
> $(X,Y)$ 在 $\{x\ge 0,y\ge 0,x+y\le 1\}$ 上均匀，密度常数 $2$。边缘非均匀；支撑非乘积 → 不独立。

> [!example] $\mathrm{Var}(X+Y)$ 数值
> 上表：$\mathrm{Var}(X+Y)=0.24+0.21+2(-0.02)=0.41$。
> 若误当独立相加得 $0.45$，会**高估**总方差（此处负相关抵消）。

---

## 8. 与后续统计的衔接

- **LLN / CLT**：$\operatorname{Var}(\bar X)=\sigma^2/n$ 默认独立（或不相关）；相关样本改变有效样本量。  
- **回归**：斜率与 $\operatorname{Cov}(X,Y)/\operatorname{Var}X$ 同型；相关散点图是诊断起点。

---

## 9. 自检与参考答案

1. 会从联合求边缘与条件；用联合 $=$ 边缘之积检验独立。  
2. 会算 $\operatorname{Cov}$、$\rho$，并叙述 $|\rho|\le 1$ 与完全线性相关。  
3. 会用 $\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}$；独立时交叉项消失。  
4. 分清：独立 $\Rightarrow$ 不相关，反之一般不成立（联合正态例外）。

> [!success]- 参考答案
> 1. 边缘 $=$ 对另一变量求和/积分；条件 $=$ 联合/边缘；独立 $\Leftrightarrow$ 联合 $=$ 边缘乘积。
> 2. $\mathrm{Cov}=E[XY]-\mu_X\mu_Y$；$\rho=\mathrm{Cov}/(\sigma_X\sigma_Y)$；$|\rho|=1\Leftrightarrow$ 完全线性。
> 3. 和的方差必须加 $2\mathrm{Cov}$；不相关/独立时交叉项为 0。
> 4. 独立 $\Rightarrow\mathrm{Cov}=0$；$\mathrm{Cov}=0\not\Rightarrow$ 独立（除非联合正态）。

> [!example] 练习：条件概率
> 用上表求 $P(X=1\mid Y=1)$ 与 $E[X\mid Y=1]$。

> [!success]- 练习参考答案
> $P(X=1\mid Y=1)=0.40/0.70=4/7$。因 $X\in\{0,1\}$，$E[X\mid Y=1]=4/7$。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, MIT OCW Spring 2022（joint distributions / covariance）
- https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
