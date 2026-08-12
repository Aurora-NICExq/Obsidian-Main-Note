---
aliases:
  - MMSE与LMMSE估计
  - MMSE and LMMSE Estimation
  - 最小均方误差
  - 线性最小均方误差
  - orthogonality principle
  - 正交原理
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[Joint Distributions Covariance and Correlation]]"
  - "[[Conditional Probability and Bayes Theorem]]"
  - "[[Wide-Sense Stationary Processes]]"
  - "[[Wiener Filtering]]"
  - "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
down:
  - "[[Wide-Sense Stationary Processes]]"
---
# MMSE 与 LMMSE 估计：正交原理

> [!summary] 核心结论
> 在均方误差 $\mathbb{E}[\lVert X-\hat X\rVert^2]$ 意义下，**最优估计**是条件均值 $\hat X_{\mathrm{MMSE}}=\mathbb{E}[X\mid Y]$。若限制 $\hat X$ 为 $Y$ 的**仿射**函数（LMMSE），最优解由**正交原理**刻画：误差 $X-\hat X$ 与观测的一切允许线性函数正交。法方程给出
> $$
> \hat X_{\mathrm{LMMSE}}=\mu_X+R_{XY}R_Y^{-1}(Y-\mu_Y)
> $$
> （标量 / 向量形式同构）。**联合高斯**时条件均值恰为仿射 ⇒ MMSE = LMMSE。这是 Wiener / Kalman 的代数内核；概率预备见 [[Joint Distributions Covariance and Correlation]]。

> 底本：MIT 6.011 OCW Spring 2018 — MMSE / LMMSE；贝叶斯条件见 [[Conditional Probability and Bayes Theorem]]。

---
## 1. 估计问题

随机变量（或向量）$X$ 待估，观测 $Y$。估计量 $\hat X=g(Y)$。风险取 MSE：
$$
\mathrm{MSE}(g)=\mathbb{E}\bigl[\lVert X-g(Y)\rVert^2\bigr].
$$
无观测时最优是 $\hat X=\mathbb{E}[X]$（常数）。有观测时，在可测函数类中最优为条件期望。

![[ssi-lmmse.svg]]

---
## 2. MMSE：条件均值

$$
\hat X_{\mathrm{MMSE}}(Y)=\mathbb{E}[X\mid Y].
$$
证明素描：对任意 $g$，
$$
\mathbb{E}[\lVert X-g\rVert^2]=\mathbb{E}[\lVert X-\mathbb{E}[X\mid Y]\rVert^2]+\mathbb{E}[\lVert\mathbb{E}[X\mid Y]-g\rVert^2],
$$
交叉项因条件期望的正交性消失。故条件均值唯一（a.s.）最优。

计算需要完整条件分布——非线性、高维时往往不可行。于是限制 $g$ 为仿射，只依赖一、二阶矩。

---
## 3. 正交原理与 LMMSE

在类 $\hat X=AY+b$（$A$ 矩阵，$b$ 向量）中最小化 MSE。最优时误差与观测仿射空间正交：
$$
\mathbb{E}\bigl[(X-\hat X)\bigr]=0,\qquad
\mathbb{E}\bigl[(X-\hat X)Y^\top\bigr]=0.
$$
由此推出中心化形式
$$
\hat X=\mu_X+\underbrace{R_{XY}R_Y^{\dagger}}_{K}(Y-\mu_Y),
$$
其中 $R_Y=\mathrm{Cov}(Y)$，$R_{XY}=\mathrm{Cov}(X,Y)$（伪逆处理奇异）。增益 $K$ 即「回归系数」矩阵。

标量情形：
$$
\hat x=\mu_x+\frac{\mathrm{Cov}(x,y)}{\mathrm{Var}(y)}(y-\mu_y),\qquad
\mathrm{MMSE}_{\mathrm{lin}}=\mathrm{Var}(x)-\frac{\mathrm{Cov}(x,y)^2}{\mathrm{Var}(y)}.
$$

> [!example] 标量 LMMSE 数值
> $X\sim$ 均值 $0$、方差 $4$；$Y=X+W$，$W$ 与 $X$ 不相关、方差 $1$。则
> $$
> \mathrm{Cov}(X,Y)=\mathrm{Var}(X)=4,\quad\mathrm{Var}(Y)=4+1=5.
> $$
> $$
> \hat X_{\mathrm{LMMSE}}=\frac{4}{5}Y=0.8\,Y.
> $$
> 线性 MMSE 误差方差 $=4-(16)/5=4-3.2=0.8$。若再设联合高斯，则这也是真正的 MMSE；且 $\mathbb{E}[X\mid Y=y]=0.8\,y$。信噪比 $\mathrm{Var}(X)/\mathrm{Var}(W)=4$ 越高，增益越接近 $1$。

