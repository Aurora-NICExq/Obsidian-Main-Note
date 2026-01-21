有一个字符串“小明”，把这个字符串变成“小小明”

```c
#include <stdio.h>

int main() {
    char source[] = "小明";
    
    // 1. 准备一个足够大的新数组来存放结果
    // "小" (假设UTF-8占3字节) + "小明" (6字节) + 结束符'\0' (1字节) = 至少10字节
    // 为了安全，我们通常给大一点的空间
    char result[50]; 

    // 2. 使用 sprintf 进行格式化拼接
    // 逻辑：把 "小" 和 source 变量里的内容拼起来，写入 result
    sprintf(result, "小%s", source);

    printf("原来的字符串: %s\n", source);
    printf("新的字符串: %s\n", result);

    return 0;
}
```

