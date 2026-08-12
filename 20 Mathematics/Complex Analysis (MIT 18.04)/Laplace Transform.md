---
aliases:
  - 拉普拉斯变换
  - Laplace Transform
  - Bromwich
  - Topic 12 Laplace
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Argument Principle]]"
  - "[[Analytic Continuation and the Gamma Function]]"
  - "[[Continuous-Time Fourier Transform]]"
  - "[[The Laplace Transform]]"
down: []
---
# 拉普拉斯变换

> [!summary] 核心结论
> 单边 Laplace 变换 $F(s)=\int_0^\infty e^{-st}f(t)\,dt$ 在右半平面 $\operatorname{Re}s>a$（ROC）解析。求导/移位/延迟把微分方程变成代数；$G(s)$ 的极点在 LHP $\Leftrightarrow$ LTI 系统（因果）稳定。反演是 Bromwich 积分：对 $t>0$ 向左闭合，
> $$
> f(t)=\sum\operatorname{Res}\!\big(F(s)e^{st}\big).
> $$
> 延迟反馈在特征方程中引入 $e^{-s\tau}$，根的计数可再接 [[Argument Principle]]。

> 底本：MIT 18.04 Topic 12（Jeremy Orloff）。与信号课 [[The Laplace Transform]] 互补：这里强调复平面 / 围道 / 留数。

---
## 1. 定义与收敛域（ROC）

对因果信号（约定 $t<0$ 时 $f=0$），
$$
F(s)=\mathcal{L}\{f\}(s)=\int_0^\infty e^{-st}f(t)\,dt,\qquad s\in\mathbb{C}.
$$

若 $|f(t)|\le Me^{at}$（指数型），则积分在
$$
\operatorname{Re}s>a
$$
**绝对收敛**；该半平面称为收敛域（region of convergence, ROC）。在 ROC 内 $F$ 解析（可在积分号下求导）。

> [!example] $f(t)=e^{\alpha t}$（$t\ge 0$）
> $$
> F(s)=\frac{1}{s-\alpha},\qquad \operatorname{Re}s>\operatorname{Re}\alpha.
> $$

> [!example] $f=1$（单位阶跃）
> $$
> F(s)=\frac{1}{s},\qquad \operatorname{Re}s>0.
> $$

与 [[Continuous-Time Fourier Transform]] 的关系：若 $f$ 在 $t<0$ 为零，则
$$
\hat f(\omega)=\mathcal{L}\{f\}(i\omega)
$$
（当虚轴落在 ROC 内时）。Laplace 是 Fourier 向复频率的延拓。

---
## 2. 基本性质

以下均假设相应变换在公共 ROC 内存在。

| 性质 | 时域 | $s$-域 |
|------|------|--------|
| 线性 | $af+bg$ | $aF+bG$ |
| 微分 | $f'(t)$ | $sF(s)-f(0^-)$ |
| 二阶 | $f''(t)$ | $s^2F-sf(0^-)-f'(0^-)$ |
| $s$-移位 | $e^{at}f(t)$ | $F(s-a)$ |
| 延迟 | $f(t-\tau)u(t-\tau)$ | $e^{-s\tau}F(s)$ |
| 积分 | $\int_0^t f$ | $F(s)/s$ |
| $s$-微分 | $-tf(t)$ | $F'(s)$ |

