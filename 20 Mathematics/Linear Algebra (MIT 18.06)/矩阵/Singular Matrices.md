---
aliases: [singular矩阵, Singular Matrices, 奇异矩阵]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[The Matrix Viewpoint|矩阵的视角]], [[How Matrix Multiplication Works|矩阵乘法的原理]], [[Matrices (Systems, Elimination, Inverse)|矩阵]], [[Determinants and Their Properties|行列式及其性质]]"
down: ""
---
# Singular Matrices

> [!summary] 核心结论
> 奇异矩阵 (singular matrix) 不可逆，等价于：$\det A=0$、$A\mathbf x=\mathbf0$ 有非零解、列向量线性相关、秩小于列数、消元出现零主元。几何上它把空间压到更低维。

---

## 1. 定义 (Definition)

$A$ 奇异 (singular) 即 $A$ 不可逆，不存在 $A^{-1}$。

## 2. 等价条件 (Equivalent Conditions)

- $\det A=0$；
- $A\mathbf x=\mathbf0$ 有非零解（零空间非平凡）；
- 列向量线性相关；
- 秩 $<$ 列数；
- 消元中至少出现一个零主元 (zero pivot)。

## 3. 几何意义 (Geometry)

奇异矩阵把空间压到更低维对象：平面压成直线、三维压成平面——体积缩为零（对照 [[Determinants and Their Properties|行列式及其性质]] 的 $\det=0$）。

## 4. 与可解性的关系 (Solvability)

$A$ 奇异时 $A\mathbf x=\mathbf b$ 可能无解或有无穷多解，取决于 $\mathbf b$ 是否在 $C(A)$ 中。

---

> [!important] 一句话总结
> 看到 singular，立即联想 $\det A=0$、$A^{-1}$ 不存在、$A\mathbf x=\mathbf0$ 有非零解。
