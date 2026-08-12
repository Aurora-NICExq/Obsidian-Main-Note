---
aliases: [微分方程与线性代数, Differential Equations through Linear Algebra]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Ordinary Differential Equations (Foundations and Methods)|一阶微分方程]], [[Particular-Solution Forms Table|非齐次特解微分方程特解表格]], [[Nonhomogeneous Linear ODEs|非齐次微分方程]], [[Differential Equations and the Number e|微分方程与自然常数]]"
down: ""
---
# Differential Equations through Linear Algebra

> [!summary] 核心结论
> 线性微分方程本质上是**无穷维向量空间中的线性代数**：微分算子 $L$ 扮演矩阵 $A$ 的角色，函数 $y(x)$ 扮演向量 $\mathbf x$。于是"通解 $=$ 齐次通解 $+$ 特解"与线性方程组 $A\mathbf x=\mathbf b$ 的解结构**完全一致**——求齐次解就是求算子 $L$ 的零空间 (kernel)。

---

## 1. 核心对应字典 (The Dictionary)

| 概念 | 线性代数 (Linear Algebra) | 线性微分方程 (Linear ODE) |
| :-- | :-- | :-- |
| 基本方程 | $A\mathbf x=\mathbf b$ | $L[y]=g(x)$ |
| 算子/变换 | 矩阵 $A$ | 微分算子 $L=\tfrac{d^2}{dx^2}+p\tfrac{d}{dx}+q$ |
| 未知量 | 向量 $\mathbf x$ | 函数 $y(x)$ |
| 齐次方程 | $A\mathbf x=\mathbf 0$ | $L[y]=0$，即 $y''+py'+qy=0$ |
| 非齐次项 | 向量 $\mathbf b$ | 函数 $g(x)$（驱动力） |

---

## 2. 通解的结构 (Structure of the General Solution)

两边的解结构公式**完全一致** [[Vector Spaces and Subspaces#^981165|通解与特解的关系]]：

$$\text{通解}=\text{齐次通解}+\text{非齐次特解}.$$

对方程 $y''+p(t)y'+q(t)y=g(t)$：

$$y(t)=y_h(t)+y_p(t),$$

- $y_h(t)$（齐次通解）：是 $y''+py'+qy=0$ 的解，通常由两个线性无关解线性组合 $C_1y_1+C_2y_2$；
- $y_p(t)$（特解）：非齐次方程的某个特定解。

**结论**：求通解，就是先找微分算子 $L$ 的"零空间 (kernel)"，再叠加一个偏移量（特解）——与解 $A\mathbf x=\mathbf b$ 时"零空间 + 特解"如出一辙。

---

## 3. 线性无关与基底 (Linear Independence & Basis)

- **线性代数**：若零空间维数为 $n$，需 $n$ 个线性无关向量 $\mathbf v_1,\dots,\mathbf v_n$ 作基底，齐次通解为 $c_1\mathbf v_1+\cdots+c_n\mathbf v_n$；无关性用秩 (rank) 或行列式判定 [[Linear Independence, Basis, and Dimension#^8403a0|线性代数的基]]。
- **微分方程**：$n$ 阶线性方程的解空间维数通常为 $n$，需 $n$ 个线性无关函数 $y_1,\dots,y_n$；无关性用**朗斯基行列式 (Wronskian)** 判定。

> [!note] 朗斯基行列式的意义
> 朗斯基行列式本质上就是在检验这些函数（连同其各阶导数）构成的"向量"是否线性无关——它是行列式判无关性在函数空间的翻版。

---

## 4. 共同根源：求导是线性运算 (Differentiation Is Linear)

一切对应的根源在于：求导算子 $\tfrac{d}{dx}$ 本身是线性的，满足**叠加原理 (superposition)**：

$$L[c_1y_1+c_2y_2]=c_1L[y_1]+c_2L[y_2].$$

正因为 $L$ 线性，才能像拆解向量那样，把复杂方程拆成"齐次部分 + 特解部分"分别求解，最后叠加。
