---
aliases:
  - 线积分与 Cauchy 定理
  - Line Integrals
  - Cauchy's Theorem
  - Cauchy Theorem
  - Topic 3 Line Integrals
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Analytic Functions]]"
  - "[[Cauchy's Integral Formula]]"
  - "[[Complex Algebra and the Complex Plane]]"
down: []
---
# 线积分与 Cauchy 定理

> [!summary] 核心结论
> 复线积分 $\int_\gamma f\,dz$ 用参数化化为普通实积分；若 $f=F'$，则沿路径的积分等于端点 $F$ 之差（复版本微积分基本定理）。在**单连通**区域上，$f$ 解析 $\Rightarrow$ 闭围道积分 $\oint_\gamma f\,dz=0$（Cauchy 定理），从而积分**与路径无关**。变形定理把围道换成同伦的另一条；环域版允许“挖洞”。经典锚点：$\oint_{|z|=1}\dfrac{dz}{z}=2\pi i$。

> 底本：MIT 18.04 Topic 3（Jeremy Orloff）。工科重点：会参数化算积分、会用 Cauchy 定理判零、会变形到圆、会算 $\oint dz/z$。

---
## 1. 路径与复线积分

### 1.1 光滑路径

复平面上的（分段）光滑路径（contour / path）$\gamma:[a,b]\to\mathbb{C}$，
$$
\gamma(t)=x(t)+iy(t),\qquad \gamma'(t)=x'(t)+iy'(t).
$$
- **起点 / 终点**：$\gamma(a)$、$\gamma(b)$
- **闭路径（闭围道）**：$\gamma(a)=\gamma(b)$
- **正向**：通常取**逆时针**为边界的正方向（区域“在左侧”）

### 1.2 定义

$$
\int_\gamma f(z)\,dz
:=\int_a^b f\big(\gamma(t)\big)\,\gamma'(t)\,dt.
$$
这是把复值函数拆成实部虚部后做两次普通定积分。若 $\gamma$ 分段光滑，则分段求和。

> [!tip] 记忆口诀
> 把 $dz$ 想成 $\gamma'(t)\,dt$；一切回到实积分。

![[ca-contour-cauchy.svg]]

---
## 2. 基本例子：$z^2$ 与 $\bar z$

### 2.1 沿单位圆：$f(z)=z^2$

取 $\gamma(\theta)=e^{i\theta}$，$\theta\in[0,2\pi]$，则 $\gamma'=ie^{i\theta}$。
$$
\int_\gamma z^2\,dz
=\int_0^{2\pi}(e^{i\theta})^2\cdot ie^{i\theta}\,d\theta
=i\int_0^{2\pi}e^{3i\theta}\,d\theta=0.
$$
与 Cauchy 定理一致（$z^2$ 整函数）。

### 2.2 沿单位圆：$f(z)=\bar z$

在单位圆上 $\bar z=1/z$，故
$$
\int_\gamma \bar z\,dz
=\int_0^{2\pi}e^{-i\theta}\cdot ie^{i\theta}\,d\theta
=i\int_0^{2\pi}1\,d\theta=2\pi i.
$$
$\bar z$ **不解析**，闭积分不必为零——这是“解析性决定积分”的反面教材。

### 2.3 关键：$f(z)=1/z$

$$
\oint_{|z|=1}\frac{dz}{z}
=\int_0^{2\pi}\frac{1}{e^{i\theta}}\cdot ie^{i\theta}\,d\theta
=i\int_0^{2\pi}d\theta=2\pi i.
$$
$1/z$ 在 $0$ 处奇异，单位圆围住奇点，积分**不为零**。此式是整门课的“校准常数”。

> [!warning] 半径无关
> 对任意 $R>0$，$\oint_{|z|=R}dz/z=2\pi i$。后面变形定理会解释：所有绕原点一周的简单闭曲线结果相同。

---
## 3. 微积分基本定理（复路径版）

若在包含路径 $\gamma$ 的开集上存在原函数 $F$（即 $F'=f$），则
$$
\int_\gamma f(z)\,dz=F\big(\gamma(b)\big)-F\big(\gamma(a)\big).
$$
特别地：闭路径上 $\oint_\gamma f\,dz=0$。

