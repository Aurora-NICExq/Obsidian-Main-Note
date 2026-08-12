---
aliases: [wget curl, File Transfer, 文件下载, download]
tags: [linux, networking]
up: "[[Linux MOC]]"
related: "[[Networking Basics|网络基础]], [[Archiving and Compression|压缩与解压]], [[Package Management (yum)|软件管理]]"
down: ""
---
# File Transfer (wget, curl)

> [!summary] 核心结论
> 命令行下载/请求网络资源的两把工具：`wget` 是非交互式文件下载器（`-b` 后台下载），`curl` 发送 HTTP 请求并可下载文件（`-O` 按远端文件名保存）。两者都直接接 URL。

前置知识：[[Networking Basics|网络基础]]（IP / DNS）。

---

## 1. `wget` — Non-interactive Downloader (文件下载器)

```
wget [-b] <url>
```

- **`-b`** — download in the **background**; logs are written to `wget-log` in the current
  directory.
- **url** — the download link.

```bash
wget https://example.com/file.tar.gz
wget -b https://example.com/big.iso      # background; check progress in ./wget-log
```

## 2. `curl` — HTTP Requests and Downloads (网络请求)

`curl` sends HTTP requests — fetching information or downloading files.

```
curl [-O] <url>
```

- **`-O`** (capital O) — save the response to a file named after the **remote** filename
  (use when the URL points at a file).
- **url** — the address to request.

```bash
curl https://example.com/api          # print the response to the terminal
curl -O https://example.com/file.zip  # save as file.zip
```

> [!tip]
> Rule of thumb: `wget` is purpose-built for **downloading files**, while `curl` is a
> general-purpose **HTTP client** (test APIs, send headers, POST data) that *also* downloads.

---

> [!important] 一句话总结
> 下整文件用 `wget url`，调接口/灵活请求用 `curl url`；要把下载内容存成文件就加 `curl -O`。下载完的压缩包用 [[Archiving and Compression]] 解开。
