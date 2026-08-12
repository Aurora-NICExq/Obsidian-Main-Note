---
aliases:
  - 稳定性能达性可观测性
  - Stability Reachability and Observability
  - 能控能观
  - controllability observability
  - PBH test
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[State-Space Models]]"
  - "[[Eigenvalues and Eigenvectors]]"
  - "[[Observers for State Estimation]]"
  - "[[State Feedback and Observer-Based Control]]"
down:
  - "[[Observers for State Estimation]]"
---
# 稳定性、能达性与可观测性

> [!summary] 核心结论
> **内部（渐近）稳定**：自由响应 $e^{At}x_0\to 0$（CT：$\mathrm{Re}\,\lambda(A)<0$；DT：$\lvert\lambda(A)\rvert<1$）。**BIBO 稳定**看输入–输出，对最小实现与内部稳定一致，否则可能被隐模态欺骗。**能达（能控）**：输入能否在有限时间把状态从 $0$ 驱动到任意 $x^*$——秩判据 $\mathrm{rank}\,\mathcal{C}=n$，$\mathcal{C}=[B\ AB\ \cdots\ A^{n-1}B]$。**能观**：能否从 $y$（及已知 $u$）唯一重建 $x_0$——$\mathrm{rank}\,\mathcal{O}=n$，$\mathcal{O}=[C^\top\ (CA)^\top\ \cdots]^\top$。**PBH 检验**用特征向量给出等价条件。不能达 / 不能观的模态是**隐模态**，状态反馈或输出反馈可能碰不到它们。

> 底本：MIT 6.011 OCW Spring 2018 — stability / reachability / observability；矩阵秩与特征见 [[Eigenvalues and Eigenvectors]]。

---
## 1. 两类稳定性

### 1.1 内部渐近稳定
$u\equiv 0$ 时，对任意 $x(0)$，$x(t)\to 0$（CT）或 $x[k]\to 0$（DT）。对 LTI：看 $A$ 的谱。

| 时间 | 渐近稳定充要（LTI） |
|---|---|
| 连续 | 所有特征值满足 $\mathrm{Re}(\lambda_i)<0$ |
| 离散 | 所有 $\lvert\lambda_i\rvert<1$ |

边缘：纯虚轴 / 单位圆上的简单特征值 ⇒ Lyapunov 意义下可能临界稳定（不发散也不趋零），工程上常不够。

### 1.2 BIBO 稳定
任意有界输入 ⇒ 有界输出。对卷积系统：$\int\lvert h\rvert<\infty$（CT）或 $\sum\lvert h\rvert<\infty$（DT）。对**能达且能观**的实现，BIBO ⇔ 内部稳定。若存在不稳定但不能观的模态，输出可有界而状态爆炸。

> [!warning] 「传递函数稳定」的陷阱
> 只看 $H(s)$ 极点在左半平面不够：对消掉的右半平面极点仍可在状态方程中。务必对 $A$ 做特征值检查，或先验证最小性。

---
## 2. 能达性（Reachability / Controllability）

对 CT LTI，在区间 $[0,T]$ 内，是否存在输入使 $x(0)=0\mapsto x(T)=x^*$ 对任意 $x^*$？等价于**能控性矩阵**满秩：
$$
\mathcal{C}=\bigl[B\ \ AB\ \ A^2B\ \ \cdots\ \ A^{n-1}B\bigr],\qquad
\mathrm{rank}\,\mathcal{C}=n.
$$
（多输入时 $B$ 有 $m$ 列，$\mathcal{C}$ 为 $n\times nm$。）DT 形式相同（一步推进的代数结构类似）。

直觉：Kalman 秩条件说「$B$ 及其在 $A$ 反复作用下扫出的方向」必须张成整个 $\mathbb{R}^n$。若某不变子空间永远碰不到输入，该子空间内的模态不可控。

---
## 3. 可观测性（Observability）

已知 $u(\cdot)$ 与 $y(\cdot)$ 在 $[0,T]$ 上，能否唯一确定 $x(0)$？能观性矩阵
$$
\mathcal{O}=\begin{pmatrix}C\\CA\\CA^2\\\vdots\\CA^{n-1}\end{pmatrix},\qquad
\mathrm{rank}\,\mathcal{O}=n.
$$
对偶：$(\mathcal{A},\mathcal{B})$ 能达 ⇔ $(\mathcal{A}^\top,\mathcal{B}^\top)$ 能观（尺寸对应时）。不能观 ⇒ 存在非零状态产生零输出（在 $u=0$ 时），该方向对测量「隐身」。

---
## 4. PBH 检验（Popov–Belevitch–Hautus）

对每个特征值 $\lambda$（或每个复数 $s$）：

- **能达**：$\mathrm{rank}\,[sI-A\ \ B]=n$ 对所有 $s$（尤其 $s=\lambda_i(A)$）。
- **能观**：$\mathrm{rank}\,\begin{bmatrix}sI-A\\C\end{bmatrix}=n$ 对所有 $s$。

等价说法：不存在 $A$ 的左特征向量 $w^\top\neq 0$ 使 $w^\top B=0$（否则该模态不受输入）；不存在右特征向量 $v\neq 0$ 使 $Cv=0$（否则该模态在输出中消失）。

PBH 对「哪个模态坏了」更直观，也便于符号计算与低维手算。

