---
tags:
  - embedded
  - 控制算法
---
# PID_Algorithms

>[!note]
>PID 控制算法，是工业控制里最常见的一种**反馈控制算法**。  
它的目标很简单：**让系统输出尽量接近期望值**。



## 简介

PID ：Proportional、Integral、Derivative

控制器会先计算误差：
$$
e(t)=r(t)-y(t)
$$
其中：

- $r(t)$：目标值
- $y(t)$：实际输出值
- $e(t)$:误差

PID 控制器输出为：
$$
u(t)=K_p e(t)+K_i \int e(t)\,dt + K_d \frac{de(t)}{dt}
$$
这里： $K_p$：比例系数、$K_i$：积分系数、$K_d$：微分系数

## 反馈控制框图


![[tikz-pid_algorithms-01.svg]]

## 建模

### 电机的电学方程

![[tikz-pid_algorithms-02.svg]]

$$
L_a\frac{dI_a}{dt}+R_aI_a=U_a-K_e\omega
$$

### 电机的机械方程
