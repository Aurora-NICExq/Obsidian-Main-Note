---
aliases: [MIT18.1-Lec12-相关变化率（Related Rates）, 相关变化率, Related Rates]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L05 Implicit Differentiation]], [[MIT 18.01 L11 Max-Min Problems]], [[MIT 18.01 L13 Newton's Method]]"
down: "[[MIT 18.01 L13 Newton's Method]]"
---
# Related Rates

> [!summary] 核心结论
> 相关变化率 (related rates)：变量之间有几何/物理约束，且都随时间变化。**先写变量关系，再对时间 $t$ 求导**（隐式求导的时间版），最后代入特定时刻数据求目标速率。

> 关键词：对时间求导、几何约束、代入时刻数据、单位。

---

## 1. 核心思想 (Idea)

变量间有约束 $F(x,y,\dots)=0$，但都依赖时间 $x(t),y(t),\dots$。对 $t$ 求导（用 [[MIT 18.01 L05 Implicit Differentiation|链式/隐式求导]]）得到速率之间的关系。

## 2. 标准流程 (Procedure)

1. 画图并标注变量；
2. 写约束方程；
3. 对 $t$ 求导；
4. **代入特定时刻**数据；
5. 解出目标速率；
6. 单位检查。

## 3. 例题 (Examples)

- **梯子下滑**：$x^2+y^2=L^2$，对 $t$ 求导得 $2x\dot x+2y\dot y=0$，即 $\dot y=-\dfrac{x}{y}\dot x$。
- **圆面积变化**：$A=\pi r^2\Rightarrow \dot A=2\pi r\,\dot r$。

## 4. 易错点 (Pitfalls)

- **先代值再求导**（必须先求导，后代时刻值）；把 $\tfrac{d}{dt}$ 误写成 $\tfrac{d}{dx}$；图没画导致约束方程写错。

---

> [!important] 一句话总结
> 相关变化率 = 写约束 → 对时间求导 → 代时刻值；切忌过早代入数值。
