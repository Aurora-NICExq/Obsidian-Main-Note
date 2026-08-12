---
title: "Carrier Drift and Diffusion"
aliases: ["载流子输运", "漂移与扩散", "爱因斯坦关系", "迁移率"]
tags: [electronic_circuits, ee, semiconductor]
up: "[[Electronic Circuits I MOC]]"
down: ["[[PN Junction in Equilibrium & Reverse Bias]]"]
related: ["[[Basic Physics of Semiconductors]]", "[[Caltech Analog Circuit Design-103N-Carrier Drift and Mobility]]"]
---
# Carrier Drift and Diffusion

## 载流子输运：漂移、扩散与爱因斯坦关系

> [!summary] 核心结论
> 载流子只有两种运动方式：被电场推（漂移）和顺着浓度梯度自己走（扩散）。
> 两者由爱因斯坦关系 $D/\mu=V_T$ 绑在一起 —— 这不是巧合，而是同一个热运动的两种表现。PN 结在平衡时正是这两股流精确抵消。

---
## 1. 漂移：电场推着走

外加电场 $E$ 时，载流子获得一个平均漂移速度：

$$
v_n = -\mu_n E,\qquad v_p = \mu_p E
$$

$\mu$ 是**迁移率**，量纲 $\mathrm{cm^2/(V\cdot s)}$。Si 中 $\mu_n\approx1350\,\mathrm{cm^2/(V\cdot s)}$，$\mu_p\approx480\,\mathrm{cm^2/(V\cdot s)}$ ——电子快约 3 倍，这就是 NMOS 比同尺寸 PMOS 驱动能力强的物理原因。

漂移电流密度：

$$
J_{drift} = q(n\mu_n + p\mu_p)E \;=\; \sigma E
$$

即欧姆定律的微观形式，电导率 $\sigma=q(n\mu_n+p\mu_p)$。

### 速度饱和

![[ec-carrier-drift-and-diffusion-01.svg]]

$v=\mu E$ 只在低场下成立。场强上去后载流子与晶格的散射急剧增加，速度趋于 $v_{sat}\approx10^{7}\,\mathrm{cm/s}$：

$$
v = \frac{\mu E}{1 + \mu E/v_{sat}}
$$

对现代短沟道 MOS，沟道里的场强轻易超过 $10^{4}\,\mathrm{V/cm}$，器件长期工作在速度饱和区。后果是 $I_D$ 对 $V_{ov}$ 从平方律退化成接近线性——这一点在 [[MOSFET Characteristics and Small-Signal Model]] 里会再次出现。

---
## 2. 扩散：浓度梯度自己走

![[ec-carrier-drift-and-diffusion-02.svg]]

不需要任何电场。载流子的随机热运动，在浓度不均匀时统计上就表现为从高浓度流向低浓度：

$$
J_n = qD_n\frac{dn}{dx},\qquad
J_p = -qD_p\frac{dp}{dx}
$$

注意两个符号差异：一是电子带负电（电流方向与粒子流方向相反），二是「往低浓度流」本身带一个负号，两者在 $J_n$ 里抵消掉了。

$D$ 是扩散系数，量纲 $\mathrm{cm^2/s}$。

---
## 3. 爱因斯坦关系

漂移和扩散不是两个独立机制，它们都源于同一个热运动：

$$
\boxed{\;\frac{D}{\mu} = \frac{kT}{q} = V_T \approx 26\,\mathrm{mV}\;（300\,\mathrm{K}）\;}
$$

于是 $D_n\approx35\,\mathrm{cm^2/s}$，$D_p\approx12\,\mathrm{cm^2/s}$。

> [!important] $V_T$ 是这门课出现频率最高的常数
> 它会以三副面孔反复出现：
> - 爱因斯坦关系里的 $D/\mu$
> - 二极管方程与 $I_C=I_Se^{V_{BE}/V_T}$ 的指数尺度
> - 小信号参数 $r_d=V_T/I_D$、$g_m=I_C/V_T$
>
> 三者是同一个 $kT/q$，所以「电流变 $10\times$、电压变 $60\,\mathrm{mV}$」这条规律在二极管、BJT、MOS 亚阈值区里通通成立。

---
## 4. 总电流

一般情况下两种机制同时存在：

$$
J_n = q\mu_n n E + qD_n\frac{dn}{dx}
$$

这条式子是下一讲的出发点。**PN 结在热平衡下的定义就是：漂移电流与扩散电流处处精确抵消，净电流为零。** 内建电势 $V_0$ 正是让这个抵消成立所需要的那个电势差 —— 把上式令为 0 并积分，就直接得到

$$
V_0 = V_T\ln\frac{N_AN_D}{n_i^2}
$$

---
## 5. 与其他笔记的关系

- 上一讲提供了 $n$、$p$：[[Basic Physics of Semiconductors]]。
- 下一讲把这两股流放进 PN 结：[[PN Junction in Equilibrium & Reverse Bias]]。
- Caltech 版对迁移率与散射讲得更细：[[Caltech Analog Circuit Design-103N-Carrier Drift and Mobility]]。
