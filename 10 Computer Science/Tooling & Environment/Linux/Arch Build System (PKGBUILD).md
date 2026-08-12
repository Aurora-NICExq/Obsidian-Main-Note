---
aliases: [Arch 软件构建体系, Arch Build System, PKGBUILD, makepkg, pacman]
tags: [linux, packaging]
up: "[[Linux MOC]]"
related: "[[Package Management (yum)|yum 软件管理]], [[Archiving and Compression|压缩与解压]], [[File Operations|文件操作]]"
down: ""
---
# Arch Build System (PKGBUILD)

> [!summary] 核心结论
> Arch Linux 不推荐源码直接 `make install` 进系统，而是：用 `PKGBUILD`（一个 Bash 脚本）描述构建规则 → `makepkg` 据此构建出 `.pkg.tar.zst` 软件包 → `pacman -U` 安装。这样软件**可查询、可升级、可卸载、可复现**。本笔记以构建 GNU `hello` 为例走通整个流程。

前置知识：[[Package Management (yum)|yum 软件管理]]（包管理的基本概念，作为对照）。

---

## 1. Overview of the Arch Build System (体系概览)

Arch's recommended way to install software is **not** to `make install` source straight into
the system, but rather:

```text
source code
  ↓
PKGBUILD describes the build rules
  ↓
makepkg builds an Arch package
  ↓
produces .pkg.tar.xz / .pkg.tar.zst
  ↓
pacman installs the package
  ↓
software lands in /usr/bin, /usr/lib, /usr/share, etc.
```

In other words, Arch prefers:

```text
source → package → managed by pacman
```

rather than:

```text
source → sudo make install → dumped straight into system directories
```

The benefits:

- pacman knows exactly which files the software installed.
- It can later be queried, upgraded, and uninstalled cleanly.
- It is less likely to clutter the system directories.
- The build process is reproducible.

## 2. Core Tools and Files (核心工具和文件)

### 2.1 pacman

`pacman` is Arch's package manager. Common operations:

```bash
sudo pacman -S <pkg>          # install from the official repositories
sudo pacman -U <local-pkg>    # install a locally built package
pacman -Q <pkg>               # query whether a package is installed
pacman -Ql <pkg>              # list which files a package installed
pacman -Qo /usr/bin/<cmd>     # find which package owns a file
sudo pacman -R <pkg>          # uninstall a package
```

### 2.2 PKGBUILD

`PKGBUILD` is the heart of the Arch packaging system. It is essentially a **Bash script**
that describes:

- package name, software version, package release
- supported CPU architectures
- description, source URL, source checksums
- dependencies
- how to build, and how to install into the temporary packaging directory

Example:

```bash
pkgname=hello
pkgver=2.12.1
pkgrel=1
pkgdesc="GNU Hello, a simple greeting program"
arch=('aarch64')
url="https://www.gnu.org/software/hello/"
license=('GPL3')
depends=('glibc')
source=("https://ftp.gnu.org/gnu/hello/hello-${pkgver}.tar.gz")
sha256sums=('SKIP')

build() {
    cd "hello-${pkgver}"
    ./configure --prefix=/usr
    make
}

package() {
    cd "hello-${pkgver}"
    make DESTDIR="$pkgdir" install
}
```

Key fields:

- `pkgname` — the package name.
- `pkgver` — the **upstream** software version.
- `pkgrel` — the **Arch packaging** release. When the source version is unchanged but the
  packaging is modified, bump `pkgrel`.
- `arch` — supported architectures. On an Apple Silicon Mac running Arch Linux under
  OrbStack, the system is most likely `aarch64`:

```bash
uname -m       # → aarch64
```

So `PKGBUILD` needs `arch=('aarch64')`, or to support several architectures:

```bash
arch=('x86_64' 'aarch64')
```

### 2.3 makepkg

`makepkg` builds a package from a `PKGBUILD`:

```bash
makepkg        # build only
makepkg -s     # build, auto-installing missing dependencies
makepkg -i     # build, then install the resulting package
makepkg -si    # auto-install deps, then install after building
```

That is: `-s = syncdeps` (auto-install dependencies), `-i = install` (install after
building).

## 3. Hands-on: Building the GNU hello Package (实际操作)

### 3.1 Install Base Tools

```bash
sudo pacman -Syu
sudo pacman -S base-devel git pacman-contrib
```

- `base-devel` — common compilation and packaging tools.
- `git` — to fetch source or AUR repositories.
- `pacman-contrib` — provides helpers such as `updpkgsums`.

### 3.2 Create a Working Directory

```bash
mkdir -p ~/pkgbuild-practice/hello
cd ~/pkgbuild-practice/hello
```

### 3.3 Create the PKGBUILD

```bash
nvim PKGBUILD
```

Write the `PKGBUILD` shown in §2.2. On a plain x86_64 machine use `arch=('x86_64')`, or
`arch=('x86_64' 'aarch64')` to support both.

### 3.4 Build the Package

In the directory containing `PKGBUILD`:

```bash
makepkg          # or: makepkg -s
makepkg -si      # to build and install in one step
```