> [!example] $f(z)=z^2$，$F(z)=z^3/3$
> 从 $0$ 到 $1+i$ 沿任意路径：
> $$
> \int_\gamma z^2\,dz=\frac{(1+i)^3}{3}-\frac{0}{3}=\frac{-2+2i}{3}.
> $$

> [!example] 为何 $1/z$ 在穿孔平面上**没有单值原函数**？
> 若有，则沿单位圆积分应为 $0$，但实际是 $2\pi i$。多值对数 $\log z$ 的导数是 $1/z$，但绕原点一周辐角跳 $2\pi$，单值原函数不存在。

**推论（路径无关的判定）**：若 $f$ 在区域 $A$ 上有原函数，则 $A$ 内任意同端点路径上的积分相等。

---
## 4. Cauchy 定理（单连通版）

### 4.1 单连通

区域 $A$ **单连通（simply connected）**：其中任意闭曲线可在 $A$ 内连续收缩成一点（“没有洞”）。开圆盘、半平面、整平面都是；环形 $\{r<|z|<R\}$、穿孔平面 $\mathbb{C}\setminus\{0\}$ **不是**。

### 4.2 定理陈述（工科常用形）

设 $A$ 单连通，$f$ 在 $A$ 上解析，$\gamma$ 为 $A$ 内分段光滑闭围道。则
$$
\oint_\gamma f(z)\,dz=0.
$$

等价说法：

1. **路径无关**：$A$ 内同端点的任意两条路径，积分相等。
2. **存在原函数**：在单连通 $A$ 上，解析 $f$ 必有原函数 $F$。

> [!note]- 证明提纲（Cauchy ↔ Green）
> 写 $f=u+iv$，$dz=dx+i\,dy$，展开后实部虚部各自是平面向量场的线积分。CR 恰使两场无旋（curl 为零），故单连通域上环量为零。严谨版：Green（需 $f'$ 连续）或 Goursat（仅需解析）。

### 4.3 立刻能用的例子

| $f$ | 区域 | 闭积分 |
|-----|------|--------|
| 多项式、$e^z$、$\sin z$ | 任意 | $0$ |
| $1/(z-a)$ | 不含 $a$ 的单连通域 | $0$ |
| $1/(z-a)$ | 圆盘含 $a$ | $2\pi i$（见下节变形） |
| $\bar z$、$|z|^2$ | — | 一般 $\neq 0$ |

---
## 5. 变形定理与环域扩展

### 5.1 变形（homotopy）直觉

若 $f$ 在两条闭围道 $\gamma_0$、$\gamma_1$ **之间的区域**上解析（两条曲线可在解析域内互相变形），则
$$
\oint_{\gamma_0}f\,dz=\oint_{\gamma_1}f\,dz.
$$
工科用法：把奇形怪状的围道**换成圆**，积分不变。

### 5.2 环域 / 挖洞版 Cauchy

设 $f$ 在环域 $r<|z-z_0|<R$ 上解析。对外圈 $\gamma_R$ 与内圈 $\gamma_r$（同方向，例如都逆时针）有
$$
\oint_{\gamma_R}f\,dz=\oint_{\gamma_r}f\,dz.
$$
若再规定内圈取**反向**（使“环域边界定向”正确），则外圈积分减去内圈积分等于零——这是多连通区域上 Cauchy 定理的原型。

> [!example] 绕原点的任意简单闭曲线 $C$
> 在 $\mathbb{C}\setminus\{0\}$ 上 $1/z$ 解析。把 $C$ 变形到单位圆：
> $$
> \oint_C\frac{dz}{z}=2\pi i.
> $$
> 若 $C$ **不围**原点，则可变形到一点，积分为 $0$。

### 5.3 绕数预告

更精确的语言是**绕数（winding number）** $n(C,z_0)$：
$$
\oint_C\frac{dz}{z-z_0}=2\pi i\cdot n(C,z_0).
$$
简单正定向闭曲线围住 $z_0$ 时 $n=1$。留数定理是这一思想的推广。

---
## 6. 计算流程（工科清单）

面对 $\int_\gamma f\,dz$，按顺序问：

1. **有无原函数？** 有 → 端点求值（闭路径则 $0$）。
2. **$f$ 是否在围道内部（含边界）解析？** 单连通域上解析 → Cauchy $\Rightarrow 0$。
3. **奇点在哪里？** 能变形到圆则在圆上参数化；典型结果含 $2\pi i$。
4. **不解析（如 $\bar z$）** → 老老实实参数化，或拆成 $dx,dy$ 实积分。

