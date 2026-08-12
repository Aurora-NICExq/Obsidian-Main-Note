---
aliases:
  - 估计用随机过程
  - Random Processes for Estimation
  - ACF WSS
  - 宽平稳过程
  - 自相关函数
tags: [ee, estimation_kalman]
up: "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
related:
  - "[[Linear MMSE and Innovations]]"
  - "[[Signals and Systems MOC]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
  - "[[Joint Distributions Covariance and Correlation]]"
  - "[[Continuous Random Variables]]"
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
down:
  - "[[Linear MMSE and Innovations]]"
---
# 估计用随机过程

> [!summary] 核心结论
> 估计理论把“未知信号 / 状态”建模为**随机过程**，用**二阶统计**（均值、自相关 / 功率谱）刻画。宽平稳（WSS）下自相关只依赖时差，经 LTI 系统后相关与谱按已知规则变换——这是 Wiener / Kalman 设计的语言。NPTEL L2–L10 的压缩目标：会写 ACF、判 WSS、算线性系统输出的二阶矩，并为后续正交原理铺垫。

> 底本：NPTEL 108105059 *Estimation of Signals and Systems*（Mukhopadhyay）随机过程单元；辅读：概率笔记 [[Joint Distributions Covariance and Correlation]]、信号系统 [[Signals and Systems MOC]]。

> 关键词：随机过程、ACF、WSS、功率谱、白噪声、LTI 滤波

---

## 1. 从随机变量到随机过程

固定时刻 $t$，观测 $X(t)$ 是随机变量；全体 $\{X(t)\}$ 是**随机过程**（discrete-time 记 $X[n]$）。估计问题关心的是：给定部分观测，如何推断另一时刻 / 另一过程的取值——需要联合分布，至少需要**均值与相关**。

**均值函数**
$$
\mu_X(t)=\mathbb{E}[X(t)].
$$
**自相关（ACF）**
$$
R_X(t_1,t_2)=\mathbb{E}\bigl[X(t_1)X(t_2)^*\bigr]
$$
（实过程常省略共轭）。**自协方差**
$$
C_X(t_1,t_2)=R_X(t_1,t_2)-\mu_X(t_1)\mu_X(t_2)^*.
$$
与 [[Continuous Random Variables|连续随机变量]] 的方差、[[Joint Distributions Covariance and Correlation|协方差]] 同一代数，只是“指标”变成时间。

---

## 2. 宽平稳（WSS）

过程 $X$ 为 **wide-sense stationary**，若：

1. $\mu_X(t)=\mu$ 常数；
2. $R_X(t_1,t_2)$ 只依赖 $\tau=t_1-t_2$，记 $R_X(\tau)$。

则功率 $\mathbb{E}[|X(t)|^2]=R_X(0)$ 与时间无关。严格平稳（所有有限维分布时移不变）$\Rightarrow$ WSS；反之不必。工程上多数噪声 / 扰动模型只保证到 WSS。

> [!tip] 离散时间
> 采样后写 $R_X[k]=\mathbb{E}[X[n+k]X[n]]$（实、零均值时常如此）。Kalman 递推里“时变但白”的过程噪声仍常用：每步独立、方差可随 $k$ 变，**不必**全局 WSS。

---

## 3. 白噪声与着色噪声

**白噪声**（离散）：$\mathbb{E}[w[n]]=0$，$R_w[k]=\sigma_w^2\delta[k]$。谱平坦；经 LTI 滤波后变“有色”。

**连续白噪声**是理想化（功率无限），实际用宽带噪声或在积分方程 / 状态空间里用形式记号；实现上仍回到离散 KF 或带限模型。

**MA / AR 直觉**：白噪声过 FIR → MA（有限相关长度）；过 IIR → AR / ARMA（指数衰减相关）。系统辨识里常用这些二阶结构（见 [[System Identification and Recursive Least Squares]]）。

---

## 4. 通过线性系统的二阶统计

设 LTI：$Y=h*X$（卷积；离散同理）。若 $X$ WSS，则 $Y$ 也 WSS，且
$$
R_Y(\tau)=h(\tau)*h(-\tau)^* * R_X(\tau)
$$
（连续；离散把积分换成求和）。频域：
$$
S_Y(j\omega)=\lvert H(j\omega)\rvert^2 S_X(j\omega),
$$
其中 $S_X$ 是 $R_X$ 的傅里叶变换（功率谱密度，Wiener–Khinchin）。

这正是 [[Signals and Systems MOC|信号与系统]] 中“滤波改频谱”在**功率**意义上的版本：设计噪声整形、预白化、Wiener 滤波器时，输入输出相关由 $H$ 决定。

> [!example] 一阶低通着色
> 离散：$y[n]=a y[n-1]+w[n]$，$|a|<1$，$w$ 白、方差 $q$。稳态
> $$
> R_y[0]=\frac{q}{1-a^2},\qquad R_y[k]=\frac{q}{1-a^2}\,a^{|k|}.
> $$
> 相关长度由 $|a|$ 控制：$a\to 1$ 时过程“慢”、强相关——状态估计里常见于缓慢漂移扰动。

