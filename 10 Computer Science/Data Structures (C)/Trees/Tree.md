---
aliases: [Tree, 树, Binary Tree, 二叉树, Binary Search Tree, 二叉搜索树, Huffman Tree, 哈夫曼树]
tags: [c_language, data_structure]
up: "[[C_DataStruct MOC]]"
related: "[[Graph|Graph]], [[Stack|Stack & Queue]], [[Splay Tree|Splay Tree]], [[Scapegoat Tree|Scapegoat Tree]]"
down: "[[Splay Tree|Splay Tree]], [[Scapegoat Tree|Scapegoat Tree]], [[Greedy Algorithm,Minimum Spanning Tree|Greedy & MST]]"
---
# 树

> [!summary] 核心思想
> 树以**层次结构**组织数据：一个根节点，其他每个节点有且仅有一个父节点。它是包含关系、目录结构和决策路径的自然模型。**二叉搜索树**的特化使元素保持有序，在平衡时搜索、插入和删除的时间复杂度为 $O(\log n)$。树是[[Graph|图]]的特例——连通且无环。

前置知识：递归、指针和[[Stack|队列]]（用于层序遍历）。

---

## 1. 树的基本概念

**树**是 $n \ge 0$ 个节点的有限集合，满足：

- 当 $n = 0$ 时为**空树**；
- 当 $n > 0$ 时，有且仅有一个特殊的**根**节点，其余节点划分成 $m \ge 0$ 个互不相交的子集，每个子集本身也是一棵树——根的**子树**。

![[tikz-tree-01.svg]]

### 术语

- **父节点 / 子节点**——直接位于另一个节点上方/下方的节点。
- **兄弟节点**——同一父节点的子节点。
- **叶子节点**——没有子节点的节点；**分支节点**——至少有一个子节点的节点。
- **节点的度**——其子节点的个数；**树的度**——所有节点度的最大值。
- **路径**——两个节点之间的节点序列；**路径长度**——路径上的边数。
- **层次**——根为第 1 层；**高度（深度）**——树中的最大层次。

### 关键性质

1. 除根节点外，每个节点有且仅有一个父节点。
2. 一个节点可以有 $0$ 个或多个子节点。
3. 节点之间是**层次**关系，而非简单的前驱/后继顺序。
4. 一棵 $n$ 个节点的树恰好有 **$n - 1$ 条边**。

### 表示方法

每个节点存储一个数据域加若干指针。"第一个孩子 / 下一个兄弟"表示法用每节点仅两个指针来建模任意树：

```c
typedef struct TreeNode {
    int data;
    struct TreeNode *firstChild;   // first child
    struct TreeNode *nextSibling;  // next sibling
} TreeNode;
```

二叉树节点及先序遍历：

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    char data;
    struct Node *left, *right;
} Node;

Node *newNode(char x) {
    Node *p = (Node *)malloc(sizeof(Node));
    p->data = x;
    p->left = p->right = NULL;
    return p;
}

void preorder(Node *root) {
    if (root == NULL) return;
    printf("%c ", root->data);   // root
    preorder(root->left);        // left
    preorder(root->right);       // right
}