> [!example] $\displaystyle\oint_{|z|=2}\frac{e^z}{z-1}\,dz$
> $e^z/(z-1)$ 在 $|z|<2$ 内仅 $z=1$ 处不解析，**不能**直接用 Cauchy 定理得零。下一讲的 Cauchy 积分公式直接给出答案 $2\pi i\,e^1$。目前可用变形：换成 $|z-1|=\varepsilon$ 的小圆再参数化（繁），或等 CIF。

> [!example] $\displaystyle\int_\gamma \bar z\,dz$，$\gamma$ 为从 $0$ 到 $1$ 再竖直到 $1+i$ 的折线
> 必须分段参数化：
> - $\gamma_1:t\in[0,1]$，$z=t$，$\bar z=t$，$dz=dt$ $\Rightarrow$ $\int_0^1 t\,dt=1/2$
> - $\gamma_2:t\in[0,1]$，$z=1+it$，$\bar z=1-it$，$dz=i\,dt$
> $$
> \int_0^1(1-it)i\,dt=i\int_0^1 1\,dt+\int_0^1 t\,dt=i+\frac12.
> $$
> 总和 $=1+i$。换路径（例如直线 $z=t(1+i)$）一般得不同值——与“无原函数 / 不解析”一致。

---
## 7. 与实分析线积分的对照

| | 实平面向量场 | 复线积分 |
|--|--------------|----------|
| 对象 | $\mathbf{F}=(P,Q)$，$\int P\,dx+Q\,dy$ | $f(z)\,dz$ |
| 无旋条件 | $Q_x=P_y$ | CR（解析） |
| 单连通 + 无旋 | 保守场，路径无关 | Cauchy：闭积分为零 |
| 典型非零环量 | 绕原点的 $(-y,x)/r^2$ | $dz/z$ |

复分析把“无旋 + 单连通 $\Rightarrow$ 保守”包装成更强的解析性语言，并进一步推出 CIF、幂级数、留数——这是课程后半段的发动机。

---
## 8. 自检

1. 会用参数化定义计算 $\int_\gamma f\,dz$（尤其单位圆）。
2. 记住 $\oint dz/z=2\pi i$；会对比 $z^2$（积分为零）与 $\bar z$（不必为零）。
3. 单连通 + 解析 $\Rightarrow$ Cauchy 定理（闭积分为零 / 路径无关 / 有原函数）。
4. 会用变形定理把围道换成圆；分清“奇点在内 / 在外”。

> [!success]- 参考答案
> 1. $z=\gamma(t)$，$\int f(\gamma)\gamma'\,dt$；单位圆 $\gamma=e^{i\theta}$，$\gamma'=ie^{i\theta}$。
> 2. $\oint_{|z|=R}dz/z=2\pi i$（任意 $R>0$）。$z^2$ 有原函数 $\Rightarrow$ 闭积分为 $0$；$\bar z$ 不解析，闭积分可非零。
> 3. 单连通域上解析 $\Rightarrow$ 闭积分为零 $\Leftrightarrow$ 路径无关 $\Leftrightarrow$ 有原函数。穿孔平面上 $1/z$ 反例。
> 4. 内部无奇点可缩成一点得 $0$；仅围住原点的简单闭曲线上 $\oint dz/z=2\pi i$。奇点在外 $\Rightarrow$ 可变形到无奇区域 $\Rightarrow 0$。

> [!example] 练习：奇点在内还是在外
> 计算（或判断）$\displaystyle\oint_{|z|=2}\frac{dz}{z-3}$ 与 $\displaystyle\oint_{|z|=2}\frac{dz}{z-1}$。

> [!success]- 练习参考答案
> $|z|=2$ 不围 $z=3$（在外）$\Rightarrow$ 被积在闭盘上解析 $\Rightarrow$ 积分为 $0$。
> 围住 $z=1$：$dz/(z-1)$ 同 $dz/w$ 绕 $0$ 一周 $\Rightarrow 2\pi i$。

下一讲：Cauchy 积分公式——把“围住一点的值”写成围道积分。

## 参考

- Jeremy Orloff, *18.04 Topic 3: Line integrals and Cauchy's theorem*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
