---
aliases:
  - 最小二乘与最优滤波器
  - Least Squares
  - Optimal Filters
  - Wiener Filter
  - 维纳滤波
tags: [ee, estimation_kalman]
up: "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
related:
  - "[[Linear MMSE and Innovations]]"
  - "[[Adaptive Filters]]"
  - "[[System Identification and Recursive Least Squares]]"
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
  - "[[Signals and Systems MOC]]"
  - "[[Linear Regression]]"
down:
  - "[[Adaptive Filters]]"
---
# 最小二乘与最优滤波器

> [!summary] 核心结论
> **最小二乘（LS）** 在确定性 / 有限数据上拟合参数或波形；随机设定下，二阶最优的线性滤波器满足 **Wiener–Hopf** 方程。因果约束导向 IIR / 谱分解实现；非因果 Wiener 在频域为 $H(j\omega)=S_{xy}/S_y$。LS、LMMSE、Wiener、Kalman 是同一投影思想在不同约束（批 / 因果 / 状态空间）下的面孔。

> 底本：NPTEL 108105059 L15；交叉：[[Linear Regression]]、[[Signals Systems and Inference (MIT 6.011) MOC]]。

> 关键词：LS、法方程、Wiener–Hopf、因果最优、谱因式分解

---

## 1. 线性最小二乘

模型 $y=\Phi\theta+e$（回归）或滤波形式 $y[n]=\sum_{i=0}^{M-1}w_i u[n-i]+e[n]$。给定数据，最小化
$$
J(\theta)=\lVert y-\Phi\theta\rvert_2^2.
$$
法方程：$\Phi^\mathsf{T}\Phi\,\hat\theta=\Phi^\mathsf{T}y$（满秩时 $\hat\theta=(\Phi^\mathsf{T}\Phi)^{-1}\Phi^\mathsf{T}y$）。加权 LS 用 $W$ 正定：$\Phi^\mathsf{T}W\Phi$。

与 [[Linear Regression|线性回归]] / 投影几何相同：$\hat y$ 是 $y$ 在 $\mathrm{col}(\Phi)$ 上的投影。

> [!example] 两参数批 LS
> $y=\begin{bmatrix}1\\2\\2\end{bmatrix}$，$\Phi=\begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix}$。
> $$
> \Phi^\mathsf{T}\Phi=\begin{bmatrix}3&3\\3&5\end{bmatrix},\quad
> \Phi^\mathsf{T}y=\begin{bmatrix}5\\6\end{bmatrix},\quad
> \hat\theta=\begin{bmatrix}7/6\\1/2\end{bmatrix}.
> $$
> 残差 $e=y-\Phi\hat\theta$ 正交于 $\Phi$ 的列——离散版正交原理。

---

## 2. LS 与随机 LMMSE 的联系

若把 $e$ 当白噪声、$\theta$ 当未知常值，LS 是 BLUE / MLE（高斯）的经典结果。若 $\theta$ 本身随机且已知先验二阶矩，**贝叶斯线性估计 / 正则化 LS**（ridge）把先验并入：相当于增大“测量”维度。Kalman 可视为时变、带过程噪声的递推正则化。

---

## 3. Wiener 滤波（非因果素描）

平稳：$x$ 待估，$y$ 观测，联合 WSS。找时不变 $h$ 使 $\mathbb{E}[(x[n]-h*y[n])^2]$ 最小。频域解（非因果、可双无限）：
$$
H(j\omega)=\frac{S_{xy}(j\omega)}{S_y(j\omega)}.
$$
与标量 LMMSE 增益 $R_{xy}/R_y$ 同形，只是“每个频率各自加权”。

---

## 4. 因果约束与最优 IIR

实时系统要求 $h[n]=0$（$n<0$）。Wiener–Hopf 积分 / 求和方程在因果半轴上成立；求解常用：

1. **谱因式分解** $S_y=S_y^+S_y^-$（最小相位因子）；
2. 预白化 → 因果截断 → 成形。

结果一般是 **IIR**（有理谱时），不是任意 FIR。FIR 截断是工程近似；自适应 LMS 常直接训 FIR（[[Adaptive Filters]]）。

