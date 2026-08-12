---
title: "Course Review"
aliases:
  - "课程回顾"
  - "6.006 总结"
tags:
  - Algorithms
  - MIT6006
  - Review
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Algorithms Next Steps]]"
related:
  - "[[Algorithms and Computation]]"
  - "[[Complexity]]"
---

# Lec20 Course Review：把整门课串成一条线

## 本讲主线
- 这讲不是新算法，而是回看整门课到底训练了什么能力。
- 官方强调学生应能做到四件事：
  - 解决困难的计算问题
  - 论证算法正确
  - 论证算法“好”
  - 清晰表达以上内容

## 课程主线回顾

### 1. 建模
- 先把实际问题抽象成：
  - 输入是什么
  - 输出正确性的标准是什么
  - 数据规模如何增长

### 2. 算法设计
- 常见范式：
  - 递归与分治
  - 图搜索
  - 贪心
  - 动态规划
  - 数据结构增强与平衡

### 3. 正确性证明
- 常见武器：
  - 归纳法
  - 循环不变式
  - 交换论证
  - 割与路径性质
  - 最优子结构

### 4. 复杂度分析
- 不能只说“跑得快”，要说明：
  - 时间复杂度
  - 空间复杂度
  - 最坏 / 期望 / 摊还
  - 对什么输入参数分析

## 从 6.006 到后续课程
- 官方讲义把后续方向指向：
  - `6.046`：Design and Analysis of Algorithms
  - `6.851`：Advanced Data Structures
  - `6.854`：Advanced Algorithms

## 进一步扩展的方向
- 在“放宽问题定义”方向上：
  - 随机算法
  - 数值算法 / 连续优化
  - 近似算法
- 在“改变计算模型”方向上：
  - Cache / memory hierarchy
  - Quantum computing
  - Parallel / distributed computation

## 复习时应怎么串联整门课
- 看到问题先判断它像哪一类：
  - sequence / set
  - graph
  - shortest path
  - DP
  - complexity
- 再问：
  - 需要什么接口
  - 正确性靠什么证明
  - 时间瓶颈在哪里

## 这一讲的真正提醒
- 学完整门课，不是会 20 个孤立算法。
- 真正目标是形成一套完整工作流：

```text
抽象问题
-> 选模型与数据结构
-> 设计算法
-> 证正确
-> 分析复杂度
-> 清晰表达
```

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Algorithms Next Steps]]（下一讲）
- [[Algorithms and Computation]]
- [[Complexity]]

## 复习提问
- 6.006 这门课最核心的学习目标是什么？
- 正确性证明和复杂度分析为什么与“写出代码”同等重要？
- 哪些常见算法范式已经在课程中反复出现？
- 学完整门课后，解决新问题的流程应该是什么？
