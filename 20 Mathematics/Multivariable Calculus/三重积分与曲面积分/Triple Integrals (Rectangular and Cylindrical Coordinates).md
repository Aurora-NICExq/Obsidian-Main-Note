---
aliases: ["triple integral（直角坐标与柱坐标）", Triple Integrals, Triple Integrals in Cylindrical Coordinates]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Spherical Coordinates and Surface Area|球坐标与表面积]], [[Change of Variables and the Jacobian|换元法和雅各比矩阵]], [[Divergence Theorem (Gauss's Theorem)|散度定理（高斯定理）]], [[Double Integrals|二重积分]]"
down: "[[Spherical Coordinates and Surface Area|球坐标与表面积]]"
---
# Triple Integrals (Rectangular and Cylindrical Coordinates)

> [!summary] 核心结论
> 三重积分 (triple integral) $\iiint_E f\,dV$ 累加空间体积贡献；计算靠切片把 3D 降到 1D。**柱坐标 (cylindrical coordinates)** 是二维极坐标在三维的自然推广，体积元 $dV=r\,dr\,d\theta\,dz$。

前置知识：[[Double Integrals|二重积分]]、[[Change of Variables and the Jacobian|换元法和雅各比矩阵]]。

---

## 1. 意义 (Meaning)

对空间区域 $E$ 上的标量函数 $f$：把 $E$ 切成小盒子 $\Delta V_i$，用 $f(\text{点}_i)\Delta V_i$ 近似加权体积取极限：

$$\iiint_E f\,dV,\qquad \iiint_E 1\,dV=\mathrm{Vol}(E).$$

## 2. 迭代积分：切片降维 (Slicing)

先对 $z$ 积分：

$$\iiint_E f\,dV=\iint_D\left(\int_{z_1(x,y)}^{z_2(x,y)}f\,dz\right)dA.$$

做题关键：把 $E$ 描述清楚（常用"上下两曲面夹着 + 投影到 $xy$ 平面 $D$"）。

## 3. 应用：质量、质心、平均值 (Applications)

密度 $\rho$：质量 $m=\iiint_E\rho\,dV$；平均值 $f_{\text{avg}}=\dfrac{1}{\mathrm{Vol}(E)}\iiint_E f\,dV$；质心分量把 $f$ 换成 $x\rho,y\rho,z\rho$。

## 4. 柱坐标 (Cylindrical Coordinates)

$$x=r\cos\theta,\quad y=r\sin\theta,\quad z=z,\qquad dV=r\,dr\,d\theta\,dz.$$

其中 $r$ 是局部体积伸缩因子，与 [[Change of Variables and the Jacobian|Jacobian]] 一致，本质同 [[Applications of Determinants#^3bbccb|行列式求体积]]（线性近似下的体积缩放）：

$$\iiint_E f\,dV=\iiint_{E'}f(r\cos\theta,r\sin\theta,z)\,r\,dr\,d\theta\,dz.$$

## 5. 何时用柱坐标 (When to Use)

出现 $x^2+y^2$、圆柱 $x^2+y^2=a^2$、圆盘投影，或约束形如 $x^2+y^2\le g(z)$（化为 $r^2\le g(z)$）时优先。

## 6. 例：圆柱体体积 (Example)

半径 $a$、高 $h$：

$$\mathrm{Vol}=\int_0^{2\pi}\int_0^a\int_0^h r\,dz\,dr\,d\theta=2\pi\cdot\frac{a^2}{2}\cdot h=\pi a^2 h.$$

## 7. Checklist

1. 画图找上下边界（$z=z_1,z_2$）与投影 $D$；
2. 有 $x^2+y^2$/圆柱对称 ⟹ 柱坐标；
3. 柱坐标别漏 Jacobian 的 $r$。

---

> [!important] 一句话总结
> 三重积分先描述空间区域、再选坐标；柱坐标必带体积元 $r\,dr\,d\theta\,dz$。