## 4. Errors Encountered During the Build (构建过程中遇到的错误)

### 4.1 Architecture Error

```text
ERROR: hello is not available for the 'aarch64' architecture.
```

Cause: the system is `aarch64`, but `PKGBUILD` says `arch=('x86_64')`. Fix it by editing
`PKGBUILD` to `arch=('aarch64')` (or `arch=('x86_64' 'aarch64')`), and check the current
architecture with `uname -m`.

### 4.2 Source Checksum Failure

```text
hello-2.12.1.tar.gz ... FAILED
ERROR: One or more files did not pass the validity check!
```

Cause: the `sha256sums` in `PKGBUILD` does not match the downloaded source's hash.

- Temporary workaround: `sha256sums=('SKIP')`.
- Proper fix: install `pacman-contrib` and regenerate the sums:

```bash
sudo pacman -S pacman-contrib
updpkgsums
makepkg -si
```

> [!note]
> Don't rely on `SKIP` for real packaging — the checksum verifies that the source has not
> been corrupted or tampered with.

## 5. Directory Structure After a Successful Build (目录结构)

After a successful build, `ls` might show:

```text
PKGBUILD
hello-2.12.1-1-aarch64.pkg.tar.xz
hello-2.12.1.tar.gz
pkg
src
```

- **PKGBUILD** — the packaging script (source URL, version, architecture, how to build,
  how to install to a temp dir, how to package).
- **hello-2.12.1.tar.gz** — the **source tarball** from the `source=(...)` line. It is *not*
  an Arch package and cannot be installed with `pacman -U`.
- **src/** — the source unpack & build directory. `makepkg` extracts the source here (e.g.
  `src/hello-2.12.1/`) and runs `build()`.
- **pkg/** — the temporary packaging directory. `package()` installs the built files here
  first; a file destined for `/usr/bin/hello` lands at `pkg/hello/usr/bin/hello` so
  `makepkg` can pack that tree into a package.
- **hello-2.12.1-1-aarch64.pkg.tar.xz** — the final **Arch package**; this is what
  `pacman -U` installs.

## 6. Package Filename Format (软件包文件名含义)

Taking `hello-2.12.1-1-aarch64.pkg.tar.xz`:

```text
hello        package name
2.12.1       upstream software version
1            Arch packaging release (pkgrel)
aarch64      CPU architecture
pkg.tar.xz   Arch package compression format
```

So the overall format is:

```text
<name>-<version>-<pkgrel>-<arch>.pkg.tar.xz
```

Note the contrast: `hello-2.12.1.tar.gz` is the **source** package;
`hello-2.12.1-1-aarch64.pkg.tar.xz` is the **Arch** package.

## 7. Installing the Local Package (安装本地软件包)

```bash
sudo pacman -U hello-2.12.1-1-aarch64.pkg.tar.xz
sudo pacman -U hello-*.pkg.tar.xz          # wildcard also works
```

Do **not** write `hello-*.pkg.tar.gz` — the built package is `.pkg.tar.xz`, not
`.pkg.tar.gz`. If a wildcard matches nothing, the shell passes the literal text to
`pacman`, producing:

```text
error: 'hello-*.pkg.tar.gz': could not find or read package
```

## 8. Verifying After Installation (安装后验证)

```bash
hello                       # → Hello, world!
pacman -Q hello             # → hello 2.12.1-1
pacman -Ql hello            # list installed files, e.g. /usr/bin/hello
pacman -Qo /usr/bin/hello   # → /usr/bin/hello is owned by hello 2.12.1-1
```

The last command confirms `/usr/bin/hello` was installed by, and is managed by, the
`hello` package.

## 9. Uninstalling (卸载软件包)

```bash
sudo pacman -R hello
hello        # → command not found
```

The `command not found` confirms `pacman` removed it completely.

## 10. makepkg vs pacman (二者的关系)

```text
makepkg = "builds packages"
pacman  = "installs, queries, removes, manages packages"
```

More fully:

```text
PKGBUILD
  ↓
makepkg
  ↓
local package .pkg.tar.xz
  ↓
pacman -U
  ↓
system software
```

## 11. Full Flow Summary (完整流程总结)

```text
1. create the hello packaging directory
        ↓
2. write PKGBUILD
        ↓
3. makepkg reads PKGBUILD
        ↓
4. download source hello-2.12.1.tar.gz
        ↓
5. verify the source
        ↓
6. extract source into src/
        ↓
7. run build()
        ↓
8. run package()
        ↓
9. files temporarily land in pkg/
        ↓
10. produce hello-2.12.1-1-aarch64.pkg.tar.xz
        ↓
11. sudo pacman -U installs the local package
        ↓
12. the hello command enters /usr/bin
        ↓
13. pacman can query, manage, and uninstall it
```

---

> [!important] 一句话总结
> Arch 构建体系的核心：不要把源码直接装进系统，而是用 `PKGBUILD` 描述构建、`makepkg` 生成软件包、再交给 `pacman` 管理——这样安装才可查询、可卸载、可复现、可维护。
