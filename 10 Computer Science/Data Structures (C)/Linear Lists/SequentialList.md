---
aliases: [Sequential List, 顺序表, Array List]
tags: [c_language, data_structure]
up: "[[C_DataStruct MOC]]"
related: "[[LinkedList|Linked List]], [[DoubleLinkedList|Doubly Linked List]], [[Stack|Stack & Queue]]"
down: ""
---
# 顺序表

> [!summary] 核心思想
> 顺序表将元素存储在**连续**的内存块中，通过下标访问，实现 $O(1)$ 的随机访问。代价是插入和删除必须移动元素以维持连续性，平均和最坏情况下的开销为 $O(n)$。

前置知识：C 数组、结构体和指针。另一种以随机访问换取廉价插入的链接方案是[[LinkedList|链表]]。

---

**顺序表**是一种将数据元素存储在**地址连续**的内存单元中的线性结构，一个接一个排列。逻辑顺序与物理顺序一致：逻辑位置 $i$ 上的元素在物理上与 $i-1$ 和 $i+1$ 位置的元素相邻。由于存储是连续的，任何元素的地址都可以直接从基地址得出，这正是常数时间随机访问的实现基础。

## 1. C 语言实现

在 C 中，我们需要的不仅仅是裸数组——还需要一个字段记录当前存储的元素个数。用 `struct` 将**数组**和**长度**捆绑在一起。

### 静态分配

数组大小固定，存在于 `SqList` 变量所在的位置（通常是栈上）：

```c
#define MAX_SIZE 100        // maximum capacity

typedef int ElemType;       // element type (change once to switch, e.g. to float)

typedef struct {
    ElemType data[MAX_SIZE]; // fixed-size array holding the elements
    int length;              // number of valid elements currently stored
} SqList;
```

### 动态分配

动态顺序表将元素保存在**堆**上，因此可以在运行时扩容：

```c
typedef int ElemType;

typedef struct {
    ElemType *data;  // pointer to a heap-allocated array
    int MaxSize;     // current capacity
    int length;      // number of valid elements
} SeqList;
```

## 2. 初始化

初始化构建一个**空**表。我们传入指针以便函数修改调用者的结构体：

```c
// Pass a pointer so we can modify the caller's struct.
void InitList(SqList *L) {
    L->length = 0;
    // The contents of data[] need not be cleared: with length == 0 the list is
    // logically empty, and stale values are overwritten on insertion.
}

int main(void) {
    SqList myList;
    InitList(&myList);   // must pass the address
    return 0;
}
```

动态版本额外需要申请堆内存，并必须检查申请是否成功：

```c
#include <stdlib.h>      // for malloc

#define INIT_SIZE 10     // default initial capacity

void InitSeqList(SeqList *L) {
    L->data = (ElemType *)malloc(sizeof(ElemType) * INIT_SIZE);
    if (L->data == NULL) {
        return;          // allocation failed: abort initialization
    }
    L->length  = 0;          // no elements yet
    L->MaxSize = INIT_SIZE;  // record the capacity
}
```

> [!warning] 内存管理
> 每次成功的 `malloc` 最终都必须由对应的 `free` 匹配。对于动态顺序表，丢弃时 `data` 缓冲区必须被释放，否则堆块会泄漏。使用 `malloc` 前务必检查其结果是否为 `NULL`。

## 3. 插入

将元素 `e` 插入到下标 `i` 处：

1. **检查是否已满**——若 `length == MaxSize`，表已满；拒绝以避免溢出。
2. **检查边界**——合法范围为 `0 ... length`（允许在末尾插入）。
3. **移动**——从**最后一个**元素开始，每个元素向右移动一个位置，直到位置 `i` 空出。移位必须从后往前，否则前面的元素会覆盖后面的。
4. **写入**——将 `e` 放入 `data[i]`。
5. **更新**——`length` 自增。

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int length;
} SqList;

// Insert element e at position index. Returns true on success, false on failure.
bool ListInsert(SqList *L, int index, int e) {
    if (L->length >= MAX_SIZE) {            // 1. full
        printf("Insertion failed: list is full\n");
        return false;
    }
    if (index < 0 || index > L->length) {   // 2. illegal position
        printf("Insertion failed: illegal position\n");
        return false;
    }
    for (int j = L->length - 1; j >= index; j--) {   // 3. shift back-to-front
        L->data[j + 1] = L->data[j];
    }
    L->data[index] = e;                     // 4. write
    L->length++;                            // 5. update length
    return true;
}
```

复杂度：

- 最好情况（尾部插入）：无需移动，$O(1)$。
- 最坏情况（头部插入）：移动所有 $n$ 个元素，$O(n)$。
- 平均情况：移动 $\tfrac{n}{2}$ 次，即 $O(n)$。

## 4. 删除

删除操作必须使剩余元素保持连续，因此被删位置之后的每个元素都向左**移动一个位置**。最后一个物理位置保留一个过期的副本，但由于它超出 `length` 范围，无害且无需清除。

删除下标 `i` 处的元素：

1. **检查边界**——要求 $0 \le i < \text{length}$。
2. **保存**（可选）——复制元素以便返回。
3. **移动**——将 $i+1$ 到 $n-1$ 的元素左移一位。
4. **更新**——`length` 自减。

```c
#define MAXSIZE 100

typedef struct {
    int data[MAXSIZE];
    int length;
} SeqList;

// Delete the element at position i; store its value through e.
// Returns 1 on success, 0 on failure.
int ListDelete(SeqList *L, int i, int *e) {
    if (i < 0 || i >= L->length) {   // 1. out of range
        return 0;
    }
    *e = L->data[i];                 // 2. save the removed value
    for (int j = i; j < L->length - 1; j++) {   // 3. shift left
        L->data[j] = L->data[j + 1];
    }
    L->length--;                     // 4. update length
    return 1;
}
```

复杂度：

- 最好情况（删除最后一个元素）：无需移动，$O(1)$。
- 最坏情况（删除第一个元素）：移动所有剩余元素，$O(n)$。
- 平均情况：移动 $\tfrac{n-1}{2}$ 次，即 $O(n)$。

## 5. 按值查找

返回第一个等于 `e` 的元素位置：

```c
// Returns the 1-based logical position, or 0 if not found.
int LocateElem(SeqList L, int e) {
    for (int i = 0; i < L.length; i++) {
        if (L.data[i] == e) {
            return i + 1;   // found: report which element (index + 1)
        }
    }
    return 0;               // not found
}
```

可能需要扫描整个表，因此按值查找为 $O(n)$。

## 6. 传值与传地址的选择

选择依据**数据流动方向**：

- **插入——数据*流入*顺序表**（调用者 → 函数 → 顺序表）。函数只需读取值并复制到数组中，因此使用值参数 `int e` 即可。
- **删除——数据*流出*顺序表**（顺序表 → 函数 → 调用者）。我们既需要成功/失败状态，又需要被删的值。由于 `return` 已经携带了状态（`1`/`0`），被删的值通过指针参数传回——指针为 C 提供了有效的"多返回值"机制。

> [!warning] 为什么删除不能用普通的 `int e`
> 如果函数签名为 `int ListDelete(..., int e)`，那么 `e = L->data[i]` 赋值给的是**局部副本**，函数返回时即被销毁；调用者的变量永远不会收到被删的值。需要使用指针参数（`int *e`）才能写回调用者的存储空间。

---

> [!important] 一句话总结
> 顺序表是数组加长度：按索引访问为 $O(1)$，插入或删除因元素移动为 $O(n)$。
