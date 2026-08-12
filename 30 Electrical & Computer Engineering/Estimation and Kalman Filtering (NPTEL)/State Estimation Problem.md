---
aliases:
  - 状态估计问题
  - State Estimation Problem
  - 状态空间估计
  - 过程噪声与测量噪声
tags: [ee, estimation_kalman]
up: "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
related:
  - "[[Kalman Filter Derivation]]"
  - "[[Linear MMSE and Innovations]]"
  - "[[Random Processes for Estimation]]"
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
  - "[[Signals and Systems MOC]]"
down:
  - "[[Kalman Filter Derivation]]"
---
# 状态估计问题

> [!summary] 核心结论
> 把待估对象压成有限维**状态** $x_k$，用**过程模型**描述动态、用**测量模型**描述传感器。噪声分为过程噪声 $w_k$（模型不确定 / 未建模输入）与测量噪声 $v_k$。状态估计要在线给出 $\hat x_{k\mid k}$ 或 $\hat x_{k\mid k-1}$ 及不确定度 $P$——线性–高斯下最优解即 Kalman filter。问题提清楚（维数、可观测性、$Q$/$R$ 含义）比套公式更重要。

> 底本：NPTEL 108105059 L17；辅读：MIT 16.322 状态估计表述；交叉 [[Signals Systems and Inference (MIT 6.011) MOC]]。

> 关键词：状态空间、可观测性、$Q$/$R$、先验/后验估计

---

## 1. 为何要状态空间？

FIR / 传递函数描述输入–输出，但对“内部积蓄的能量、位置–速度、偏置”等不便递推。**状态** $x_k\in\mathbb{R}^n$ 是最小充分统计（线性系统）：未来演化与未来输出在已知输入下由 $x_k$ 决定。

离散线性模型（NPTEL / 工程默认）：
$$
\begin{aligned}
x_{k+1}&=F_k x_k+G_k u_k+w_k,\\
y_k&=H_k x_k+v_k.
\end{aligned}
$$
$u_k$ 已知控制 / 激励；$w_k,v_k$ 随机。连续时间 $\dot x=Ax+Bu+w$ 采样或离散化后进入同一框架（16.322 更强调连续）。

![[ekf-kf-cycle.svg]]

---

## 2. 噪声假设（标准 KF）

常用：
$$
\mathbb{E}[w_k]=0,\quad\mathbb{E}[v_k]=0,\quad
\mathbb{E}[w_k w_j^\mathsf{T}]=Q_k\delta_{kj},\quad
\mathbb{E}[v_k v_j^\mathsf{T}]=R_k\delta_{kj},
$$
且 $w$ 与 $v$ 互不相关、与初始 $x_0$ 不相关。$x_0$ 有先验均值 $\hat x_{0\mid-1}$（或 $\hat x_0$）与协方差 $P_{0\mid-1}$。

> [!warning] $Q$ 与 $R$ 不是“调参旋钮”的全部故事
> 它们应反映**真实**模型误差与传感器噪声。乱调虽能“看起来跟得上”，但 $P$ 失去概率意义，新息白化检验会失败。见 [[Kalman Filter Properties and Steady State]] 与应用篇。

---

## 3. 估计量的时间标记

| 符号 | 含义 |
|------|------|
| $\hat x_{k\mid k-1}$ | 用到 $y_{0:k-1}$ 的预测（先验） |
| $\hat x_{k\mid k}$ | 用到 $y_{0:k}$ 的滤波（后验） |
| $\hat x_{k\mid N}$（$N>k$） | 平滑 |

协方差 $P_{k\mid k-1}$、$P_{k\mid k}$ 同理。口语“先验 / 后验”在 KF 里指测量更新前后，与贝叶斯 [[Bayesian Inference|先验/后验]] 一致（线性高斯时 $P$ 即后验协方差）。

---

## 4. 目标：最小化误差协方差

在线性估计类中，找 $\hat x$ 使误差协方差矩阵在 Löwner 序下最小（或最小化任意 $\mathbb{E}[\tilde x^\mathsf{T}W\tilde x]$，$W\succeq 0$）。正交原理 + 状态空间递推 → Kalman。高斯时即条件均值与条件协方差的递推。

---

## 5. 可观测性与可估计性直觉

