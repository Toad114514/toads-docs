# Termux 命令
更新于 2024/10/20
## 包管理器
termux不仅支持`apt`，同时也在此基础上封装了`pkg`，其指令向下兼容`apt`。如下为`pkg`指令的使用方法：
```bash
pkg search <query> # 搜索包
pkg install <package> # 安装包
pkg uninstall <package> # 卸载包
pkg update # 更新源
pkg upgrade # 更新包
pkg list-all # 列出所有包
pkg list-installed # 列出已安装的包
pkg show <package> # 显示该包的详细信息
pkg files <package> # 显示该包的相关文件夹路径
```
建议使用 `pkg` 命令安装包，因为每次使用 `pkg` 安装包前，会自动执行`apt update`命令更新源，会比较方便
## deb包管理器
除开上述的`pkg`外，如果某个牢底给你发来了一个deb软件包文件或者有deb软件包文件，可以通过`dpkg`安装，这就是dpkg（Debian 特有的.deb软件包管理器）。以下为`dpkg`的使用方法：
```bash
dpkg -i <deb文件名> # 安装deb包
dpkg remove <软件包名字> # 卸载软件包
dpkg -l # 查看已安装的包
man dpkg # 查看 dpkg 包文档
```
## 路径
下面都是 termux 提供的特殊变量，用于脚本制作和开发等
```bash
echo $HOME
/data/data/com.termux/files/home
echo $PREFIX
/data/data/com.termux/files/usr
echo $TMPPREFIX
/data/data/com.termux/files/usr/tmp/zsh
```
## 查看端口
### Android 10 以下版本
Android 10 以下版本可通过`netstat`查看端口
```bash
netstat -an # 查看本机的所有端口
```
### Android 10 以上版本
由于未知原因，Android 10 以上版本无法使用`netstat -an`，唯一的解决办法则是`nmap`
```bash
pkg install nmap # 安装端口扫描工具
nmap 127.0.0.1 # 扫描本地端口
```
## ifconfig
输入 ifconfig 可以查看该设备的端口
```bash
ifconfig
```
## 终端文件管理
`termux` 提供了各种各样的文件管理命令，其实都属于是Linux自带的文件管理命令：
```bash
touch <文件名>  # 创建文件
mkdir <文件夹名>  # 创建文件夹
rm -rf <文件名/文件夹名>  # 彻底删除某个文件/某个文件夹
mv <文件名路径1> <文件名路径2> # 移动文件名/文件夹到<文件名路径2>
# mv 还可以用于修改文件名，用法为：
mv <原文件名> <新文件名>
cp <文件名路径> <文件名路径2> # 复制文件并粘贴到<文件名路径2>
cp -r <文件夹名路径> <文件夹名路径2> # 复制文件夹并粘贴到<文件夹名路径2>
chmod <权限> <文件名> # 修改某个文件的访问权限，具体使用方法请百度
```
## 参考
[Termux 高级终端安装使用配置教程 | 国光](https://www.sqlsec.com/2018/05/termux.html)