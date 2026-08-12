---
tags:
  - AnalogCircuitDesign
  - DifferentialPair
  - CurrentMirror
  - SingleEnded
  - GainBoost
  - Cascode
source_srt: "srt字幕文件/加州理工学院【中英⚡模拟电路设计|2019 Analog Circuit Design】 - 030 - p29 130N. MOS Differential-to-Single-Ended Conversion. Gain Enhancement.srt"
---

# Caltech｜模拟电路设计（2019）130N：MOS 差分转单端——电流镜负载的“加法”与 Cascode 增益增强

讲座的出发点：很多系统内部是差分信号，但你最终可能需要**单端输出**。差分到单端的转换，本质上是在做“电流/电压的重组”，其中一个经典方法就是 **电流镜负载**。

---

## 1) 电流镜实现差分转单端：把“减法”变成“加法”

在对称差模激励下：
$$
v_{i+}=+\frac{v_{id}}{2},\qquad v_{i-}=-\frac{v_{id}}{2}.
$$
每支路的小信号电流（跨导电流）大致为：
$$
i_{d1}\approx +g_{m1}\frac{v_{id}}{2},\qquad
i_{d2}\approx -g_{m2}\frac{v_{id}}{2}.
$$

讲座强调“关键一步”在电流镜：
- 镜像会把其中一支路的电流**反射到输出节点**
- 并且可视作做了极性翻转，使得两份电流在输出节点**同向注入**

于是输出节点得到“加性”的小信号电流（对称时近似）：
$$
i_{out}\approx g_m\frac{v_{id}}{2}+g_m\frac{v_{id}}{2}=g_m v_{id}.
$$

输出节点看到的等效电阻主要是上下两只管的输出电阻并联：
$$
R_{out,node}\approx r_{op}\parallel r_{on}.
$$
因此单端电压增益（量级）：
$$
A_v\approx g_m\,(r_{op}\parallel r_{on}).
$$

---

## 2) 讲座里的数量级例子：为什么“增益不高”？

讲座用一组数字估算 $r_o$ 并并联：
- 例如 $r_{on}\sim 20\text{k}\Omega$，$r_{op}\sim 80\text{k}\Omega$
- 则并联约为 $16\text{k}\Omega$

若此时 $g_m$ 量级对应 $1\text{ mA}\times 16\text{k}\Omega\approx 16$ 的电压增益（讲座就是在这个数量级上做判断），就会得到结论：
> 这不是很高的增益，需要进一步提高。

---

## 3) MOS 的一个“与 BJT 不同点”：$g_m$ 不只由电流决定

讲座明确对比：
- BJT：$g_m=I_C/V_T$，两只管若电流相同，$g_m$ 就基本相同
- MOS：$g_m$ 与 $W/L$、$\mu C_{ox}$、工作区有关；你可以通过选择 $W/L$ 来改变 $g_m$ 比例

工程含义：
- 差分转单端电路里，你必须意识到：镜像管、输入管的 $g_m$ 未必天然相等
- 这既是风险（失配/非理想），也是手段（可用尺寸比做“跨导配比”）

---

## 4) 如何提高增益：先从提高输出电阻 $r_o$ 入手

讲座讨论“选沟道长度 $L$”的直觉：
- 想提高 $r_o$（降低 $\lambda$）⇒ 选更大的 $L$

但随之而来的权衡（讲座点名）：
- **速度**：器件变大，电容增加，带宽下降
- **头间隙/摆幅**：对固定电流，若 $W/L$ 变小（例如增大 $L$），为了维持相同 $I_D$ 往往需要更大的过驱动 $V_{ov}=V_{GS}-V_T$  
  ⇒ 需要更大的电压余量，摆幅变差，更容易把管子推向三极区

讲座还提到一个很现实的版图视角：在模拟 IC 里，很多时候面积/寄生可能反而被焊盘、互连等限制，而不是单个晶体管本体。

---

## 5) 增益增强（Gain enhancement）：Cascode 化整个结构

讲座给出的直接策略：**把电流镜负载与下方器件都 Cascode 化**。

关键点：
- 差模驱动产生的跨导电流仍然是 $g_m v_{id}/2$ 这种形式（“电流产生机制”没变）
- 变化的是输出节点往上/往下看的等效电阻：Cascode 让它被器件内在增益 $g_m r_o$ 成倍抬升

因此你可以把增益近似理解为：
$$
A_v \sim g_m \cdot R_{out,\text{cascode}},
\qquad
R_{out,\text{cascode}}\approx (g_m r_o)\,r_o\ \text{量级}.
$$

代价同 124N 的结论一致：
- 需要额外的 $V_{bias}$ 来偏置 Cascode 管
- 多叠器件会吃掉摆幅（headroom）

