---
aliases:
  - 匹配滤波
  - Matched Filtering
  - matched filter
  - 相关器
  - correlator
  - 最大SNR
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[Hypothesis Testing and Signal Detection]]"
  - "[[Wiener Filtering]]"
  - "[[Filtering]]"
  - "[[Transforms and Energy Spectra]]"
  - "[[Power Spectral Density]]"
down: []
---
# 匹配滤波：最大化 SNR 的相关器

> [!summary] 核心结论
> 在加性**白**噪声中检测**已知波形** $s(t)$，线性滤波器在采样时刻 $t_0$ 的输出 SNR 由 Cauchy–Schwarz 界定：最优冲激响应（可差一常数）为
> $$
> h(t)=s(t_0-t)
> $$
> ——即**匹配滤波器**（时间反转并对齐到 $t_0$）。最大 SNR $=2E/N_0$（双边密度 $N_0/2$ 约定下，$E=\int\lvert s\rvert^2$）。实现上等价于与 $s$ 做**相关**再在 $t_0$ 采样。有色噪声：先白化再匹配。它服务**检测**（下一判决阈值），与 Wiener（随机信号波形估计）问题不同。

> 底本：MIT 6.011 OCW Spring 2018 — matched filters；检测框架见 [[Hypothesis Testing and Signal Detection]]。

---
## 1. 问题设定

观测 $y(t)=s(t)+w(t)$，$w$ 为白、PSD $N_0/2$。已知 $s$，在时刻 $t_0$ 看线性滤波输出 $z(t_0)=(h*y)(t_0)$，定义
$$
\mathrm{SNR}=\frac{\lvert\text{信号分量}\rvert^2}{\mathbb{E}[\lvert\text{噪声分量}\rvert^2]}.
$$
目标：选 $h$ 最大化 SNR（不是直接最小化波形 MSE）。

![[ssi-matched.svg]]

---
## 2. 推导素描（白噪声）

信号分量 $\int h(\tau)s(t_0-\tau)\,d\tau$。噪声方差（白噪声）$\propto\lVert h\rVert^2=\int\lvert h\rvert^2$。由 Cauchy–Schwarz，
$$
\biggl\lvert\int h(\tau)s(t_0-\tau)\,d\tau\biggr\rvert^2\le\lVert h\rVert^2\lVert s\rVert^2,
$$
等号当 $h(\tau)\propto s(t_0-\tau)$。故匹配于**反转波形**。频域：$H(j\omega)\propto S^*(j\omega)e^{-j\omega t_0}$（相位对齐到采样时刻）。

最大 SNR（标准约定）
$$
\mathrm{SNR}_{\max}=\frac{2E}{N_0},\qquad E=\int_{-\infty}^{\infty}\lvert s(t)\rvert^2\,dt.
$$
只依赖信号能量与噪声密度，**与波形形状无关**——但「匹配」保证你真正达到这个界；错配滤波器则更差。

> [!example] 矩形脉冲匹配滤波
> $s(t)=A$，$0\le t\le T$，否则 0；$E=A^2 T$。白噪声密度 $N_0/2$。匹配到 $t_0=T$：$h(t)=A$（$0\le t\le T$）（常数增益不计）。输出信号在 $t=T$ 为 $\int_0^T A\cdot A\,dt=A^2 T$。噪声方差 $= (N_0/2)\int_0^T A^2\,dt=(N_0/2)A^2 T$。
> $$
> \mathrm{SNR}=\frac{(A^2 T)^2}{(N_0/2)A^2 T}=\frac{2A^2 T}{N_0}=\frac{2E}{N_0}.
> $$
> 数值：$A=1$，$T=1\,\mathrm{ms}$，$N_0=10^{-6}$ ⇒ $E=10^{-3}$，$\mathrm{SNR}_{\max}=2\cdot 10^{-3}/10^{-6}=2000$（约 $33\,\mathrm{dB}$）。相关器观点：计算 $\int_0^T y(t)A\,dt$ 与上述 $z(T)$ 相同。

---
## 3. 相关器等价

因果实现常用：**将 $y(t)$ 与 $s(t)$ 相乘积分**（或用 $h(t)=s(T-t)$ 的滤波器）至符号结束时刻采样。有限观测窗口 $[0,T]$ 上，匹配滤波 ↔ 相关统计量
$$
\ell=\int_0^T y(t)s(t)\,dt
$$
（实信号）。在白高斯下，$\ell$ 是检测的充分统计量，再与阈值比较即 LRT（见上一篇）。

> [!warning] 匹配滤波 ≠ Wiener 去噪
> Wiener 估随机过程的波形，目标 MSE；匹配滤波对**已知确定性** $s$ 最大化**采样瞬间 SNR**，服务假设检验。信号若是随机消息波形，问题变成估计 / 通信接收机结构，准则与公式都不同。

---
## 4. 有色噪声

若噪声 PSD $S_w(\omega)$ 非白：先通过白化滤波器 $1/\sqrt{S_w}$（谱因子），再对白化后的信号波形做匹配；合并后
$$
H(j\omega)\propto\frac{S^*(j\omega)}{S_w(\omega)}e^{-j\omega t_0}.
$$
直觉：在噪声强的频带自动抑制，在信号强、噪声弱的频带加重——与非因果 Wiener 的 $S_x/(S_x+S_w)$ **形似但准则不同**（这里信号已知确定，分母只有噪声谱）。

