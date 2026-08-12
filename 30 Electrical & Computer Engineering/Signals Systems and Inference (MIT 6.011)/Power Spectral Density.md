---
aliases:
  - 功率谱密度
  - Power Spectral Density
  - PSD
  - Wiener-Khinchin
  - 维纳-辛钦
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[Wide-Sense Stationary Processes]]"
  - "[[Transforms and Energy Spectra]]"
  - "[[Wiener Filtering]]"
  - "[[Filtering]]"
down:
  - "[[Wiener Filtering]]"
---
# 功率谱密度（PSD）与 Wiener–Khinchin

> [!summary] 核心结论
> 对 WSS 过程，**功率谱密度** $S_x(\omega)$ 与自相关 $R_x(\tau)$ 构成 Fourier 对（**Wiener–Khinchin**）：
> $$
> S_x(\omega)=\int_{-\infty}^{\infty}R_x(\tau)e^{-j\omega\tau}\,d\tau,\qquad
> R_x(\tau)=\frac{1}{2\pi}\int_{-\infty}^{\infty}S_x(\omega)e^{j\omega\tau}\,d\omega.
> $$
> $S_x(\omega)\ge 0$（实过程还满足 $S_x(-\omega)=S_x(\omega)$）。稳定 LTI：$S_y(\omega)=\lvert H(j\omega)\rvert^2 S_x(\omega)$。$R_x(0)=\frac{1}{2\pi}\int S_x$ 把「总平均功率」写成频谱积分。这是噪声带宽、SNR、Wiener 滤波频域公式的共同语言；确定性原型见 [[Transforms and Energy Spectra]] 的 ESD。

> 底本：MIT 6.011 OCW Spring 2018 — power spectra；前置 [[Wide-Sense Stationary Processes]]。

---
## 1. 从自相关到频谱

功率信号 / WSS 过程通常没有经典平方可积意义下的 FT。Wiener–Khinchin 绕开样本路径 FT，直接对 $R_x(\tau)$ 变换得到 $S_x(\omega)$：**平均功率如何随频率分布**。

离散时间：
$$
S_x(e^{j\Omega})=\sum_{k=-\infty}^{\infty}R_x[k]e^{-j\Omega k},\qquad
R_x[k]=\frac{1}{2\pi}\int_{-\pi}^{\pi}S_x(e^{j\Omega})e^{j\Omega k}\,d\Omega.
$$

---
## 2. 基本性质

1. **非负**：$S_x(\omega)\ge 0$（由协方差半正定 / Bochner 定理）。
2. **对称**：实值过程 ⇒ $S_x$ 为偶函数。
3. **功率**：$R_x(0)=\mathbb{E}[\lvert X\rvert^2]=\frac{1}{2\pi}\int S_x(\omega)\,d\omega$。
4. **白噪声**：$S$ 常数 ↔ $R$ 为 $\delta$。
5. **带通噪声**：$S$ 集中在某频带 ↔ $R(\tau)$ 缓慢振荡衰减（相关时间 ~ $1/$带宽）。

> [!warning] 单边 vs 双边 PSD
> 通信文献常画 $f>0$ 的单边谱，并把负频功率折到正频（因子 2）。6.011 / 信号教材常用**双边**角频率形式。读 SNR 公式时先核对 $N_0/2$ 约定：双边密度 $N_0/2$ 对应单边 $N_0$。

---
## 3. LTI 传输公式

输入 WSS、稳定 LTI $H(j\omega)$：
$$
S_y(\omega)=\lvert H(j\omega)\rvert^2 S_x(\omega).
$$
推导路径：时域 $R_y=h*(-h^*)*R_x$ → 取 FT → 乘上 $H(j\omega)H(-j\omega)^*=\lvert H\rvert^2$（实系数系统）。MIMO / 互谱有矩阵版本 $S_y=H S_x H^*$。

这直接给出：

