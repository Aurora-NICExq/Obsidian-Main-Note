---
aliases: [所有权, Rust 所有权, Ownership, 借用, 引用, Rust 切片, move, clone, Copy]
tags: [rust, ownership]
up: "[[Rust MOC]]"
related: "[[Variables, Data Types, Functions, and Control Flow|变量与基础语法]], [[Common Collections|常用集合]], [[Structs, Methods, and Associated Functions|结构体]], [[Generics, Traits, and Lifetimes|泛型 Trait 与生命周期]]"
down: "[[Common Collections|常用集合]]"
---
# Ownership, Borrowing, and Slices

> [!summary] 核心结论
> 所有权让 Rust 在没有垃圾回收器的情况下管理内存：每个值有且仅有一个所有者，所有者离开作用域时值被清理。赋值和传参可能发生 move；借用 `&T` / `&mut T` 可以临时访问而不取得所有权。借用规则可概括为“同一时刻要么多个共享引用，要么一个可变引用”，并且引用必须始终有效。

前置知识：[[Variables, Data Types, Functions, and Control Flow|变量、作用域和函数]]。

---

## 1. The Three Ownership Rules（所有权三规则）

1. Rust 中每个值都有一个**所有者（owner）**。
2. 同一时刻一个值只能有一个所有者。
3. 所有者离开作用域时，值会被丢弃（drop）。

```rust
{
    let s = String::from("hello"); // s 从这里开始有效
    println!("{s}");
} // s 离开作用域，String 的堆内存被释放
```

这里的 `drop` 是确定发生的，不需要等待垃圾回收器。Rust 也不允许对同一资源释放两次。

## 2. Stack, Heap, and `String`（栈、堆与 String）

字符串字面量 `&str` 通常指向程序二进制中的只读数据；`String` 拥有一段可增长的 UTF-8 堆内存：

```rust
let literal: &str = "hello";
let mut owned = String::from("hello");
owned.push_str(", world");
```

一个 `String` 在栈上的元数据可理解为：指针、当前长度和容量；实际字符数据存放在堆上。

![[d2-ownership-borrowing-and-slices-01.svg]]

`String` 离开作用域时，Rust 根据这份所有权信息释放它拥有的堆内存。

## 3. Move, Clone, and Copy（移动、克隆与复制）

### Move（移动）

```rust
let s1 = String::from("hello");
let s2 = s1;

// println!("{s1}"); // ❌ s1 已被移动
println!("{s2}");
```

赋值时，`String` 的栈上元数据交给 `s2`，堆数据不会自动深拷贝。为了避免 `s1` 和 `s2` 最后重复释放同一块内存，Rust 使 `s1` 失效；这就是 **move**。

### `clone`（深拷贝）

确实需要独立堆数据时显式调用 `clone`：

```rust
let s1 = String::from("hello");
let s2 = s1.clone();

println!("{s1}, {s2}"); // 二者都有效
```

`clone` 可能包含堆分配和数据复制，应把它视为可见的成本，而不是默认行为。

### `Copy`（按位复制）

整数、布尔、字符等固定大小的简单类型通常实现了 `Copy`：

```rust
let x = 5;
let y = x;
println!("{x}, {y}"); // ✅ x 仍有效
```

常见 `Copy` 类型包括所有整数、浮点数、`bool`、`char`，以及元素全都实现 `Copy` 的元组和数组。实现了 `Drop` 的类型不能同时实现 `Copy`。

## 4. Ownership and Functions（所有权与函数）

传参和赋值遵循同一规则：非 `Copy` 值会移动，`Copy` 值会复制；返回值也能转移所有权。

```rust
fn takes_ownership(text: String) {
    println!("{text}");
}

fn gives_ownership() -> String {
    String::from("hello")
}

let s = gives_ownership();
takes_ownership(s);
// println!("{s}"); // ❌ 所有权已传入函数
```

如果函数只需要读取值，传入并再返回所有权非常笨重；应改用**引用**。

## 5. Shared References and Borrowing（共享引用与借用）

