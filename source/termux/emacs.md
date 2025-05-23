# Emacs in termux
本文档创建于 2024/10/20  
Emacs，一个神的编辑器，上手难度大但却又很nb
- 代码高亮、代码补全、实时语法检测等基础编程功能
- 将快捷键运用到极致，无论什么时都可以通过快捷键解决，高效工作
- 可以直接进行编译、调试、版本管理等各类开发任务操作
- 可扩展和定制化空间大，插件生态丰富
- Emacs Lisp 使得更有灵活性，插件与插件间很容易进行组合协作
## 准备
如果你是准备从vim转到emacs，可以在emacs里安装`evil`，该插件将可以使用vim的快捷键布局到Emacs，适合从vim转至Emacs的佬安装
## 安装
```bash
pkg install emacs
```
## 启动
```bash
emacs
```
直接输入便可进入到Emacs编辑器，在其命令之后接上文件名可以打开文件  
第一次启动时将见到初始页面，主要是Emacs的一些教程  
![Emacs 教程](_img/termux/emacs-setup.jpg)
## 快捷键
Emacs 中有五个功能键： `Control`、 `Meta`、 `Shift`、 `Super`、 `Hyper`。其中部分名称是几十年前的键盘上的按键名称，其中的 Hyper 键更是在现代键盘上消失了。其他的按键例如 Meta 对应于 PC 键盘上的 Alt 键，Control 对应 Ctrl 键，Super 对应 PC 键盘上的 Win 键 (Termux 中需要借助输入法使用 Super 键)。  
 同时，我们需要随时随地修改快捷键，需要有一种方式来表达快捷键，以便修改配置文件。见下表（下文快捷键以 `Emacs快捷键缩写-字母` 格式表示，例如`C-a`表达的是`Control+a`）：
| Emacs 快捷键 | 缩写 | 对应键盘按键 |
| --- | --- | --- |
| Control | C | Ctrl (音量加) |
| Meta | M | Alt |
| Shift | S | Shift |
| Super | s | Win |
| Hyper | H | 没有 |
## Emacs 命令
Emacs 也是通过命令进行操作的，而所谓的命令就是 Elisp 语言定义的一些功能函数。  
对 Emacs 下输入 `M-z` 便可以输入命令，此时左下角将出现 `M-z` 标识并等待输入。**当你忘记某个快捷键时，便可以通过命令去进行操作，这也是你最重要的东西之一。**命令名的传统是有连字符连接的多个有意义的英文单词，在输入时可以用空格代替连字符，也可以通过 `Tab` 去进行命令补全。
## 基础快捷键
在Emacs中，大部分的快捷键需要按两次，毕竟在这其中是个操作那都用一个快捷键搞定。所以基础的快捷键会以 `快捷键` `快捷键`的形式展示。
### 退出
- `C-z` 挂起 Emacs 到后台。在命令框中输入`fg`便可返回到Emacs
- `C-x` `C-c` 退出
- 如果中途不想按了，可以按下快捷键`C-g`放弃输入，此外也可以在任何卡住的地方使用 `C-g` 打断
### 光标移动
很奇怪是不是，Emacs 连光标移到都有对应的快捷键
- `C-p` 对应方向键上
- `C-n` 对应方向键下
- `C-b` 对应方向键左
- `C-f` 对应方向键右
用久了就会发现，其实很顺手的