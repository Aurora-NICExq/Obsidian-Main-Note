---
aliases: [Linked List, 链表, 单链表, Singly Linked List]
tags: [c_language, data_structure]
up: "[[C_DataStruct MOC]]"
related: "[[DoubleLinkedList|Doubly Linked List]], [[SequentialList|Sequential List]], [[Stack|Stack & Queue]]"
down: ""
---
# 链表

> [!summary] 核心思想
> 链表将元素存储在散布于内存各处的**离散**节点中；每个节点携带一个指向下一节点的指针，因此逻辑顺序通过链接而非物理相邻来维护。这带来了在已知位置上 $O(1)$ 的插入和删除（无需移动元素），但放弃了[[SequentialList|顺序表]]的随机访问——访问第 $i$ 个节点需 $O(n)$。

前置知识：C 指针、`struct` 和 `malloc`/`free`。与连续存储的[[SequentialList|顺序表]]对比。

---

链表依赖于两个概念：

- **离散存储**——元素在内存中不必紧邻，可以散布在任何位置。
- **链接**——为了到达下一个元素，每个节点存储一个指向下一节点**地址**的指针。

链表的基本单元是**节点**，在 C 中由两部分组成：**数据域**保存载荷（如 `int`、`student_info` 结构体）和**指针域**保存下一节点的**地址**。

## 1. C 语言实现

```c
typedef struct Node {
    int data;              // data field
    struct Node *next;     // pointer field: address of the next node
} LNode, *LinkList;
```