---
## 4. 高斯 ⇒ 线性最优

若 $(X,Y)$ 联合高斯，则 $\mathbb{E}[X\mid Y]$ 是 $Y$ 的仿射函数，公式恰为上式 LMMSE。因此「只知协方差 + 高斯假定」时，线性估计即全局最优。非高斯时 LMMSE 仍是最佳**线性**估计，但可能劣于非线性 MMSE（例如观测是 $X^2$ 的噪声版本时）。

> [!warning] 不相关 ≠ 独立；正交原理不是「误差与 $X$ 正交」
> 正交原理说误差 ⊥ **观测生成的线性空间**。误差与 $X$ 一般不正交。另外，LMMSE 只用到二阶矩：不相关的高斯才独立；非高斯时不相关仍可有非线性依赖，条件均值可能弯曲。

---
## 5. 向量观测与「信息融合」直觉

多传感器 $Y=(Y_1,\ldots,Y_m)$：$R_Y$ 编码观测间相关。若噪声独立、同构，LMMSE 类似精度加权平均。Kalman 更新正是「先验状态 vs 新测量」的一次向量 LMMSE 步骤；Wiener 滤波是 WSS 过程上的 LMMSE（卷积 / 频域形式）。见 [[Wiener Filtering]]、[[Estimation and Kalman Filtering (NPTEL) MOC]]。

与最小二乘：确定性 LS 是「几何投影」；LMMSE 是「随机向量在子空间上的投影」——同一几何，内积换成 $\mathbb{E}[UV^\top]$。

---
## 6. 偏差与误差协方差

LMMSE 估计无偏：$\mathbb{E}[\hat X]=\mathbb{E}[X]$。误差协方差
$$
P=\mathrm{Cov}(X-\hat X)=R_X-R_{XY}R_Y^{-1}R_{YX}.
$$
$P$ 越小说明观测越「有信息」。若 $R_{XY}=0$，则 $P=R_X$，观测无用，退回均值。

---
## 7. 与检测 / 滤波的课程地图

| 主题 | 角色 |
|---|---|
| 本篇 LMMSE | 静态随机向量估计 |
| [[Wide-Sense Stationary Processes]] / PSD | 过程的二阶描述 |
| [[Wiener Filtering]] | 过程上的 LMMSE 滤波 / 平滑 / 预测 |
| 状态观测器 / Kalman | 动态状态递归 LMMSE |
| [[Hypothesis Testing and Signal Detection]] | 决策（0-1 损失等）而非 MSE 点估计 |

---
## 8. 序贯更新直觉（Kalman 一步）

已有先验估计 $\hat X^-$ 与误差协方差 $P^-$，新到观测 $Y=HX+V$。把 $(X,Y)$ 的 LMMSE 公式走一遍，得
$$
\hat X^+=\hat X^-+K(Y-H\hat X^-),\qquad
K=P^-H^\top(HP^-H^\top+R_V)^{-1}.
$$
这正是 Kalman 测量更新；$K$ 是又一次「协方差加权」。本课先吃透静态正交原理，动态递归留给 [[Estimation and Kalman Filtering (NPTEL) MOC]]。

---
## 9. 自检与参考答案

1. MMSE 最优估计是什么？证明思路的关键一步？
2. 写出标量 LMMSE 公式与误差方差。
3. 陈述正交原理。
4. 何时 MMSE = LMMSE？
5. $R_{XY}=0$ 时结论是什么？

> [!success]- 参考答案
> 1. $\mathbb{E}[X\mid Y]$；MSE 分解为条件方差项 + 偏离条件均值项，后者 ≥ 0。
> 2. $\hat x=\mu_x+\frac{\mathrm{Cov}(x,y)}{\mathrm{Var}(y)}(y-\mu_y)$；误差方差 $\sigma_x^2-\mathrm{Cov}^2/\sigma_y^2$。
> 3. 最优线性误差与任意观测仿射函数不相关（期望积为零）。
> 4. 联合高斯（或条件均值碰巧仿射）时。
> 5. 观测不提供线性信息，$\hat X=\mu_X$，误差协方差 = $R_X$。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[Joint Distributions Covariance and Correlation]]、[[Wiener Filtering]]
