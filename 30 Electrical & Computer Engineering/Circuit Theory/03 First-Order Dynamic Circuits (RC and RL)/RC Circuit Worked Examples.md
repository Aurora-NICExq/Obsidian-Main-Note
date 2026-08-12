---
title: "RC Circuit Worked Examples"
aliases: ["RC 电路例题套路", "RC Circuit Examples"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[First-Order Shortcut Method]]"]
related: ["[[Introduction to RC Circuits]]", "[[Source-Free and Driven RC Response]]", "[[Thevenin's Theorem]]", "[[Norton's Theorem]]"]
---
# RC Circuit Worked Examples

## RC 电路例题

> [!definition] 最快的解题思路
> 先确定初值和终值，再写出指数衰减的一阶模板——这是解决 RC 问题的最快途径。

---
## 1. 一阶模板

对于任意一阶 RC 量（电容电压或电阻电流），使用统一模板：
$$
x(t)=x(\infty)+\big[x(0^+)-x(\infty)\big]e^{-t/\tau}
$$

其中：
$$
\tau=R_{\text{eq}}C
$$

---
## 2. 解题步骤

> [!example] 五步法
> 1. **识别状态变量**——通常为电容电压 $v_C(t)$。
> 2. **求初值**——电容电压连续，因此 $v_C(0^+)=v_C(0^-)$。
> 3. **求终值**——$t\to\infty$ 时电容开路；求解直流稳态。
> 4. **求时间常数**——从电容端看入求 $R_{\text{eq}}$，则 $\tau=R_{\text{eq}}C$。
> 5. **代入模板**并检查单位和极限值。

---
## 3. 常见结果形式

放电：
$$
v_C(t)=V_0e^{-t/\tau}
$$

充电：
$$
v_C(t)=V_f\left(1-e^{-t/\tau}\right)
$$

对应的电流也是指数形式；其符号取决于所选参考方向。

---
## 4. 常见错误

> [!attention] 注意
> - 将 $v_C(0^+)$ 写成 $0$（忽略了电压连续性）。
> - 时间常数中取了错误的 $R_{\text{eq}}$（没有从电容端看入）。
> - 只写下公式而未检查 $t=0$ 和 $t\to\infty$ 是否满足物理边界条件。

---
## 5. 总结

> [!attention] RC 例题
> 一旦"初值 + 终值 + 时间常数"确定，一阶 RC 响应就基本确定了。

## 参见
- [[Introduction to RC Circuits#4. Time Constant and Physical Meaning]]
- [[Source-Free and Driven RC Response]]
- [[Thevenin's Theorem]]
- [[Norton's Theorem]]
- [[First-Order Shortcut Method]]
