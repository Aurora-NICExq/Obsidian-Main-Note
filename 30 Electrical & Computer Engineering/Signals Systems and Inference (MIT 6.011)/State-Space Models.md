---
aliases:
  - 状态空间模型
  - State-Space Models
  - 状态方程
  - state-space representation
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[Transforms and Energy Spectra]]"
  - "[[Systems Represented by Differential and Difference Equations]]"
  - "[[Linear Algebra and Differential Equations]]"
  - "[[Eigenvalues and Eigenvectors]]"
  - "[[Stability Reachability and Observability]]"
down:
  - "[[Stability Reachability and Observability]]"
---
# 状态空间模型：$\dot x=Ax+Bu$，$y=Cx+Du$

> [!summary] 核心结论
> **状态** $x(t)\in\mathbb{R}^n$ 是刻画系统未来所需的最小内部记忆。线性时不变（LTI）状态空间
> $$
> \dot x=Ax+Bu,\qquad y=Cx+Du
> $$
> 把高阶微分方程压成一阶向量 ODE；离散时间类比为 $x[k+1]=Ax[k]+Bu[k]$。传递函数 $H(s)=C(sI-A)^{-1}B+D$ 连接输入–输出观点。非线性系统可在工作点**线性化**得局部 $(A,B,C,D)$。后续能达/能观、观测器与状态反馈全建立在这组矩阵上。

> 底本：MIT 6.011（Verghese / Oppenheim）OCW Spring 2018 — state-space 单元；线性代数见 [[Eigenvalues and Eigenvectors]]、[[Linear Algebra and Differential Equations]]。

---
## 1. 为什么要状态空间？

输入–输出（卷积 / 传递函数）擅长频域与稳态；但**多输入多输出、初始条件、内部模态、反馈与估计**时，显式状态更干净：

- 统一处理 MIMO：$B$ 多列、$C$ 多行、$D$ 直通矩阵。
- 初始状态 $x(0)$ 直接进入解；不完全由「零状态响应」掩盖。
- 控制器 / 观测器设计在状态域（极点配置、Luenberger）再映射回实现。

![[ssi-state-space.svg]]

---
## 2. 连续时间 LTI 形式

$$
\begin{aligned}
\dot x(t)&=Ax(t)+Bu(t),\\
y(t)&=Cx(t)+Du(t).
\end{aligned}
$$

| 矩阵 | 尺寸（SISO 时） | 角色 |
|---|---|---|
| $A$ | $n\times n$ | 自由动力学 / 模态 |
| $B$ | $n\times m$ | 输入如何驱动状态 |
| $C$ | $p\times n$ | 状态如何映到输出 |
| $D$ | $p\times m$ | 直通（常为 $0$） |

**零输入解**（$u=0$）：$x(t)=e^{At}x(0)$。若 $A=V\Lambda V^{-1}$，则模态 $e^{\lambda_i t}$ 由特征值决定（见 [[Eigenvalues and Eigenvectors]]）。**渐近稳定**（内部）⇔ 所有 $\mathrm{Re}(\lambda_i(A))<0$（严格条件在下一篇细说）。

**零状态响应**可用卷积 / 状态转移：
$$
x(t)=\int_0^t e^{A(t-\tau)}Bu(\tau)\,d\tau,\quad
y=Cx+Du.
$$

---
## 3. 从高阶标量方程到状态空间

SISO 例：$\ddot y+a_1\dot y+a_0 y=b_0 u$（无输入导数时）。取相变量
$$
x_1=y,\quad x_2=\dot y
$$
得
$$
\dot x=\begin{pmatrix}0&1\\-a_0&-a_1\end{pmatrix}x+\begin{pmatrix}0\\1\end{pmatrix}u,\quad
y=\begin{pmatrix}1&0\end{pmatrix}x.
$$
这是**可控标准型**的雏形；$A$ 的特征多项式即系统特征多项式。有输入导数时需小心选取状态（或用观察者型 / 规范化实现），避免代数回路与隐式微分。

> [!example] RC 电路状态空间
> 串联 $R$、$C$，输入电压 $u$，输出电容电压 $y=v_C$。取 $x=v_C$：
> $$
> \dot x=-\frac{1}{RC}x+\frac{1}{RC}u,\qquad y=x
> $$
> 即 $A=-1/(RC)$，$B=1/(RC)$，$C=1$，$D=0$。令 $R=1\,\mathrm{k}\Omega$，$C=1\,\mu\mathrm{F}$，则 $RC=10^{-3}\,\mathrm{s}$，$A=-1000$。时间常数 $\tau=1\,\mathrm{ms}$；特征值 $\lambda=-1000$ 严格左半平面 ⇒ 渐近稳定。阶跃 $u=5\,\mathrm{V}$ 时稳态 $y\to 5$，瞬态 $x(t)=5+(x_0-5)e^{-1000t}$。

