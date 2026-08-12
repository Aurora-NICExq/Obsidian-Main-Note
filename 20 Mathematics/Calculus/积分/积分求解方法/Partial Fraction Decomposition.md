---
aliases: [部分分式, Partial Fraction Decomposition, Partial Fractions]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Integration by Parts|分部积分]], [[Derivative and Integral Formula Tables|导数和积分公式]], [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]"
down: ""
---
# Partial Fraction Decomposition

> [!summary] 核心结论
> 部分分式 (partial fractions) 是积**有理函数 (rational function)** $\frac{P(x)}{Q(x)}$ 的标准方法：把一个难积的分式拆成若干"简单分式"之和，每一项都能用基本公式（$\ln|u|$ 或 $\arctan u$）积出。前提是先化为**真分式 (proper fraction)**。

前置知识：[[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]、因式分解。

---

## 1. 第一步：化为真分式 (Make It Proper)

被积函数 $f(x)=\dfrac{P(x)}{Q(x)}$ 必须满足 $\deg P<\deg Q$（真分式）。

- 若 $\deg P\ge\deg Q$（**假分式**, improper），先做**多项式长除法 (polynomial long division)**，化为"多项式 $+$ 真分式"，再对真分式部分拆分。

**长除法示例**：

$$\int\frac{5x^2+x-3}{x^2-1}\,dx.$$

$$\begin{array}{r}5\phantom{xxxx}\\ x^2-1\,\overline{)\,5x^2+x-3}\\ \underline{5x^2\phantom{+x}-5}\\ x+2\phantom{xx}\end{array}$$

商为 $5$，余为 $x+2$，故

$$\frac{5x^2+x-3}{x^2-1}=5+\frac{x+2}{x^2-1}.$$

---

## 2. 第二步：拆分与积分 (Decompose & Integrate)

1. **分解分母**：把 $Q(x)$ 彻底分解为一次因式 $(ax+b)$ 与不可约二次因式 $(ax^2+bx+c)$ 之积。
2. **写拆分形式**（设待定系数）：按因子类型套用下表。
3. **求系数**：通分后用**赋值法**（代入根使某些项为零）或**比较系数法 (matching coefficients)** 解出 $A,B,C,\dots$。
4. **逐项积分**：结果通常含 $\ln|u|$ 或 $\arctan u$。

### 拆分规则表 (Decomposition Table)

| 分母因子类型 (Factor) | 对应部分分式 (Term) |
| :-- | :-- |
| 互异一次因子 $(ax+b)$ | $\dfrac{A}{ax+b}$ |
| 重复一次因子 $(ax+b)^k$ | $\dfrac{A_1}{ax+b}+\cdots+\dfrac{A_k}{(ax+b)^k}$ |
| 不可约二次因子 $(ax^2+bx+c)$ | $\dfrac{Ax+B}{ax^2+bx+c}$ |
| 重复二次因子 $(ax^2+bx+c)^k$ | $\dfrac{A_1x+B_1}{ax^2+bx+c}+\cdots+\dfrac{A_kx+B_k}{(ax^2+bx+c)^k}$ |

"重复"指该因子在分母中以 $k$ 次幂出现，需为每一阶都设一项。

---

## 3. 完整示例 (Worked Example)

$$\int\frac{1}{x^2-1}\,dx.$$

1. **分解分母**：$x^2-1=(x-1)(x+1)$。
2. **设拆分**：$\dfrac{1}{(x-1)(x+1)}=\dfrac{A}{x-1}+\dfrac{B}{x+1}$。
3. **求系数**（赋值法）：通分得 $1=A(x+1)+B(x-1)$。
   - 令 $x=1$：$1=2A\Rightarrow A=\tfrac12$；
   - 令 $x=-1$：$1=-2B\Rightarrow B=-\tfrac12$。
4. **积分**：

$$\int\left(\frac{1/2}{x-1}-\frac{1/2}{x+1}\right)dx=\frac12\ln|x-1|-\frac12\ln|x+1|+C.$$

> [!tip] 与其它方法的衔接
> 当拆分后出现 $\frac{Ax+B}{ax^2+bx+c}$ 型，常需"配方 + 凑微分"导出 $\arctan$；遇到对数/反三角与多项式相乘的项，则转用 [[Integration by Parts|分部积分]]。基本积分表见 [[Derivative and Integral Formula Tables|导数和积分公式]]。