- 输出功率 $=\frac{1}{2\pi}\int\lvert H\rvert^2 S_x\,d\omega$；
- 等效噪声带宽：把 $\lvert H\rvert^2$ 换成同高度矩形时的宽度。

> [!example] 理想带通内的白噪声功率
> $S_x(\omega)=N_0/2$，理想带通 $|H|=1$ 当 $\omega\in[\omega_c-W/2,\omega_c+W/2]$（及对称负频），否则 $0$。双边积分宽度共 $2W$（正负频各 $W$ 若 $\omega_c>W/2$）。
> $$
> P_y=\frac{1}{2\pi}\int\lvert H\rvert^2\frac{N_0}{2}\,d\omega=\frac{N_0}{2\pi}\cdot W_{\mathrm{total}}.
> $$
> 若正负频各宽 $B$（rad/s）共 $2B$，则 $P_y=\frac{N_0}{2\pi}\cdot 2B=\frac{N_0 B}{\pi}$。换用 Hz：设单边带宽 $W$ Hz、双边密度 $N_0/2$，经典结果 **$P=N_0 W$**（注意 Hz 与 rad/s 换算）。取 $N_0=10^{-12}\,\mathrm{W/Hz}$，$W=1\,\mathrm{MHz}$ ⇒ $P=10^{-6}\,\mathrm{W}=1\,\mu\mathrm{W}$。

---
## 4. 互谱与相干（草图）

两联合 WSS 过程：互相关 $R_{xy}(\tau)=\mathbb{E}[X(t+\tau)Y^*(t)]$，互谱 $S_{xy}=\mathcal{F}\{R_{xy}\}$。线性关系 $Y=h*X+$噪声时，$S_{xy}=H S_x$ 等恒等式支撑系统辨识与因果 Wiener 滤波推导。相干函数 $|\gamma|^2=\lvert S_{xy}\rvert^2/(S_x S_y)$ 衡量线性相关强度（≤ 1）。

---
## 5. 估计实践（概念）

有限记录估 PSD：周期图（数据 FT 模方）、Welch 平均、加窗。分辨率 ~ $1/T$，方差需平均降低。理论课强调 $R\leftrightarrow S$ 与 LTI 公式；实现细节属 DSP。关键：估出的 $\hat S$ 应非负；相关函数估 $\hat R$ 再 FT 时要注意偏置与窗。

---
## 6. 与能量谱、确定性信号的对照

| | 能量信号 | WSS 功率信号 / 过程 |
|---|---|---|
| 时域二阶 | $r_x(\tau)=\int x(t+\tau)x^*(t)\,dt$ | $R_x(\tau)=\mathbb{E}[X(t+\tau)X^*(t)]$ |
| 频域 | ESD $\lvert X\rvert^2$ | PSD $S_x$ |
| LTI | $\lvert Y\rvert^2=\lvert H\rvert^2\lvert X\rvert^2$ | $S_y=\lvert H\rvert^2 S_x$ |

记忆口诀：**同一张乘法表，换期望与归一化**。

---
## 7. 通向 Wiener 滤波

频域 LMMSE（非因果 Wiener）形如
$$
H_{\mathrm{opt}}(j\omega)=\frac{S_{sx}(\omega)}{S_x(\omega)}
$$
（$s$ 为期望信号，$x$ 为观测）——完全用 PSD / 互 PSD 写成。因果情形需谱分解（谱因式分解），下一篇给直觉。

---
## 8. 窄带过程与相关时间

若 $S_x(\omega)$ 集中在带宽 $B$（rad/s）量级，则 $R_x(\tau)$ 的包络大致在 $|\tau|\sim 1/B$ 内显著——**相关时间**与带宽成反比。通信里符号间隔、雷达脉冲间隔、采样是否「近似独立」都用这个尺子。白噪声理想化 $B\to\infty$ ⇒ 相关时间 $0$；经系统带宽限制后必成有色。