> [!example] 二阶手算：能达与能观
> 取
> $$
> A=\begin{pmatrix}0&1\\0&-2\end{pmatrix},\quad
> B=\begin{pmatrix}0\\1\end{pmatrix},\quad
> C=\begin{pmatrix}1&0\end{pmatrix}.
> $$
> $\mathcal{C}=[B\ AB]=\begin{pmatrix}0&1\\1&-2\end{pmatrix}$，$\det=-1\neq 0$ ⇒ 能达。
> $\mathcal{O}=\begin{pmatrix}C\\CA\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ 满秩 ⇒ 能观。
>
> 若改 $C=\begin{pmatrix}0&1\end{pmatrix}$，则 $\mathcal{O}=\begin{pmatrix}0&1\\0&-2\end{pmatrix}$，秩 $1<2$，不能观。PBH：$\lambda=0$ 时特征向量 $v=(1,0)^\top$，$Cv=0$，正是「位置积分模态」若只测速度则看不见初始位置（在此结构下）。（具体模态解释随 realization 而变，但秩亏的事实明确。）

---
## 5. 隐模态与传递函数对消

若系统不能达或不能观，存在坐标使 $A$ 分块，传递函数只反映能达且能观的子系统。$H(s)$ 中的零极点对消对应被消去的内部模态——**隐模态**：

- 不稳定隐模态：灾难性（内部发散、输出仍可「看起来 OK」）。
- 稳定隐模态：输入–输出 OK，但状态估计 / 故障诊断可能仍需看见它们。

状态反馈 $u=-Kx$ **只能搬动能达模态**的特征值；观测器增益 $L$ **只能配置能观模态**相关的误差极点。这解释了下一篇与再下一篇设计前提：先检验秩 / PBH。

---
## 6. 与 BIBO、最小实现的关系

- **最小实现**：能达 + 能观；状态维 = McMillan 度 = $H(s)$ 的本质阶次。
- 最小实现下：内部渐近稳定 ⇔ BIBO 稳定。
- 非最小：必须分开讨论内部谱与 $H$ 的极点。

工程清单：建模 → 线性化 → 查 $\mathrm{rank}\,\mathcal{C}$、$\mathrm{rank}\,\mathcal{O}$ → 再谈极点配置与观测器。

---
## 7. 能稳与能检测（设计用弱化条件）

若目标只是**镇定**而非任意极点配置：

- **能稳（stabilizable）**：不能达模态本身已渐近稳定——存在 $K$ 使 $A-BK$ 稳定。
- **能检测（detectable）**：不能观模态已稳定——存在 $L$ 使 $A-LC$ 稳定。

PBH 版本：对所有 $\mathrm{Re}(s)\ge 0$（CT）检查秩条件即可，而不必对稳定半平面的每个 $s$。LQR / Kalman 存在性常用这对弱条件。6.011 先抓满秩能达/能观；弱化条件在最优控制课再现。

---
## 8. 自检与参考答案

1. 写出 CT / DT 内部渐近稳定的特征值条件。
2. 能达性矩阵与能观性矩阵的定义与满秩条件。
3. 陈述 PBH 能达与能观判据。
4. 何为隐模态？对反馈设计有何限制？
5. 为何「$H(s)$ 稳定」不足以保证内部稳定？

> [!success]- 参考答案
> 1. CT：$\mathrm{Re}\,\lambda(A)<0$；DT：$\lvert\lambda(A)\rvert<1$。
> 2. $\mathcal{C}=[B\ AB\ \cdots\ A^{n-1}B]$，$\mathrm{rank}=n$；$\mathcal{O}$ 堆叠 $C,CA,\ldots$，秩 $n$。
> 3. 对一切 $s$：$\mathrm{rank}[sI-A\ B]=n$；$\mathrm{rank}\begin{bmatrix}sI-A\\C\end{bmatrix}=n$。
> 4. 不能达或不能观的内部模态；状态反馈搬不动不能达极点，观测器「看不见」不能观方向。
> 5. 不稳定模态可能被零极点对消而不出现在 $H(s)$，但仍在 $A$ 中。

---
## 附录补充：相似变换下的不变性

$x=Tz$（$T$ 可逆）⇒ $\bar A=T^{-1}AT$，$\bar B=T^{-1}B$，$\bar C=CT$。能达/能观性、特征值、传递函数均不变；能控矩阵变为 $T^{-1}\mathcal{C}$，秩不变。因此「选坐标」不创造或消灭能达性——检验可在任意方便实现（可控标准型、对角模态坐标）上进行。对角坐标下 PBH 尤其透明：看 $B$ 的行是否在某模态上为零。

---
## 9. 数值秩与条件数

手算 $\det\mathcal{C}\neq 0$ 在低维清晰；高维浮点下应用数值秩（奇异值阈值）。$\mathcal{C}$ 条件数极大 ⇒ 「理论上能达、实际上几乎不能达」：需要巨大输入能量才能激发弱方向，执行器饱和后等价失去能达性。平衡实现 / 可控 Gramian 特征值刻画各方向「能达难度」，与后续模型降阶相通。

对偶地，能观 Gramian 小特征值方向对输出贡献弱，观测器需要大增益才看得见——再次与噪声放大权衡挂钩。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[State-Space Models]]、[[Observers for State Estimation]]
