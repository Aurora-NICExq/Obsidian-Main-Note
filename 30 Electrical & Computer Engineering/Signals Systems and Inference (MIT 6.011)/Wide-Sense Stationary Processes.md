---
aliases:
  - 宽平稳过程
  - Wide-Sense Stationary Processes
  - WSS
  - 广义平稳
  - autocorrelation function
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[MMSE and LMMSE Estimation]]"
  - "[[Power Spectral Density]]"
  - "[[Joint Distributions Covariance and Correlation]]"
  - "[[Convolution]]"
down:
  - "[[Power Spectral Density]]"
---
# 宽平稳（WSS）过程

> [!summary] 核心结论
> 随机过程 $X(t)$ **宽平稳（WSS / 广义平稳）**：均值 $\mu_X(t)=\mu_X$ 为常数，且自相关只依赖时差，
> $$
> R_X(t+\tau,t)=R_X(\tau)=\mathbb{E}\bigl[X(t+\tau)X^*(t)\bigr].
> $$
> （常同时要求二阶矩有限。）WSS 输入通过稳定 LTI 后，输出（稳态下）仍为 WSS，且
> $$
> R_y=h*(-h^*)*R_x\quad\text{（卷积形式）},\qquad
> S_y(\omega)=\lvert H(j\omega)\rvert^2 S_x(\omega)
> $$
> （功率谱形式，详见下一篇）。WSS + 二阶矩是 Wiener 滤波与许多通信噪声模型的默认舞台。

> 底本：MIT 6.011 OCW Spring 2018 — WSS processes；协方差直觉对齐 [[Joint Distributions Covariance and Correlation]]。

---
## 1. 严格平稳 vs 宽平稳

- **严格平稳**：所有有限维分布对时间平移不变。
- **宽平稳**：只约束一、二阶矩（均值常数 + 自相关依时差）。

严格平稳 + 二阶矩有限 ⇒ WSS；反之不然。高斯过程例外：WSS 的高斯过程也是严格平稳（因高斯由一、二阶矩完全决定）。

工程噪声、热噪声近似、许多通信干扰用 WSS 建模即可——Wiener–Khinchin 与 LTI 传输只需要二阶。

---
## 2. 自相关与自协方差

$$
R_X(\tau)=\mathbb{E}[X(t+\tau)X^*(t)],\qquad
C_X(\tau)=R_X(\tau)-\lvert\mu_X\rvert^2.
$$
性质：

| 性质 | 内容 |
|---|---|
| 共轭对称 | $R_X(-\tau)=R_X^*(\tau)$ |
| 功率 | $R_X(0)=\mathbb{E}[\lvert X\rvert^2]\ge\lvert R_X(\tau)\rvert$ |
| 半正定 | 对任意采样时刻集合，协方差矩阵 ⪰ 0 |

离散时间 $X[n]$：$R_X[k]=\mathbb{E}[X[n+k]X^*[n]]$，同样只依赖 lag $k$。

> [!warning] 「平稳」不等于「不相关」或「白」
> WSS 允许强时间相关（有色噪声）。**白噪声**是 WSS 的极端：$C_X(\tau)=\sigma^2\delta(\tau)$（CT 理想化），频谱平坦。切勿把「平稳」读成「每次独立」。

---
## 3. 白噪声与有色噪声

理想 CT 白噪声：$R_W(\tau)=\frac{N_0}{2}\delta(\tau)$，$S_W(\omega)=N_0/2$。物理上是平坦频谱的近似（在系统带宽内）。通过成形滤波器 $H(j\omega)$ 后得有色 WSS，PSD 为 $\lvert H\rvert^2 N_0/2$——这是仿真有色噪声的标准做法。

---
## 4. LTI 过滤 WSS

设稳定 LTI，冲激响应 $h$，输入 WSS $X$，输出 $Y=h*X$（卷积在均方意义下理解）。则（稳态、忽略瞬态）：

1. $\mu_Y=\mu_X\int h$（或 $H(0)\mu_X$）。
2. 互相关 / 自相关：$R_{yx}=h*R_x$，$R_y=h*(-h^*)*R_x$（实冲激时 $R_y=h(-\,\cdot\,)*h*R_x$ 等等价写法）。
3. 频域：$S_y=\lvert H\rvert^2 S_x$（下一篇严格定义 $S$）。

![[ssi-wss-lti.svg]]

这与确定性能量情形 $\lvert Y\rvert^2=\lvert H\rvert^2\lvert X\rvert^2$ **同构**，只是对象换成功率密度。

> [!example] RC 低通过滤白噪声
> 白噪声 PSD $S_x=N_0/2$，RC 低通 $H(j\omega)=\frac{1}{1+j\omega RC}$。则
> $$
> S_y(\omega)=\frac{N_0/2}{1+(\omega RC)^2}.
> $$
> 输出功率（方差，零均值时）
> $$
> R_y(0)=\frac{1}{2\pi}\int_{-\infty}^{\infty}S_y(\omega)\,d\omega=\frac{N_0}{4RC}.
> $$
> （积分用 $\int\frac{d\omega}{1+(\omega a)^2}=\pi/a$，$a=RC$。）数值：$N_0=10^{-10}\,\mathrm{W/Hz}$，$RC=10^{-3}\,\mathrm{s}$ ⇒ $R_y(0)=2.5\times 10^{-8}$。时间常数越大，噪声带宽越窄，输出方差越小——与「等效噪声带宽」直觉一致。

