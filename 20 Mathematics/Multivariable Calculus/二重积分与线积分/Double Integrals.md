---
aliases: [二重积分, Double Integrals]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Double Integrals in Polar Coordinates and Applications|极坐标的二重积分应用]], [[Change of Variables and the Jacobian|换元法和雅各比矩阵]], [[Green's Theorem (Circulation Form)|格林定理]], [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]"
down: "[[Double Integrals in Polar Coordinates and Applications|极坐标的二重积分应用]]"
---
# Double Integrals

> [!summary] 核心结论
> 二重积分 (double integral) $\iint_R f\,dA$ 把二维区域上的小面积贡献 $f(x_i,y_i)\Delta A_i$ 累加取极限，几何上表示曲面与 $xy$ 平面之间的**带符号体积 (signed volume)**。计算靠**切片 (slicing)** 化为迭代积分，难点在描述区域 $R$。

前置知识：[[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]、[[Total Differential and the Chain Rule|微分、链式法则]]。

---

## 1. 几何意义 (Geometry)

类比一元：$\int_a^b f\,dx$ 是曲线下方（带符号）面积；二元 $\iint_R f(x,y)\,dA$ 是曲面 $z=f(x,y)$ 在区域 $R$ 上方与 $xy$ 平面之间的带符号体积。$dA$ 的 $A$ 是 area（面积元素），两个 $\int$ 表示在二维区域里累加。

![[tikz-double-integrals-01.svg]]

## 2. 定义：二维黎曼和 (2D Riemann Sum)

把 $R$ 划分成小块，每块面积 $\Delta A_i$，取点 $(x_i,y_i)$，用 $f(x_i,y_i)\Delta A_i$ 近似小柱体体积，求和并令最大块面积 $\to0$ 取极限即 $\iint_R f\,dA$。

## 3. 计算：迭代积分 (Iterated Integral)

核心思想是**切片**：固定 $x$ 用平行于 $yz$ 平面的平面切出竖直切片，面积 $S(x)=\int f(x,y)\,dy$，再沿 $x$ 累加：

$$\iint_R f\,dA=\int_{a}^{b}\left(\int_{g_1(x)}^{g_2(x)}f(x,y)\,dy\right)dx.$$

> [!warning] 关键点
> 内层积分的上下限通常**依赖外层变量**；外层上下限必须是**纯常数**。先对 $y$、再对 $x$ 时 $dA=dy\,dx$（反之 $dx\,dy$）。

## 4. 标准流程 (Workflow)

1. **画 $R$**，明确投影区域与边界曲线；
2. 选切片方向（竖切：$y\in[g_1(x),g_2(x)],x\in[a,b]$；横切对调）；
3. 写迭代积分；
4. 先算内层（外层变量当常数），再算外层。

## 5. 例题 (Examples)

- **方形区域**：$\int_0^1\int_0^1(1-x^2-y^2)\,dy\,dx$，边界为常数。
- **四分之一圆盘**：$R:x^2+y^2\le1$（第一象限），固定 $x$ 时 $y:0\to\sqrt{1-x^2},\ x:0\to1$。直角坐标需三角代换，换 [[Double Integrals in Polar Coordinates and Applications|极坐标]] 更自然。

## 6. 交换积分次序 (Switching Order)

$$\int_0^1\int_{x}^{\sqrt x}\frac{e^y}{y}\,dy\,dx$$

$\int\frac{e^y}{y}\,dy$ 无初等原函数。改为固定 $y$ 切片：$x$ 从 $y^2$ 到 $y$、$y$ 从 $0$ 到 $1$，则内层对 $x$ 只算"长度"，$\frac{e^y}{y}$ 当常数，问题可解。

> [!note] 交换次序的本质
> 不是"交换符号"，而是**重画区域、重写边界**——用另一种方式描述同一个 $R$。

---

> [!important] 一句话总结
> 二重积分 = 区域上小柱体体积之和的极限；计算靠切片，内层界常依赖外层，换序须重描区域。
