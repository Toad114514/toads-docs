# C in termux
本文档创建于于 2024/10/22，更新于 2024/10/22
## 简介
一个历史久远、应用广泛的计算机语言。易于学习、编译快，同时也可以通过它制作各种高效率的程序。值得一提的是，C 语言就是为了开发 Unix 而出现的。
## 安装
```bash
pkg install clang
```
使用上述命令安装`clang`包。可以通过`clang -v`检查版本
## 快速入门
以下是一个简单的 `Hello World` 示例：
```c
#include <stdio.h>
 
int main()
{
   /* 我的第一个 C 程序 */
   printf("Hello, World! \n");
   return 0;
}
```
简单分析一下该代码：
1. `#include <stdio.h>` 是预处理器指令，编译时要包含有 `stdio.h` 文件
2. `int main()` 是主函数，命令从这里开始
3. `/*...*/` 是系统的注释，编译时将忽略
4. `printf(...)` 是 C 语言中的其中一个函数，会在屏幕上面打印文字
5. `return 0` 终止 `main()` 函数并返回 **0**
## 编译
先使用`vim`打开一个文件
```bash
vim hello.c
```
接着将上方的示例复制并粘贴到vim编辑器中。完成后输入`:wq`退出  
接下来使用 `clang` 将文件编译成 .o 文件并执行
```bash
# 编译文件
clang helloworld.c -o helloworld.o
# 执行 .o 文件
./helloworld.o
```
接着在你的控制台中应看到 `Hello, World!` 出现
## 参考
- [C 程序结构 | 菜鸟教程](https://www.runoob.com/cprogramming/c-program-structure.html)