---
## 5. 各态历经性（点到为止）

**均值各态历经**：时间平均 $\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}X(t)\,dt$ 以均方 / a.s. 等于 $\mu_X$。自相关各态历经类似。实验上用一条长记录估 $R(\tau)$ 依赖此性质。WSS 不自动蕴含各态历经；混有随机常数直流等可破坏。课程使用中：理论用期望，实验用时间平均，并声明假定。

---
## 6. 离散时间与采样

WSS 序列经 DT LTI：$S_y(e^{j\Omega})=\lvert H(e^{j\Omega})\rvert^2 S_x(e^{j\Omega})$。对 CT WSS 采样：若原过程带限且采样足够密，离散相关是连续相关的采样；别混叠频谱。数字 Wiener / LMS 自适应滤波都在 DT WSS 框架下叙述。

---
## 7. 联合 WSS 与互相关

两过程 $X,Y$ **联合宽平稳**：各自 WSS，且互相关 $R_{xy}(t+\tau,t)=R_{xy}(\tau)$ 只依时差。输入–输出、信号–观测、多传感器阵列都用这个语言。线性滤波下 $R_{yx}=h*R_x$ 等关系是辨识 $h$ 与推导 Wiener–Hopf 方程的原料。

若仅各自 WSS 但互相关随绝对时间变，则「联合」失败——例如开关时段不同的非同步源。建模时先问：平移一段录音，二阶统计变不变？

---
## 8. 课程中的位置

WSS 提供「只有 $R(\tau)$ / $S(\omega)$ 就够做线性估计与滤波」的设定。下一步：[[Power Spectral Density]] 用 Wiener–Khinchin 把 $R\leftrightarrow S$ 钉死；再 [[Wiener Filtering]] 在频域写 LMMSE 滤波器。

---
## 9. 自检与参考答案

1. 写出 WSS 的两条定义条件。
2. $R_X(0)$ 的含义？$\lvert R_X(\tau)\rvert$ 上界？
3. 稳定 LTI 对 WSS 输入的输出相关 / 谱如何变？
4. 白噪声的 $R$ 与 $S$ 是什么？
5. 严格平稳与 WSS 的关系？高斯情形呢？

> [!success]- 参考答案
> 1. 均值常数；自相关只依赖 $\tau$。
> 2. 平均功率 $\mathbb{E}[\lvert X\rvert^2]$；$\lvert R(\tau)\rvert\le R(0)$。
> 3. $R_y=h*(-h^*)*R_x$；$S_y=\lvert H\rvert^2 S_x$。
> 4. $R=\frac{N_0}{2}\delta$；$S=N_0/2$（约定下）。
> 5. 严格+二阶⇒WSS；WSS⇏严格。高斯 WSS⇒严格平稳。

---
## 附录补充：谐波过程与线谱

$X(t)=A\cos(\omega_0 t+\Theta)$，$\Theta$ 均匀 $[0,2\pi)$，则 WSS，且 $R_X(\tau)=\frac{A^2}{2}\cos(\omega_0\tau)$，$S_X$ 在 $\pm\omega_0$ 含冲激（线谱）。这与「有限功率正弦」的确定性功率谱图景一致。滤波后线谱被 $\lvert H(j\omega_0)\rvert^2$ 加权。随机相位是把永续正弦纳入 WSS 期望框架的标准手法。

---
## 10. 从相关函数读「记忆」

$R_X(\tau)$ 衰减快 ⇒ 短记忆、宽频谱；衰减慢 ⇒ 长记忆、窄频谱（与 Wiener–Khinchin 对偶一致）。AR(1) 离散模型 $X[n]=\rho X[n-1]+W[n]$（$|\rho|<1$）给出 $R[k]\propto\rho^{|k|}$，几何记忆；$\rho\to 1$ 时接近随机游走（非 WSS 或临界）。仿真有色噪声：白噪声通过 $H(z)=1/(1-\rho z^{-1})$ 即得。

跨笔记：[[Joint Distributions Covariance and Correlation]] 的 $\mathrm{Cov}(X_i,X_j)$ 是有限维切片；WSS 要求整条过程的二阶切片只靠时差组织起来。

实验上估 $\hat R[k]=\frac{1}{N}\sum_{n}x[n+k]x[n]$（或 $1/(N-k)$ 无偏版）时，$|k|$ 大、平均项少，方差大——通常只信 $|k|\ll N$ 的相关峰。这与各态历经假定一起构成「用一条记录代替期望」的实践边界。

把 WSS 当作「二阶世界的坐标系」：一进来就问均值是否常量、相关是否只靠 $\tau$；不满足就不要硬套 Wiener–Khinchin 与稳态 $S_y=|H|^2 S_x$。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[Transforms and Energy Spectra]]、[[Power Spectral Density]]
