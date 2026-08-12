---
aliases: [Doubly Linked List, 双向链表, 双链表]
tags: [c_language, data_structure]
up: "[[C_DataStruct MOC]]"
related: "[[LinkedList|Linked List]], [[SequentialList|Sequential List]]"
down: ""
---
# 双向链表

> [!summary] 核心思想
> 双向链表为每个节点增加一个向后指针（`prev`）以及向前的指针（`next`）。这第二个链接消除了单链表的最大弱点——删除节点时需要前驱——从而使已知节点的删除达到 $O(1)$ 并支持自然的反向遍历，代价是每个节点多一个指针。

前置知识：单向[[LinkedList|链表]]（节点、`next` 指针、头插法）。

---

**双向链表**是一种线性链接结构，其中每个节点包含三个字段：**数据域**、指向前驱的指针（`prev`）和指向后继的指针（`next`）。两个指针使得链表可以双向遍历。

![[tikz-doublelinkedlist-01.svg]]

## 1. C 语言实现

```c
typedef int ElemType;

typedef struct DNode {
    ElemType data;                  // data field
    struct DNode *prev, *next;      // predecessor and successor pointers
} DNode;
```

指针必须声明为 `struct DNode *`（完整标签名），因为在自身定义内部，typedef 别名 `DNode` 尚未进入作用域。

## 2. 为什么需要第二个指针？

在单链表中，如果只知道指向节点 `p` 的指针，要删除该节点必须先找到它的**前驱**，因为需要重定向前驱的 `next`——这是从头部开始的 $O(n)$ 搜索。`prev` 指针使得前驱立即可得，因此双向链表获得两个优势：

- **已知节点 `p` 的删除为 $O(1)$**——无需搜索前驱。
- **从尾部到头部的反向遍历变得自然。**

## 3. 插入

指针更新必须**双向**连接新节点并修复相邻节点的指针。要在节点 `L` 之后插入节点 `p`（头插法）：

1. 设置新节点的 `data`。
2. 将新节点链接到其相邻节点：`p->prev = L`，`p->next = L->next`。
3. 如果存在后继节点，修复其向后指针：`L->next->prev = p`。
4. 最后重定向前驱：`L->next = p`。

```c
// Assumes node p has already been allocated.
void insertAfter(DNode *L, DNode *p, ElemType e) {
    p->data = e;
    p->prev = L;
    p->next = L->next;
    if (L->next != NULL) {     // guard: there may be no successor
        L->next->prev = p;
    }
    L->next = p;
}
```

> [!warning] 指针更新顺序
> 在覆盖 `L->next` **之前**修复后继节点的 `prev` 链接。如果先重赋值 `L->next`，原后继节点的地址就丢失了，其 `prev` 再也无法到达，链表被破坏。尾插法遵循对称逻辑，此处从略。

## 4. 复杂度

- **已知**节点上的插入或删除为 $O(1)$。
- 按值或位置查找节点仍需 $O(n)$，因为链接是一个接一个遍历的。
- 与[[LinkedList|单链表]]相比，每个节点多用一个指针的内存。

---

> [!important] 一句话总结
> 双向链表增加了一个 `prev` 指针，使得已知节点的删除可以在 $O(1)$ 内完成，并且链表可以双向遍历。
