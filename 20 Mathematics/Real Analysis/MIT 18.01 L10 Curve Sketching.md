---
aliases: [MIT18.1-Lec10-曲线描绘（Curve Sketching）, 曲线描绘, Curve Sketching]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L09 Linear and Quadratic Approximations]], [[MIT 18.01 L11 Max-Min Problems]]"
down: "[[MIT 18.01 L11 Max-Min Problems]]"
---
# Curve Sketching

> [!summary] 核心结论
> 曲线描绘 (curve sketching) 用**一阶导数 (first derivative)** 判断增减与极值，用**二阶导数 (second derivative)** 判断凹凸与拐点，再结合渐近线拼出全局形状。

> 关键词：增减表、极值、凹凸、拐点、渐近线、全局形状。

---

## 1. 一阶导数：增减与极值 (Monotonicity & Extrema)

- $f'>0$ 递增，$f'<0$ 递减；
- 临界点 (critical point)：$f'=0$ 或 $f'$ 不存在；
- 一阶判别 (first derivative test)：$f'$ 由 $+\to-$ 为极大，$-\to+$ 为极小。

## 2. 二阶导数：凹凸与拐点 (Concavity & Inflection)

- $f''>0$ 凹（concave up），$f''<0$ 凸（concave down）；
- 拐点 (inflection point)：凹凸性改变处（仅 $f''=0$ 不够，需变号）。

## 3. 推荐流程 (Recommended Order)

1. 定义域（分母为 $0$、根号、对数）；
2. 对称性（奇偶/周期）；
3. 零点与截距；
4. 算 $f'$：增减表，定极值；
5. 算 $f''$：凹凸表，定拐点；
6. 极限与渐近线：$x\to\pm\infty$ 及奇点附近。

## 4. 例题 (Examples)

- **多项式**：$f=x^3-3x$，$f'=3(x-1)(x+1)$（极值在 $x=\pm1$），$f''=6x$（拐点 $x=0$）。
- **有理函数**：$f=\dfrac{1}{x-1}$，$x\to1^\mp$ 时 $f\to\mp\infty$（竖直渐近线 $x=1$），$x\to\infty$ 时 $f\to0$（水平渐近线 $y=0$）。

## 5. 易错点 (Pitfalls)

- 把 $f''=0$ 当作必拐点；忘检查端点/不可导点；渐近线只看图不算极限。

---

> [!important] 一句话总结
> 一阶导定增减与极值，二阶导定凹凸与拐点，渐近线收束全局——按固定流程走最稳。
