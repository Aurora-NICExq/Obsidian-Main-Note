---
aliases: [Graph, 图, Adjacency Matrix, 邻接矩阵, Adjacency List, 邻接表]
tags: [c_language, data_structure]
up: "[[C_DataStruct MOC]]"
related: "[[Tree|Tree]], [[LinkedList|Linked List]]"
down: ""
---
# 图

> [!summary] 核心思想
> 图 $G = (V, E)$ 是最一般的关系结构：由边连接的顶点集合，没有层次或环的限制。[[Tree|树]]是连通且无环的特例。两种常见表示方法在空间和查询速度之间权衡：**邻接矩阵**提供 $O(1)$ 的边检测，但需要 $O(V^2)$ 空间；而**邻接表**仅需 $O(V + E)$ 空间，适合稀疏图。

前置知识：[[LinkedList|链表]]（用于构建邻接表）和[[Tree|树]]（图的一个特例）。

---

## 1. 定义

**图**是**顶点集**和**边集**的结构，记作
$$ G = (V, E). $$
$V$ 是顶点（节点）的集合；$E$ 是边的集合，每条边表示两个顶点之间的关系。树是分层的无环网络，而图是一般的关系网络——树是连通且无环的图。

![[tikz-graph-01.svg]]

## 2. 分类

按边方向：

- **无向图**——边 $(u,v)$ 和 $(v,u)$ 是同一条边。
- **有向图**——边有方向；$\langle u,v \rangle$ 从 $u$ 指向 $v$。

按边权：

- **无权图**——边仅记录连接是否存在。
- **带权图**——每条边带有权重（距离、成本、时间等）。

按可达性：

- **连通图**（无向）——任意两个顶点可互相到达。
- **强连通图**（有向）——任意两个顶点可沿着方向互相到达。
- **非连通图/非强连通图**——不符合上述条件。

## 3. 术语

**度。**

- 无向图：度 $\deg(v)$ 是与 $v$ 相关联的边的数量。
- 有向图：**入度** $indeg(v)$ 统计指向 $v$ 的边数，**出度** $outdeg(v)$ 统计从 $v$ 出发的边数，且 $\deg(v) = indeg(v) + outdeg(v)$。

**路径与环。**

- **路径**——顶点序列 $v_1 \to v_2 \to \cdots \to v_k$；其**长度**是边的数量（或权重之和）。**简单路径**不重复顶点。
- **环**——起点与终点重合的路径。无环图很重要：**DAG**（有向无环图）是拓扑排序的核心。

**子图与完全图。**

- **子图**——由顶点和边的子集构成的图。
- **完全图**——每对顶点都相邻。无向图 $K_n$ 有 $\frac{n(n-1)}{2}$ 条边；有向完全图（无自环）有 $n(n-1)$ 条边。

**稠密与稀疏。** 稠密图边数很多（接近完全图）；稀疏图边数很少。图的密度决定表示方法的选择：矩阵适合稠密图，邻接表适合稀疏图。

## 4. 表示方法

### 边列表

边列表将每条边存储为一个记录，通常为 `(u, v)` 加可选权重 `w`：

```c
#include <stdio.h>
#define MAXE 100

typedef struct {
    int u, v;
    int w;
} Edge;

int main(void) {
    Edge edges[MAXE] = {
        {0, 1, 5},
        {0, 2, 2},
        {1, 3, 1},
        {2, 3, 7}
    };
    int edgeCount = 4;
    for (int i = 0; i < edgeCount; i++) {
        printf("edge %d: (%d -> %d), w = %d\n",
               i, edges[i].u, edges[i].v, edges[i].w);
    }
    return 0;
}
```

### 邻接矩阵

邻接矩阵是一个 $n \times n$ 数组 `A`，顶点编号 `0...n-1`，其中 `A[i][j]` 表示从顶点 `i` 到顶点 `j` 的关系（是否存在边或边的权重）。对于顶点 `0,1,2,3` 和无向边 `(0,1),(0,2),(1,3),(2,3)`：

$$
\begin{bmatrix}
0 & 1 & 1 & 0 \\
1 & 0 & 0 & 1 \\
1 & 0 & 0 & 1 \\
0 & 1 & 1 & 0
\end{bmatrix}
$$

矩阵是对称的（无向图），且在无权情况下，第 `i` 行中 1 的个数等于 $\deg(i)$。其性质：

1. **边检测为 $O(1)$**——直接读取 `A[i][j]`。
2. **列出顶点的邻居为 $O(n)$**——扫描整行。
3. **空间固定为 $O(n^2)$**。
4. 无向图给出的矩阵是**对称**的；有向图一般不对称。
5. 对于有向（无权）图：第 `i` 行非零 = 出度；第 `j` 列非零 = 入度。

```c
#define MAXV 100
#define INF  0x3f3f3f3f

typedef struct {
    int vexnum;            // number of vertices
    int arcnum;            // number of edges
    int mat[MAXV][MAXV];   // adjacency matrix
} MGraph;
```

### 邻接表

邻接表为每个顶点维护一个由其关联边组成的链表，只记录该顶点实际连接的邻居。它避免了矩阵浪费空间存储大量"非边"。其复杂度：

- **空间**为 $O(V + E)$——在稀疏图上远小于 $O(V^2)$。
- **列出顶点的邻居**与度数成正比——高效。
- **检测 `u` 与 `v` 是否相连**需扫描 `u` 的链表：最坏情况 $O(\deg(u))$。
- **全图遍历**（DFS/BFS）运行时间为 $O(V + E)$——这些算法理想复杂度的来源。

```c
#define MAXV 100

// edge node
typedef struct ArcNode {
    int adjvex;             // index of the adjacent vertex
    int weight;             // weight (omit for unweighted graphs)
    struct ArcNode *next;   // next edge
} ArcNode;

// vertex node
typedef struct {
    int data;               // vertex payload (could be char, etc.)
    ArcNode *first;         // pointer to the first incident edge
} VNode;

// graph
typedef struct {
    VNode vertices[MAXV];
    int vexnum;             // number of vertices
    int arcnum;             // number of edges
} ALGraph;
```

---

> [!important] 一句话总结
> 图是顶点加边；在稠密图上用邻接矩阵以获得 $O(1)$ 边检测，在稀疏图上用邻接表以获得 $O(V+E)$ 的空间和遍历效率。