int main(void) {
    //      A
    //     / \
    //    B   C
    //   / \
    //  D   E
    Node *A = newNode('A');
    Node *B = newNode('B');
    Node *C = newNode('C');
    Node *D = newNode('D');
    Node *E = newNode('E');
    A->left = B; A->right = C;
    B->left = D; B->right = E;
    preorder(A);   // A B D E C
    return 0;
}
```

## 2. 二叉树

**二叉树**是每个节点至多有两个子节点的树，严格区分为**左孩子**和**右孩子**。当一个节点只有一个孩子时，这个孩子是左还是右是有区别的，因此二叉树是**有序树**。

![[tikz-tree-02.svg]]

设层次从 1 开始，$h$ 为高度。则：

1. 第 $i$ 层最多有 $2^{i-1}$ 个节点。
2. 高度为 $h$ 的二叉树最多有 $2^h - 1$ 个节点。
3. 若 $n_0$ 为叶子节点数，$n_2$ 为度为 2 的节点数，则 $n_0 = n_2 + 1$。
4. $n$ 个节点的二叉链表有 $n + 1$ 个空指针域。（每个节点有 2 个指针，共 $2n$ 个域；有 $n - 1$ 条边，即 $n - 1$ 个非空指针，因此 $2n - (n-1) = n + 1$ 个为空。）

两种特殊形态：

- **满二叉树**——每个非叶子节点都有两个孩子，所有叶子在同一层；恰好有 $2^h - 1$ 个节点。
- **完全二叉树**——除最后一层外每层都是满的，且最后一层从左到右填充。这种形态适合紧凑地存储在数组中（堆是经典应用）。

## 3. 二叉搜索树（BST）

对于每个节点，其**左**子树中的所有键值**小于**该节点的键值，**右**子树中的所有键值**大于**该节点的键值：左 < 根 < 右。

![[tikz-tree-03.svg]]

BST 将搜索从线性结构的 $O(n)$ 降低到理想情况下的 $O(\log n)$（树高约为 $\log_2 n$）。可以将其视为一个自排序的目录：目标值较小时向左，较大时向右，每步排除约一半的剩余搜索空间——与二分查找相同的排除原理。

### 插入（递归）

```c
BstNode *InsertNode(BstNode *root, int data) {
    if (root == NULL) {
        root = GetNewNode(data);
    } else if (data <= root->Data) {
        root->Left = InsertNode(root->Left, data);
    } else {
        root->Right = InsertNode(root->Right, data);
    }
    return root;
}
```

### 搜索（递归）

```c
bool SearchNode(BstNode *root, int data) {
    if (root == NULL)
        return false;
    else if (root->Data == data)
        return true;
    else if (root->Data >= data)
        return SearchNode(root->Left, data);
    else
        return SearchNode(root->Right, data);
}
```

![[tikz-tree-04.svg]]

### 最小值和最大值

对于任意节点 `x`，左子树保存更小的键值，右子树保存更大的键值。因此**最小值**通过一直向左走得到，**最大值**通过一直向右走得到。

```c
typedef struct Node {
    int key;
    struct Node *left, *right;
} Node;

Node *findMin(Node *root) {
    if (root == NULL) return NULL;   // empty tree
    Node *p = root;
    while (p->left != NULL) {
        p = p->left;
    }
    return p;
}
```

![[tikz-tree-05.svg]]

```c
Node *findMax(Node *root) {
    if (root == NULL) return NULL;   // empty tree
    Node *p = root;
    while (p->right != NULL) {
        p = p->right;
    }
    return p;
}
```

### 树的高度

**空树**的高度为 $0$；否则高度 $= \max(\text{左子树高度}, \text{右子树高度}) + 1$。这是经典的分治模式：解决两个子树，然后合并。

$$
H(T)=
\begin{cases}
0, & T = \varnothing \\
\max(H(T.left), H(T.right)) + 1, & T \neq \varnothing
\end{cases}
$$

```c
int treeHeight(TreeNode *root) {
    if (root == NULL) return 0;   // empty tree has height 0
    int lh = treeHeight(root->left);
    int rh = treeHeight(root->right);
    return (lh > rh ? lh : rh) + 1;
}
```

## 4. 遍历

遍历按某种顺序访问每个节点恰好一次。有两类遍历：

- **深度优先（DFS）**——先序（根、左、右）、中序（左、根、右）、后序（左、右、根）。
- **广度优先（BFS）**——层序，从上到下、从左到右，由队列驱动。队列的 **FIFO** 机制保证先发现的节点先被处理，这正是"按层、按顺序"的要求。

以下示例树：

![[tikz-tree-06.svg]]

该树的遍历结果：

- 先序（根、左、右）：`A B D E C F`
- 中序（左、根、右）：`D B E A F C`
- 后序（左、右、根）：`D E B F C A`
- 层序（按层）：`A B C D E F`

单个递归函数根据访问位置不同即可实现所有三种 DFS 顺序：

```c
void dfs(TreeNode *root) {
    if (root == NULL) return;
    // place the visit here -> preorder
    dfs(root->left);
    // place the visit here -> inorder
    dfs(root->right);
    // place the visit here -> postorder
}
```

层序（BFS）使用队列：根节点入队；当队列非空时，出队并访问队首节点，然后将其子节点从左到右入队；直到队列为空。

```c
void levelOrder(TreeNode *root) {
    if (root == NULL) return;
    Queue q;
    initQueue(&q);
    enqueue(&q, root);
    while (!isEmpty(&q)) {
        TreeNode *cur = dequeue(&q);
        printf("%d ", cur->val);
        if (cur->left)  enqueue(&q, cur->left);
        if (cur->right) enqueue(&q, cur->right);
    }
}
```

## 5. 验证 BST

**中序遍历必须严格递增。** BST 的中序遍历产生严格递增的序列（假设无重复键）。维护一个 `prev` 指针，在访问每个节点时检查前一个值严格更小；否则立即失败。

```c
static bool inorderCheck(TreeNode *root, TreeNode **prev) {
    if (root == NULL) return true;
    if (!inorderCheck(root->left, prev)) return false;
    // the current value must exceed the previous inorder value
    if (*prev != NULL && root->val <= (*prev)->val) {
        return false;
    }
    *prev = root;
    return inorderCheck(root->right, prev);
}

