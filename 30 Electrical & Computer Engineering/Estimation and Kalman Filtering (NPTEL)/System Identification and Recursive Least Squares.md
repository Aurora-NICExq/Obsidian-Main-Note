---
aliases:
  - 系统辨识与递推最小二乘
  - System Identification
  - Recursive Least Squares
  - RLS
  - 参数估计
tags: [ee, estimation_kalman]
up: "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
related:
  - "[[Least Squares and Optimal Filters]]"
  - "[[Adaptive Filters]]"
  - "[[Practical Identification and Instrumentation]]"
  - "[[Kalman Filter Derivation]]"
  - "[[Linear Regression]]"
  - "[[Maximum Likelihood Estimation]]"
down:
  - "[[Practical Identification and Instrumentation]]"
---
# 系统辨识与递推最小二乘

> [!summary] 核心结论
> **系统辨识**从输入–输出数据估计动态模型参数（FIR、ARX、OE 等）。批 LS 解法方程；**RLS** 递推同一准则，可带遗忘因子跟踪缓变。参数向量当作状态、随机游走过程噪声时，RLS ≈ 某设定下的 KF。辨识质量取决于激励、模型类与噪声假设——下一笔记做校验与仪表。

> 底本：NPTEL 108105059 L23–L26。

> 关键词：ARX、回归元、RLS、遗忘因子、持续激励

---

## 1. 辨识问题

已知（或可设计）输入 $u$，测输出 $y$，求在给定模型类中的 $\theta$，使仿真 / 预测误差小。与控制设计、Kalman 建模共用：没有模型就没有 $F,H$。

![[ekf-identification.svg]]

---

## 2. 线性回归形式：ARX 例

ARX：
$$
y[n]+a_1 y[n-1]+\cdots+a_{n_a}y[n-n_a]=b_1 u[n-1]+\cdots+b_{n_b}u[n-n_b]+e[n].
$$
整理为
$$
y[n]=\varphi[n]^\mathsf{T}\theta+e[n],
$$
$\varphi$ 含过去 $y,u$（回归元），$\theta$ 含 $a_i,b_j$。则 **LS / RLS** 直接套用。方程误差 $e$ 白是理想；有色时 LS 有偏，需 OE / PEM / 工具变量等（进阶）。

与 [[Linear Regression]] 同构；动态来自 $\varphi$ 中的延迟。

---

## 3. 批 LS

数据 $n=1\ldots N$：
$$
\hat\theta_N=\Bigl(\sum_{n=1}^N\varphi[n]\varphi[n]^\mathsf{T}\Bigr)^{-1}\sum_{n=1}^N\varphi[n]y[n].
$$
存在条件：信息矩阵满秩 ↔ 输入**持续激励**（阶次足够的频谱内容）。

> [!example] 一阶 FIR 数值
> $y[n]=b_0 u[n]+e[n]$，数据：$(u,y)=\{(1,1.1),(2,1.9),(3,3.2)\}$。  
> $\sum u^2=1+4+9=14$，$\sum uy=1.1+3.8+9.6=14.5$，  
> $\hat b_0=14.5/14\approx 1.036$。残差约 $\{0.064,-0.171,0.093\}$。

---

## 4. RLS 递推

令 $P_n^{-1}=\sum_{i=1}^n\lambda^{n-i}\varphi_i\varphi_i^\mathsf{T}$（或带初始化 $P_0$）。更新：
$$
\begin{aligned}
K_n&=\frac{P_{n-1}\varphi_n}{\lambda+\varphi_n^\mathsf{T}P_{n-1}\varphi_n},\\
\hat\theta_n&=\hat\theta_{n-1}+K_n\bigl(y_n-\varphi_n^\mathsf{T}\hat\theta_{n-1}\bigr),\\
P_n&=\frac{1}{\lambda}\bigl(P_{n-1}-K_n\varphi_n^\mathsf{T}P_{n-1}\bigr).
\end{aligned}
$$
$\lambda=1$：精确递推 LS；$\lambda<1$：指数遗忘，跟踪时变 $\theta$。

