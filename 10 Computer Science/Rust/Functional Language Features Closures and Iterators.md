---
aliases: [函数式语言特性, 闭包, 迭代器, Closures, Iterators, Functional Features]
tags: [rust, closures, iterators]
up: "[[Rust MOC]]"
related: "[[Building a CLI Search Tool (minigrep)|minigrep]], [[Ownership, Borrowing, and Slices|所有权]], [[Generics, Traits, and Lifetimes|Trait]], [[Common Collections|集合]], [[Writing Automated Tests|测试]]"
down: "[[More about Cargo and Crates.io|Cargo 进阶]]"
---
# Functional Language Features: Closures and Iterators

> [!summary] 核心结论
> **闭包**是可捕获环境的匿名函数，可存进变量、当参数传递；捕获方式对应 `FnOnce` / `FnMut` / `Fn`。**迭代器**惰性处理序列，实现 `Iterator` 的 `next`；适配器（`map`/`filter`）产生新迭代器，消费器（`collect`/`sum`）才真正执行。闭包 + 迭代器是惯用 Rust，零成本抽象，常比手写循环更快或相当。

对应《The Rust Programming Language》**第 13 章**。前置：[[Ownership, Borrowing, and Slices|所有权]]、[[Building a CLI Search Tool (minigrep)|minigrep]]、[[Writing Automated Tests|测试]]。

---

## 1. Closures（闭包）

闭包：可**捕获定义处环境**的匿名函数。可在一处创建，在另一处调用。

```rust
let expensive_closure = |num: u32| -> u32 {
    println!("calculating slowly...");
    num
};
```

### 1.1 Syntax vs Functions（语法对比）

| | 函数 | 闭包 |
| --- | --- | --- |
| 名字 | `fn add(x: i32) -> i32` | 通常匿名，可赋给变量 |
| 参数 | `(x: i32)` | `|x|` 或 `|x: i32|` |
| 类型标注 | 必须 | **常可省略**（编译器推断） |
| 函数体 | 必须 `{}` | 单表达式可省略 `{}` |

```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

首次调用会锁定参数/返回类型；同一闭包不能再当另一种类型用。

### 1.2 Capturing the Environment（捕获环境）

```rust
let list = vec![1, 2, 3];
let only_borrows = || println!("From closure: {list:?}");
only_borrows();
println!("After: {list:?}"); // list 仍可用：闭包只不可变借用
```

捕获方式由闭包**如何使用**环境变量决定：

| Trait | 捕获 | 可调用次数 |
| ----- | ---- | ---------- |
| `FnOnce` | 拿走所有权（move） | 至少一次；拿走后不能再调 |
| `FnMut` | 可变借用 | 多次（可改环境） |
| `Fn` | 不可变借用 | 多次 |

需要强制拿走所有权时用 `move`：

```rust
let list = vec![1, 2, 3];
thread::spawn(move || println!("From thread: {list:?}"))
    .join()
    .unwrap();
```

> [!note]
> 三个 Trait 有继承关系：实现 `Fn` 也实现 `FnMut` 与 `FnOnce`。API 若只要“能调用一次”，常写 `FnOnce`。

### 1.3 Storing Closures（缓存示例思路）

可用结构体字段存闭包 + `Option` 缓存结果（书中的昂贵计算示例）：只有第一次调用真正算，之后复用——闭包类型用泛型 + `Fn` bound 即可。

---

## 2. Iterators（迭代器）

迭代器**惰性**：创建后不做事，直到调用消费方法。

```rust
let v = vec![1, 2, 3];
let mut iter = v.iter();       // 得到迭代器
assert_eq!(iter.next(), Some(&1));
assert_eq!(iter.next(), Some(&2));
assert_eq!(iter.next(), Some(&3));
assert_eq!(iter.next(), None);
```

| 方法 | 元素类型 | 是否消耗集合 |
| ---- | -------- | ------------ |
| `iter()` | `&T` | 否 |
| `iter_mut()` | `&mut T` | 否 |
| `into_iter()` | `T` | 是（拿走所有权） |

`for x in v` 实际调用 `into_iter()`（或等价转换）。

### 2.1 The `Iterator` Trait

```rust
pub trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
    // 大量默认方法：map、filter、sum…
}
```

自己实现迭代器时主要实现 `next`；其余适配器免费获得。

### 2.2 Adapters vs Consumers（适配器 vs 消费器）

- **迭代器适配器**：返回新迭代器，仍惰性（`map`、`filter`、`enumerate`…）  
- **消费适配器**：拿走迭代器并产出最终值（`collect`、`sum`、`count`、`any`…）

```rust
let v = vec![1, 2, 3];
let doubled: Vec<_> = v.iter().map(|x| x * 2).collect();
```

没有 `collect`（或其它消费）时，`map` 闭包根本不会执行。

```rust
let shoes = vec![/* ... */];
shoes.into_iter().filter(|s| s.size == 10).collect::<Vec<_>>()
```

### 2.3 Creating from Scratch（自定义迭代器）

结构体保存状态，`impl Iterator for ...` 里写 `next`——例如计数器每次返回下一个整数，直到上限。

---

## 3. Improving minigrep（改进 I/O 项目）

第 12 章的搜索可用迭代器重写，更短且意图清晰：

```rust
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    contents
        .lines()
        .filter(|line| line.contains(query))
        .collect()
}
```

`Config::new` 也可改为接收 `env::args` 的迭代器，避免先 `collect` 再 `clone`（书中 `build` + `Iterator<Item = String>` 写法）。

---

## 4. Performance（性能）

闭包与迭代器是**零成本抽象**：编译后通常与手写等价循环同级，有时因优化更好。优先写清晰的迭代器链，不必为“性能”先写成繁琐循环。

---

> [!important] 一句话总结
> 闭包 = 带环境的匿名函数（`Fn`/`FnMut`/`FnOnce`）；迭代器 = 惰性序列（适配器搭管道，消费器才执行）。二者组合是惯用、可测、高效的 Rust 风格。
