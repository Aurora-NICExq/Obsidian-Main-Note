---
aliases: [行列式的应用, Applications of Determinants]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Determinants and Their Properties|行列式及其性质]], [[Determinant Formula and Cofactors|行列式公式及协因子]], [[Change of Variables and the Jacobian|换元法和雅各比矩阵]]"
down: ""
---
# Applications of Determinants

> [!summary] 核心结论
> 行列式 (determinant) 的应用都围绕一个问题：线性变换是否保体积、压缩体积或压扁空间。三大用途：克拉默法则 (Cramer's rule)、面积/体积缩放、判断线性无关性。

前置知识：[[Determinants and Their Properties|行列式及其性质]]、[[Determinant Formula and Cofactors|行列式公式及协因子]]。

---

## 1. 克拉默法则 (Cramer's Rule)

设 $A\mathbf x=\mathbf b$、$A$ 可逆，则 $\mathbf x=A^{-1}\mathbf b$。代入逆的协因子公式 $A^{-1}=\dfrac{1}{\det A}C^{\mathsf T}$：

$$\mathbf x=\frac{1}{\det A}C^{\mathsf T}\mathbf b,\qquad x_j=\frac{\det(B_j)}{\det A},$$

其中 $B_j$ 是把 $A$ 的第 $j$ 列替换成 $\mathbf b$ 所得矩阵（$C^{\mathsf T}\mathbf b$ 的第 $j$ 分量正是协因子展开 $\det B_j$，见 [[Determinant Formula and Cofactors#^7b5043|协因子展开替换向量]]）。

> [!note] 为何只剩 $x_j$
> $C$ 的第 $j$ 列与 $\mathbf b$ 的点积，利用"异类协因子展开为零"（[[Determinant Formula and Cofactors#^7b5043|异类协因子展开结果]]）得 $\det A\cdot x_j+0+\cdots=\det B_j$，故只剩 $x_j$。矩阵乘法细节见 [[How Matrix Multiplication Works|矩阵乘法的原理]]。

## 2. 行列式求体积 (Volume via Determinant)

^3bbccb

**$|\det A|$ 等于矩阵列向量所围平行多面体的体积。**

### 符号的意义 (Sign = Orientation)

$\det A$ 可为负：符号代表"手系/方向"。$+$ 保持右手系，$-$ 翻转为左手系，$0$ 无体积（被压扁）。

### 计算 (Computation)

消元（剪切）把 $A$ 变上三角 $U$，体积不变，等于主元之积：

$$\text{Volume}=\det A=\det U=p_1p_2\cdots p_n,$$

每个主元 $p_i$ 是该边垂直于前 $i-1$ 条边所成空间的"高度"，体积自然是这些高度之积。

### 连接微积分：雅可比行列式 (Jacobian)

多重积分换元（如直角→极坐标 $dx\,dy\to r\,dr\,d\theta$）时，**Jacobian 矩阵的行列式**是局部体积缩放因子（局部线性近似），这正是积分里出现 $J$（或 $r$）的原因（见 [[Change of Variables and the Jacobian|多重积分换元]]）。

---

> [!important] 一句话总结
> 行列式的应用都在问：线性变换如何改变体积——保持、缩放还是压扁；并由此得到克拉默法则与换元因子。
