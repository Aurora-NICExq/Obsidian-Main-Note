---
aliases: [MIT18.1-Lec04-链式法则（Chain Rule）, 链式法则, Chain Rule]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L03 Derivatives]], [[MIT 18.01 L05 Implicit Differentiation]]"
down: "[[MIT 18.01 L05 Implicit Differentiation]]"
---
# Chain Rule

> [!summary] 核心结论
> 链式法则 (chain rule) 处理**复合函数 (composite function)** 求导：先识别内外层，再把外层变化率乘以内层变化率——"外导乘内导"。

> 关键词：复合函数、外导乘内导、多层链式、结构识别。

---

## 1. 核心公式 (The Formula)

若 $y=f(u)$、$u=g(x)$，则

$$\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}=f'(g(x))\,g'(x).$$

> [!note] 直觉
> 用莱布尼茨记号写成 $\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}$，形式上像"$du$ 约分"。严格地，它来自差商 $\frac{\Delta y}{\Delta x}=\frac{\Delta y}{\Delta u}\cdot\frac{\Delta u}{\Delta x}$ 在 $\Delta x\to0$（从而 $\Delta u\to0$）时的极限。

## 2. 结构识别 (Identify the Layers)

比背公式更重要：从**外到内**分层，最外层运算决定第一步；多层复合则每层都乘上对应导数。

## 3. 常见模板 (Templates)

$(u^n)'=nu^{n-1}u'$，$(\sin u)'=\cos u\,u'$，$(\cos u)'=-\sin u\,u'$。

## 4. 典型例题 (Examples)

- 幂复合：$\dfrac{d}{dx}(1+x^3)^5=5(1+x^3)^4\cdot 3x^2$；
- 三角复合：$\dfrac{d}{dx}\sin(x^2)=\cos(x^2)\cdot 2x$；
- 多层复合：$\dfrac{d}{dx}\cos(\sqrt{1+x})=-\sin(\sqrt{1+x})\cdot\dfrac{1}{2\sqrt{1+x}}$。

## 5. 易错点 (Pitfalls)

- 漏掉最里层导数；括号少写导致层级判断错。

---

> [!important] 一句话总结
> 链式法则 = 外层变化率 × 内层变化率，是 [[MIT 18.01 L05 Implicit Differentiation|隐函数求导]] 的基础。
