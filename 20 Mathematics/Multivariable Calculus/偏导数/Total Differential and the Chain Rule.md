---
aliases: [微分、链式法则, Total Differential and the Chain Rule, Total Differential]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Functions of Several Variables, Level Sets, and Partial Derivatives|等值面、偏导数]], [[Gradient and Directional Derivative|梯度、方向导数]], [[Change of Variables and the Jacobian|换元法和雅各比矩阵]], [[Lagrange Multipliers|拉格朗日乘数法]]"
down: "[[Gradient and Directional Derivative|梯度、方向导数]]"
---
# Total Differential and the Chain Rule

> [!summary] 核心结论
> 全微分 (total differential) $df=f_x\,dx+f_y\,dy+f_z\,dz$ 是多元线性近似的核心工具。链式法则 (chain rule) 与换元都来自"先写 $df$，再把 $dx,dy,dz$ 按变量依赖关系继续展开"。注意 $df$ 是微分对象，**不是** $\Delta f$。

前置知识：[[Differentiation|求导]]、[[Functions of Several Variables, Level Sets, and Partial Derivatives|等值面、偏导数]]。

---

## 1. 从单变量微分说起 (1D Differential)

单变量里 $dy=f'(x)\,dx$，可用于隐函数求导（如由 $x=\sin y$ 推 $\tfrac{dy}{dx}=\tfrac{1}{\cos y}$）。

## 2. 全微分 (Total Differential)

对三元函数 $f(x,y,z)$：

$$df=f_x\,dx+f_y\,dy+f_z\,dz.$$

它编码了 $x,y,z$ 发生小变化时，$f$ 的一阶变化如何由各方向偏导"加权合成"。

> [!warning] $df\neq\Delta f$
> $\Delta x,\Delta y,\Delta z$ 是**数**；而 $dx,dy,dz,df$ 是**微分符号/对象**，用于组织线性近似与求导规则。不能把 $d$ 与 $\Delta$ 混着约分。

## 3. $df$ 的两种核心用法 (Two Uses)

**用法 A：线性近似 (tangent approximation)** — 把 $dx,dy,dz$ 用实际小增量 $\Delta x,\Delta y,\Delta z$ 代入，得一阶近似 ^aa8e28

$$\Delta f\approx f_x\Delta x+f_y\Delta y+f_z\Delta z.$$

这就是多元版"切平面近似"（见 [[Functions of Several Variables, Level Sets, and Partial Derivatives#^0abe80|二元函数的切平面近似]]）。

**用法 B：链式法则 (chain rule)** — 若 $x=x(t),y=y(t),z=z(t)$，除以 $dt$：

$$\frac{df}{dt}=f_x\frac{dx}{dt}+f_y\frac{dy}{dt}+f_z\frac{dz}{dt}.$$

可用"先代入变成一元函数再求导"核验，结果一致。

## 4. 多对多换元 (Change of Variables)

典型结构 $w=f(x,y)$，$x=x(u,v)$，$y=y(u,v)$。从微分出发：

$$dw=f_x\,dx+f_y\,dy,\quad dx=x_u\,du+x_v\,dv,\quad dy=y_u\,du+y_v\,dv,$$

代回并按 $du,dv$ 合并系数：

$$\frac{\partial f}{\partial u}=f_xx_u+f_yy_u,\qquad \frac{\partial f}{\partial v}=f_xx_v+f_yy_v.$$

> [!warning] 不能把 $\partial x$ 当公因子约分
> 与一元导数不同，单独的 $\partial f$ 没有独立意义；多对多换元须回到微分展开 + 系数匹配。系统的矩阵化处理见 [[Change of Variables and the Jacobian|换元法和雅各比矩阵]]。

## 5. 应用：极坐标偏导转写 (Polar Transcription)

当 $x=r\cos\theta,\ y=r\sin\theta$：

$$f_r=f_x\frac{\partial x}{\partial r}+f_y\frac{\partial y}{\partial r}=f_x\cos\theta+f_y\sin\theta,$$

同理得 $f_\theta$。即把 $(f_x,f_y)$ 翻译成 $(f_r,f_\theta)$。

## 6. 用链式法则推乘积/商法则 (Deriving Product/Quotient Rules)

把 $f=uv$、$g=u/v$ 看成 $u(t),v(t)$ 的复合，链式法则给出 $\tfrac{d(uv)}{dt}=vu'+uv'$、$\tfrac{d(u/v)}{dt}=\tfrac{u'v-uv'}{v^2}$——乘积法则只是链式法则的一个投影。

## 7. 做题流程 (Workflow)

1. 先写 $df$（或 $dw$）：变化拆成各偏导乘对应微分；
2. 有参数 $t$：把 $dx$ 换成 $\tfrac{dx}{dt}dt$，再除 $dt$；
3. 换元 $(u,v)$：先写 $dx,dy$ 关于 $du,dv$，代回收集系数；
4. 需近似：把 $dx,dy,dz$ 换成 $\Delta x,\Delta y,\Delta z$。

---

> [!important] 一句话总结
> 先写 $df$，再代入变量依赖关系——这是处理线性近似、链式法则与换元的统一稳定方法。
