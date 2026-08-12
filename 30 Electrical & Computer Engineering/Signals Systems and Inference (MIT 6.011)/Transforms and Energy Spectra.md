---
aliases:
  - 变换与能量谱
  - Transforms and Energy Spectra
  - Energy Spectral Density
  - ESD
  - 能量谱密度
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[Continuous-Time Fourier Transform]]"
  - "[[Fourier Transform Properties]]"
  - "[[Power Spectral Density]]"
  - "[[State-Space Models]]"
down:
  - "[[State-Space Models]]"
---
# 变换与能量谱：从信号与系统到推断的桥

> [!summary] 核心结论
> 对**能量有限**信号，$x(t)$ 的傅里叶变换 $X(j\omega)$ 给出振幅/相位分解；**能量谱密度** $\lvert X(j\omega)\rvert^2$ 描述能量如何按频率分布，并由 **Parseval** 与时域能量 $\int\lvert x\rvert^2$ 对等。确定性**自相关** $r_x(\tau)=\int x(t+\tau)x^*(t)\,dt$ 与 $\lvert X\rvert^2$ 构成 Fourier 对——这是后文随机过程里 Wiener–Khinchin（功率谱）的确定性原型。6.011 用这条桥把 [[Signals and Systems MOC|S&S]] 的变换工具接到状态空间与统计推断。

> 底本：MIT 6.011（Verghese / Oppenheim）OCW Spring 2018 — transforms / energy spectra 单元；前置 [[Continuous-Time Fourier Transform]]、[[Fourier Transform Properties]]。

---
## 1. 能量信号 vs 功率信号（回顾与分界）

连续时间信号若
$$
E_x=\int_{-\infty}^{\infty}\lvert x(t)\rvert^2\,dt<\infty,
$$
称为**能量信号**（平方可积）。典型：有限支撑脉冲、指数衰减、许多瞬态。

若 $E_x=\infty$ 但时间平均功率
$$
P_x=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}\lvert x(t)\rvert^2\,dt
$$
有限且常非零，则属**功率信号**（如非零直流、永续正弦、许多平稳随机过程的实现）。6.011 前半侧重确定性能量视角与状态空间；后半进入宽平稳过程时，对象切换到功率 / PSD（见 [[Power Spectral Density]]）。

> [!warning] 不要把 ESD 与 PSD 混用
> 能量谱密度 $\lvert X(j\omega)\rvert^2$ 单位随「能量 / 频率」；功率谱密度 $S_x(\omega)$ 是功率按频率的密度。对功率信号，经典 FT 往往不存在（含 $\delta$ 或分布意义），应用 Wiener–Khinchin 从自相关出发。

---
## 2. 傅里叶变换与能量分解

