---
aliases: [智能指针, Smart Pointers, Box, Rc, RefCell, Deref, Drop]
tags: [rust, smart-pointers]
up: "[[Rust MOC]]"
related: "[[Ownership, Borrowing, and Slices|所有权]], [[Generics, Traits, and Lifetimes|Trait]], [[Functional Language Features Closures and Iterators|闭包与迭代器]], [[Fearless Concurrency|并发]]"
down: "[[Fearless Concurrency|Fearless Concurrency]]"
---
# Smart Pointers

> [!summary] 核心结论
> 智能指针是行为像指针、且带**额外元数据与能力**的结构体（常实现 `Deref` / `Drop`）。常用：`Box<T>` 堆分配、递归类型；`Rc<T>` 单线程多所有权；`RefCell<T>` 内部可变性（借用规则改到运行时检查）。组合如 `Rc<RefCell<T>>` 可多处共享且可改；循环引用会导致内存泄漏，可用 `Weak<T>` 打破。

对应《The Book》**第 15 章**。前置：[[Ownership, Borrowing, and Slices|所有权与借用]]、[[Generics, Traits, and Lifetimes|Trait]]。

---

## 1. What Are Smart Pointers?（什么是智能指针）

普通引用 `&T` 只借用。智能指针通常**拥有**数据，并实现：

- `Deref`：可用 `*` 解引用，像引用一样用  
- `Drop`：离开作用域时自定义清理  

标准库例子：`String`、`Vec<T>` 也可视为智能指针；本章聚焦 `Box`、`Rc`、`RefCell` 等。

---

## 2. `Box<T>` — Heap Allocation

`Box<T>` 把数据放在**堆**上，栈上只留指针。用途：

1. 类型大小在编译期未知，又需要确切大小的上下文  
2. 传递大型数据时不想拷贝（只传所有权）  
3. 只要实现某 Trait 的值，类型本身不重要（`Box<dyn Trait>`）

```rust
let b = Box::new(5);
println!("b = {b}");
// 离开作用域：先 drop 堆上数据，再回收 Box
```

### 2.1 Enabling Recursive Types（递归类型）

Rust 需知类型大小；直接 `enum List { Cons(i32, List), Nil }` 无穷大。用 `Box` 包一层：

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use List::{Cons, Nil};
let list = Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));
```

---

## 3. `Deref` and `Drop`

### 3.1 `Deref`

实现 `Deref` 后可用 `*`；函数参数里还有 **deref coercion**：`&String` → `&str`，`&Box<T>` → `&T` 等自动转换。

```rust
use std::ops::Deref;

struct MyBox<T>(T);

impl<T> Deref for MyBox<T> {
    type Target = T;
    fn deref(&self) -> &Self::Target {
        &self.0
    }
}
```

可变借用对应 `DerefMut`。

### 3.2 `Drop`

```rust
impl Drop for MyBox<T> {
    fn drop(&mut self) {
        println!("Dropping MyBox");
    }
}
```

不能手动调用 `Drop::drop`；要提前清理用 `std::mem::drop(value)`。

---

## 4. `Rc<T>` — Reference Counted（单线程共享所有权）

多个所有者读同一数据时（单线程），用 `Rc<T>`：克隆 `Rc` 只增加引用计数，不深拷贝内层。

```rust
use std::rc::Rc;

let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
let b = Cons(3, Rc::clone(&a));
let c = Cons(4, Rc::clone(&a));
// Rc::strong_count(&a) 可见计数
```

习惯写 `Rc::clone(&a)` 而不是 `a.clone()`，强调“只加计数”。`Rc` **非** `Send`/`Sync`，不能跨线程。

---

## 5. `RefCell<T>` and Interior Mutability（内部可变性）

借用规则通常在**编译期**检查。`RefCell<T>` 把检查挪到**运行时**：仍遵守“或多项不可变，或一项可变”，违反则 **panic**。

| 类型 | 所有权 | 可变性检查 |
| ---- | ------ | ---------- |
| `&T` / `&mut T` | 借用 | 编译期 |
| `Rc<T>` | 多所有权 | 编译期（不可变） |
| `RefCell<T>` | 单所有权 | 运行时 |
| `Rc<RefCell<T>>` | 多所有权 | 运行时可变 |

```rust
use std::cell::RefCell;

let x = RefCell::new(5);
*x.borrow_mut() += 1;
assert_eq!(*x.borrow(), 6);
```

典型场景：即便外层只有 `&self`，仍要改内部字段（mock 对象、缓存等）。

---

## 6. Reference Cycles and `Weak<T>`（循环引用）

`Rc` 相互指向可使强引用计数永不为 0 → **内存泄漏**。树形结构里父拥有子用 `Rc`，子指回父用 `Weak<T>`（不增加强计数）：

```rust
use std::rc::{Rc, Weak};
// parent: RefCell<Weak<Node>>
// children: RefCell<Vec<Rc<Node>>>
```

`upgrade()` 把 `Weak` 变成 `Option<Rc<_>>`：父还在则 `Some`，否则 `None`。

---

> [!important] 一句话总结
> `Box` 管堆与递归大小；`Rc` 管单线程共享所有权；`RefCell` 管运行时借用与内部可变；`Weak` 打破 `Rc` 环。先选清所有权模型，再组合这些指针。