---
## 5. 雷达模糊与通信符号

- **雷达**：发射脉冲 $s$，回波延迟未知 ⇒ 一组匹配滤波 / 相关对可能延迟扫描；距离分辨率与脉宽 / 带宽有关。
- **通信**：已知脉冲成形 $p(t)$，匹配 $p(-t)$ 后按符号周期采样（再加均衡抗 ISI）。在 AWGN、无 ISI 时匹配滤波 + 采样是最优前端。

输出 SNR $=2E/N_0$ 直接进入误码公式（如 BPSK $Q(\sqrt{2E_b/N_0})$）——连接检测理论与链路预算。

---
## 6. 采样时刻与因果实现细节

匹配到 $t_0$ 意味着：若 $s$ 支撑在 $[0,T]$，常取 $t_0=T$，使 $h(t)=s(T-t)$ 在 $[0,T]$ 上因果。过早采样（$t_0<T$）丢掉尚未进入的能量，SNR 严格低于 $2E/N_0$。多径 / 未知到达时间时，接收机对一簇延迟各跑一个匹配支路（或用匹配滤波输出的连续时间包络再峰值搜索）——雷达距离门、通信定时恢复同构。

离散时间：已知序列 $s[n]$，匹配 $h[n]=s[N-1-n]$，在 $n=N-1$ 取输出。FFT 快速相关是大规模码（如扩频）的实现手段，数学仍是同一相关统计量。

---
## 7. 与课程主线收束

1. [[Transforms and Energy Spectra]]：$E$ 与频谱。
2. 状态空间支线：控制与观测器（确定性）。
3. LMMSE → WSS → PSD → Wiener：随机波形估计。
4. 检测 LRT → **匹配滤波**：已知波形 + 噪声下的最优线性前端。

三条线共用线性代数 / 二阶统计 / LTI，但**损失与约束**不同，公式不可随手替换。

---
## 8. 附录：SNR 与误码的数量级

AWGN 下二进制反极性信号经匹配滤波后，判决误差概率常为 $Q(\sqrt{2E_b/N_0})$。若 $E_b/N_0=9.6\,\mathrm{dB}\approx 9.12$（线性），则 $\sqrt{2E_b/N_0}\approx 4.27$，$Q(4.27)\approx 10^{-5}$ 量级——经典「未编码 BPSK 约 $10^{-5}$」链路预算锚点。匹配滤波保证前端不先损失 SNR；其后的编码 / 均衡是另一层。

多进制正交信号（如 M-FSK）的充分统计是一组匹配滤波支路；最大输出支路即 ML 判决。波形能量仍决定指数级的错误概率斜率（联合界 / 并集界）。

---
## 9. 实现核对表与常见失误

1. 确认噪声近似白、或已白化；否则按 $S^*/S_w$ 设计。
2. 采样时刻对准符号/脉冲末端；定时误差直接损 SNR。
3. 增益常数不影响 SNR，但影响后续阈值与 ADC 动态范围。
4. 截断冲激响应（FIR 近似）会损失部分能量——用足够长的抽头覆盖 $s$ 的有效支撑。
5. 不要把匹配滤波输出当「波形重建」；它是检测统计量通道。

与 [[Filtering]] 中理想滤波器对比：那里按通带指标塑形频谱；这里按**已知模板**塑形冲激响应。二者都是 LTI，目标函数不同。

> [!example] 三角脉冲能量
> $s(t)=1-|t|/T$（$|t|\le T$），$E=\int_{-T}^{T}(1-|t|/T)^2dt=2T/3$。若 $N_0=10^{-8}$，$T=3\times 10^{-4}$，则 $E=2\times 10^{-4}$，$\mathrm{SNR}_{\max}=2E/N_0=4\times 10^{4}$（约 $46\,\mathrm{dB}$）。把 $T$ 减半（能量减半）⇒ SNR 降 $3\,\mathrm{dB}$——脉宽/幅度权衡的定量感。

## 10. 自检与参考答案

1. 白噪声下匹配滤波器的时域与频域形式。
2. $\mathrm{SNR}_{\max}$ 公式及含义（与波形形状关系）。
3. 为何相关器与匹配滤波等价？
4. 有色噪声时如何改？
5. 与 Wiener 滤波的目标差异？

> [!success]- 参考答案
> 1. $h(t)\propto s(t_0-t)$；$H(j\omega)\propto S^*(j\omega)e^{-j\omega t_0}$。
> 2. $2E/N_0$；只依赖能量与 $N_0$，匹配时达到，与形状无关（未匹配则达不到）。
> 3. 卷积在 $t_0$ 的输出 $=\int y(\tau)s(\tau-(t_0-T_{\mathrm{align}}))\,d\tau$，对齐后即相关。
> 4. 白化后匹配，或 $H\propto S^*/S_w$。
> 5. 匹配：已知确定信号、最大瞬时 SNR / 检测；Wiener：随机信号、最小 MSE 波形估计。

---
## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[Hypothesis Testing and Signal Detection]]、[[Wiener Filtering]]、[[Filtering]]
