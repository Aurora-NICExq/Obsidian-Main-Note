---
aliases:
  - 线性 MMSE 与新息
  - Linear MMSE
  - Innovations
  - 正交原理
  - 新息过程
tags: [ee, estimation_kalman]
up: "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
related:
  - "[[Random Processes for Estimation]]"
  - "[[Least Squares and Optimal Filters]]"
  - "[[Kalman Filter Derivation]]"
  - "[[Bayesian Inference]]"
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
  - "[[Joint Distributions Covariance and Correlation]]"
down:
  - "[[Least Squares and Optimal Filters]]"
---
# 线性 MMSE 与新息

> [!summary] 核心结论
> 在只允许**线性**估计器时，最小化均方误差 $\mathbb{E}[\lVert X-\hat X\rVert^2]$ 等价于**正交原理**：误差 $X-\hat X$ 与所有可用观测线性组合正交。**新息（innovation）** $\nu_k=y_k-\hat y_{k\mid k-1}$ 是观测中“真正新的”部分；白化后的新息使递推估计（含 Kalman）结构清晰。高斯时线性 MMSE = 条件均值（全最优）。

> 底本：NPTEL 108105059 L11–L14；交叉：[[Signals Systems and Inference (MIT 6.011) MOC]]、[[Bayesian Inference]]。

> 关键词：MMSE、正交原理、新息、投影、条件期望

---

## 1. MMSE 问题

待估随机向量 $X$，观测 $Y$。估计器 $\hat X=g(Y)$。**MMSE**：
$$
\hat X_{\mathrm{MMSE}}=\arg\min_g\,\mathbb{E}\bigl[\lVert X-g(Y)\rvert^2\bigr]=\mathbb{E}[X\mid Y].
$$
一般非线性、难算。限制 $g$ 为仿射：$g(Y)=AY+b$，得 **线性 MMSE（LMMSE）**。

零均值时常取 $b=0$，$\hat X=AY$，法方程由正交给出。

![[ekf-gaussian-update.svg]]

---

## 2. 正交原理

$\hat X$ 为 $Y$ 的线性函数且 MMSE，当且仅当
$$
\mathbb{E}\bigl[(X-\hat X)\,Y^\mathsf{T}\bigr]=0
$$
（误差与每个观测分量不相关）。几何图像：把 $X$ 投影到 $\mathrm{span}\{Y\}$ 上；残差垂直于子空间。

对标量、零均值：
$$
\hat x=\frac{\mathbb{E}[xy]}{\mathbb{E}[y^2]}\,y=\frac{R_{xy}}{R_y}\,y.
$$
向量：$\hat X=R_{XY}R_Y^{-1}Y$（$R_Y$ 可逆）。这与 [[Joint Distributions Covariance and Correlation|协方差矩阵]] 块运算一致。

> [!example] 标量联合估计
> $x,y$ 零均值，$\mathrm{Var}(x)=4$，$\mathrm{Var}(y)=1$，$\mathrm{Cov}(x,y)=1$。观测 $y=2$。
> $$
> \hat x=\frac{1}{1}\cdot 2=2,\qquad
> \mathbb{E}[(x-\hat x)^2]=4-\frac{1^2}{1}=3.
> $$
> 误差方差 $=R_x-R_{xy}R_y^{-1}R_{yx}$。若无观测，MMSE 估 $0$、MSE$=4$；观测把 MSE 降到 $3$。

---

## 3. 高斯与“线性已足够”

若 $(X,Y)$ 联合高斯，则 $\mathbb{E}[X\mid Y]$ 恰为 $Y$ 的仿射函数 → LMMSE = 全 MMSE。Kalman 在线性–高斯模型下因此全局最优，不只是“线性类最优”。

非高斯时，LMMSE 仍是最好的**线性**估计，但可能远差于条件均值（可用粒子滤波等，见 [[Nonlinear Filtering EKF and Beyond]]）。

---

## 4. 新息过程

序列观测 $y_0,y_1,\ldots$。定义一步预测 $\hat y_{k\mid k-1}$（基于 $y_{0:k-1}$ 的 LMMSE），**新息**
$$
\nu_k=y_k-\hat y_{k\mid k-1}.
$$

![[ekf-innovation.svg]]

性质（线性 / 合适正则下）：

1. $\nu_k$ 与过去观测不相关（正交于过去）。
2. $\{\nu_k\}$ 彼此不相关（新息序列白——在线性估计意义下）。
3. $y_{0:k}$ 与 $\nu_{0:k}$ 张成同一线性空间：可用新息递推更新估计。

