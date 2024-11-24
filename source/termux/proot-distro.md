# Proot-Distro
一个由官方提供的proot容器管理脚本，供你在termux中运行各种linux发行版
```bash
# 安装命令
pkg install proot-distro
```
## 命令
```bash
# 列出所有发行版本
# 使用下面任何一个命令获取发行版本列表
# 同时也需要在此处获取 <alias>
proot-distro list
proot-distro ls
pd list
pd ls

# 安装某个发行版本
proot-distro install <alias>
proot-distro i <alias>
pd install <alias>
pd i <alias>

# 启动并进入proot容器
proot-distro login <alias>
proot-distro sh <alias>
pd login <alias>
pd sh <alias>

# 删除容器
# 谨慎使用该命令！
proot-distro remove <alias>
proot-distro rm <alias>
pd remove <alias>
pd rm <alias>
```
## 初始操作
容器安装后需要你进行初始操作，见下篇容器初始化  
如需在容器里安装桌面环境，见 X11 in termux