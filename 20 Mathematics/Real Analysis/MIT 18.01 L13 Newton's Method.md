---
aliases: [MIT18.1-Lec13-牛顿法（Newton's Method）, 牛顿法, Newton's Method]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L09 Linear and Quadratic Approximations]], [[MIT 18.01 L14 Mean Value Theorem]]"
down: "[[MIT 18.01 L14 Mean Value Theorem]]"
---
# Newton's Method

> [!summary] 核心结论
> 牛顿法 (Newton's method) 用**切线的零点**迭代逼近方程 $f(x)=0$ 的根。在根附近且 $f'(r)\neq0$ 时通常二次收敛 (quadratic convergence)。

> 关键词：求根、切线迭代、收敛、初值、停止条件。

---

## 1. 迭代公式 (Iteration)

$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}.$$

> [!note] 公式来历
> 在 $x_n$ 处作线性近似 $f(x)\approx f(x_n)+f'(x_n)(x-x_n)$（见 [[MIT 18.01 L09 Linear and Quadratic Approximations]]），令其为 $0$ 解出 $x$，即得迭代式——下一步就是切线与 $x$ 轴的交点。

## 2. 几何解释 (Geometry)

用 $x_n$ 处切线近似曲线，取切线与 $x$ 轴交点作为下一个近似值。

## 3. 收敛直觉 (Convergence)

根附近且 $f'(r)\neq0$ 时收敛极快（典型二次收敛）。失败信号：$f'(x_n)\approx0$，或迭代跳出合理区间。

## 4. 例题 (Examples)

- $\sqrt2$：$f(x)=x^2-2$，得 $x_{n+1}=\tfrac12\big(x_n+\tfrac{2}{x_n}\big)$（即"巴比伦法"）；
- 解 $x=\cos x$：取 $f(x)=x-\cos x$ 按公式迭代。

## 5. 易错点 (Pitfalls)

- 停止条件只看 $|x_{n+1}-x_n|$ 而不看 $|f(x_n)|$；忽略初值选择导致发散。

---

> [!important] 一句话总结
> 牛顿法 = 反复"作切线、取零点"，是线性近似思想的迭代化。
