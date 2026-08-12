---
aliases: [面向对象特性, OOP, Trait Objects, 面向对象, Object-Oriented Features]
tags: [rust, oop, trait-objects]
up: "[[Rust MOC]]"
related: "[[Generics, Traits, and Lifetimes|Trait]], [[Smart Pointers|Box]], [[Packages, Crates, and Modules|可见性]], [[Fearless Concurrency|并发]]"
down: "[[Patterns and Matching|模式进阶]]"
---
# Object-Oriented Features of Rust

> [!summary] 核心结论
> Rust 可做 OOP 常见事，但不绑死继承：用结构体 + 方法做**封装**，用 **Trait Objects**（`dyn Trait`）做运行时多态。`Box<dyn Trait>` 等指向“实现了某 Trait 的任意类型”；对象安全有限制。状态模式等可用结构体/枚举或 Trait Object 实现——更惯用的往往是类型系统与枚举，而不是深继承树。

对应《The Book》**第 17 章**。前置：[[Generics, Traits, and Lifetimes|Trait]]、[[Smart Pointers|Box]]、[[Packages, Crates, and Modules|pub 封装]]。

---

## 1. What Is OOP?（Rust 里有哪些）

经典 OOP 特征对照：

| 特征 | Rust |
| ---- | ---- |
| 对象 = 数据 + 行为 | `struct`/`enum` + `impl` 方法 |
| 封装 | 模块与 `pub`；字段默认可私有 |
| 继承 | **无**类型继承；用 Trait 共享行为、默认方法复用代码 |
| 多态 | 静态：泛型 + Trait bound；动态：Trait Object |

---

## 2. Encapsulation（封装）

```rust
pub struct AveragedCollection {
    list: Vec<i32>,      // 私有
    average: f64,        // 私有缓存
}

impl AveragedCollection {
    pub fn add(&mut self, value: i32) { /* 更新 list 与 average */ }
    pub fn average(&self) -> f64 { self.average }
}
```

外界不能直接改 `list` 而留下过期的 `average`——这就是封装。

---

## 3. Trait Objects（Trait 对象）

需要**运行时**决定具体类型时，用 Trait Object：

```rust
pub trait Draw {
    fn draw(&self);
}

pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}

impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

- `dyn Draw`：实现了 `Draw` 的某类型的**动态**对象  
- 常放在 `Box`、`Rc`、`&` 后（大小不确定，必须通过指针）  
- 调用走**动态分发**（虚表），与泛型单态化的静态分发相对  

```rust
Screen {
    components: vec![
        Box::new(Button { /* ... */ }),
        Box::new(SelectBox { /* ... */ }),
    ],
}
.run();
```

同一 `Vec` 可混装不同具体类型，只要都实现 `Draw`。

### 3.1 Generics vs Trait Objects

| | 泛型 `T: Draw` | `Box<dyn Draw>` |
| --- | --- | --- |
| 分发 | 静态（单态化） | 动态 |
| 同一集合 | 通常同一具体 `T` | 可多种具体类型 |
| 性能 | 常可内联优化 | 间接调用 |

### 3.2 Object Safety（对象安全）

只有**对象安全**的 Trait 才能变成 `dyn Trait`。大致要求：

- 方法返回类型不能是 `Self`  
- 方法不能有泛型类型参数  

例如标准库的 `Clone` 返回 `Self`，不能直接 `dyn Clone`。

---

## 4. OO Design Patterns（状态模式示例）

书中博客帖示例：用 Trait Object 表示草稿 / 审核 / 发布等状态，`request_review` / `approve` 返回新状态。

也可用 `enum` 穷举状态 + `match`——往往更简单、更 Rust。Trait Object 适合状态种类会扩展、且想对扩展开放的插件式场景。

---

> [!important] 一句话总结
> 封装靠 `pub`；共享行为靠 Trait；运行时多态靠 `dyn Trait`（对象安全）；优先枚举与泛型，需要异质子集合时再上 Trait Object。
