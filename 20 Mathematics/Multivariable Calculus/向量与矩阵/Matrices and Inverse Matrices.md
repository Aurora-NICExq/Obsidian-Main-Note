---
aliases: [矩阵与逆矩阵, Matrices and Inverse Matrices]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Matrices and Equations of Planes|矩阵和平面方程]], [[Cross Product and Determinants|行列式叉积]], [[Change of Variables and the Jacobian|换元法和雅各比矩阵]], [[Eigenvalues and Eigenvectors|特征值和特征向量]]"
down: "[[Change of Variables and the Jacobian|换元法和雅各比矩阵]]"
---
# Matrices and Inverse Matrices

> [!summary] 核心结论
> 矩阵 (matrix) 表示线性变换，逆矩阵 (inverse matrix) 把变换**撤销**。多变量微积分中的局部线性化（雅可比矩阵）与换元都依赖这一视角。

---

## 1. 线性关系与坐标变换 (Linear Relations)

现实中很多变量关系是线性的；换坐标系时新坐标 $U$ 是旧坐标 $X$ 的线性组合：

$$U=AX,$$

其中 $A$ 是系数矩阵，$X,U$ 为列向量。雅可比矩阵 (Jacobian) 正是非线性映射的"局部线性化"版本（见 [[Change of Variables and the Jacobian|换元法和雅各比矩阵]]）。

## 2. 矩阵乘法 (Matrix Multiplication)

- **规则**：积的每个元素是"左矩阵某行"与"右矩阵某列"的点积；
- **维度**：能相乘取决于内维度匹配；
- **不可交换**：$AB\neq BA$ 一般成立，推导时须区分左乘/右乘。

## 3. 线性变换视角 (Transformations)

把矩阵当作"动作"：

- **单位矩阵 $I$**：$IX=X$，即恒等变换 (identity)；
- **旋转矩阵 (rotation)**：把 $(x,y)\mapsto(-y,x)$ 等几何动作写成矩阵。

## 4. 旋转矩阵示例 (Rotation Example)

平面 $90^\circ$ 逆时针旋转 $(x,y)\mapsto(-y,x)$ 写成矩阵：

$$R=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},\qquad R\begin{pmatrix}x\\ y\end{pmatrix}=\begin{pmatrix}-y\\ x\end{pmatrix}.$$

它没有实特征值（纯旋转），见 [[Eigenvalues and Eigenvectors#^fa8cf9|线性代数中的旋转矩阵]]。用幂展示几何意义：$R^2=-I$（旋转 $180^\circ$），$R^4=I$（转四次复原）。

## 5. 逆矩阵 (Inverse)

逆矩阵是"撤销变换"的工具：方阵 $A^{-1}$ 满足 $AA^{-1}=A^{-1}A=I$。

- **解线性系统**：$AX=B$ 左乘 $A^{-1}$ 得 $X=A^{-1}B$（必须左乘，尺寸与消去逻辑所需）；
- **反向换元**：若 $U=AX$ 是坐标变换，则 $X=A^{-1}U$ 把 $U$ 变回 $X$。

---

> [!important] 一句话总结
> 矩阵是局部线性化的语言，逆矩阵是反向换元与解线性系统的工具。
