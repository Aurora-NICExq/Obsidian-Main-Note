---
aliases:
  - 用留数计算定积分
  - Definite Integrals Using Residues
  - Contour Integrals Residues
  - Topic 9 Definite Integrals
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Residue Theorem]]"
  - "[[Taylor and Laurent Series]]"
  - "[[Argument Principle]]"
down: []
---
# 用留数计算定积分

> [!summary] 核心结论
> 实定积分 $\int_{a}^{b}f(x)\,dx$ 的标准套路：选解析延拓 $g(z)$、闭围道、估弧上贡献、用留数定理、取极限还原实积分。半圆在衰减条件（如 $|f|\sim|z|^{-\alpha}$，$\alpha>1$）下贡献 $\to 0$；Fourier 型用上下半平面；$z=e^{i\theta}$ 把三角有理式变单位圆；多值 $x^{\alpha}$ 用钥匙孔；$\sin x/x$ 等用凹陷围道 + 主值。

> 底本：MIT 18.04 Topic 9 / LibreTexts §10（Jeremy Orloff）。

---
## 1. 五步法（万能骨架）

对目标 $\displaystyle\int_{a}^{b}f(x)\,dx$：

1. **选复化** $g(z)$：在实轴上与 $f$ 一致，或密切相关（如 $f=\cos x$ 取 $g=e^{iz}$）。
2. **选闭围道** $C$，使其一段（或极限下一段）覆盖积分区间。
3. **分段估计**：除实轴段外，弧 / 竖边 / 小圆上的积分可算或 $\to 0$。
4. **留数定理**：$\oint_{C}g=2\pi i\sum\operatorname{Res}$（内部）。
5. **拼起来**：解出实轴贡献，必要时取 $R\to\infty$、$r\to 0$、$\varepsilon\to 0$。

失败模式几乎总是：围道选错半平面、衰减不够、忘了支割线、或小圆弧贡献不是 $0$。

> [!warning] 半平面与支割
> Fourier 型 $e^{iaz}$（$a>0$）应在**上**半平面闭合（$\operatorname{Im}z>0$ 时指数衰减）。钥匙孔积分必须先固定 $\arg$ 的支；换支会改跳跃因子 $e^{2\pi i\alpha}$，整条答案翻车。

---
## 2. 半圆与衰减：$|f|\sim R^{-\alpha}$，$\alpha>1$

标准上半圆：$C=[-R,R]\cup\Gamma_{R}$（$\Gamma_R:z=Re^{i\theta}$，$\theta\in[0,\pi]$）。

![[ca-semicircle-contour.svg]]

**Jordan 型估计（工科版）**：若在上半平面大 $|z|$ 上 $|f(z)|\le M/|z|^{\alpha}$ 且 $\alpha>1$，则
$$
\Bigl|\int_{\Gamma_R}f\,dz\Bigr|\le \pi R\cdot\frac{M}{R^{\alpha}}=\pi M R^{1-\alpha}\to 0\quad(R\to\infty).
$$
于是
$$
\int_{-\infty}^{\infty}f(x)\,dx=2\pi i\sum_{\operatorname{Im}z_k>0}\operatorname{Res}(f,z_k)
$$
（若实轴无奇点，且 $f$ 在实轴连续、积分收敛）。

> [!example] $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^{2}+1}=\pi$
> $f(z)=1/(z^{2}+1)$，上半平面仅 $z=i$，单极点，$\operatorname{Res}=1/(2i)$。
> $$
> \int_{-\infty}^{\infty}=2\pi i\cdot\frac{1}{2i}=\pi.
> $$

有理函数 $P/Q$：$\deg Q\ge\deg P+2$ 且实轴无极点时，上述适用。

---
## 3. Fourier 型与矩形围道

目标常为
$$
\int_{-\infty}^{\infty}f(x)\cos(ax)\,dx,\quad
\int_{-\infty}^{\infty}f(x)\sin(ax)\,dx\quad(a>0).
$$
取 $g(z)=f(z)e^{iaz}$（$a>0$ 时在**上**半平面 $|e^{iaz}|=e^{-a\operatorname{Im}z}$ 衰减）。

