---
aliases: [深度学习 MOC, Deep Learning Index, MIT 6.7960 MOC, 深度学习索引]
tags: [DeepLearning, MIT-6.7960, MOC]
up: ""
related: "[[Rust MOC|Rust MOC]], [[Mathematics MOC|数学 MOC]]"
down: "[[P02-How to Train Neural Networks|如何训练神经网络]], [[P03-Approximation Theory|近似理论]], [[P04-Architecture-Grid|架构：网格]], [[P05-Architecture-Graph|架构：图]], [[P07-Optimization Scaling Rules|优化的缩放规则]], [[P08-Architecture-Transformer|架构：Transformer]], [[P09-Deep Learning Hacker Guide|深度学习黑客指南]], [[P10-Architecture-Memory|架构：记忆]]"
---
# Deep Learning MOC

> [!summary] 学习主线
> MIT 6.7960 *Deep Learning*（Fall 2024）课堂复习笔记，按讲座编号一讲一份，由中英 SRT 字幕整理。主线为：**训练机制**（P02）→ **表达能力**（P03）→ **结构化架构**（P04 网格 / P05 图 / P08 Transformer / P10 记忆）→ **规模与工程**（P07 缩放 / P09 经验法则）。

## 一、训练与优化基础

- [[P02-How to Train Neural Networks|P02 如何训练神经网络]]：优化、计算图与自动微分的共同语言
- [[P07-Optimization Scaling Rules|P07 优化的缩放规则]]：最优学习率为何漂移，如何让训练可扩展

## 二、理论：网络能表示什么

- [[P03-Approximation Theory|P03 近似理论]]：通用近似定理能解释多少、又解释不了什么

## 三、结构化架构

- [[P04-Architecture-Grid|P04 架构：网格]]：从 MLP 到 CNN，归纳偏置与权值共享
- [[P05-Architecture-Graph|P05 架构：图]]：图神经网络与消息传递
- [[P08-Architecture-Transformer|P08 架构：Transformer]]：token、注意力、位置编码与掩码
- [[P10-Architecture-Memory|P10 架构：记忆]]：CNN → RNN → LSTM → 自回归的序列建模

## 四、工程实践

- [[P09-Deep Learning Hacker Guide|P09 深度学习黑客指南]]：数据、评估、归一化、增强与 EMA

## 推荐复习顺序

先搭框架再补细节：

1. **P02** — 训练与反向传播的共同语言（优化 / 计算图 / 自动微分）
2. **P03** — 表达能力与“通用近似”的边界
3. **P04 + P05** — 结构化架构的两个代表（网格与图）
4. **P08** — Transformer 的具体实现
5. **P10** — 序列与记忆（CNN → RNN → LSTM → 自回归）
6. **P07** — 规模上来后为什么调参会崩，“缩放”想解决什么
7. **P09** — 把训练系统跑稳的经验法则

> [!note] 缺讲说明
> P01 与 P06 无对应字幕来源，故本库中暂缺。
