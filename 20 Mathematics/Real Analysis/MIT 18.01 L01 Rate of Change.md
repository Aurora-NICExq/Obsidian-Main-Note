---
aliases: [MIT18.1-Lec01-变化率（Rate of Change）, 变化率, Rate of Change]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L02 Limits]], [[MIT 18.01 L03 Derivatives]], [[Differentiation|求导]]"
down: "[[MIT 18.01 L02 Limits]]"
---
# Rate of Change

> [!summary] 核心结论
> 变化率 (rate of change) 把"变化快慢"统一表示为**差商 (difference quotient)** 的极限；导数 (derivative) 就是瞬时变化率 (instantaneous rate of change)。

> 关键词：平均变化率、瞬时变化率、差商、切线、量纲。

---

## 1. 学习目标 (Goals)

- 用统一的数学对象表达"变化快慢"：斜率 (slope) / 速度 (velocity) / 增长率 (growth rate)。
- 理解"瞬时"概念为何必须通过**极限 (limit)** 定义。

## 2. 核心概念与记号 (Concepts & Notation)

- 增量 (increment)：$\Delta x$、$\Delta y=f(x+\Delta x)-f(x)$。
- 平均变化率（割线斜率，secant slope）：$\dfrac{\Delta y}{\Delta x}=\dfrac{f(x+\Delta x)-f(x)}{\Delta x}$。
- 差商 (difference quotient)：记 $\Delta x=h$，即 $\dfrac{f(x+h)-f(x)}{h}$。
- 量纲 (dimension)：变化率单位 =（输出单位）/（输入单位）。

## 3. 从割线到切线 (Secant → Tangent)

割线给出平均趋势；当第二个点沿曲线逼近第一个点，割线趋于**切线 (tangent line)**。"瞬时斜率"就是割线斜率在 $h\to 0$ 下的稳定极限——其严格化见 [[MIT 18.01 L02 Limits]]。

## 4. 典型例题 (Worked Examples)

### 例 1：用差商求 $f(x)=x^2$ 的导数

$$\frac{(x+h)^2-x^2}{h}=\frac{2xh+h^2}{h}=2x+h\ \xrightarrow{h\to 0}\ f'(x)=2x.$$

### 例 2：瞬时速度

位移 $s(t)=t^3$，平均速度 $\dfrac{(t+h)^3-t^3}{h}=3t^2+3th+h^2\xrightarrow{h\to 0}v(t)=3t^2$。

### 例 3：从数据表估计

在目标点左右取小步长 $h$，比较 $\dfrac{f(a+h)-f(a)}{h}$ 与 $\dfrac{f(a)-f(a-h)}{h}$；若两者接近，则瞬时变化率约为该公共值。

## 5. 方法清单 (Method)

- 从定义出发：**写差商 → 化简（消 $h$）→ 取极限**。
- 估算题：先确认 $h$ 足够小，再用左右差分自检。

## 6. 易错点 (Pitfalls)

- 把 $h=0$ 直接代入差商（应取极限）。
- 把只在 $h\neq 0$ 成立的化简误当作在 $h=0$ 成立。
- 忽略单位。

---

> [!important] 一句话总结
> 变化率把"变化快慢"统一为差商的极限，导数就是瞬时变化率——它是整门微积分的起点。