口头：新息 = “模型没料到的那部分测量”。Kalman 更新正是 $\hat x\leftarrow\hat x^- + K\nu$。

---

## 5. 递推思想（通向 KF）

批处理：$R_Y$ 随数据变长而变大，求逆昂贵。新息递推把“投影到越来越大的空间”拆成：已有估计 + 对新息的增益校正。状态空间模型再把“信号”压成有限维状态，得 Kalman 滤波器（[[Kalman Filter Derivation]]）。

连续时间对应 **Wiener–Hopf** / 因果 Wiener 滤波；离散新息是同一几何的时间展开。

---

## 6. 与贝叶斯更新的对照

| | 贝叶斯（一般） | 线性 MMSE |
|--|----------------|-----------|
| 目标 | 后验 $\pi(x\mid y)$ | 最小化 MSE 的线性 $\hat x$ |
| 高斯线性 | 后验均值 = LMMSE | 同左 |
| 需要 | 似然 + 先验全部分布 | 仅二阶矩 |

[[Bayesian Inference]] 强调整条后验；本课工程路径常用二阶矩闭环——二者在 KF 处会合。

---

## 7. 预白化视角

若观测噪声有色，可先经滤波器使新息（或等效残差）近白，再做匹配 / 增益加权。KF 的 $S_k=HP^-H^\mathsf{T}+R$ 就是新息协方差；归一化新息 $\tilde\nu=S^{-1/2}\nu$ 用于一致性检验（[[Practical Identification and Instrumentation]]）。

---

## 8. 陷阱

> [!warning] 不相关 ≠ 独立
> 正交原理只保证误差与观测**不相关**。非高斯时仍可能有非线性依赖可挖——LMMSE 会“留信息在桌上”。

> [!warning] 均值处理
> 非零均值要先减均值或显式仿射项 $b$；状态空间里常把均值并入确定性输入 / 标称轨迹。

---

## 9. 多观测递推投影

已有基于 $Y_{k-1}$ 的 $\hat X_{k-1}$。新观测 $y_k$ 到来时，先对 $y_k$ 做关于 $Y_{k-1}$ 的预测得新息 $\nu_k$，再
$$
\hat X_k=\hat X_{k-1}+K_k\nu_k,
$$
$K_k$ 由 $\mathrm{Cov}(X,\nu_k)\mathrm{Cov}(\nu_k)^{-1}$ 给出。这是所有递推线性估计（含 KF）的骨架：**旧估计 + 增益 × 新息**。

> [!example] 两次标量观测
> $x$ 零均值方差 $4$；两次独立测量 $y_i=x+v_i$，$R_{v}=4$。  
> 第一次 $y_1=2$：$\hat x_1=\frac{4}{4+4}\cdot 2=1$，$P_1=2$。  
> 第二次 $y_2=3$：把 $P_1$ 当先验，$K=2/(2+4)=1/3$，  
> $\hat x_2=1+(1/3)(3-1)=5/3$，$P_2=(1-1/3)\cdot 2=4/3$。  
> 与一次把两测量堆叠的批 LMMSE 相同（线性高斯）。

---

## 10. 自检与参考答案

1. 叙述正交原理；说明它如何给出标量增益公式。
2. 何谓新息？为何说它“白”？
3. 联合高斯时，为何不必找非线性估计器？
4. 误差方差公式 $R_x-R_{xy}R_y^{-1}R_{yx}$ 的意义？
5. 新息与 Kalman 更新项的关系？
6. 上例两次更新后 $P_2=4/3$，相对先验 $4$ 说明了什么？

> [!success]- 参考答案
> 1. $\mathbb{E}[(x-\hat x)y]=0\Rightarrow\hat x=(\mathbb{E}[xy]/\mathbb{E}[y^2])y$。
> 2. $\nu_k=y_k-\hat y_{k\mid k-1}$；与过去观测正交，故序列互不相关（线性意义下白）。
> 3. 条件均值已是仿射，线性类已达全 MMSE。
> 4. 先验不确定度减去“被观测线性解释掉”的部分；观测越相关、噪声越小，减去越多。
> 5. 更新 $\hat x=\hat x^-+K\nu$，其中 $\nu$ 即测量新息。
> 6. 两次噪声方差为 4 的测量把方差从 4 降到 $4/3$，信息量可加（独立时）。

## 参考

- NPTEL 108105059 L11–L14（LMMSE、正交、新息）
- MIT 6.011 / SSI：线性估计与推断（本库 MOC）
- Kailath，《Linear Estimation》（经典新息视角）
