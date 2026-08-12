---
aliases: [P08, 架构（Transformer）：token、注意力与位置编码]
up: "[[Deep Learning MOC]]"
related: "[[P07-Optimization Scaling Rules]], [[P09-Deep Learning Hacker Guide]]"
tags:
  - DeepLearning
  - MIT-6.7960
  - LectureNotes
lecture: P08
title: 架构（Transformer）：token、注意力与位置编码
source: SRT字幕（中英）
---

# P08 架构：Transformer（实践导向版）

## 0. 讲座定位与三大核心思想
讲座开门见山：这是一场更偏实践的课，目标是让你知道“Transformer 这个具体实现怎么回事”。

课程把 Transformer 拆成三块核心思想：
1. **基于 token 的操作**（把输入变成一串 token 向量）
2. **注意力机制（attention）**（讲座说这是“真正的新内容”，其他很多是旧概念换名字）
3. **位置编码（positional encoding）**（把顺序/坐标信息注入模型）

## 1. Token 视角：把输入统一成一个矩阵
讲座用统一表示法讲 token：
- 有 `n` 个 token（序列长度/patch 数）
- 每个 token 是 `d` 维向量
- 整体可以写成 `X ∈ R^{n×d}`

在这个视角下，“对每个 token 做同一个 MLP”就是一种 **token 级的点态非线性（pointwise nonlinearity）**：参数共享、逐行处理。

## 2. 注意力的直觉：输出 token = 输入 token 的加权组合
讲座反复强调一个直觉：注意力做的事情非常像“加权平均/加权组合”：
- 你不是只看局部邻域（像卷积）
- 而是学一个权重矩阵，让每个 token 能从其他 token 汇聚信息

这也解释了注意力为什么适合处理长距离依赖：它允许“直接连到任意位置”。

## 3. Query–Key–Value 注意力：最常见的数学形式
讲座给出注意力最常见的形式：查询（Q）、键（K）、值（V）。

核心流程（抓住计算图就够了）：
1. 线性投影：`Q = X W_Q`, `K = X W_K`, `V = X W_V`
2. 相似度：用 `Q K^T` 得到 token 两两之间的匹配分数
3. 缩放 + 归一化：讲座提到会**除以维度的平方根**，再对分数做 softmax 得到注意力权重
4. 聚合：用注意力权重对 `V` 做加权组合得到输出

讲座提到 softmax 带来“良好的归一化与数值优势”，以及注意力矩阵元素如何解释为“分配了多少注意力”。

把它写成一行公式（讲座称之为“著名的注意力方程”）：
```text
Attention(Q,K,V) = softmax( (QK^T) / sqrt(d) ) · V
```
这里 `d` 是注意力内部用来做相似度的向量维度（讲座用“除以维度的平方根”来解释缩放的必要性）。

## 4. 自注意力（Self-Attention）
自注意力指 Q/K/V 都来自同一组输入 token 序列。
讲座用视觉 token 的例子解释：观察某个 token 的自注意力，就是看它对所有其他 token 的关注强度分布。

## 5. 多头注意力（Multi-Head）
讲座给的核心理解是：
- 不只做一个注意力层
- 而是并行做 `k` 个注意力层（heads）
- 不同 head 可以学会关注不同类型的信息

## 6. Transformer block：残差 + 归一化 + MLP + 注意力
讲座在结构图里提到了典型组件：
- 残差连接（residual）
- token norm / 层归一化（LayerNorm）：减均值、按方差归一化等，讲座强调它对优化有好处（归一化激活值会影响权重更新的尺度）
- MLP（也被叫作“前馈层 feed-forward”，本质是对每个 token 应用同一个 MLP）

## 7. 位置编码：注意力本身是“排列不变/等变”的，需要注入位置信息
讲座明确指出：注意力机制在没有位置信息时，对 token 的排列是对称的。
要让模型理解顺序/坐标，就要加位置编码。

讲座涉及的点包括：
- 正弦位置编码（sinusoidal）
- 傅里叶位置编码（讲座提到其在一些场景里更好）
- 位置编码不仅是“序号”，也可以注入领域知识（例如经纬度等）

## 8. 因果注意力与掩码（Causal Mask）
讲座讨论了自回归语言建模的因果性：
- 前面的 token 影响后面的 token
- 但后面的 token 不该反向“看见未来”

实现上用因果掩码（mask）作用到注意力矩阵：把不允许关注的位置屏蔽掉（形成上三角/下三角结构的可见性约束）。

讲座也提到交叉注意力（cross-attention）等扩展形态，用于多模态或 encoder–decoder 结构。

## 9. 复习清单
- token 矩阵 `n×d` 的视角为什么重要？它把哪些操作统一了？
- 注意力的本质为什么可以理解成“加权组合”？
- Q/K/V 三个投影各自扮演什么角色？softmax 在干嘛？
- 为什么必须要位置编码？因果掩码解决什么问题？
- Transformer block 里残差、LayerNorm、MLP 的存在各自有什么直觉价值？
