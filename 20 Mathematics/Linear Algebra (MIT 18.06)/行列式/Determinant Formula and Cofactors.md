---
aliases: [行列式公式及协因子, Determinant Formula and Cofactors, Cofactor Expansion]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Determinants and Their Properties|行列式及其性质]], [[Applications of Determinants|行列式的应用]]"
down: "[[Applications of Determinants|行列式的应用]]"
---
# Determinant Formula and Cofactors

> [!summary] 核心结论
> 行列式可按**排列 (permutation)** 或**协因子 (cofactor)** 展开；协因子公式还给出逆矩阵的显式表达 $A^{-1}=\dfrac{1}{\det A}C^{\mathsf T}$。每个乘积项必须"每行每列各取一个元素"。

前置知识：[[Determinants and Their Properties|行列式及其性质]]。

---

## 1. 排列展开 (Permutation Formula)

每个乘积项每行每列各取一个元素，确保在 $n$ 维真正"撑开"体积：

$$\det A=\sum_{\sigma}\operatorname{sgn}(\sigma)\,a_{1\sigma(1)}a_{2\sigma(2)}\cdots a_{n\sigma(n)}.$$

每项的符号 $\pm$ **恰是对应置换矩阵 $P$ 的行列式**：恒等置换 $\det I=+1$；一次交换 $\det P=-1$。故

$$\det A=\sum_{\text{all }P}\det(P)\times(\text{$A$ 沿 $P$ 的元素之积).}$$

（正负的另一种理解见 [[Determinant Formula and Cofactors#^e00bf1|展开协因子的符号]]。）

**多重线性**：行列式对每一行线性（见 [[Determinants and Their Properties#^25af88|行列式基本性质3]]）。拆 $2\times2$ 行列式时，只有"占据不同行不同列"的组合（$ad$、$bc$）幸存，含全零行/列的项消失。

## 2. 协因子 (Cofactors)

展开式 $\det A=a_{11}C_{11}+a_{12}C_{12}+\cdots$ 中 $C_{ij}$ 是**协因子**；由协因子组成的矩阵称**伴随矩阵 (adjugate)**。

### 协因子的符号 (Sign)

^e00bf1

符号为 $(-1)^{i+j}$，来自把元素"归位"到主对角线所需的交换次数。

> [!note] 证明
> 把 $a_{ij}$ 搬到 $(1,1)$ 需向上跨 $i-1$ 行、向左跨 $j-1$ 列，共 $(i-1)+(j-1)$ 次交换，每次变号（交换一次符号变反一次 ^5c8d1b），故符号为 $(-1)^{i+j}$。

## 3. 逆矩阵公式 (Inverse via Cofactors)

$$A^{-1}=\frac{1}{\det A}C^{\mathsf T},\qquad\text{等价于}\quad A\cdot C^{\mathsf T}=\det(A)\,I.$$

**证明**：$P=A\cdot C^{\mathsf T}$ 的 $P_{ij}=$（$A$ 第 $i$ 行）·（$C$ 第 $j$ 行）。

- **对角 $i=j$**：$P_{ii}=a_{i1}C_{i1}+\cdots+a_{in}C_{in}=\det A$；
- **非对角 $i\neq j$**：$P_{ij}=0$，因为它等于一个"第 $i$ 行与第 $j$ 行相同"的矩阵的行列式。 ^e5cada

故 $A\cdot C^{\mathsf T}=\det(A)I$，两边除以 $\det A$ 即得逆公式。

### 非对角元素为零的本质 (Why Off-Diagonal = 0)

^7b5043

如 $P_{12}=a_{11}C_{21}+\cdots+a_{1n}C_{2n}$ 实际是下述矩阵 $B$ 的行列式——它的第 2 行被填入了第 1 行的数（两行相同），故 $\det B=0$：

$$B=\begin{bmatrix}a_{11}&\cdots&a_{1n}\\ a_{11}&\cdots&a_{1n}\\ a_{31}&\cdots&a_{3n}\\ \vdots&&\vdots\end{bmatrix}.$$

（即 [[Determinant Formula and Cofactors#^e5cada|非对角线元素的填字游戏]]。）

---

> [!important] 一句话总结
> 协因子展开适合理解结构与小规模计算；大规模行列式应交给消元（三角化后乘对角线）。