**Jordan 引理**：若 $f$ 在上半平面大弧上 $|f|\to 0$，则 $\int_{\Gamma_R}f(z)e^{iaz}\,dz\to 0$。

技巧：

- 求 $\int f\cos$：取 $\operatorname{Re}\oint f e^{iz}$。
- 求 $\int f\sin$：取 $\operatorname{Im}$（注意奇偶：$\sin$ 搭配奇/偶 $f$）。
- 若 $a<0$，改闭上半平面。

矩形围道：处理带周期极点的函数（如 $\pi\cot(\pi z)\,f(z)$ 求和），或 $\tanh$、有理乘指数在竖边上相消的情形。竖边长固定、底边 $\to\infty$ 时估计 $|e^{iz}|$。

> [!example] $\displaystyle\int_{-\infty}^{\infty}\frac{\cos x}{x^{2}+1}\,dx=\pi/e$
> $g(z)=e^{iz}/(z^{2}+1)$，上半平面 $\operatorname{Res}_{z=i}=e^{-1}/(2i)$。
> $$
> \oint\to 2\pi i\cdot\frac{e^{-1}}{2i}=\frac{\pi}{e}=\int\frac{\cos x+i\sin x}{x^{2}+1}\,dx.
> $$
> 虚部（奇函数）积分为 $0$，实部即所求。

---
## 4. 单位圆：三角有理积分

对
$$
I=\int_{0}^{2\pi}R(\cos\theta,\sin\theta)\,d\theta
$$
（$R$ 为有理函数），令 $z=e^{i\theta}$，则
$$
\cos\theta=\frac{z+z^{-1}}{2},\quad
\sin\theta=\frac{z-z^{-1}}{2i},\quad
d\theta=\frac{dz}{iz}.
$$
积分变为单位圆 $|z|=1$ 上的围道积分，用留数计算。

> [!example] $\displaystyle\int_{0}^{2\pi}\frac{d\theta}{a+b\cos\theta}$（$a>|b|>0$）
> 代入后得有理函数在单位圆内的留数；答案为 $\dfrac{2\pi}{\sqrt{a^{2}-b^{2}}}$。

检查：分母零点哪些在圆内——通常解二次方程取 $|z|<1$ 的根。

---
## 5. 钥匙孔围道：多值 $x^{\alpha-1}$ 等

处理
$$
\int_{0}^{\infty}x^{\alpha-1}f(x)\,dx
$$
（$0<\alpha<1$ 或使两端收敛的范围），$f$ 有理且在正实轴无极点。$z^{\alpha-1}=e^{(\alpha-1)\operatorname{Log}z}$ 需支割线，常取正实轴。

**钥匙孔（keyhole）**：$C=$ 外大圆 + 上沿割线 + 内小圆 + 下沿割线。

![[ca-keyhole.svg]]

要点：

- 上沿：$\arg=0$，$z^{x}=x^{\alpha-1}$。
- 下沿：$\arg=2\pi$，$z^{\alpha-1}=x^{\alpha-1}e^{2\pi i(\alpha-1)}$，方向相反。
- 内外圆弧在合适 $\alpha$ 与衰减下 $\to 0$。
- $\oint_{C}=2\pi i\sum\operatorname{Res}$（避开正实轴上的支割）。

上下沿相差因子 $(1-e^{2\pi i(\alpha-1)})$，从而解出实积分。

> [!example] 经典型 $\displaystyle\int_{0}^{\infty}\dfrac{x^{\alpha-1}}{1+x}\,dx=\dfrac{\pi}{\sin(\pi\alpha)}$（$0<\alpha<1$）
> 钥匙孔 + $z^{\alpha-1}/(1+z)$ 在 $z=-1$ 的留数。

---
## 6. 凹陷围道与主值：$\sin x/x$

$\operatorname{sinc}$ 积分
$$
\int_{-\infty}^{\infty}\frac{\sin x}{x}\,dx=\pi
$$
不能直接把极点放在实轴上硬套半圆（$z=0$ 在路径上）。标准修法：

