---
title: "Complexity"
aliases:
  - "复杂度类"
  - "P NP EXP R"
  - "规约"
  - "NP-hard"
tags:
  - Algorithms
  - Complexity
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Course Review]]"
related:
  - "[[Dynamic Programming Part 4]]"
  - "[[Algorithms Next Steps]]"
---

# Lec19 Complexity：P、NP、EXP、R 与规约

## 本讲主线
- 课程从“如何设计算法”进一步走到“哪些问题本质上难”。
- 重点不是记定义，而是建立复杂性分类的思维框架。
- 官方强调的关键词：
  - `P`
  - `NP`
  - `EXP`
  - `R`
  - hardness / completeness
  - reductions

![[alg-complexity-01.svg]]

## 判定问题视角
- 复杂性理论通常先把问题写成**判定问题**：
  - 输出只有 YES / NO
- 这样更便于统一比较问题难度。

## 类 `P`
- 存在确定性多项式时间算法的问题集合。
- 直观理解：
  - 按目前标准，这类问题“有效可解”

## 类 `EXP`
- 可在指数时间内求解的问题集合。
- 一般认为远比 `P` 大。
- 直观上：
  - “可算”，但通常不现实

## 类 `NP`
- YES 实例存在多项式长度证书，且证书可在多项式时间内验证。
- 要点：
  - `NP` 不是“不能多项式解决”
  - 它是“答案若为 YES，可快速验证”

## 类 `R`
- 引入随机化算法的复杂性类。
- 课程用它说明：
  - 一旦允许随机性，算法模型和可解性边界会发生变化

## Hardness 与 Completeness
- `A` 对某类问题是 hard：
  - 意味着该类中所有问题都能规约到 `A`
  - 所以 `A` 至少一样难
- `A` 是 complete：
  - 既属于该类
  - 又是该类 hardest 的代表

## 规约（Reduction）
- 规约是复杂性理论的核心工具。
- 目标：
  - 用一个已知难的问题，证明另一个问题也难
- 典型做法：
  - 把问题 `X` 的任意实例，多项式时间变换成问题 `Y` 的实例
  - 且两者答案保持等价
- 若 `X <=p Y` 且 `X` 很难，那么 `Y` 至少不更容易。

## 典型 NP-complete / NP-hard 例子
- 官方讲义列举：
  - Subset Sum
  - 3-Partition
  - Rectangle Packing
  - Longest Simple Path
  - Traveling Salesman Problem
  - 3-Coloring
  - Clique
  - SAT
  - Sudoku、Minesweeper 等谜题

## 这一讲最该形成的判断
- 算法设计不只是“能不能想到做法”，还要问：
  - 这个问题是否可能本质上就没有多项式算法？
- 当怀疑问题太难时：
  - 下一步不是乱试，而是考虑规约与复杂性分类

## 学习重点
- `P`：快解
- `NP`：快验
- `EXP`：慢解但可解
- `R`：允许随机
- reduction：复杂性证明的主要武器

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Course Review]]（下一讲）
- [[Dynamic Programming Part 4]]
- [[Algorithms Next Steps]]

## 复习提问
- 为什么复杂性理论喜欢先把问题写成判定问题？
- `NP` 的准确含义是什么？
- “hard”和“complete”差在哪里？
- 为什么规约能证明问题困难？
