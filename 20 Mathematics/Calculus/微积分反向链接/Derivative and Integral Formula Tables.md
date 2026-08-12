---
aliases: [导数和积分公式, Derivative and Integral Formula Tables]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Integration by Parts|分部积分]], [[Partial Fraction Decomposition|部分分式]], [[Chain Rule for Variable-Limit Integrals (Worked Example)|不定积分链式求导法则示例]]"
down: ""
---
# Derivative and Integral Formula Tables

> [!summary] 核心结论
> 基本初等函数的导数 (derivative) 与积分 (integral) 公式速查表。由于积分是求导的逆运算，左右两列**互为镜像**——记牢左列求导公式，右列积分公式即可反推。

> [!note] 配套笔记
> 这些公式是 [[Integration by Parts|分部积分]]、[[Partial Fraction Decomposition|部分分式]] 等积分技巧的基石；变限积分的链式求导见 [[Chain Rule for Variable-Limit Integrals (Worked Example)|不定积分链式求导法则示例]]。

---

## 公式对照表 (Derivatives ↔ Integrals)

$$
\begin{align*}
\textbf{导数公式} & \qquad \textbf{积分公式} \\[1em]
\frac{\mathrm{d}}{\mathrm{d}x} x^a = a x^{a-1} & \qquad \int x^a \mathrm{d}x = \frac{x^{a+1}}{a+1} + C \quad (\text{如果 } a \neq -1) \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \ln(x) = \frac{1}{x} & \qquad \int \frac{1}{x} \mathrm{d}x = \ln|x| + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} e^x = e^x & \qquad \int e^x \mathrm{d}x = e^x + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} b^x = b^x \ln(b) & \qquad \int b^x \mathrm{d}x = \frac{b^x}{\ln(b)} + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \sin(x) = \cos(x) & \qquad \int \cos(x) \mathrm{d}x = \sin(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \cos(x) = -\sin(x) & \qquad \int \sin(x) \mathrm{d}x = -\cos(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \tan(x) = \sec^2(x) & \qquad \int \sec^2(x) \mathrm{d}x = \tan(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \sec(x) = \sec(x) \tan(x) & \qquad \int \sec(x) \tan(x) \mathrm{d}x = \sec(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \cot(x) = -\csc^2(x) & \qquad \int \csc^2(x) \mathrm{d}x = -\cot(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \csc(x) = -\csc(x) \cot(x) & \qquad \int \csc(x)\cot(x) \mathrm{d}x = -\csc(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \sin^{-1}(x) = \frac{1}{\sqrt{1-x^2}} & \qquad \int \frac{1}{\sqrt{1-x^2}}\mathrm{d}x = \sin^{-1}(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \tan^{-1}(x) = \frac{1}{1+x^2} & \qquad \int \frac{1}{1+x^2}\mathrm{d}x = \tan^{-1}(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \sec^{-1}(x) = \frac{1}{|x|\sqrt{x^2-1}} & \qquad \int \frac{1}{|x|\sqrt{x^2-1}}\mathrm{d}x = \sec^{-1}(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \sinh(x) = \cosh(x) & \qquad \int \cosh(x)\mathrm{d}x = \sinh(x) + C \\[0.5em]
\frac{\mathrm{d}}{\mathrm{d}x} \cosh(x) = \sinh(x) & \qquad \int \sinh(x)\mathrm{d}x = \cosh(x) + C
\end{align*}
$$