`&T` 是对 `T` 的共享引用。创建引用称为**借用**：函数可以观察值，但不取得所有权。

```rust
fn calculate_length(s: &String) -> usize {
    s.len()
}

let s1 = String::from("hello");
let len = calculate_length(&s1);
println!("{s1} has length {len}"); // s1 仍属于调用者
```

共享引用默认不能修改其指向的数据：

```rust
fn change(s: &String) {
    // s.push_str("!"); // ❌ 不能通过 &String 修改 String
}
```

## 6. Mutable References（可变引用）

要通过引用修改值，变量和引用两端都要写 `mut`：

```rust
fn change(s: &mut String) {
    s.push_str(", world");
}

let mut text = String::from("hello");
change(&mut text);
```

### Borrowing Rules（借用规则）

对同一个值，在一次有效借用期间：

- 可以有任意多个共享引用 `&T`；或
- 只能有一个可变引用 `&mut T`；
- 两种状态不能重叠。

```rust
let mut s = String::from("hello");

let r1 = &s;
let r2 = &s;
println!("{r1} and {r2}"); // r1、r2 最后一次使用

let r3 = &mut s;           // ✅ 共享借用已结束
r3.push('!');
```

现代 Rust 会根据引用的**最后一次使用**判断借用何时结束，而不必机械地等到花括号结束；这称为非词法生命周期（NLL）。

> [!important] 为什么限制这么严格？
> 共享引用保证读取期间数据不会突然被改写或迁移；可变引用保证修改期间没有其它观察者。编译器因此能在编译期阻止数据竞争和迭代器失效等问题。

## 7. Dangling References（悬垂引用）

引用不能比它所引用的数据活得更久。下面函数试图返回局部变量的引用，会被编译器拒绝：

```rust
// fn dangle() -> &String {
//     let s = String::from("hello");
//     &s
// } // s 在函数结束时被释放，返回的引用将无效
```

正确做法是直接返回拥有所有权的值：

```rust
fn no_dangle() -> String {
    String::from("hello")
}
```

## 8. Slices（切片）

切片是对集合中一段连续元素的引用，不拥有数据。范围采用前闭后开：

```rust
let s = String::from("hello world");
let hello = &s[0..5];
let world = &s[6..11];
let whole = &s[..];
```

字符串切片类型是 `&str`。函数参数优先写 `&str` 而不是 `&String`，这样既能接收字符串字面量，也能接收 `String` 的切片：

```rust
fn first_word(s: &str) -> &str {
    match s.find(' ') {
        Some(index) => &s[..index],
        None => s,
    }
}

let owned = String::from("hello world");
assert_eq!(first_word(&owned), "hello");
assert_eq!(first_word("single"), "single");
```

数组也有切片：

```rust
let a = [1, 2, 3, 4, 5];
let slice: &[i32] = &a[1..3];
assert_eq!(slice, &[2, 3]);
```

> [!warning] 字符串切片的边界
> `String` 使用 UTF-8。`&s[a..b]` 的边界必须落在有效 UTF-8 字符边界上，否则运行时会 panic；不要把字节下标误当作“第几个字符”。详见 [[Common Collections#3. String and UTF-8（String 与 UTF-8）|String 与 UTF-8]]。

## 9. Ownership Decision Table（判断速查）

| 需求 | 参数形式 | 结果 |
| --- | --- | --- |
| 只读取，不取得所有权 | `&T` | 调用后原值仍可用 |
| 修改，不取得所有权 | `&mut T` | 独占借用期间其它引用不可用 |
| 函数需要长期保存或消费值 | `T` | 所有权移动进函数 |
| 需要一份完全独立的数据 | `value.clone()` | 显式复制，可能有成本 |
| 小型 `Copy` 值按值传递 | `T` | 自动复制 |

---

> [!important] 一句话总结
> 所有权决定“谁负责释放”，move 决定“所有权交给谁”，引用决定“谁暂时能访问”；共享借用可多读，可变借用只准一写，所有引用都不得悬垂。切片则是在不取得所有权的前提下借用一段连续数据。
