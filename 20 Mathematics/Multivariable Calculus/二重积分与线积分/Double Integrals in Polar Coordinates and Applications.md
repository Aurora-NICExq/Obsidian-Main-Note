---
aliases: [极坐标的二重积分应用, Double Integrals in Polar Coordinates, Polar Double Integrals]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Double Integrals|二重积分]], [[Change of Variables and the Jacobian|换元法和雅各比矩阵]], [[Green's Theorem (Circulation Form)|格林定理]], [[Triple Integrals (Rectangular and Cylindrical Coordinates)|triple integral（直角坐标与柱坐标）]]"
down: ""
---
# Double Integrals in Polar Coordinates and Applications

> [!summary] 核心结论
> 极坐标 (polar coordinates) 适合圆形/扇形区域，关键是面积元必须带 Jacobian 因子：$dA=r\,dr\,d\theta$（不是 $dr\,d\theta$）。二重积分的物理应用（面积、质量、平均值、质心、转动惯量）都是"权重 × 量"的积分。

前置知识：[[Double Integrals|二重积分]]、[[Change of Variables and the Jacobian|换元法和雅各比矩阵]]。

---

## 1. 为何用极坐标 (Why Polar)

"四分之一单位圆盘"用直角坐标会出现 $\sqrt{1-x^2}$ 边界，难算；换极坐标后边界直接变成常数 $r=1$。

## 2. 定义与面积元 (Definition & Area Element)

$x=r\cos\theta,\ y=r\sin\theta$。小扇形块两边近似 $\Delta r$ 与弧长 $r\Delta\theta$，故 $\Delta A\approx r\,\Delta r\,\Delta\theta$，极限得

$$dA=r\,dr\,d\theta.$$

![[tikz-double-integrals-in-polar-coordinates-and-applicat-01.svg]]

## 3. 设界："先 $r$ 后 $\theta$" (Setting Limits)

极坐标按射线方向切片：固定 $\theta$ 沿射线让 $r$ 变化。

$$\iint_R f\,dA=\int_{\alpha}^{\beta}\int_{r_1(\theta)}^{r_2(\theta)}f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta.$$

口诀：**先定方向 $\theta$，再沿该方向看能走多远 $r$**。

## 4. 例题 (Example)

$\iint_R(1-x^2-y^2)\,dA$，$R$ 为第一象限四分之一单位圆盘。极坐标下 $x^2+y^2=r^2$，$0\le r\le1,0\le\theta\le\tfrac\pi2$：

$$\int_0^{\pi/2}\int_0^1(1-r^2)\,r\,dr\,d\theta=\frac\pi8.$$

> [!tip] 何时该用极坐标
> 取决于"区域更简单"还是"被积函数更简单"。若函数本就简单（如 $f=x$），换极坐标反而多出三角函数。

## 5. 二重积分的应用 (Applications)

设密度 $\delta(x,y)$：

- **面积**：$\text{Area}(R)=\iint_R 1\,dA$；
- **质量**：$m=\iint_R\delta\,dA$；
- **平均值**：$\bar f=\dfrac{1}{\text{Area}}\iint_R f\,dA$（不均匀时加权）；
- **质心**：$\bar x=\dfrac1m\iint_R x\,\delta\,dA,\ \bar y=\dfrac1m\iint_R y\,\delta\,dA$；
- **转动惯量**：绕原点 $I_0=\iint_R r^2\delta\,dA$，绕 $x$ 轴 $I_x=\iint_R y^2\delta\,dA$。

> [!warning] 质心不能用"$\bar r,\bar\theta$"算
> 不要分别求 $r,\theta$ 的平均来拼质心（圆盘的 $\bar r$ 不可能为 $0$）。

**例**：均匀圆盘（$\delta=1$，半径 $a$）绕中心 $I_0=\int_0^{2\pi}\int_0^a r^2\cdot r\,dr\,d\theta=\tfrac{\pi a^4}{2}$；绕圆周上一点（边界 $r=2a\cos\theta$）得 $\tfrac32\pi a^4$，即"难 3 倍"。

---

> [!important] 一句话总结
> 极坐标二重积分的关键不是 $x,y\to r,\theta$，而是 $dA=r\,dr\,d\theta$；应用都是"权重 × 量"的积分。