> [!tip] 为何微分方程变代数
> $\mathcal{L}\{y'''+ay''+\cdots\}=$ 关于 $Y(s)$ 的多项式，初值进入右端。传递函数观点忽略初值（零状态响应）。

### 2.1 常用对（节选）

| $f(t)$（$t\ge 0$） | $F(s)$ | ROC |
|---------------------|--------|-----|
| $1$ | $1/s$ | $\operatorname{Re}s>0$ |
| $t^{n}/n!$ | $1/s^{n+1}$ | $\operatorname{Re}s>0$ |
| $e^{at}$ | $1/(s-a)$ | $\operatorname{Re}s>\operatorname{Re}a$ |
| $\cos\omega t$ | $s/(s^2+\omega^2)$ | $\operatorname{Re}s>0$ |
| $\sin\omega t$ | $\omega/(s^2+\omega^2)$ | $\operatorname{Re}s>0$ |
| $e^{at}\cos\omega t$ | $(s-a)/((s-a)^2+\omega^2)$ | $\operatorname{Re}s>\operatorname{Re}a$ |

幂次与 Gamma 的联系见 [[Analytic Continuation and the Gamma Function]]：$\mathcal{L}\{t^{z-1}\}=\Gamma(z)/s^z$。

---
## 3. 传递函数与稳定性

LTI 系统、输入 $u$、输出 $y$，零状态下
$$
Y(s)=G(s)U(s).
$$
$G(s)$ 称**系统函数 / 传递函数**。对常系数 ODE，$G$ 为有理函数：零点、极点刻画模态。

> [!abstract] 稳定性（因果、有理 $G$）
> BIBO 稳定 $\Leftrightarrow$ $G$ 的全部极点满足 $\operatorname{Re}s<0$（严格在 LHP）。
> 虚轴极点通常对应临界（如无阻尼振荡）；RHP 极点 $\Rightarrow$ 指数发散。

这与 [[Argument Principle]] 中 Nyquist 判据一致：$1+KG$ 的 RHP 零点 = 闭环不稳定模态。

> [!example] $G(s)=\dfrac{1}{s^2+2\zeta\omega_n s+\omega_n^2}$
> 阻尼 $\zeta>0$ 时极点在 LHP；$\zeta=0$ 时在 $\pm i\omega_n$。

---
## 4. Bromwich 反演

逆变换（Bromwich / Fourier–Mellin）：
$$
f(t)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}F(s)e^{st}\,ds,
$$
其中竖线 $\operatorname{Re}s=c$ 落在 ROC 内（全部奇点之右）。

![[ca-bromwich.svg]]

### 4.1 留数计算（$t>0$）

对 $t>0$，$e^{st}$ 在左半平面衰减（$\operatorname{Re}s\to-\infty$）。用大左半圆弧闭合（Jordan 型估计在合理增长条件下成立），得
$$
f(t)=\sum_{\text{poles of }F}\operatorname{Res}\!\big(F(s)e^{st}\big)
\quad(t>0).
$$

对 $t<0$ 向右闭合，若右半无奇点则 $f(t)=0$（与单边约定一致）。

> [!example] $F(s)=\dfrac{1}{s(s+1)}$
> 极点 $0,-1$。对 $t>0$：
> $$
> f(t)=\operatorname{Res}_{0}+\operatorname{Res}_{-1}
> =1+(-e^{-t})=1-e^{-t}.
> $$

> [!example] 复共轭极点
> $F=\omega/((s-a)^2+\omega^2)$ 给出 $e^{at}\sin\omega t$——留数成对，保证 $f$ 为实。

---
## 5. 延迟与反馈（简介）

纯延迟 $\tau>0$：$\mathcal{L}\{f(t-\tau)u(t-\tau)\}=e^{-s\tau}F(s)$。

带延迟的单位反馈，特征方程常呈
$$
1+KG(s)e^{-s\tau}=0
$$
（或等价形式）。这是**超越方程**：RHP 根个数可用辐角原理 / Nyquist（对 $KG(i\omega)e^{-i\omega\tau}$）估计，而不是有理根公式。

> [!warning] 工科提醒
> 延迟使相位随 $\omega$ 线性变负，Nyquist 图更易包围 $-1$。小增益或加补偿是常见对策；分析工具仍是 Topic 11 的绕数。

---
## 6. 自检

1. 写出定义、ROC；由指数型判断收敛半平面。
2. 熟练：微分、$s$-移位、延迟；把 ODE 化为 $Y(s)$。
3. 会用极点位置判因果 LTI 稳定性；会算简单 Bromwich 留数和。
4. 知道延迟反馈如何进入 $e^{-s\tau}$，并链到 Nyquist。

> [!success]- 参考答案
> 1. $F(s)=\int_0^\infty e^{-st}f(t)\,dt$；若 $|f|\le Me^{at}$ 则 ROC 含 $\operatorname{Re}s>a$。
> 2. $\mathcal{L}\{f'\}=sF-f(0)$；$\mathcal{L}\{e^{at}f\}=F(s-a)$；延迟乘 $e^{-s\tau}$。ODE $\to$ 代数方程解 $Y(s)$。
> 3. 因果稳定 $\Leftrightarrow$ 极点全在 LHP。Bromwich：$t>0$ 向左闭合，$f(t)=\sum\operatorname{Res}(F(s)e^{st})$。
> 4. 特征式含 $1+KG(s)e^{-s\tau}$；用辐角原理 / Nyquist 数 RHP 根。

> [!example] 练习：Bromwich 留数
> $F(s)=1/(s(s+1))$。对 $t>0$ 用留数求 $f(t)$。

> [!success]- 练习参考答案
> 极点 $0,-1$：$\operatorname{Res}_0=1$，$\operatorname{Res}_{-1}=-e^{-t}$，故 $f(t)=1-e^{-t}$（与部分分式一致）。

下一讲：[[Analytic Continuation and the Gamma Function]]——$\Gamma$ 与 $\mathcal{L}\{t^{z-1}\}$。

## 参考

- Jeremy Orloff, *18.04 Topic 12: Laplace transform*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
