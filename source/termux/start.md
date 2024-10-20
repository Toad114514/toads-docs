# Termux 开始
本文档更新于2024/10/20，本页面内容引自 [Termux Wiki](https://wiki.termux.com/wiki/Getting_started)，机翻，Toad114514 修正及添加部分内容
## 开始
Termux 是一个终端仿真器应用程序，通过移植到 Android 操作系统的大量命令行实用程序进行了增强。主要目标是为移动设备用户提供 Linux 命令行体验，而无需 root 或其他特殊设置。
## 它是如何工作的
终端仿真器基本上是一个应用程序，它使用系统调用 [execve(2)](https://www.man7.org/linux/man-pages/man2/execve.2.html) 来启动命令行程序，并将标准输入、输出和错误流重定向到显示器上。  
Android 操作系统上可用的大多数终端应用程序都可以使用非常有限的程序，这些实用程序通常由操作系统或其他Root工具（如 Magisk）提供。我们决定更进一步，将 GNU/Linux 系统上通常可用的包移植到 Android 操作系统。  
Termux 既不是虚拟机，也不是任何其他类型的模拟或模拟环境。提供的所有包都使用 `Android NDK` 进行交叉编译，并且只有兼容性补丁才能让它们在 Android 上运行，操作系统不提供对其文件系统的完全访问权限。因此` Termux 无法将包文件安装到标准目录中`，例如 /bin、/etc、/usr 或 /var。相反，所有文件都安装到位于
```
/data/data/com.termux/files/usr
```
我们称该目录为 “prefix”（通常将其称为 “$PREFIX”），这也是 Termux shell 中导出的环境变量。请注意，此目录无法更改或移动到 SD 卡，因为：
- 文件系统必须支持 unix 权限和特殊文件，例如符号链接或套接字。
- 前缀路径被硬编码到所有二进制文件中。

除了前缀之外，用户还可以将文件存储在主目录（或“$HOME”）中，目录为
```
/data/data/com.termux/files/home
```
但是，文件系统并不是与传统 Linux 发行版的唯一区别。有关更多信息，请阅读[与 Linux 的差异（转至Termux Wiki）](https://wiki.termux.com/wiki/Differences_from_Linux)。
## 我可以用 Termux 做什么？
Termux 应用程序有许多可以做到的：
- 使用 Python 进行数据处理
- 在开发环境中编程
- 使用有些年头的工具下载和管理文件和页面
- 了解 Linux 命令行环境的基础知识
- 运行 SSH 客户端
- 同步和备份您的文件

当然，使用不仅限于上面列出的功能。我们的软件源中有 1000 多个包。如果这些包没有你要找的东西，你可以编译自己的 - 我们有各种构建工具，包括C、C++、Go、Rust等语言的编译器。NodeJS、Python、Ruby 等常用语言的解释器也可以使用。  
请注意，Termux 不是 Root 工具，除非您足够熟练地破解 Android 操作系统的安全性，否则不会为您提供 root 权限。
## 需要 root
通常 Termux 不需要对设备进行 root 操作。事实上，它针对于非root的设备。  
您可能希望将设备 root 后实现：
- 修改设备固件
- 修改操作系统或内核的参数
- 以非交互方式安装/卸载 APK
- 对设备上的所有文件系统具有完全读/写访问权限
- 可以直接访问硬件设备，例如 BT/Wi-Fi 模块或串行线路、访问调制解调器
- 通过 chroot（**不是 proot！**）或Docker等容器在 Android 上安装 Linux 发行版和容器服务
- 对您的设备有 “完全” 控制权

如果上述的应用你不会用上，那么 root 就不必要了，况且root设备可能损坏你的设备变成板砖！

## 技巧
以下是有关如何安全使用 Termux 的基本方法：
- **学习 shell 脚本！**
- **始终使您的软件包保持最新状态！**定期运行命令，或者至少在安装新软件包之前运行命令。即`pkg upgrade`  
- **始终进行备份！**如果没有备份，到时候出现问题，您可能无法恢复到原来的情况。请注意，软件开发人员应注意备份已使用的编译器、解释器或依赖项的 debfile，因为 Termux 不提供较旧的包版本，这些包都是随时随地更新！查看备份 Termux 以获取有关如何备份和恢复的信息。  
- **不要执行你不知道或者无法确定的事情！**根据从 Internet 上的内容仔细考虑您在终端中准备要执行的内容。  
- **仔细阅读打印到终端的所有内容！**了解信息性消息有助于解决可能发生的问题。（您可能需要一个翻译器）

## 是否有任何教程
我们无法维护有关 Linux 命令、shell 脚本和其他通用信息的整个文档，因此提供了指向外部资源的链接。  
我们强烈建议您避免阅读 YouTube 教程，尤其是与黑客攻击相关的教程。有很多针对没有经验的用户的点击诱饵。如果您决定遵循这些命令，请确保您完全理解执行的命令。还要始终检查下载文件的内容。如果下载的脚本的内容被混淆，那应该是关于潜在不安全内容的警报。不要抱怨 Termux 没有达到您的期望。  
注意！你应该在国内的视频平台或者互联网的博客寻找教程！（例如b站，其实你现在所访问的文档就是你所需要的教程）

### 命令和 Shell 脚本
发现命令并了解如何有效地使用 shell。
[https://linuxjourney.com/](https://linuxjourney.com/)
[http://mywiki.wooledge.org/BashGuide](http://mywiki.wooledge.org/BashGuide)
[https://www.tldp.org/LDP/Bash-Beginners-Guide/html/](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/)
这些链接可能对高级用户有用：
[https://wiki-dev.bash-hackers.org/](https://wiki-dev.bash-hackers.org/) Bash 内置命令示例的参考，请使用
[https://debian-handbook.info/Debian](https://debian-handbook.info/Debian) Debian 手册。
在遵循教程示例时，请记住 Termux 不是 Linux 发行版。某些命令可能不起作用，例如，由于不存在的路径以及 Linux 和 Android 在 Termux 发行版方面的其他差异。`ls /home`