---
## 4. 离散时间类比

采样或天然离散系统：
$$
x[k+1]=A_d x[k]+B_d u[k],\qquad y[k]=C x[k]+D u[k].
$$
连续 LTI 在采样周期 $T_s$ 下（零阶保持直觉）
$$
A_d=e^{A T_s},\qquad B_d=\int_0^{T_s}e^{A\tau}B\,d\tau.
$$
稳定性判据变为：$\lvert\lambda_i(A_d)\rvert<1$（单位圆内）。差分方程实现、数字控制与 Kalman 离散更新都用这套语言；后续课程 [[Estimation and Kalman Filtering (NPTEL) MOC]] 大量使用 DT 状态空间。

---
## 5. 传递函数与实现

对连续 LTI，零状态下
$$
H(s)=C(sI-A)^{-1}B+D.
$$
极点是 $A$ 的特征值（若实现**最小**——能达且能观）；非最小实现可含**隐模态**（下一篇）：极点在 $H(s)$ 中消去，但仍在内部动力学中。

同一 $H(s)$ 有无穷多实现 $(A,B,C,D)$（相似变换 $x=Tz$ 改变坐标但不改输入–输出）。设计时常选可控/可观标准型、平衡实现等。

> [!warning] $H(s)$ 稳定 ≠ 内部一定稳定
> 若存在不稳定但不可观 / 不可达的模态，$H(s)$ 可能看起来「稳定」，内部状态却发散。工程上必须检查 $(A,B)$ 能达与 $(A,C)$ 能观，或直接看 $A$ 的全部特征值。

---
## 6. 线性化（局部 LTI）

非线性 $\dot x=f(x,u)$，$y=g(x,u)$。在平衡点 $(x_e,u_e)$（$f(x_e,u_e)=0$）处令 $\tilde x=x-x_e$，$\tilde u=u-u_e$，
$$
A=\frac{\partial f}{\partial x},\quad
B=\frac{\partial f}{\partial u},\quad
C=\frac{\partial g}{\partial x},\quad
D=\frac{\partial g}{\partial u}
$$
（均在平衡点取值）。小信号行为由该 LTI 近似——倒立摆、晶体管偏置点小信号模型同此逻辑（参见 [[Feedback Example - The Inverted Pendulum]]）。大信号或强非线性时线性化失效。

---
## 7. 仿真与数值直觉

- 连续：ODE 求解器（Runge–Kutta 等）积分 $\dot x=Ax+Bu$。
- 离散：直接迭代 $x\leftarrow Ax+Bu$。
- 脉冲响应矩阵第 $(i,j)$ 元：从输入 $j$ 的冲激到输出 $i$；等于 $C e^{At}B$ 的对应元（$D$ 另计）。

MIMO 时「一个 $H(s)$」变成传递**矩阵**；状态维 $n$ 仍是内部复杂度的主指标。

---
## 8. 自检与参考答案

1. 写出 CT / DT 状态空间标准形式并解释 $A,B,C,D$。
2. 如何从二阶 LCCDE 构造相变量实现？
3. $H(s)$ 与 $(A,B,C,D)$ 的关系？最小实现意味着什么？
4. 采样连续系统时 $A_d$ 如何得到？稳定判据如何变？
5. 线性化在什么条件下可信？

> [!success]- 参考答案
> 1. CT：$\dot x=Ax+Bu,\ y=Cx+Du$；DT：$x^+=Ax+Bu$。$A$ 动力学，$B$ 输入矩阵，$C$ 输出矩阵，$D$ 直通。
> 2. $x_1=y,\ x_2=\dot y$，把最高阶导数用低阶与 $u$ 表示，写入 $\dot x=Ax+Bu$。
> 3. $H=C(sI-A)^{-1}B+D$；最小 ⇒ 能达且能观，极点恰为 $A$ 的全部特征值且无对消。
> 4. $A_d=e^{AT_s}$；稳定 ⇔ $\lvert\lambda(A_d)\rvert<1$。
> 5. 轨迹靠近平衡点、扰动小；大偏离或强非线性时需保留非线性或换工作点。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[Systems Represented by Differential and Difference Equations]]、[[The Laplace Transform]]