bool isValidBST_Inorder(TreeNode *root) {
    TreeNode *prev = NULL;
    return inorderCheck(root, &prev);
}
```

**范围约束。** 每个节点必须位于有效的开区间 $(low, high)$ 内：根节点在 $(-\infty, +\infty)$ 内；向左下降收紧上界为当前值；向右下降收紧下界。任何超出区间的节点均不合法。

```c
static bool rangeCheck(TreeNode *root, long long low, long long high) {
    if (root == NULL) return true;
    if ((long long)root->val <= low || (long long)root->val >= high) {
        return false;
    }
    return rangeCheck(root->left, low, root->val) &&
           rangeCheck(root->right, root->val, high);
}

bool isValidBST_Range(TreeNode *root) {
    return rangeCheck(root, LLONG_MIN, LLONG_MAX);
}
```

## 6. 从 BST 中删除节点

删除键 `key` 既要移除目标节点，又要保持 BST 性质（左 < 根 < 右）。

![[d2-tree-01.svg]]

有三种情况：

- **情况 1——叶子节点**（无子节点）：直接移除；将父节点的相应指针设为 `NULL`。
- **情况 2——一个子节点**：绕过该节点，将其父节点指向它唯一的子节点。
- **情况 3——两个子节点**：不直接删除。找到**中序后继**（右子树的最小值）或**中序前驱**（左子树的最大值）；将其值复制到当前节点的值上；然后从相应的子树中删除那个后继/前驱节点。

使用后继 `s`（右子树的最小值）是可行的，因为 `s` 大于左子树中的所有键值（它位于右子树中）且是右子树中最小的键值，因此它不会违反右子树的顺序。

> [!warning] 释放被删节点
> 在所有情况下，重链后物理上被移除的节点必须 `free`，否则其内存会泄漏。

## 7. 哈夫曼树

哈夫曼树是一种**带权二叉树**，每个叶子是一个符号，其权重为频率（或概率）。从根到叶子的路径是该符号的编码，通常约定**0 表示左、1 表示右**（反之亦可，只要保持一致）。平均编码长度等于叶子权重 × 叶子深度的加权和，哈夫曼的构造方法使其最小化。

![[tikz-tree-07.svg]]

---

> [!important] 一句话总结
> 树是每个节点一个父节点的层次结构；BST 使其保持有序，以在平衡时实现 $O(\log n)$ 的搜索、插入和删除，遍历方式为深度优先（先序/中序/后序）或广度优先（通过队列的层序）。
