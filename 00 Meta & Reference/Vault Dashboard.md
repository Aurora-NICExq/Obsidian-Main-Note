---
aliases: [仪表盘, Vault Dashboard, 笔记库概览]
tags: [meta, dataview]
---
# Vault Dashboard

> [!info] 说明
> 本页全部由 **Dataview** 实时生成，不需要手动维护。新建/修改笔记后重新打开本页即会更新。
> 若下方显示为代码块而非表格，说明 Dataview 插件未启用。

---

## 1. 各学科笔记数量

```dataview
TABLE length(rows) AS 篇数
FROM ""
GROUP BY split(file.folder, "/")[0] AS 学科
SORT length(rows) DESC
```

---

## 2. 待补充的坑

散落在各处的待办标记，一次看全：

```dataview
LIST
FROM #待补充 OR #待补充的内容 OR #待补充的实验 OR #实验补充 OR #NVIC知识点
SORT file.name ASC
```

---

## 3. 缺少导航字段的笔记

`up:` 指向所属 MOC。下列笔记还没接入导航体系：

```dataview
TABLE file.folder AS 所在目录
FROM ""
WHERE !up AND !contains(file.name, "MOC") AND file.name != this.file.name
SORT file.folder ASC, file.name ASC
LIMIT 40
```

---

## 4. 缺少 aliases 的笔记

`aliases` 影响搜索命中率（尤其中文别名）：

```dataview
TABLE file.folder AS 所在目录
FROM ""
WHERE !aliases AND file.name != this.file.name
SORT file.folder ASC
LIMIT 40
```

---

## 5. 全部 MOC

```dataview
TABLE file.folder AS 所在目录, length(file.outlinks) AS 链出数
FROM ""
WHERE contains(file.name, "MOC")
SORT file.folder ASC
```

---

## 6. 最近修改

```dataview
TABLE file.folder AS 目录, file.mtime AS 修改时间
FROM ""
WHERE file.name != this.file.name
SORT file.mtime DESC
LIMIT 15
```

---

## 7. 孤岛笔记（无人链入）

没有任何笔记链接过来，可能是被遗忘的内容：

```dataview
TABLE file.folder AS 所在目录
FROM ""
WHERE length(file.inlinks) = 0 AND file.name != this.file.name
SORT file.folder ASC
LIMIT 40
```
