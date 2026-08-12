---
aliases: [不定积分链式求导法则示例, Chain Rule for Variable-Limit Integrals]
tags: [math, calculus]
up: "[[Variable-Limit Integrals and the Leibniz Rule|变限积分]]"
related: "[[Variable-Limit Integrals and the Leibniz Rule|变限积分]], [[Derivative and Integral Formula Tables|导数和积分公式]], [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]"
down: ""
---
# Chain Rule for Variable-Limit Integrals (Worked Example)

> [!summary] 核心结论
> 当变上限积分的上限是 $x$ 的复合函数（如 $x^2$）时，单凭微积分第一基本定理 (FTC I) 不够，必须再叠一层**链式法则 (chain rule)**：先对"上限变量"求导得被积函数，再乘以上限对 $x$ 的导数。

前置知识：[[Variable-Limit Integrals and the Leibniz Rule|变限积分]]（莱布尼茨求导公式）、FTC I（见 [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]）。

---

## 题目 (Problem)

$$\frac{d}{dx}\int_0^{x^2}\tan^{-1}(t^7+3t)\,dt.$$

因为积分上限是 $x^2$ 而非 $x$，不能直接套 FTC I，需要接上链式法则。

---

## 求解 (Solution)

**引入中间变量** $u=x^2$，把积分看成 $u$ 的函数：

$$u=x^2,\qquad y=\int_0^{u}\tan^{-1}(t^7+3t)\,dt.$$

**链式法则**：

$$\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}.$$

**对 $u$ 求导（FTC I）**：上限就是 $u$，直接代入被积函数

$$\frac{dy}{du}=\tan^{-1}(u^7+3u).$$

**对 $x$ 求导**：$\dfrac{du}{dx}=2x$。两者相乘：

$$\frac{dy}{dx}=2x\,\tan^{-1}(u^7+3u).$$

**回代** $u=x^2$：

$$\frac{d}{dx}\int_0^{x^2}\tan^{-1}(t^7+3t)\,dt=2x\,\tan^{-1}\!\big(x^{14}+3x^2\big).$$

> [!tip] 一般公式
> 这正是莱布尼茨公式 $\dfrac{d}{dx}\int_{a}^{\beta(x)}f(t)\,dt=f(\beta(x))\,\beta'(x)$ 的特例（此处 $\beta(x)=x^2$）。完整公式见 [[Variable-Limit Integrals and the Leibniz Rule|变限积分]]。
