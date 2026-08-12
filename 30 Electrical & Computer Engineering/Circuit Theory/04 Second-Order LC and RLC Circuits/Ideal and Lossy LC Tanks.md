---
title: "Ideal and Lossy LC Tanks"
aliases: ["理想与有损 LC 谐振回路", "Ideal and Lossy LC Tank"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: []
related: ["[[LC Circuits and Second-Order ODEs]]", "[[Introduction to RLC Circuits]]", "[[Inductors and RL Circuits]]", "[[Capacitors and Their Properties]]"]
---
# Ideal and Lossy LC Tanks

## 理想与有损 LC 谐振回路

> [!definition] 谐振回路
> **谐振回路**是电感与电容的并联（或串联）组合，在其电场与磁场之间交换能量，以谐振频率振荡。

---
## 1. 理想（无损）LC 谐振回路

无电阻时，并联 LC 回路服从无阻尼项的二阶方程（参见 [[LC Circuits and Second-Order ODEs#2nd-Order Differential Equations]]）：
$$
LC\frac{d^2v}{dt^2}+v=0
$$

> [!theorem] 谐振频率
> 无损谐振回路以谐振频率做正弦振荡，无衰减：
> $$
> \omega_0=\frac{1}{\sqrt{LC}},\qquad f_0=\frac{1}{2\pi\sqrt{LC}}
> $$

能量守恒，在每个四分之一周期内在 $C$ 和 $L$ 之间完全交换：
$$
\frac{1}{2}C V_0^2=\frac{1}{2}L I_{\max}^2
$$

---
## 2. 有损（阻尼）谐振回路

实际谐振回路包含损耗，用并联在 $L$ 和 $C$ 两端的电阻 $R$ 建模：

![[tikz-ideal-and-lossy-lc-tanks-01.svg]]

对于并联 RLC 谐振回路，阻尼（奈培）频率和阻尼频率分别为：
$$
\alpha=\frac{1}{2RC},\qquad \omega_d=\sqrt{\omega_0^2-\alpha^2}
$$

当 $\alpha<\omega_0$ 时，谐振回路处于**欠阻尼**状态，呈衰减正弦振荡：
$$
v(t)=V_0\,e^{-\alpha t}\cos(\omega_d t+\varphi)
$$

---
## 3. 品质因数

> [!definition] 品质因数 $Q$
> $Q$ 衡量能量显著衰减前振荡的弧度数。对于并联谐振回路：
> $$
> Q=\frac{\omega_0}{2\alpha}=R\sqrt{\frac{C}{L}}=\omega_0 R C
> $$
> $R$ 越大（损耗越小），$Q$ 越高，振荡衰减越慢。

> [!attention] 极限情况
> 当 $R\to\infty$（无损耗）时，$\alpha\to0$，$\omega_d\to\omega_0$，$Q\to\infty$——恢复到 §1 中的理想无损谐振回路。

---
## 4. 算例

> [!example] 谐振回路的振铃衰减
> 一个 $L=1\ \mathrm{mH}$、$C=10\ \mathrm{nF}$ 的谐振回路：
> $$
> \omega_0=\frac{1}{\sqrt{LC}}=\frac{1}{\sqrt{10^{-3}\cdot 10^{-8}}}=10^{5}\ \mathrm{rad/s}.
> $$
> 若并联 $R=10\ \mathrm{k\Omega}$，则 $\alpha=\dfrac{1}{2RC}=5\times10^{3}\ \mathrm{s^{-1}}$，
> 因此 $\alpha\ll\omega_0$：谐振回路处于强欠阻尼状态，以接近 $\omega_0$ 的频率振荡，其包络按 $e^{-\alpha t}$ 衰减。

---
## 参见
- [[LC Circuits and Second-Order ODEs]]
- [[Introduction to RLC Circuits#3. RLC Circuits]]
- [[Inductors and RL Circuits]]
- [[Capacitors and Their Properties#4. Energy Storage and Power]]
