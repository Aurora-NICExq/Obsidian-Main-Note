---
aliases: [模块系统, Package Crate Module, 包与模块, Modules, use, pub, super self, 路径 path]
tags: [rust, module]
up: "[[Rust MOC]]"
related: "[[Enums and Pattern Matching|枚举]], [[Structs, Methods, and Associated Functions|结构体]], [[Rust Compiler and Cargo|Cargo 与编译器]], [[Error Handling|错误处理]], [[Generics, Traits, and Lifetimes|泛型 Trait 与生命周期]]"
down: "[[Error Handling|错误处理]]"
---
# Packages, Crates, and Modules

> [!summary] 核心结论
> Rust 的模块系统分四层：**Package（包）** 由 `Cargo.toml` 描述，最多 1 个 library crate、任意多个 binary crate，至少 1 个；**Crate（单元包）** 是一次编译的单元、一棵模块树，产出一个 library 或可执行文件，入口是 crate root（`src/main.rs` / `src/lib.rs`）；**Module（模块）+ use** 控制代码组织、作用域与私有边界；**Path（路径）** 用 `::` 定位条目，分绝对（从 `crate` 开始）与相对（从 `self`/`super`/当前模块开始）。默认一切**私有**，用 `pub` 对外暴露，`use` 把路径引入作用域。

前置知识：[[Rust Compiler and Cargo|Cargo 与编译器]]（了解 `cargo new` / `cargo build` 的基本流程）。

---

## 1. Overview of the Module System (模块系统总览)

| 概念 | 作用 |
| ---- | ---- |
| **Package（包）** | Cargo 的功能单位，让你构建、测试、共享 crate |
| **Crate（单元包）** | 一棵模块树，编译后产生一个 library 或可执行文件 |
| **Module（模块）、`use`** | 控制代码的组织、作用域与私有边界 |
| **Path（路径）** | 为 `struct`、`function`、`module` 等**条目（item）**命名、定位的方式 |

## 2. Packages and Crates (包 与 单元包)

**Crate** 是 Rust 一次编译的最小单位；编译器 `rustc` 每次针对一个 crate root 文件工作，产出 library 或二进制文件。一个 **Package** 的约束是：

- 必须包含 **1 个 `Cargo.toml`**，它描述如何构建这些 crate。
- **最多 1 个** library crate。
- 可以包含**任意数量**的 binary crate。
- 但**至少要包含 1 个** crate（library 或 binary）。

### Cargo's Conventions (Cargo 的惯例)

Cargo 靠约定的文件位置来识别 crate root，并把它交给 `rustc` 构建：

| 文件 | 角色 | crate 名 |
| ---- | ---- | -------- |
| `src/main.rs` | binary crate 的 crate root | 与 package 名相同 |
| `src/lib.rs`  | library crate 的 crate root | 与 package 名相同 |
| `src/bin/*.rs` | 每个文件各是一个**额外的** binary crate | 文件名 |

也就是说，一个同时含 `src/main.rs` 和 `src/lib.rs` 的 package，就包含一个二进制 crate 和一个库 crate，两者同名。

## 3. Defining Modules (定义模块)

模块用 `mod` 关键字定义，可以嵌套，从而形成一棵**模块树**。crate root 构成隐式的根模块 `crate`：

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}
        fn seat_at_table() {}
    }

    mod serving {
        fn take_order() {}
        fn serve_order() {}
        fn take_payment() {}
    }
}
```

对应的模块树（每个条目都能用一条从 `crate` 出发的路径定位）：

![[d2-packages-crates-and-modules-01.svg]]

## 4. Paths (路径)

要在模块树中找到某个条目，就要用**路径**。路径至少由一个标识符组成，标识符之间用 `::` 连接。路径有两种形式：

- **绝对路径**：从 **crate root** 开始，以 crate 名或字面量 `crate` 打头。
- **相对路径**：从**当前模块**开始，以 `self`、`super` 或当前模块中的标识符打头。

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // 绝对路径：从 crate root 出发
    crate::front_of_house::hosting::add_to_waitlist();

    // 相对路径：从当前模块（crate root）出发
    front_of_house::hosting::add_to_waitlist();
}
```

### `super` and `self` (super 与 self)

`super` 用来访问**父模块**中的内容，类似文件系统里的 `..`；`self` 指**当前模块**，类似 `.`。当子模块要调用定义在父模块里的条目时，`super` 很方便：

```rust
fn deliver_order() {} // 定义在 crate root

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();          // 相对路径：调用同模块的函数
        super::deliver_order(); // super 回到父模块（crate root），调用 deliver_order
    }

    fn cook_order() {}
}
```

## 5. Privacy Boundary and `pub` (私有边界 与 pub)

模块不仅组织代码，还定义**私有边界（privacy boundary）**。Rust 中一切条目（函数、方法、结构体、枚举、模块、常量）**默认私有**。私有性规则是单向的：

- **子模块**可以使用**祖先模块**中的条目（向上可见）。
- **父模块**却**不能**访问子模块里的私有条目（向下不可见）。

想把某个条目暴露给外部，就在它前面加 `pub`。注意：把模块标为 `pub` 只是"允许外部引用到这个模块"，模块**内部**的条目仍需各自标 `pub` 才可见。

```rust
mod front_of_house {
    pub mod hosting {        // 模块公有
        pub fn add_to_waitlist() {} // 函数也要单独标 pub
    }
}
```

## 6. `pub` on Structs and Enums (pub 用于 struct 与 enum)

