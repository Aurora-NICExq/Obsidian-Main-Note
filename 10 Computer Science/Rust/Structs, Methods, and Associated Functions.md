---
aliases: [Rust 结构体, Struct定义与实例, Struct, tuple struct, 结构体方法, impl]
tags: [rust, struct]
up: "[[Rust MOC]]"
related: "[[Ownership, Borrowing, and Slices|所有权、引用与切片]], [[Enums and Pattern Matching|枚举与模式匹配]], [[Packages, Crates, and Modules|包、Crate 与模块]], [[Generics, Traits, and Lifetimes|泛型与生命周期]]"
down: "[[Enums and Pattern Matching|枚举与模式匹配]]"
---
# Structs, Methods, and Associated Functions

> [!summary] 核心结论
> `struct` 把多个有名称、可为不同类型的字段组合成一个新类型。实例的可变性是整体性的，不能只给单个字段加 `mut`。方法写在 `impl` 块中，第一个参数是 `self` 的某种形式；不接收 `self` 的关联函数通过 `Type::function()` 调用，常用作构造函数。

前置知识：[[Ownership, Borrowing, and Slices|所有权与借用]]。

---

## 1. Defining and Instantiating a Struct（定义与实例化）

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

let user = User {
    active: true,
    username: String::from("aurora"),
    email: String::from("aurora@example.com"),
    sign_in_count: 1,
};
```

- 定义字段时写 `字段名: 类型`，实例化时写 `字段名: 值`。
- 字段顺序不必和定义顺序相同。
- 用点号读取字段：`user.email`。
- `User` 是类型，`user` 是该类型的一个实例。

## 2. Mutability of Instances（实例的可变性）

要修改字段，整个实例必须用 `mut` 声明：

```rust
let mut user = User {
    active: true,
    username: String::from("aurora"),
    email: String::from("old@example.com"),
    sign_in_count: 1,
};

user.email = String::from("new@example.com");
```

Rust 不允许只把某个字段单独声明为可变。`mut` 描述的是**绑定能否通过它修改整个值**。

## 3. Field Init Shorthand（字段初始化简写）

当变量名与字段名相同时，可以省略 `字段名:`：

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

参数中的两个 `String` 会被移动到返回的 `User` 中，因此函数返回后无需复制数据。

## 4. Struct Update Syntax（结构体更新语法）

基于现有实例创建新实例时，用 `..other` 填充未显式给出的字段：

```rust
let user1 = build_user(
    String::from("one@example.com"),
    String::from("user-one"),
);

let user2 = User {
    email: String::from("two@example.com"),
    ..user1
};
```

`..user1` 必须放在最后。这里 `username: String` 从 `user1` 移动到 `user2`，所以之后不能再整体使用 `user1`；实现了 `Copy` 的 `active` 和 `sign_in_count` 则被复制。

> [!note]
> 更新语法不是“让两个实例共享字段”。它仍遵循 [[Ownership, Borrowing, and Slices#3. Move, Clone, and Copy（移动、克隆与复制）|move / Copy 规则]]。

## 5. Tuple Structs and Unit-like Structs（元组结构体与类单元结构体）

### Tuple Struct（元组结构体）

元组结构体的字段没有名称，但整体拥有独立类型：

```rust
struct Color(u8, u8, u8);
struct Point(i32, i32, i32);

let black = Color(0, 0, 0);
let origin = Point(0, 0, 0);

println!("red = {}", black.0);
```

即使字段类型完全相同，`Color` 与 `Point` 仍是不同类型，不能相互替代。这适合用类型区分语义。

### Unit-like Struct（类单元结构体）

没有字段的结构体类似 `()`：

```rust
struct AlwaysEqual;

let subject = AlwaysEqual;
```

常用于只关心类型行为、没有实例数据的场景，例如为该类型实现某个 trait。

## 6. Ownership of Struct Fields（字段的所有权）

结构体字段通常使用 `String` 等拥有所有权的类型，让实例拥有自己的数据：

```rust
struct User {
    username: String,
}
```

字段也可以使用引用，但必须添加生命周期，确保结构体实例不会比引用的数据活得更久。初学阶段若结构体需要长期保存文本，优先使用 `String`。

## 7. Derived Traits and Debug Output（派生 trait 与调试输出）

自定义类型默认不能用 `{}` 或 `{:?}` 打印。可让编译器自动实现 `Debug`：

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

let rect = Rectangle {
    width: 30,
    height: 50,
};

println!("rect = {rect:?}");  // 单行 Debug
println!("rect = {rect:#?}"); // 美化后的多行 Debug
dbg!(&rect);                  // 打印文件、行号和值，不取得所有权
```

## 8. Methods with `impl`（方法）

方法定义在 `impl Type` 块中，第一个参数是 `self`：

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

    fn scale(&mut self, factor: u32) {
        self.width *= factor;
        self.height *= factor;
    }
}
```

| 接收者 | 含义 | 典型用途 |
| --- | --- | --- |
| `&self` | 共享借用实例 | 读取字段 |
| `&mut self` | 可变借用实例 | 修改字段 |
| `self` | 取得实例所有权 | 消费或转换实例 |

调用时使用点语法：

```rust
let mut rect = Rectangle {
    width: 30,
    height: 50,
};

println!("area = {}", rect.area());
rect.scale(2);
```

Rust 会根据方法签名自动添加借用或解引用，因此通常无需手写 `(&rect).area()`。

## 9. Associated Functions（关联函数）

定义在 `impl` 中但**没有 `self` 参数**的函数叫关联函数。它们通过 `::` 调用，常用作构造函数：

```rust
impl Rectangle {
    fn square(size: u32) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}

let square = Rectangle::square(20);
```

`Self` 是当前 `impl` 所对应类型的别名，此处等价于 `Rectangle`。一个类型可以拥有多个 `impl` 块，效果与写在一个块中相同。

## 10. Struct or Enum?（结构体还是枚举）

| 需求 | 选择 |
| --- | --- |
| 一个值同时拥有所有字段 | `struct` |
| 一个值只能是几种形态之一 | `enum` |
| 不同形态携带不同字段 | 带数据的 `enum` 变体 |

例如用户固定有名称和邮箱，适合 `struct User`；消息只能是退出、移动或写文本之一，适合 [[Enums and Pattern Matching|enum Message]]。

---

> [!important] 一句话总结
> `struct` 定义“一个值由哪些字段构成”；字段简写减少重复，`..old` 复用其余字段但仍遵循所有权；行为放进 `impl`，实例方法用 `.method()`，无 `self` 的关联函数用 `Type::function()`。
