# Termux 的安装
本页面更新于 2024/10/20
## 简介
Termux是一个适用于 Android 的终端模拟器，其环境类似于 Linux 环境。 无需Root或设置即可使用。 Termux 会自动进行最小安装 - 使用 APT 包管理器即可获得其他软件包。
- **安全性** 使用来自 OpenSSH 的 ssh 客户端访问远程服务器。 Termux 将标准的软件包与仿真终端结合在一个完美的开源解决方案中。
- **功能丰富** 你可以在 bash、fish 或 zsh 和 nano、Emacs 或 Vim 之间选择。 通过 Grep 搜索您的短信收件箱。 使用 curl 访问 API 并使用 rsync 将联系人列表的备份存储在您的远程服务器上。
- **可玩性** 通过 Debian 和 Ubuntu GNU/Linux 等从已知的 APT 包管理器中安装您所想要的。 为什么不从安装 Git 并同步您的文件开始呢？
- **可探索** 你有没有坐在公共汽车上想知道 tar 到底接受了哪些参数？ Termux 中可用的软件包与 Mac 和 Linux 上的软件包相同 - 在您的手机上安装手册页并在一个会话中阅读它们， 同时在另一个会话中进行试验。
- **便携式 - 包括电池** 你能想象一个比 readline 驱动的 Python 控制台更强大、更优雅的袖珍计算器吗？ Perl、Python、Ruby 和 Node.js 的最新版本均可用。
- **准备扩大规模** 如果需要， 连接蓝牙键盘并将您的设备连接到外部显示器 - Termux 支持键盘快捷键并具有完整的鼠标支持。
- **可修补** 通过使用 Clang 编译 Go、Rust、Swift 或 C 文件进行开发， 并使用 CMake 和 pkg-config 构建您自己的项目。 如果遇到困难需要调试，lldb/GDB 和 strace 都可以使用。

引用 [https://termux.dev/cn/](https://termux.dev/cn/)
## 安装
文档
[termux 官网](https://termux.com/)
[Github 仓库](https://github.com/termux/termux-app)
以下为下载链接
[F-Droid](https://f-droid.org/packages/com.termux/)
[Google Play（需要外网）](https://play.google.com/store/apps/details?id=com.termux)
[Github Release](https://github.com/termux/termux-app/releases/)
目前 `Termux` 的最新版本为 ![GitHub Release](https://img.shields.io/github/v/release/termux/termux-app)，本文档大部分页面都基于 0.118.1，对于老版本无法保证其兼容性！  
通过上述方法下载apk安装再打开，等待几秒便可以开始使用了。
## 安装遇阻？
如果遇下图所示（图片借网上的，我没遇到这种情况）
![https://image.3001.net/images/20200418/15871943464391.png](https://image.3001.net/images/20200418/15871943464391.png)
上述问题只会在部分网络出现，翻墙使用魔法便可解决。