---

## 5. RLS ↔ Kalman

把 $\theta_{k+1}=\theta_k+w_k$（$Q$ 小），测量 $y_k=\varphi_k^\mathsf{T}\theta_k+v_k$。KF 对 $\theta$ 的更新与 RLS 同形；$P$ 角色对应参数协方差。遗忘因子近似于人为注入过程噪声。此视角统一 [[Adaptive Filters]]、辨识与 KF。

---

## 6. 模型类选择（预告）

| 类 | 特点 |
|----|------|
| FIR | 线性于 $\theta$，稳，但阶可能很长 |
| ARX | 回归易，噪声模型粗糙 |
| ARMAX / OE | 更贴近过程噪声，估计更难（非线性优化） |

阶次 $n_a,n_b$ 用验证集、AIC/BIC、残差白化选——[[Practical Identification and Instrumentation]]。

---

## 7. 与 MLE 的联系

高斯方程误差下，LS = [[Maximum Likelihood Estimation|MLE]]。更一般 PEM（预测误差方法）最小化一步预测误差平方和，涵盖更广噪声模型。

---

## 8. 时变参数与分段

慢漂：$\lambda\in[0.95,0.995]$ 或 $\theta$ 随机游走 + KF。突变：可重置 $P$ 放大、或多模型切换。分段线性化 / 工作点表是非线性对象的实用折中——每个工作点一套 ARX。

> [!example] RLS 标量一步
> $\theta$ 标量，$\varphi=2$，$y=3.1$，$\hat\theta_{n-1}=1.4$，$P_{n-1}=0.5$，$\lambda=1$。  
> $K=0.5\cdot 2/(1+2\cdot 0.5\cdot 2)=1/3$，  
> $\hat\theta=1.4+(1/3)(3.1-2\cdot 1.4)=1.4+(1/3)(0.3)=1.5$，  
> $P=(0.5-(1/3)\cdot 2\cdot 0.5)=1/6$。  
> 参数被新息拉向更大，方差下降。

---

## 9. 陷阱

> [!warning] 闭环辨识
> 若 $u$ 由反馈依赖 $y$，回归元与噪声相关 → 朴素 LS 有偏。需工具变量、联合输入设计或直接闭环方法。

> [!warning] $P_0$ 过大 / 过小
> RLS 初值 $P_0=\alpha I$：$\alpha$ 太大早期步子疯；太小则学不动。常用较大 $\alpha$ 并限制首步、或批处理预热。

> [!warning] 只看训练拟合
> $R^2$ 高但验证残差有色 → 模型类错或过拟合。必须以确认步骤为准（下篇）。

---

## 10. 自检与参考答案

1. 把 ARX 写成 $\varphi^\mathsf{T}\theta$ 时，$\varphi$ 里有哪些量？
2. 持续激励为何必要？
3. $\lambda=0.98$ 与 $\lambda=1$ 在跟踪上的差别？
4. 如何一句话把 RLS 说成 KF？
5. 闭环下朴素 LS 的主要危险？
6. 上例中若 $\lambda=0.9$，定性上 $P$ 会比 $\lambda=1$ 更大还是更小？

> [!success]- 参考答案
> 1. 过去输出（带负号约定下的 $-y$）与过去输入（及可能的当前输入，视延迟）。
> 2. 否则信息矩阵奇异 / 病态，参数不可唯一辨识。
> 3. $0.98$ 遗忘旧数据，能跟慢变；$\lambda=1$ 记忆无限，时变时滞后且参数被旧数据钉死。
> 4. 常值（或慢游走）参数状态 + 回归测量模型下的 Kalman 更新。
> 5. 噪声与回归元相关造成有偏估计。
> 6. 通常更大：除以 $\lambda$ 放大 $P$，相当于人为注入不确定度以便跟踪。

## 参考

- NPTEL 108105059 L23–L26
- Ljung，《System Identification: Theory for the User》
- Söderström & Stoica，《System Identification》
