---
aliases: [MIT18.1-Lec21-对数的积分应用（Applications）, 对数的积分应用, Applications to Logarithms]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L20 Fundamental Theorem of Calculus II]], [[MIT 18.01 L22 Volumes]], [[Derivative and Integral Formula Tables|导数和积分公式]]"
down: "[[MIT 18.01 L22 Volumes]]"
---
# Applications of the Integral to Logarithms

> [!summary] 核心结论
> 凡被积函数是"导数除以自身" $\dfrac{f'}{f}$ 的形式，积分即得 $\ln|f|$。这把许多看似复杂的积分（含 $\tan,\cot$）统一为对数型。

> 关键词：$\int 1/x$、$\int f'/f$、对数差、三角对数型。

---

## 1. 两个核心模式 (Two Patterns)

$$\int\frac1x\,dx=\ln|x|+C,\qquad \int\frac{f'(x)}{f(x)}\,dx=\ln|f(x)|+C.$$

第二式是凑微分 (u-substitution) 的直接结果：令 $u=f(x)$，$du=f'(x)dx$。

## 2. 定积分的对数差 (Log Difference)

区间不穿过 $0$ 时：$\displaystyle\int_a^b\frac1x\,dx=\ln\Big|\frac ba\Big|$。

## 3. 典型变形 (Typical Forms)

- $\int\tan x\,dx=-\ln|\cos x|+C$（因 $\tan x=\dfrac{-(\cos x)'}{\cos x}$）；
- $\int\cot x\,dx=\ln|\sin x|+C$。

## 4. 易错点 (Pitfalls)

- 漏绝对值；把 $\ln(a+b)$ 错写成 $\ln a+\ln b$；积分区间穿过 $0$ 时需分段讨论（否则触及非法的 $\int 1/x$ 瑕点，见 [[Improper Integrals|反常积分]]）。

---

> [!important] 一句话总结
> 见到 $\dfrac{f'}{f}$ 就想到 $\ln|f|$——对数是这类积分的统一出口。