能量信号的 CTFT（工程惯用角频率）
$$
X(j\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}\,dt,\qquad
x(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(j\omega)e^{j\omega t}\,d\omega.
$$
**Parseval / Plancherel**（一种常见归一化）
$$
\int_{-\infty}^{\infty}\lvert x(t)\rvert^2\,dt=\frac{1}{2\pi}\int_{-\infty}^{\infty}\lvert X(j\omega)\rvert^2\,d\omega.
$$
右侧被积函数 $\lvert X(j\omega)\rvert^2$ 即**能量谱密度（ESD）**：在 $[\omega,\omega+d\omega]$ 内贡献的能量份额（差 $2\pi$ 因子时注意教材约定）。

物理读法：时域「总能量」= 频域「能量密度」的积分；滤波 $|H(j\omega)|^2$ 对 ESD 的加权给出输出能量（确定性 LTI）。

---
## 3. 确定性自相关与 Wiener–Khinchin 原型

定义（能量信号）
$$
r_x(\tau)=\int_{-\infty}^{\infty}x(t+\tau)\,x^*(t)\,dt.
$$
性质速览：

| 性质 | 内容 |
|---|---|
| 共轭对称 | $r_x(-\tau)=r_x^*(\tau)$（实信号则偶） |
| 峰值 | $\lvert r_x(\tau)\rvert\le r_x(0)=E_x$ |
| 线性滤波 | 输出自相关 = $h$ 与输入自相关的双重卷积（与随机情形同形） |

**关键事实**：$\mathcal{F}\{r_x\}=\lvert X(j\omega)\rvert^2$（在一致的 FT 约定下）。即
$$
r_x(\tau)\;\overset{\mathcal{F}}{\longleftrightarrow}\;\lvert X(j\omega)\rvert^2.
$$
这正是随机过程 Wiener–Khinchin 定理「自相关 ↔ 功率谱」的确定性影子：把「实现上的时间相关」换成「总体期望相关」，把 ESD 换成 PSD。

> [!example] 矩形脉冲的 ESD 与自相关
> 取 $x(t)=A$ 当 $\lvert t\rvert\le T/2$，否则 $0$（能量 $E_x=A^2 T$）。
> $$
> X(j\omega)=AT\,\mathrm{sinc}\!\left(\frac{\omega T}{2\pi}\right)
> $$
> （$\mathrm{sinc}$ 定义随教材；此处取 $\sin(\omega T/2)/(\omega T/2)$ 时 $X=AT\cdot\mathrm{sinc}_{\mathrm{unnorm}}$）。
> ESD $\lvert X\rvert^2$ 为 $\mathrm{sinc}^2$ 形。时域自相关是**三角**函数：
> $$
> r_x(\tau)=A^2(T-\lvert\tau\rvert),\quad \lvert\tau\rvert\le T;\quad 0\text{ otherwise}.
> $$
> 三角 ↔ $\mathrm{sinc}^2$ 是经典 Fourier 对，直接验证「自相关 ↔ ESD」。数值：$A=2,\ T=1$ ⇒ $E_x=4$；$r_x(0)=4$；半宽处 $\tau=0.5$ 时 $r_x=2$。

---
## 4. LTI 对能量谱的作用

输入 $x$ → LTI $h$ → $y=h*x$。频域 $Y=H(j\omega)X(j\omega)$，故
$$
\lvert Y(j\omega)\rvert^2=\lvert H(j\omega)\rvert^2\,\lvert X(j\omega)\rvert^2.
$$
输出能量
$$
E_y=\frac{1}{2\pi}\int\lvert H\rvert^2\lvert X\rvert^2\,d\omega.
$$
与后文功率情形 $S_y=\lvert H\rvert^2 S_x$ **同形**——差别只在「能量密度 vs 功率密度」。这一条贯穿滤波、匹配滤波前的「确定性 SNR 直觉」。

若只关心带通能量，可在通带上积分 $\lvert X\rvert^2$；理想带限信号的能量集中在有限带宽，是采样与噪声带宽讨论的前置。

---
## 5. 离散时间类比（草图）

序列 $x[n]\in\ell^2$：DTFT $X(e^{j\Omega})$，$2\pi$-周期；Parseval
$$
\sum_n\lvert x[n]\rvert^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X(e^{j\Omega})\rvert^2\,d\Omega.
$$
确定性自相关 $r_x[\ell]=\sum_n x[n+\ell]x^*[n]$，其 DTFT 为 $\lvert X\rvert^2$。状态空间离散模型（下一篇）常与 $z$ 变换 / DTFT 联用；能量观点在有限长记录、脉冲响应平方和（H2 范数）中再次出现。

---
## 6. 与课程后半的接口

| 确定性（本篇） | 随机 / 推断（后文） |
|---|---|
| $r_x(\tau)$ 时间相关 | $R_x(\tau)=\mathbb{E}[X(t+\tau)X^*(t)]$ |
| ESD $\lvert X\rvert^2$ | PSD $S_x(\omega)$ |
| $\lvert Y\rvert^2=\lvert H\rvert^2\lvert X\rvert^2$ | $S_y=\lvert H\rvert^2 S_x$ |
| 匹配「已知波形」相关 | 匹配滤波 / 相关器检测 |

状态空间把「输入–输出」换成「内部状态演化」；稳定性、能达/能观、观测器与反馈建立在 $A,B,C,D$ 上，但仍可用传递函数 $H(s)=C(sI-A)^{-1}B+D$ 与本篇频域语言对话。

---
## 7. 能量信号经 LTI 的时域核对

设 $y=h*x$，确定性自相关满足 $r_y=h*(-h^*)*r_x$（实 $h$ 时写法随共轭约定微调）。两端取 FT 即回到 $\lvert Y\rvert^2=\lvert H\rvert^2\lvert X\rvert^2$。可用短支撑 $h$（如长度 2 的移动平均）与矩形 $x$ 手算卷积，再数值比较两侧能量——适合作为作业级自检。匹配滤波篇会把「已知 $s$ 的能量 $E$」重新用到 SNR $=2E/N_0$。

---
## 8. 自检与参考答案

1. 区分能量信号与功率信号；各举一例。
2. 写出 Parseval（连续）并解释 ESD 的含义。
3. 定义确定性自相关，并陈述它与 $\lvert X\rvert^2$ 的关系。
4. LTI 如何变换 ESD？与 PSD 公式有何同构？
5. 为何永续正弦不宜谈经典 ESD？

> [!success]- 参考答案
> 1. 能量：$\int\lvert x\rvert^2<\infty$（如有限脉冲）；功率：时间平均功率有限（如 $A\cos\omega_0 t$）。
> 2. $\int\lvert x\rvert^2=\frac{1}{2\pi}\int\lvert X\rvert^2\,d\omega$；$\lvert X\rvert^2$ 是能量按频率的密度。
> 3. $r_x(\tau)=\int x(t+\tau)x^*(t)\,dt$；$\mathcal{F}\{r_x\}=\lvert X\rvert^2$。
> 4. $\lvert Y\rvert^2=\lvert H\rvert^2\lvert X\rvert^2$；随机侧 $S_y=\lvert H\rvert^2 S_x$ 同形。
> 5. 正弦不是平方可积，FT 含 $\delta$，应用功率 / PSD 语言。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- 前置：[[Continuous-Time Fourier Transform]]、[[Fourier Transform Properties]]、[[Filtering]]
