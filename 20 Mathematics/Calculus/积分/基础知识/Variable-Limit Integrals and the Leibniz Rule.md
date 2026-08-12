---
aliases: [变限积分, Variable-Limit Integrals, Leibniz Rule]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Definite Integrals and the Fundamental Theorem of Calculus|定积分]], [[Chain Rule for Variable-Limit Integrals (Worked Example)|不定积分链式求导法则示例]], [[Improper Integrals|反常积分]]"
down: "[[Chain Rule for Variable-Limit Integrals (Worked Example)|不定积分链式求导法则示例]]"
---
# Variable-Limit Integrals and the Leibniz Rule

> [!summary] 核心结论
> 变限积分 (variable-limit integral) 把积分上下限设为 $x$ 的函数，其求导核心是"将积分问题转化为微分问题"：对上限代入被积函数并乘上限的导数，对下限同样处理后相减——这就是莱布尼茨求导公式 (Leibniz integral rule)。

前置知识：[[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]（微积分第一基本定理）、[[Total Differential and the Chain Rule|微分、链式法则]]。

---

## 1. 莱布尼茨求导公式 (Leibniz Rule)

设 $f$ 连续，上下限 $\alpha(x),\beta(x)$ 可导，则

$$\frac{d}{dx}\int_{\alpha(x)}^{\beta(x)} f(t)\,dt=f\big(\beta(x)\big)\,\beta'(x)-f\big(\alpha(x)\big)\,\alpha'(x).$$

它由微积分第一基本定理 (FTC I) 加链式法则推出：令 $\Phi(u)=\int_{c}^{u}f$，则原式 $=\Phi(\beta)-\Phi(\alpha)$，两边对 $x$ 求导，$\Phi'=f$，即得上式。

> [!warning] 易错点
> 被积函数 $f(t)$ 中**不能含有 $x$**。若含 $x$，必须先把它"移出"积分号（提到积分外或换元），否则公式不成立。

---

## 2. 与洛必达法则联用 (With L'Hôpital's Rule)

变限积分常作为分子出现在 $\frac{0}{0}$ 型极限里：

$$\lim_{x\to 0}\frac{\displaystyle\int_0^x f(t)\,dt}{g(x)}.$$

**解题思路：**

1. **判断型**：验证 $x\to 0$ 时分子分母是否同趋于 $0$（积分上限趋于下限时 $\int_0^x f\to 0$）。
2. **先化简**：若有非积分因式，先用等价无穷小 (equivalent infinitesimal) 代换，如 $x\sim\sin x$。
3. **求导消积分**：对分子用 Leibniz 公式（此处 $\frac{d}{dx}\int_0^x f=f(x)$），对分母求导，消去积分号后再求极限。

具体的链式法则代入示例见 [[Chain Rule for Variable-Limit Integrals (Worked Example)|不定积分链式求导法则示例]]；当积分限趋于无穷或被积函数无界时，转入 [[Improper Integrals|反常积分]] 的讨论。