1. 考虑 $g(z)=e^{iz}/z$。
2. 围道：大上半圆 + 实轴，但在 $0$ 处用半径 $\varepsilon$ 的**小半圆凹下去**（绕过原点）。
3. $R\to\infty$：大弧由 Jordan 引理 $\to 0$。
4. $\varepsilon\to 0$：小半圆上 $\int g\to -i\pi\operatorname{Res}$（上半小半圆顺时针，贡献 $-\pi i\cdot 1$）。
5. 实轴剩下 Cauchy 主值
   $$
   \operatorname{p.v.}\int_{-\infty}^{\infty}\frac{e^{ix}}{x}\,dx=i\pi
   $$
   （虚部给出 $\int\sin x/x=\pi$；$\cos x/x$ 的主值是 $0$ 的奇延拓意义下需单独说）。

一般规则：若实轴上有单极点，用半径 $\varepsilon$ 的半圆凹陷，贡献 $\to \pm\pi i\times\operatorname{Res}$（符号由绕向决定：上半平面凹陷绕原点是顺时针，取负号）。

**Cauchy 主值**：
$$
\operatorname{p.v.}\int_{-\infty}^{\infty}=\lim_{\varepsilon\to 0^{+}}\Bigl(\int_{-\infty}^{-\varepsilon}+\int_{\varepsilon}^{\infty}\Bigr).
$$
留数方法自然产生主值；绝对收敛的积分则主值 = 常义积分。

---
## 7. 其它常用轮廓（速查）

| 目标类型 | 典型围道 | 注意 |
|----------|----------|------|
| $\int_{-\infty}^{\infty}$ 有理衰减 | 上 / 下半圆 | $\alpha>1$；选含指数衰减的半平面 |
| Fourier / Laplace 反演片段 | 半圆或 Bromwich | 见 Laplace 专题 |
| $0$ 到 $2\pi$ 三角有理 | 单位圆 | $z=e^{i\theta}$ |
| $x^{\alpha}f(x)$、$0\to\infty$ | 钥匙孔 / 扇形 | 支割、$\arg$ 跳跃 |
| 实轴单极点 | 凹陷半圆 | 得主值 $\pm\pi i\operatorname{Res}$ |
| $\int_{0}^{\infty}$ 偶被积 | 扩成 $-\infty\to\infty$ 再半圆 | 先判奇偶 |

扇形围道：对 $e^{-z^{n}}$ 或 $1/(1+z^{n})$ 之类，$n$ 扇形角 $2\pi/n$ 使两边被积函数相差已知相位。

---
## 8. 自检

1. 背熟五步法；先问“弧上是否消失”。
2. $\alpha>1$ 半圆；Fourier 用 $e^{iaz}$ + Jordan。
3. 三角有理 $\to$ 单位圆留数。
4. 钥匙孔处理 $x^{\alpha}$ 与正实支割。
5. 实轴极点 $\to$ 凹陷 + $\operatorname{p.v.}$；$\int\sin x/x=\pi$。

> [!success]- 参考答案
> 1. 复化 → 闭围道 → 估弧 → 留数 → 取极限还原实轴。
> 2. 有理衰减 $\alpha>1$ 大半圆 $\to 0$；$a>0$ 时 $e^{iaz}$ 闭上半平面（Jordan）。
> 3. $z=e^{i\theta}$，$d\theta=dz/(iz)$，有理式变单位圆上有理函数的留数。
> 4. 正实轴支割；大/小圆 $\to 0$ 时，上下沿差出因子 $(1-e^{2\pi i\alpha})$。
> 5. 实轴单极点用半圆凹陷，贡献 $\pm\pi i\operatorname{Res}$；$\operatorname{p.v.}\int_{-\infty}^{\infty}\frac{\sin x}{x}\,dx=\pi$。

> [!example] 练习：选半平面
> 用留数算 $\displaystyle\int_{-\infty}^{\infty}\frac{\cos x}{x^2+1}\,dx$ 时，应取哪个复化、闭上还是下半平面？答案是多少？

> [!success]- 练习参考答案
> 取 $e^{iz}/(z^2+1)$（$a=1>0$）**上**半平面；极点 $i$，留数 $e^{-1}/(2i)$。
> 积分 $=2\pi i\cdot e^{-1}/(2i)=\pi/e$。实部即 $\int\cos x/(x^2+1)\,dx=\pi/e$。

## 参考

- Jeremy Orloff, *18.04 Topic 9: Definite integrals using the residue theorem*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