Parseval 型功率积分也可只在通带上估：$\frac{1}{2\pi}\int_{\mathcal{B}}S_x$，得到带内功率，便于链路预算与干扰共存计算。

---
## 9. 自检与参考答案

1. 写出 Wiener–Khinchin 一对变换（CT）。
2. 为何 $S_x(\omega)\ge 0$？实过程还有何对称性？
3. 陈述 $S_y=\lvert H\rvert^2 S_x$ 的前提。
4. $R_x(0)$ 与 $S_x$ 的积分关系。
5. 单边 / 双边 $N_0$ 约定如何避免踩坑？

> [!success]- 参考答案
> 1. $S=\mathcal{F}\{R\}$，$R=\mathcal{F}^{-1}\{S\}$（含 $2\pi$ 约定）。
> 2. 协方差半正定 / Bochner；实过程 $S$ 偶。
> 3. 输入 WSS + 稳定 LTI（稳态输出）。
> 4. $R(0)=\frac{1}{2\pi}\int S(\omega)\,d\omega$。
> 5. 先确认密度是双边 $N_0/2$ 还是单边 $N_0$，以及频率轴是 Hz 还是 rad/s，再套 $P=N_0 W$。

---
## 附录补充：周期图与泄漏

长度 $N$ 的 DT 记录，周期图 $\hat S(e^{j\Omega})=\frac{1}{N}\lvert\sum_{n=0}^{N-1}x[n]e^{-j\Omega n}\rvert^2$ 是 $S$ 的渐近无偏但**非一致**估计（方差不随 $N$ 趋于 0）。Welch 法分块加窗再平均，用分辨率换方差。窗函数泄漏使强窄带干扰抬高邻频本底——测 PSD 时先看窗旁瓣。理论公式 $S_y=\lvert H\rvert^2 S_x$ 假定真实谱；用 $\hat S$ 设计 Wiener 时要把估计误差算进鲁棒性。

---
## 10. 互谱估计与系统辨识草图

测输入 $u$、输出 $y$（联合 WSS）时，$\hat S_{yu}/\hat S_u$ 是 $H(j\omega)$ 的估计（在相干高的频带可靠）。这与非因果 Wiener 分子分母同一家族。相干 $\lvert\gamma\rvert^2$ 低 ⇒ 该频点线性模型差或噪声大，辨识不可信。闭环数据还需工具变量 / 间接法，否则反馈污染 $\hat S_{yu}$——超出 6.011 范围，但提醒：PSD 不只是「画噪声形状」，也是 LTI 辨识语言。

> [!example] 一阶有色噪声功率
> $S_x(\omega)=\frac{N_0/2}{1+(\omega/\omega_c)^2}$。$R_x(0)=\frac{1}{2\pi}\int S=\frac{N_0\omega_c}{4}$。取 $N_0=4\times 10^{-10}$，$\omega_c=10^3$ ⇒ $R_x(0)=10^{-7}$。相关时间 $\sim 1/\omega_c=1\,\mathrm{ms}$：相隔数毫秒的采样近似弱相关。

对 DT 单位圆上的积分，功率 $R[0]=\frac{1}{2\pi}\int_{-\pi}^{\pi}S(e^{j\Omega})\,d\Omega$。若只关心 $[\Omega_1,\Omega_2]$ 带内干扰功率，缩小积分限即可——与模拟域带限功率同一逻辑。

工程口诀：先写清双边还是单边、Hz 还是 rad/s，再把 $\int S$ 与 $N_0 W$ 对表；约定错了，整份链路预算会差因子 $2$ 或 $2\pi$。PSD 是随机过程的「能量谱」换功率版——与 [[Transforms and Energy Spectra]] 对照记忆最快。

> 相关阅读顺序：[[Wide-Sense Stationary Processes]] → 本篇 → [[Wiener Filtering]]。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[Wide-Sense Stationary Processes]]、[[Wiener Filtering]]、[[Transforms and Energy Spectra]]
