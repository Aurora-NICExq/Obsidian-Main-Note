---
aliases: [Stack, 栈, Queue, 队列, Circular Queue, 循环队列]
tags: [c_language, data_structure]
up: "[[C_DataStruct MOC]]"
related: "[[SequentialList|Sequential List]], [[LinkedList|Linked List]], [[Tree|Tree]]"
down: ""
---
# 栈与队列

> [!summary] 核心思想
> **栈**是一种限制为 **LIFO**（后进先出）访问的线性结构：所有插入和删除都在同一端（栈顶）进行。**队列**限制为 **FIFO**（先进先出）：元素从队尾进入，从队首离开。两者都是刻意限制访问方式的线性结构，都可以基于数组或链表节点实现。

前置知识：[[SequentialList|顺序表]]和[[LinkedList|链表]]——栈或队列只是其中一种加上了访问限制。

---

## 第一部分 — 栈

**栈**是一种只允许在一端（称为**栈顶**）进行插入和删除的线性结构。最后压入的元素最先弹出——**LIFO**，后进先出。从概念上讲，这是一个访问被限制在单端的[[SequentialList|顺序表]]。

![[tikz-stack-01.svg]]

### 1. 基于数组的栈

结构为数组加栈顶索引：

```c
#include <stdio.h>
#define MAXSIZE 100
typedef int ElemType;

typedef struct {
    ElemType data[MAXSIZE];
    int top;   // index of the current top element
} Stack;
```

初始化将 `top` 设为 `-1`：

```c
void InitStack(Stack *s) {
    s->top = -1;
}
```

`top` 保存**当前栈顶元素的索引**。合法索引范围为 `0 ... MAXSIZE-1`。空栈没有栈顶元素，因此 `top` 必须指向所有合法索引之外；使用 `-1` 作为哨兵值。因此判空（下溢）检查为：

```c
int ifEmpty(Stack *s) {   // returns 1 if empty, else 0
    if (s->top == -1) {
        printf("Empty");
        return 1;
    }
    return 0;
}
```

入栈和出栈都在栈顶操作：

- **入栈（Push）** — 若已满则拒绝（`top >= MAXSIZE-1`）；否则先 `top` 自增，再将值写入 `data[top]`。
- **出栈（Pop）** — 若为空则拒绝（`top == -1`）；否则读取 `data[top]`，再将 `top` 自减。

```c
int push(Stack *s, ElemType e) {
    if (s->top >= MAXSIZE - 1) {
        printf("Full");
        return 0;
    }
    s->top++;
    s->data[s->top] = e;
    return 1;
}

int pop(Stack *s, ElemType *e) {   // returns popped value through e
    if (s->top == -1) {
        printf("Empty");
        return 0;
    }
    *e = s->data[s->top];
    s->top--;
    return 1;
}
```

### 2. 链式栈

链式栈将栈顶保持在单链表的**头部**，因此入栈和出栈分别是头插和头删：

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct {
    Node *top;   // points to the top node
} LinkedStack;

void initLinkedStack(LinkedStack *s) {
    s->top = NULL;
}

bool isEmptyLinked(LinkedStack *s) {
    return s->top == NULL;
}

// push: head insertion
bool pushLinked(LinkedStack *s, int x) {
    Node *node = (Node *)malloc(sizeof(Node));
    if (!node) return false;       // allocation failed
    node->data = x;
    node->next = s->top;
    s->top = node;
    return true;
}

// pop: head deletion
bool popLinked(LinkedStack *s, int *x) {
    if (isEmptyLinked(s)) return false;
    Node *tmp = s->top;
    *x = tmp->data;
    s->top = tmp->next;
    free(tmp);                     // release the popped node
    return true;
}

// peek: read the top without removing it
bool peekLinked(LinkedStack *s, int *x) {
    if (isEmptyLinked(s)) return false;
    *x = s->top->data;
    return true;
}
```

> [!warning] 内存管理
> 每次 `pushLinked` 分配一个节点，每次 `popLinked` 必须 `free` 它。丢弃链式栈时不出栈（或未释放节点）会导致内存泄漏。

对于数组和链表两种实现，入栈、出栈和读取栈顶均为 $O(1)$。

## 第二部分 — 队列

**队列**是一种允许在一端插入、另一端删除的线性结构。插入端称为**队尾**；删除端称为**队首**。元素从队尾进入，从队首离开——**FIFO**，先进先出。

### 3. 判空

使用数组索引 `front` 和 `rear`，当 `front == rear` 时队列为空。

![[tikz-stack-02.svg]]

```c
int QueueEmpty(Queue *Q) {     // returns 1 if empty, else 0
    if (Q->front == Q->rear) {
        printf("Empty");
        return 1;
    }
    return 0;
}
```

### 4. 出队

`front` 自增即可逻辑上移除队首元素：队首索引简单地推进到下一个元素。

```c
ElemType dequeue(Queue *Q) {
    ElemType e = Q->data[Q->front];
    Q->front++;
    return e;
}
```

### 5. 循环队列

普通的线性队列浪费空间，因为 `front` 和 `rear` 只能向前移动。**循环队列**使用模运算包装索引，使释放的队首位置可被重用：

```c
#define MAXSIZE 100
typedef int ElemType;

typedef struct {
    ElemType data[MAXSIZE];
    int front;
    int rear;
} Queue;

void InitQueue(Queue *q) {
    q->front = q->rear = 0;
}

int IsEmpty(Queue *q) {
    return q->front == q->rear;
}

int EnQueue(Queue *q, ElemType x) {
    if ((q->rear + 1) % MAXSIZE == q->front) return 0;  // full
    q->data[q->rear] = x;
    q->rear = (q->rear + 1) % MAXSIZE;
    return 1;
}

int DeQueue(Queue *q, ElemType *x) {
    if (IsEmpty(q)) return 0;   // empty
    *x = q->data[q->front];
    q->front = (q->front + 1) % MAXSIZE;
    return 1;
}
```

这种实现刻意保留一个空位，以便区分**满**和**空**：空为 `front == rear`，满为 `(rear + 1) % MAXSIZE == front`。因此循环队列最多容纳 `MAXSIZE - 1` 个元素。入队和出队均为 $O(1)$。

---

> [!important] 一句话总结
> 栈是 LIFO（在同一端入栈/出栈），队列是 FIFO（队尾入队，队首出队）；两者每次操作均为 $O(1)$，既可基于数组也可基于链表实现。
