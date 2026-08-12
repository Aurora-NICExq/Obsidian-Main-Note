---
aliases:
  - 估计与卡尔曼滤波
  - Estimation and Kalman Filtering
  - NPTEL 108105059
  - Kalman Filtering MOC
  - 信号与系统估计
tags: [ee, estimation_kalman, MOC]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
  - "[[Signals and Systems MOC]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
  - "[[STM32 MOC]]"
down:
  - "[[Random Processes for Estimation]]"
  - "[[Linear MMSE and Innovations]]"
  - "[[Least Squares and Optimal Filters]]"
  - "[[Adaptive Filters]]"
  - "[[State Estimation Problem]]"
  - "[[Kalman Filter Derivation]]"
  - "[[Kalman Filter Properties and Steady State]]"
  - "[[Kalman Filter Applications]]"
  - "[[Nonlinear Filtering EKF and Beyond]]"
  - "[[System Identification and Recursive Least Squares]]"
  - "[[Practical Identification and Instrumentation]]"
---
# Estimation and Kalman Filtering (NPTEL) MOC

> 主课：[NPTEL *Estimation of Signals and Systems*](https://nptel.ac.in/courses/108105059)（IIT Kharagpur，Prof. S. Mukhopadhyay，课程号 **108105059**）。随机过程 → 线性 MMSE / 新息 → 最小二乘与最优滤波 → 自适应 → 状态估计与 **Kalman filter** → 系统辨识 / RLS → 实用校验与仪表。
>
> **辅读：** [MIT OCW 16.322 Stochastic Estimation and Control](https://ocw.mit.edu/courses/16-322-stochastic-estimation-and-control-fall-2004/)（随机估计与控制视角；非线性与连续时间表述更完整）。可选：Siena *Statistical Estimation and Filtering* 类讲义中的 EKF / UKF 笔记（见 [[Nonlinear Filtering EKF and Beyond]]）。
>
> 与 [[Signals Systems and Inference (MIT 6.011) MOC]]（LMMSE、Wiener、状态空间推断）、[[Signals and Systems MOC]]（LTI / 卷积）、[[Probability and Statistics (MIT 18.05) MOC]]（期望、协方差、Bayes）交叉阅读。

![[ekf-moc-roadmap.svg]]

## 01 随机过程与线性估计
- [[Random Processes for Estimation]]：ACF、WSS、线性系统下的二阶统计（压缩 NPTEL L2–L10）
- [[Linear MMSE and Innovations]]：正交原理、新息、递推结构（L11–L14）
- [[Least Squares and Optimal Filters]]：LS、最优 IIR / Wiener 直觉（L15）
- [[Adaptive Filters]]：LMS / RLS 自适应直觉（L16）

## 02 卡尔曼滤波
- [[State Estimation Problem]]：状态空间、噪声模型、估计目标（L17）
- [[Kalman Filter Derivation]]：预测 / 更新、标量数值走查（L18–L19）
- [[Kalman Filter Properties and Steady State]]：最优性、稳态增益、代数 Riccati（L20–L21）
- [[Kalman Filter Applications]]：跟踪、传感器融合素描（L22 + 16.322 风味）
- [[Nonlinear Filtering EKF and Beyond]]：EKF / UKF / 粒子滤波简述（Siena / 16.322 辅读）

## 03 系统辨识与实践
- [[System Identification and Recursive Least Squares]]：参数估计、RLS 与 KF 联系（L23–L26）
- [[Practical Identification and Instrumentation]]：阶次、残差检验、仪表直觉（L27–L29；轻链 [[STM32 MOC]]）

## 插图（预生成 SVG）

嵌入 `90 Assets/diagrams/estimation-kalman/`（`ekf-….svg`）。重新生成：

```bash
cd "90 Assets/scripts/estimation_kalman"
.venv/bin/python generate_all.py
```

| 文件 | 用途 |
|------|------|
| `ekf-moc-roadmap.svg` | 本 MOC 路线 |
| `ekf-kf-cycle.svg` | 预测 / 更新循环 |
| `ekf-innovation.svg` | 新息 |
| `ekf-adaptive.svg` | 自适应滤波 |
| `ekf-gaussian-update.svg` | 高斯更新直觉 |
| `ekf-identification.svg` | 系统辨识流程 |
| `ekf-nonlinear.svg` | EKF 线性化思路 |