- `next` 指针的类型必须是 `struct Node *`，因为它指向的是同一结构体类型的另一个对象。
- 关于将 `*LinkList` 读取为结构体指针 typedef，参见 [[Keywords#^842fec|typedef for a struct pointer]]。

## 2. 初始化

单链表有两种风格：**带头（哨兵）节点**和**不带头节点**。

带头节点的链表区分两种事物：

- **头指针**（`L`）——始终指向链表前端的变量。
- **头节点**——刻意插入在最前面的**哨兵**。它**不存储**有效数据（或存储链表长度）；其 `next` 指向第一个真正的数据节点。其用途是统一性：有了哨兵，第一个节点的处理方式与其他任何节点完全相同，因此不需要为"在第一个节点之前插入"编写特殊的 `if`。

![[tikz-linkedlist-01.svg]]

带头节点的初始化分配哨兵节点并将其 `next` 指向 `NULL`：

```c
typedef struct Node {
    int data;
    struct Node *next;
} LNode, *LinkList;

// Build and return an empty list (a lone head node).
LinkList InitList(void) {
    LinkList L = (LinkList)malloc(sizeof(LNode));   // 1. allocate the head node
    if (L == NULL) {
        return NULL;     // 2. allocation failed
    }
    L->next = NULL;      // 3. empty list: nothing follows the head node
    return L;
}

int main(void) {
    LinkList L;          // wild pointer until assigned
    L = InitList();      // now L points to a valid head node
    return 0;
}
```

不带头节点时，`L` 直接指向第一个真正的元素，因此空链表就是一个空指针：

```c
void InitList(LinkList *L) {
    *L = NULL;   // a completely empty list — not even a head node
}
```

> [!warning] 省略头节点的代价
> 由于 `L` 可能为 `NULL`，每个插入**第一个**元素的操作都必须特殊处理（`if (L == NULL) ...`）。虚拟头节点正是为了避免这种情况。

成功初始化带头节点的链表后，状态为：

| 变量/内存 | 状态 |
|---|---|
| `L`（头指针）| 持有地址（如 `0x100`），指向头节点 |
| `L->data` | 垃圾值（头节点的数据域未使用）|
| `L->next` | `NULL` |

## 3. 头插法

每个新元素紧接在头节点之后插入，因此输出顺序与输入顺序**相反**：

```c
// Build a singly linked list by head insertion; return the head pointer.
LinkList List_HeadInsert(LinkList L) {
    LNode *s;   // points to each newly allocated node
    int x;      // holds each input value

    L = (LinkList)malloc(sizeof(LNode));
    L->next = NULL;   // start from an empty list — essential!

    printf("Enter numbers (9999 to stop):\n");
    scanf("%d", &x);
    while (x != 9999) {
        s = (LNode *)malloc(sizeof(LNode));   // allocate a new node
        s->data = x;
        s->next = L->next;   // new node points to the current first node
        L->next = s;         // head node points to the new node
        scanf("%d", &x);
    }
    return L;
}
```

头插法的用途：

1. **逆向输出**——如以逆序存储文件数据。
2. **实现[[Stack|栈]]**——LIFO 与头插法完全匹配。
3. **链表反转**——将节点从旧链表摘除，再头插到新链表中。

## 4. 遍历

从第一个真正节点开始，直到 `next` 指针到达 `NULL`：

```c
void PrintList(LinkList L) {
    LNode *p = L->next;   // start at the first real node (skip the head node)
    while (p != NULL) {
        printf("%d -> ", p->data);
        p = p->next;      // advance to the next node
    }
    printf("NULL\n");
}
```

两种常见遍历错误：

- **从头节点开始打印**（`LNode *p = L;`）：第一次迭代打印头节点未初始化的数据域——垃圾值。
- **移动 `L` 本身**（`L = L->next;`）：推进头指针会丢失头节点的地址。如果该节点是堆分配的且没有其他指针持有它，该节点就泄漏了。

计算长度是遍历的典型应用：

```c
int ListLength(LinkList L) {
    LNode *p = L->next;   // start at the first real node
    int len = 0;
    while (p != NULL) {
        len++;
        p = p->next;
    }
    return len;
}
```

## 5. 尾插法

每个新元素追加到尾部。朴素地追加意味着每次都从头走到尾，构建整个链表复杂度为 $O(n^2)$。应始终维护一个**尾指针** `r`（rear），指向当前最后一个节点。追加节点 `s`：`r->next = s;` 然后 `r = s;`。

![[tikz-linkedlist-02.svg]]

```c
LinkList List_TailInsert(LinkList L) {
    int x;
    L = (LinkList)malloc(sizeof(LNode));
    LNode *s;
    LNode *r = L;     // tail pointer starts at the head node!

    printf("Enter numbers (9999 to stop):\n");
    scanf("%d", &x);
    while (x != 9999) {
        s = (LNode *)malloc(sizeof(LNode));
        s->data = x;
        r->next = s;  // 1. attach the new node after the old tail
        r = s;        // 2. move the tail pointer to the new node
        scanf("%d", &x);
    }
    r->next = NULL;   // 3. terminate the list — otherwise the tail dangles
    return L;
}
```

> [!warning] 尾部终止
> 循环结束后，`r` 指向最后一个节点。其 `next` 必须设为 `NULL`；否则它会保留 `malloc` 留下的任意地址，成为悬空指针。

头插与尾插一览：

| 性质 | 头插法 | 尾插法 |
|---|---|---|
| 顺序 | 倒序（1,2,3 → 3,2,1）| 正序（1,2,3 → 1,2,3）|
| 所需指针 | 仅头指针 `L` | 头指针 `L` + 尾指针 `r` |
| 时间复杂度 | $O(n)$ | $O(n)$ |
| 核心操作 | 插到前端 | 追加到后端 |
| 典型用途 | 链表反转、栈 | 正常构建、队列 |

## 6. 在给定位置插入

规则是**先链接后断开**：先将**新节点的 `next`** 指向**后继节点**，然后再将**前驱的 `next`** 重定向到新节点。颠倒顺序会丢失后继节点的地址，从而破坏链表。

![[tikz-linkedlist-03.svg]]

```c
// Insert value data at position index (0-based).
// Returns 1 on success, 0 on failure (illegal position).
int insert_at(Node **head_ref, int index, int data) {
    Node *new_node = (Node *)malloc(sizeof(Node));
    if (new_node == NULL) return 0;   // allocation failed
    new_node->data = data;

    if (index == 0) {                 // special case: insert at the head
        new_node->next = *head_ref;
        *head_ref = new_node;
        return 1;
    }

    // find the predecessor: the (index-1)-th node
    Node *p = *head_ref;
    int k = 0;
    while (p != NULL && k < index - 1) {
        p = p->next;
        k++;
    }
    if (p == NULL) {                  // index out of range
        free(new_node);               // not inserted: release the node
        return 0;
    }

    // link before unlink
    new_node->next = p->next;         // Step 1
    p->next = new_node;               // Step 2
    return 1;
}
```

> [!warning] 失败路径上的释放
> 如果位置在分配后被发现非法，必须 `free` 未使用的 `new_node` 再返回，否则会泄漏。

## 7. 删除

要删除单链表中的一个节点，需要找到它的**前驱**，因为只有前驱的 `next` 可以被绕过目标节点。对于 `A -> B -> C -> D`，删除 `B`：

1. **定位** `B` 的前驱 `A`。
2. **重链** `A->next` 指向 `B->next`（即指向 `C`）。
3. **释放** `B` 以归还其内存。

```c
// Returns the (possibly new) head pointer.
Node *deleteNode(Node *head, int val) {
    if (head == NULL) return NULL;

    // case 1: the target is the head node
    if (head->data == val) {
        Node *temp = head;        // hold the node so it is not lost
        head = head->next;        // advance the head pointer
        free(temp);               // release the old head
        printf("Deleted head node: %d\n", val);
        return head;
    }

    // case 2: the target is in the middle or at the tail
    Node *current = head;
    while (current->next != NULL && current->next->data != val) {
        current = current->next;
    }
    if (current->next == NULL) {
        printf("Value %d not found.\n", val);
    } else {
        Node *target = current->next;   // the node to delete
        current->next = target->next;   // predecessor skips the target
        free(target);                   // release its memory
        printf("Deleted node: %d\n", val);
    }
    return head;
}
```

> [!warning] 始终释放被删节点
> 第 3 步（`free`）是必需的。绕过节点而不释放它会导致该节点堆内存泄漏。

## 8. 释放整个链表

逐个节点释放，在释放当前节点前备份 next 指针：

1. **备份**下一节点的地址到临时指针。
2. **释放**当前节点。
3. **推进**当前指针到备份的节点。

```c
void freeList(Node *head) {
    Node *current = head;
    Node *nextNode;
    while (current != NULL) {
        nextNode = current->next;   // 1. back up: current->next is unreachable after free
        free(current);              // 2. release the current node
        current = nextNode;         // 3. advance
    }
}
```

> [!warning] 释放后使用和悬空头指针
> 在 `free(current)` **之前**读取 `current->next`，因为访问已释放的内存是未定义行为。调用 `freeList` 后，调用者还应将自己的 `head` 设为 `NULL`，否则 `head` 成为悬空指针。

## 9. 快慢指针

一个指针（`slow`）每次前进一个节点，另一个（`fast`）每次前进两个节点。其速度差可以在单次遍历中解决多个问题：

1. **中间节点**——当 `fast` 到达末尾时，`slow` 位于中点。一次遍历，而"测量长度再走一半"需要 1.5 次遍历。
2. **环检测**——Floyd 判环算法：如果存在环，`fast` 必然追上与 `slow` 相遇；如果不存在，`fast` 先到达 `NULL`。
3. **倒数第 $k$ 个节点**——"前导/后随指针"变体：让 `fast` 先走 $k$ 步，然后两个指针同步前进；当 `fast` 到达末尾时，`slow` 即为倒数第 $k$ 个节点。

```c
// For an even-length list, returns the second of the two middle nodes (a common convention).
Node *findMiddle(Node *head) {
    if (head == NULL) return NULL;
    Node *slow = head;
    Node *fast = head;
    // fast must be non-NULL and have a next, so it can take two steps
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;          // slow advances 1
        fast = fast->next->next;    // fast advances 2
    }
    return slow;                    // slow now sits at the midpoint
}
```

寻找中点：

![[tikz-linkedlist-04.svg]]

环检测：

![[tikz-linkedlist-05.svg]]

---

> [!important] 一句话总结
> 链表以随机访问为代价换取 $O(1)$ 的结构性编辑：维护头指针（以及常有的尾指针），始终"先链接后断开"，并 `free` 你移除的每个节点。
