---
aliases: [行列式及其性质, Determinants and Their Properties]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Determinant Formula and Cofactors|行列式公式及协因子]], [[Applications of Determinants|行列式的应用]], [[Singular Matrices|singular矩阵]]"
down: "[[Determinant Formula and Cofactors|行列式公式及协因子]]"
---
# Determinants and Their Properties

> [!summary] 核心结论
> 行列式 (determinant) 刻画体积缩放、可逆性与行变换的影响。三条基本性质（$\det I=1$、交换两行变号、单行线性）推出全部其余性质。**$\det A=0 \iff$ 矩阵奇异（不可逆）**。

前置知识：[[Matrices (Systems, Elimination, Inverse)|矩阵]]。

---

## 1. 三条基本性质 (Three Defining Properties)

1. **归一化**：$\det I=1$；
2. **交换两行变号**：故置换矩阵的行列式为 $\pm1$（见 [[Matrices (Systems, Elimination, Inverse)#置换矩阵 P (Permutation Matrix)|置换矩阵]]）；
3. **单行线性 (linear in each row)**：行列式对**每一行**线性，而非对整个矩阵线性。 ^25af88
   - 数乘：某行乘 $t$，行列式乘 $t$；
   - 加法：某行可拆开，其余行不变。

## 2. 推论 (Corollaries)

- **性质四**：两行相同 ⟹ $\det=0$。证明：交换该两行矩阵不变故 $D=D$，但交换变号故 $D=-D$，得 $D=0$（此时不可逆，见 [[Matrices (Systems, Elimination, Inverse)#^7ddbcc|矩阵的逆]]）。
- **性质五**：把某行的 $k$ 倍加到另一行，$\det$ 不变（消元不改变行列式）。
- **性质六**：有一行全为 $0$ ⟹ $\det=0$。
- **性质七**：三角矩阵 $\det=$ 对角线元素之积 $d_1\cdots d_n$（计算机就是先消元成三角再乘对角线）。
- **性质八**：$\det A=0\iff A$ 奇异（singular，见 [[Singular Matrices|singular矩阵]]）。可逆时消元后对角线无 $0$（各列有主元，见 [[Vector Spaces and Subspaces#阶梯形矩阵 (Row Echelon Form)|阶梯形矩阵]]）；不可逆时必有全零行。
- **性质九**：$\det(AB)=\det A\det B$，故 $\det(A^{-1})=1/\det A$。
- **性质十**：$\det(A^{\mathsf T})=\det A$，因此关于"行"的所有性质对"列"同样成立。

> [!note] 性质十的证明（$LDU$ 分解）
> 不做行交换时 $A=LDU$（$L,U$ 对角线全 $1$，$D$ 含主元）。则 $\det(A^{\mathsf T})=\det(U^{\mathsf T})\det(D^{\mathsf T})\det(L^{\mathsf T})=1\cdot\det D\cdot1=\det D=\det A$。$\blacksquare$

---

> [!important] 一句话总结
> 行列式为零表示体积被压扁，也表示矩阵不可逆；三条基本性质推出其余一切。