> [!tip] Kalman ↔ Wiener
> 时不变线性–高斯状态空间、时间 $\to\infty$ 时，稳态 Kalman 增益实现的滤波器与因果 Wiener 一致（同一 LMMSE）。KF 还覆盖瞬态与时变模型——见 [[Kalman Filter Properties and Steady State]]。

---

## 5. 最优滤波、平滑、预测

| 任务 | 要用的数据相对待估时刻 |
|------|------------------------|
| 滤波 | 到当前 |
| 预测 | 仅过去（外推） |
| 平滑 | 含未来（非实时） |

Wiener / KF 都可表述这三类；平滑误差通常更小（多信息）。NPTEL 本讲次强调滤波最优结构；应用里 RTS 平滑等是 KF 家族扩展。

---

## 6. 从批 LS 到递推

新数据到达时，重算 $(\Phi^\mathsf{T}\Phi)^{-1}$ 昂贵 → **RLS**（[[System Identification and Recursive Least Squares]]）用矩阵求逆引理递推；自适应滤波用随机梯度（LMS）近似。LS 是“离线真值”，递推是“在线近似 / 精确递推”。

---

## 7. 加权与正则化

若误差协方差已知为 $\mathbb{E}[ee^\mathsf{T}]=V$，加权 LS 用 $W=V^{-1}$ 得 BLUE。测量异方差 / 相关时不应普通 LS。  
**岭回归**：$(\Phi^\mathsf{T}\Phi+\lambda I)\hat\theta=\Phi^\mathsf{T}y$，等价于 $\theta$ 上加零均值先验方差 $\propto 1/\lambda$——通向贝叶斯线性估计与 KF 的先验 $P_0$。

---

## 8. FIR 近似因果 Wiener

实践中常截断为长度 $M$ 的 FIR，用相关法或 LS 估抽头：
$$
R_u \hat w = r_{ud},
$$
$R_u$ 为输入相关 Toeplitz，$r_{ud}$ 为互相关。$M$ 不足则偏差，$M$ 过大则方差与病态。自适应 LMS 正是在线解此方程（[[Adaptive Filters]]）。

> [!example] 标量“单抽头 Wiener”
> 零均值，$R_u=2$，$r_{ud}=1$ ⇒ $\hat w=1/2$。估计误差方差 $R_d-r_{ud}^2/R_u$（若 $R_d=1$ 则为 $1-0.5=0.5$）。与 LMMSE 标量例同构。

---

## 9. 陷阱

> [!warning] 法方程病态
> $\Phi^\mathsf{T}\Phi$ 接近奇异（共线回归元、过长 FIR + 窄带输入）→ $\hat\theta$ 方差爆炸。正则化、降阶、更好激励信号是辨识常规手段。

> [!warning] 非因果公式不能直接实时用
> $S_{xy}/S_y$ 对应的冲激响应通常双边。因果化必须做谱分解或改用 KF，不能只把负时间系数扔掉了事（除非碰巧已经近似因果）。

---

## 10. 自检与参考答案

1. 写出线性 LS 法方程；解释“残差 ⊥ 列空间”。
2. 非因果 Wiener 频域公式是什么？各符号含义？
3. 为何因果最优滤波常常是 IIR？
4. LS、LMMSE、稳态 KF 如何一句话串起来？
5. 滤波 / 预测 / 平滑的数据可用性差别？
6. 岭回归里 $\lambda$ 增大时 $\hat\theta$ 如何变？

> [!success]- 参考答案
> 1. $\Phi^\mathsf{T}\Phi\hat\theta=\Phi^\mathsf{T}y$；最优残差与每个回归元不相关（内积为零）。
> 2. $H=S_{xy}/S_y$；$S_y$ 观测谱，$S_{xy}$ 信号–观测互谱。
> 3. 有理谱的因果谱因子带来极点 → 递归实现即 IIR。
> 4. 都是二阶正交投影；差别在批/因果/是否用有限维状态递推。
> 5. 滤波用到当前；预测只用过去；平滑还用未来。
> 6. 更强收缩向 0（更信先验、更不信病态数据），方差降、偏差可能升。

## 参考

- NPTEL 108105059 L15
- Wiener，《Extrapolation, Interpolation, and Smoothing of Stationary Time Series》
- 本库 [[Signals and Systems MOC]]：LTI 与频谱工具
- [[Signals Systems and Inference (MIT 6.011) MOC]]：Wiener / 线性估计视角
