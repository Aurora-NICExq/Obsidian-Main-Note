---
aliases: [信号系统与推断, Signals Systems and Inference, MIT 6.011, 6.011, SSI]
tags: [ee, signals_systems_inference, MOC]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Signals and Systems MOC]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
  - "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
down:
  - "[[Transforms and Energy Spectra]]"
  - "[[State-Space Models]]"
  - "[[Stability Reachability and Observability]]"
  - "[[Observers for State Estimation]]"
  - "[[State Feedback and Observer-Based Control]]"
  - "[[MMSE and LMMSE Estimation]]"
  - "[[Wide-Sense Stationary Processes]]"
  - "[[Power Spectral Density]]"
  - "[[Wiener Filtering]]"
  - "[[Hypothesis Testing and Signal Detection]]"
  - "[[Matched Filtering]]"
---
# Signals Systems and Inference (MIT 6.011) MOC

> 课程底本：[MIT 6.011 Signals, Systems and Inference (Spring 2018)](https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/)（George Verghese / Alan V. Oppenheim）。在 [[Signals and Systems MOC|信号与系统]] 之上接入**状态空间、估计、宽平稳过程与检测**；概率侧对齐 [[Probability and Statistics (MIT 18.05) MOC]]；滤波/卡尔曼后续见 [[Estimation and Kalman Filtering (NPTEL) MOC]]。

![[ssi-moc-roadmap.svg]]

## 01 变换、能量与状态空间
- [[Transforms and Energy Spectra]]：从 S&S 到 ESD、确定性自相关；能量信号的频谱桥
- [[State-Space Models]]：$\dot x=Ax+Bu,\ y=Cx+Du$；离散类比与线性化
- [[Stability Reachability and Observability]]：BIBO / 渐近稳定；能达 / 能观秩与 PBH；隐模态

## 02 观测器与状态反馈
- [[Observers for State Estimation]]：Luenberger 观测器；误差动力学 $A-LC$
- [[State Feedback and Observer-Based Control]]：极点配置 $A-BK$；分离原理草图

## 03 估计与随机过程
- [[MMSE and LMMSE Estimation]]：正交原理、法方程；高斯 ⇒ 线性最优
- [[Wide-Sense Stationary Processes]]：均值 / ACF 只依赖时差；WSS 经 LTI
- [[Power Spectral Density]]：Wiener–Khinchin；$S_y=|H|^2 S_x$
- [[Wiener Filtering]]：因果 / 非因果直觉；频域 Wiener 形式

## 04 检测与匹配滤波
- [[Hypothesis Testing and Signal Detection]]：Bayes / MAP、Neyman–Pearson、ROC
- [[Matched Filtering]]：SNR 最大；相关器等价

## 插图（预生成 SVG）

嵌入 `90 Assets/diagrams/signals-systems-inference/`（文件名形如 `ssi-….svg`）。重新生成：

```bash
cd "90 Assets/scripts/signals_systems_inference"
.venv/bin/python generate_all.py
```
