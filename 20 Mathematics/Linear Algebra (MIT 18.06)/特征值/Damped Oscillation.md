---
aliases: [阻尼振动, Damped Oscillation]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Linear Algebra and Differential Equations|线性代数与微分方程]], [[Eigenvalues and Eigenvectors|特征值和特征向量]], [[Differential Equations and the Number e|微分方程与自然常数]]"
down: ""
---
# Damped Oscillation

> [!summary] 核心结论
> 阻尼振动 (damped oscillation) 的形态由特征方程的判别式 $\Delta=c^2-4mk$ 决定：两实根→过阻尼、重根→临界阻尼、共轭复根→欠阻尼。这是"特征值决定动态行为"的典型例子。

前置知识：[[Eigenvalues and Eigenvectors|特征值和特征向量]]、[[Ordinary Differential Equations (Foundations and Methods)|一阶微分方程]]。

---

## 1. 标准模型 (Model)

$$mx''+cx'+kx=0,\quad m>0,\ c\ge0,\ k>0.$$

设 $x=e^{rt}$ 得特征方程 $mr^2+cr+k=0$，判别式 $\Delta=c^2-4mk$。

## 2. 三种状态 (Three Regimes)

1. $\Delta>0$：两不同实根，**过阻尼 (overdamped)**，单调回到平衡不振荡；
2. $\Delta=0$：重根，**临界阻尼 (critically damped)**，不振荡且最快回平衡；
3. $\Delta<0$：共轭复根，**欠阻尼 (underdamped)**，振荡并指数衰减。 ^ef6510

## 3. 解的形式 (Solutions)

$$\Delta>0:\ x=C_1e^{r_1t}+C_2e^{r_2t};\quad \Delta=0:\ x=(C_1+C_2t)e^{rt};\quad \Delta<0:\ x=e^{\alpha t}(C_1\cos\omega t+C_2\sin\omega t).$$

## 4. 线性代数视角 (Linear-Algebra View)

二阶方程化为一阶系统：

$$\frac{d}{dt}\begin{bmatrix}x\\ v\end{bmatrix}=\begin{bmatrix}0&1\\ -k/m&-c/m\end{bmatrix}\begin{bmatrix}x\\ v\end{bmatrix}.$$

系统矩阵的**特征值**就是特征方程的根：**实部控制衰减，虚部控制振荡频率**（见 [[Eigenvalues and Eigenvectors|特征值和特征向量]]、[[Linear Algebra and Differential Equations|线性代数与微分方程]]）。

---

> [!important] 一句话总结
> 阻尼振动：实部看衰减、虚部看振荡——动态行为完全由系统矩阵的特征值决定。
