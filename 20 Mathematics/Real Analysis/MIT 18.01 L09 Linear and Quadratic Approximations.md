---
aliases: [MIT18.1-Lec09-线性与二次近似（Approximations）, 线性与二次近似, Linear and Quadratic Approximations]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L03 Derivatives]], [[MIT 18.01 L10 Curve Sketching]], [[MIT 18.01 L15 Differentials and Antiderivatives]]"
down: "[[MIT 18.01 L10 Curve Sketching]]"
---
# Linear and Quadratic Approximations

> [!summary] 核心结论
> 线性近似 (linear approximation) 用切线抓住**一阶变化**；二次近似 (quadratic approximation) 再加入**曲率 (curvature)** 信息。它们是泰勒多项式 (Taylor polynomial) 的低阶情形，误差量级由下一阶导数控制。

> 关键词：线性化、微分、二次近似（Taylor 二阶）、误差阶。

---

## 1. 线性近似（切线近似, Tangent-Line）

在 $x=a$ 附近：$f(x)\approx f(a)+f'(a)(x-a)$——把曲线在局部"当成直线"（即 [[MIT 18.01 L03 Derivatives|导数]] 给出的切线）。

## 2. 微分记号 (Differentials)

令 $dx=x-a$，定义 $dy=f'(a)\,dx$；当 $dx$ 很小时 $\Delta y\approx dy$（详见 [[MIT 18.01 L15 Differentials and Antiderivatives]]）。

## 3. 误差阶 (Error Order)

若 $f$ 二阶可导，由带拉格朗日余项的泰勒公式

$$f(a+h)=f(a)+f'(a)h+\tfrac12 f''(c)\,h^2,\quad c\in(a,a+h),$$

故线性近似误差量级为 $O(h^2)$——这解释了"为何近似在小范围内可靠"。

## 4. 二次近似 (Quadratic / 2nd-order Taylor)

$$f(x)\approx f(a)+f'(a)(x-a)+\tfrac12 f''(a)(x-a)^2.$$

## 5. 常用展开（$a=0$, Maclaurin）

$\sin x\approx x-\tfrac{x^3}{6}$，$\cos x\approx 1-\tfrac{x^2}{2}$，$e^x\approx 1+x+\tfrac{x^2}{2}$。

## 6. 典型例题 (Examples)

- $\sqrt{1.02}$：$f(x)=\sqrt x,a=1$，线性得 $\approx 1+\tfrac12(0.02)=1.01$；
- $\cos(0.1)\approx 1-\tfrac{0.01}{2}=0.995$。

## 7. 易错点 (Pitfalls)

- 小角近似默认弧度制；离 $a$ 太远误差放大；二次项系数 $\tfrac12$ 漏掉。

---

> [!important] 一句话总结
> 线性近似抓一阶斜率，二次近似补曲率——都是泰勒展开的截断，误差由更高阶导数控制。