---

## 5. 互相关与联合 WSS

两过程 $X,Y$：**互相关** $R_{XY}(t_1,t_2)=\mathbb{E}[X(t_1)Y(t_2)^*]$。若各自 WSS 且互相关只依赖时差，称**联合宽平稳**。Wiener 滤波要的正是 $R_Y$ 与 $R_{XY}$（观测与待估信号的互相关）。

正交原理（下篇）用内积 $\langle U,V\rangle=\mathbb{E}[UV^*]$；WSS 保证许多滤波器系数可取时不变。

---

## 6. 遍历性（直觉）

**均值遍历 / 相关遍历**：用一条足够长的样本时间平均代替集平均。实验室用一段录波估 ACF / 谱时默认某种遍历性；非平稳、短数据、强周期分量会毁掉这个近似——实用辨识要警惕（[[Practical Identification and Instrumentation]]）。

---

## 7. 与后续课的接口

| 本课对象 | 后续用法 |
|----------|----------|
| $R_X,R_{XY}$ | LMMSE、Wiener、新息白化 |
| 白噪声驱动状态方程 | Kalman 过程噪声 $Q$ |
| 测量噪声相关 | 观测噪声 $R$；有色时需增广状态 |
| 功率谱 | 稳态 KF ↔ Wiener 滤波器联系 |

[[Signals Systems and Inference (MIT 6.011) MOC]] 从推断角度讲同一套二阶工具；本课更偏 NPTEL 的估计 / 辨识工程链。

---

## 8. 常见陷阱

> [!warning] WSS ≠ 可忽略瞬态
> 滤波器刚开机时输出未达稳态相关；短数据段上估出的 $R[k]$ 混有启动效应。KF 用时变 $P_k$ 显式处理“还未稳态”；批处理 Wiener 常假设已稳态。

> [!warning] 相关估计偏差
> 有偏 / 无偏 ACF 估计、窗函数、FFT 谱泄漏都会扭曲 $S(j\omega)$。辨识与噪声建模时先画残差 ACF，再谈模型阶次。

---

## 9. 从频谱到滤波器设计的一张表

| 已知 | 可做 |
|------|------|
| $S_y,S_{xy}$ | 非因果 Wiener $H=S_{xy}/S_y$ |
| 有理 $S_y$ | 谱因子 → 因果最优 / 预白化 |
| 白 $w$ + LTI 状态 | 直接写 KF 的 $F,Q$ |
| 仅样本轨迹 | 估 ACF / 用 LS-AR 再转状态空间 |

这张表把 NPTEL 前半（过程）接到后半（KF / 辨识）。

> [!example] 白噪声过增益再低通
> $w$ 白方差 $\sigma^2$，先乘 $g$ 再经直流增益 1 的稳定低通 $H$。输出功率 $R_y(0)=\sigma^2 g^2 \lVert h\rVert_2^2$（Parseval：$\frac{1}{2\pi}\int\lvert H\rvert^2\sigma^2\mathrm{d}\omega$）。设计抗混叠时用同一能量账。

---

## 10. 自检与参考答案

1. 写出 WSS 的两条定义；举一个均值恒定但非 WSS 的例子（直觉即可）。
2. 白噪声过增益 $g$ 的静态系统，输出 ACF 是什么？
3. 解释 $S_Y=\lvert H\rvert^2 S_X$ 对“预白化”的用途。
4. 为何 Kalman 的 $w_k$ 往往建模为白，而真实扰动可能有色？如何补救？
5. 互相关 $R_{XY}$ 在估计问题中扮演什么角色？
6. 为何短录波上的样本 ACF 要谨慎解读？

> [!success]- 参考答案
> 1. 均值常数；ACF 只依赖 $\tau$。例：方差随时间变的零均值高斯独立序列（不平稳功率）。
> 2. $R_y[k]=g^2\sigma_w^2\delta[k]$（仍白，功率缩放）。
> 3. 若能估计 $H$ 使输出近白，则后续相关检测 / 匹配滤波在白噪声假设下最优更易用；也是新息过程的谱平坦目标。
> 4. 白驱动 + 线性状态可生成有色状态扰动；若测量噪声有色，把着色滤波器状态增广进状态向量，使增广噪声再近白。
> 5. 它刻画“观测里有多少关于待估信号的线性信息”，进入正交原理的法方程 / Wiener–Hopf。
> 6. 方差大、有偏估计、非平稳 / 启动瞬态都会污染 $R[k]$；需窗长与置信带。

## 参考

- S. Mukhopadhyay, NPTEL *Estimation of Signals and Systems*（108105059），随机过程与线性系统响应讲次
- Oppenheim / Willsky，《Signals and Systems》功率谱与 LTI（与本库 [[Signals and Systems MOC]] 对照）
- MIT 18.05 / 本库概率笔记：期望、协方差基础