`pub` 作用在结构体和枚举上时，行为**不一样**：

- **`pub struct`**：结构体公有，但**字段默认仍私有**，需要哪个字段公有就单独给它加 `pub`。
- **`pub enum`**：枚举公有后，它的**所有变体自动公有**。

### pub struct

因为存在私有字段，外部无法直接用字面量构造，通常要提供一个公有的关联函数来创建实例：

```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,      // 公有字段
        seasonal_fruit: String, // 私有字段：外部读写不了
    }

    impl Breakfast {
        // 提供公有构造函数，否则外部因私有字段而无法创建 Breakfast
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    let mut meal = back_of_house::Breakfast::summer("Rye");
    meal.toast = String::from("Wheat"); // ✅ toast 是 pub，可修改
    // meal.seasonal_fruit = String::from("blueberries"); // ❌ 字段私有，编译错误
}
```

### pub enum

```rust
mod back_of_house {
    pub enum Appetizer {
        Soup,  // 无需单独标 pub，变体随枚举一起公有
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let _order1 = back_of_house::Appetizer::Soup;
    let _order2 = back_of_house::Appetizer::Salad;
}
```

## 7. The `use` Keyword (use 关键字)

每次都写完整路径很啰嗦。`use` 把一条路径**引入当前作用域**，之后可用短名访问（仍受私有性规则约束）：

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting; // 引入 hosting 模块

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist(); // 直接用短路径
}
```

### Idiomatic `use` (use 的习惯用法)

| 引入对象 | 习惯做法 | 例子 |
| -------- | -------- | ---- |
| **函数** | 只引入到**父模块**，调用时带一层模块名 | `use ...::hosting;` → `hosting::add_to_waitlist()` |
| **struct / enum / 其它** | 直接引入到**条目本身** | `use std::collections::HashMap;` |

引入 struct/enum 时指定完整路径：

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new(); // 直接用 HashMap，而非 collections::HashMap
    map.insert(1, 2);
}
```

**同名条目**则引入到各自的父模块，用父模块名区分：

```rust
use std::fmt;
use std::io;

fn f1() -> fmt::Result { Ok(()) }
fn f2() -> io::Result<()> { Ok(()) } // 靠 fmt:: / io:: 区分两个 Result
```

### `as` — Local Alias (as 起别名)

`as` 为引入的路径指定一个本地别名，是解决同名冲突的另一种方式：

```rust
use std::fmt::Result;
use std::io::Result as IoResult; // 把 io::Result 重命名为 IoResult
```

### `pub use` — Re-exporting (重新导出名称)

用 `use` 引入的名称在当前作用域是**私有**的。`pub use` 会**重新导出**：既把条目引入本作用域，又允许外部代码通过本作用域访问它——常用来对外提供一套整洁的 API。

```rust
pub use crate::front_of_house::hosting; // 外部现在可用 crate::hosting 访问
```

### Using External Packages (使用外部包)

引入 crates.io 上的第三方包分两步：

1. 在 `Cargo.toml` 的 `[dependencies]` 里声明依赖。
2. 用 `use` 把需要的条目引入作用域。

```toml
# Cargo.toml
[dependencies]
rand = "0.8.5"
```

```rust
use rand::Rng;

fn main() {
    let n = rand::thread_rng().gen_range(1..=100); // 1~100 的随机数
    println!("{}", n);
}
```

标准库 `std` 也被当作外部包，只是**无需在 `Cargo.toml` 中声明**，直接 `use` 即可。

### Nested Paths and the Glob `*` (嵌套路径 与 通配符)

同一个包/模块下引入多个条目时，用**嵌套路径**把多条 `use` 合并到一行；`self` 代表模块自身：

```rust
// 这两行 ...
use std::io;
use std::io::Write;

// 可合并为一行（self 指 std::io 本身）
use std::io::{self, Write};
```

`*`（glob 通配符）把某路径下**所有公有条目**一次性引入。它会污染作用域、不易看出名字来源，**应谨慎使用**（常见于测试模块或 prelude）：

```rust
use std::collections::*;
```

## 8. Splitting Modules into Files (将模块拆分到多个文件)

当模块变大，可把内容移到独立文件里，而**模块树结构保持不变**。规则：`mod 模块名;` 若结尾是**分号**而非代码块，Rust 会去**同名文件**里加载模块内容。

```rust
// src/lib.rs —— crate root
mod front_of_house; // 注意结尾是 ; 而不是 { ... }，内容从 src/front_of_house.rs 加载

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

```rust
// src/front_of_house.rs —— front_of_house 模块的内容
pub mod hosting; // 继续下沉，内容从 src/front_of_house/hosting.rs 加载
```

```rust
// src/front_of_house/hosting.rs —— hosting 模块的内容
pub fn add_to_waitlist() {}
```

三个文件加载后，模块树与 §3 里"全写在一个文件"时**完全一致**，只是物理上拆开了。

---

> [!important] 一句话总结
> Package（含 `Cargo.toml`，≤1 库 + 任意二进制）→ Crate（一次编译、一棵模块树，root 是 `main.rs`/`lib.rs`）→ Module（`mod` 组织代码、划私有边界）→ Path（`::` 定位，`crate` 起头是绝对、`self`/`super` 起头是相对）；默认私有，`pub` 暴露（`pub struct` 字段仍需逐个 `pub`，`pub enum` 变体全公有），`use` 引入作用域（函数引到父模块、类型引到本身），`as` 起别名、`pub use` 重导出，`mod 名;` 把模块拆到同名文件。
