---
aliases: [复变函数, Complex Analysis, Complex Variables, MIT 18.04, 复变函数 MOC]
tags: [math, complex_analysis, MOC]
up: "[[Mathematics MOC]]"
related: ["[[Multivariable Calculus MOC]]", "[[Integral Calculus and Differential Equations MOC]]", "[[The Laplace Transform]]"]
down:
  - "[[Complex Algebra and the Complex Plane]]"
  - "[[Analytic Functions]]"
  - "[[Line Integrals and Cauchy's Theorem]]"
  - "[[Cauchy's Integral Formula]]"
  - "[[Harmonic Functions]]"
  - "[[Two-Dimensional Hydrodynamics and Complex Potentials]]"
  - "[[Taylor and Laurent Series]]"
  - "[[Residue Theorem]]"
  - "[[Definite Integrals Using Residues]]"
  - "[[Conformal Transformations]]"
  - "[[Argument Principle]]"
  - "[[Laplace Transform]]"
  - "[[Analytic Continuation and the Gamma Function]]"
---
# Complex Analysis (MIT 18.04) MOC

> 课程底本：[MIT 18.04 Complex Variables with Applications (Spring 2018)](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/)（Jeremy Orloff）。工科向：围道积分、留数算实积分、调和函数、二维流、共形映射、幅角原理 / Nyquist、Laplace 与 $\Gamma$。讲义 / 作业 / 考试可离线下载。

![[ca-moc-roadmap.svg]]

## 01 基础
- [[Complex Algebra and the Complex Plane]]：代数、极坐标、Euler、$n$ 次方根、$\arg$/$\mathrm{Log}$ 分支、映射视角
- [[Analytic Functions]]：复导数、CR、初等函数画廊、支割线复合

## 02 积分
- [[Line Integrals and Cauchy's Theorem]]：复线积分、路径无关、Cauchy 定理、变形、$\oint dz/z=2\pi i$
- [[Cauchy's Integral Formula]]：CIF、导数公式、$C^\infty$、估计、Liouville、最大模

## 03 调和与流动
- [[Harmonic Functions]]：Laplace、共轭、正交水平集、均值 / 极值
- [[Two-Dimensional Hydrodynamics and Complex Potentials]]：复势 $\Phi=\phi+i\psi$、源 / 涡 / 停滞流

## 04 级数与留数
- [[Taylor and Laurent Series]]：幂级数、Laurent 环域、奇点分类
- [[Residue Theorem]]：留数计算、留数定理、无穷远留数
- [[Definite Integrals Using Residues]]：半圆 / 钥匙孔 / 凹陷围道、三角有理积分

## 05 映射、稳定性与变换
- [[Conformal Transformations]]：共形、Möbius、标准映射库
- [[Argument Principle]]：$N-P$、Rouché、Nyquist
- [[Laplace Transform]]：ROC、传递函数、Bromwich
- [[Analytic Continuation and the Gamma Function]]：延拓唯一性、$\Gamma$、反射公式

## 插图（预生成 SVG）

嵌入 `90 Assets/diagrams/complex-analysis/`（文件名形如 `ca-….svg`）。重新生成：

```bash
cd "90 Assets/scripts/complex_analysis"
.venv/bin/python generate_all.py
```