若存在有限步测量使初始状态可唯一重建（确定性意义），系统**可观测**。噪声下改为：信息矩阵随时间积累是否使 $P$ 有界。不可观测模态上 $P$ 会漂移或由 $Q$ 灌入的不确定度无法被 $y$ 压下——设计传感器 / 选状态时先查可观测性。

简单判别（LTI）：$\mathcal{O}=[H^\mathsf{T},(HF)^\mathsf{T},\ldots,(HF^{n-1})^\mathsf{T}]^\mathsf{T}$ 列满秩。

> [!example] 常值偏置不可观
> 状态 $[p,b]$（位置、传感器常值偏置），测量 $y=p+b+v$。差 $p$ 与 $b$ 无法从单次测量分开；若无过程模型区分二者（如偏置几乎恒定、位置在动），需运动激励或额外测量，否则 $P$ 在“和”方向可缩、“差”方向不可缩。

---

## 6. 过程噪声 vs 测量噪声：建模语言

| | 过程 $Q$ | 测量 $R$ |
|--|----------|-----------|
| 物理 | 未建模力、机动、参数漂移 | 传感器电子噪声、量化 |
| 过大 | 更信测量，增益大，跟得猛、抖 | 更信模型，平滑、滞后 |
| 过小 | 过度平滑，模型错时固执 | 过度跟随野值 |

随机游走偏置：$b_{k+1}=b_k+w_b$，小 $Q_b$ 表示“几乎恒定但允许慢漂”。

---

## 7. 与 I/O 最优滤波的边界

Wiener 要平稳与充分相关统计；状态空间 KF：

- 允许时变 $F_k,H_k,Q_k,R_k$；
- 自然处理多输入多输出、已知 $u_k$；
- 给出全程 $P_k$（不确定度）；
- 易扩展相关噪声（状态增广）。

代价：必须写出合理状态模型——辨识与物理建模进入 [[System Identification and Recursive Least Squares]]。

---

## 8. 离散化直觉

连续 $\dot x=Ax+Bu+w_c$ 以周期 $T$ 采样时，无噪声名义
$$
F=e^{AT},\qquad G=\int_0^T e^{A\tau}B\,\mathrm{d}\tau.
$$
过程噪声离散 $Q$ 由连续谱密度 $Q_c$ 积分得到（非简单 $Q_c T$，除非粗糙近似）。$T$ 过大：线性化 / 离散模型失真；$T$ 过小：算量升、量化相对更显眼。

---

## 9. 相关噪声与增广

若 $v_k$ 由白噪声经着色滤波器产生，标准白 $R$ 假设失败。标准补救：**状态增广**——把着色滤波器状态并入 $x$，使增广测量噪声再近白。过程有色同理。代价是维数上升与可观测性变化。

---

## 10. 问题陈述清单（开写 KF 前）

1. 状态含义与单位；离散化步长。
2. $F,G,H$（或非线性 $f,h$ → EKF）。
3. $Q,R$ 来源（数据表、残差方差、调参 + 一致性检验）。
4. 初值 $\hat x_0,P_0$。
5. 任务是滤波、预测还是平滑？实时约束？
6. 测量是否延迟 / 异步？噪声是否近似白？

---

## 11. 自检与参考答案

1. 写出标准离散线性状态空间与噪声二阶假设。
2. 区分 $\hat x_{k\mid k-1}$ 与 $\hat x_{k\mid k}$。
3. 可观测性对 $P_k$ 行为意味着什么？
4. 增大 $Q$ 通常如何影响 Kalman 增益直觉？
5. 为何说 KF 问题“先建模、后公式”？
6. 测量噪声有色时标准补救是什么？

> [!success]- 参考答案
> 1. $x_{k+1}=Fx_k+Gu_k+w_k$，$y_k=Hx_k+v_k$；零均值、$Q$/$R$ 白、互不相关等。
> 2. 前者预测（未用 $y_k$），后者滤波更新后。
> 3. 不可观方向上测量不降不确定度，$P$ 可能无界或依赖 $Q$ 灌入。
> 4. 预测 $P^-$ 更大 → 增益 $K$ 往往更大 → 更跟测量。
> 5. $F,H,Q,R$ 定义了“最优”相对的世界；模型错则“最优滤波器”最优地错。
> 6. 状态增广：把着色滤波器状态并入，使增广后噪声近白。

## 参考

- NPTEL 108105059 L17
- MIT OCW 16.322 Stochastic Estimation and Control（状态估计导论讲次）
- Grewal & Andrews，《Kalman Filtering》建模章节
