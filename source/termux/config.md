# Termux 快速配置
本页面更新于2024/10/20，从博客文章转移过来并做了一点修改。  
本文章属于是给小白的快速配置教程，刚入手的小白可以根据本页面进行操作。  
要是你配置配不好那你termux还没用就成答辩了是不是
## 更新源
termux官方源在国外，运行`pkg update`时，由于更新源速度慢而导致红温，那不是得爆装备
所以接下来我们得换源：
### termux-change-repo（360度无死角推荐）
在终端输入`termux-change-repo`进入一个神奇的TUI界面：
```bash
┌────────termux-change-repo──────────────┐
│ Do you want to choose a mirror group or a 
  single mirror? Select with space.                   │
│ ┌─────────────────────────────────────┐ │
│ │(*) Main Repository  xxxxxxxxxxxxxxxxxxxxx    │ │
│ │                                                    │ │
│ │                                                    │ │
│ │                                                    │ │
│ └──────────────────────────────────┘ │
├─────────────────────────────────────┤
│           <  OK  >          <Cancel>                 │
└─────────────────────────────────────┘
```
差不多长这吊样
将光标移到`Main Repository`然后按下空格再回车计入到下一个界面
```bash
| mirrors.tuna.tsing | Mirror by Tsinghua University TUNA Assoc |
```
找到上面所示的选项，将光标移动到上面，点击空格选择，然后回车换源
就这样，你的`pkg`源就换好了
换源完成后，请第一时间更新包
```bash
pkg update
pkg upgrade -y
```
### 自动替换
输入下方命令自动替换为 TUNA 镜像源
```bash
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list
sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list
sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list
pkg update
```
孩子，在执行`pkg update`的时候，中间会卡住不动，那他🐴叫你是选择是否覆盖文件，记得回车！  
换源完了之后就包爽的了  
## 安装基础工具
termux自带的命令工具都很少，毕竟本身apk体积也是不大的，得自己安装
```bash
pkg update
pkg install vim curl wget git -y
```
## termux-setup-storage
我们的 termux 现在没有可以访问外部文件的权限，我们得搞的哇
```bash
termux-setup-storage
```
执行完该指令后，Android 6 以上的手机会弹出访问权限的请求，允许即可  
你要是点拒绝了，可以重新输入命令再来一次
## 设置软链接
手机是都是用`QQ`传文件
如果你已经授予了termux存储权限，那么会在 HOME 目录生成 storage 文件并生成诺干个软链接，都指向你手机存储卡的链接
为了方便传输，可以使用软链接指向到 QQ
```bash
# cd 到 Home 目录
cd ~
# 用QQ的使用下方命令
ln -s /data/data/com.termux/files/home/storage/shared/tencent/QQfile_recv QQ
# 用TIM的使用下方命令
ln -s /data/data/com.termux/files/home/storage/shared/tencent/TIMfile_recv TIM
```
这样将可以从 `Home 目录`直接访问 `QQ` 文件夹，提升文件操作效率
## termux.properties
termux的0.66及之后版本，termux可以通过`~/.termux/termux.properties`文件来配置termux的更多设置
### 自定义常用按键
```bash
vim ~/.termux/termux.properties
```
在文件最底部添加
```bash
extra-keys = [ \
 ['ESC','|','/','HOME','UP','END','PGUP','DEL'], \
 ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP'] \
]
```
这两行，就可以自定义常用按键了
以下为常用按键对照表
| CTRL | `特殊按键` |
|------------|----------|
| ALT        | `特殊按键` |
| FN         | `特殊按键` |
| ESC        | 退出     |
| TAB        | 表格键   |
| HOME       | 原位     |
| END        | 结尾     |
| PGUP       | 上翻页   |
| PGDN       | 下翻页   |
| INS        | 插入     |
| DEL        | 删除     |
| BKSP       | 退格     |
| UP         | 上       |
| DOWN       | 下       |
| LEFT       | 左       |
| RIGHT      | 右       |
| BACKSLASH  | 反斜杠   |
| QUOTE      | 双引号   |
| APOSTROPHE | 单引号   |
| F1~F12     | F1~F12键 |
上述标有`特殊按键`**最多只能在常用按键里出现一次**，否则报错
Toad114514个人设置的常用按键配置如下：
```bash
extra-keys = [['ESC','/','-','`','UP','QUOTE','APOSTROPHE','PGUP'], \
             ['TAB','CTRL','~','LEFT','DOWN','RIGHT','ENTER','PGDN']
```
## 启动问候语
默认的问候语对于初学者来讲有帮助
但随着你的termux经验越来越多，我们就会觉得这个玩意太low炮了
于是你得改！
```bash
vim $PERFIX/etc/motd
```
编辑问候语文件可直接修改启动语，改完后就可以长这样：
```bash
_____
|_   _|__ _ __ _ __ ___  _   ___  __
  | |/ _ \ '__| '_ ` _ \| | | \ \/ /
  | |  __/ |  | | | | | | |_| |>  <
  |_|\___|_|  |_| |_| |_|\__,_/_/\_\

Termux v0.118.1 /localhost
Welcome,zhanghao not penis!!!!!!!!
╭─u0_a442@localhost ~
╰─➤
```
`zhanghao not penis`是张浩没只因的意思，另外你可以把上面的 Termux 复制过来放到你的启动语里面
## Root
孩子们，这鬼东西无需root也能玩出花样  
但还是能用的
### Rootless
可以安装 `proot` 模拟 linux 文件系统布局模拟
```bash
pkg install proot
termux-chroot
```
这鬼东西可以模拟root，但不是真的root，输入`exit`退出
### Rooted
```bash
pkg install tsu
```
安装`tsu`，这是termux的专属`su`  
输入`tsu`可以为termux授予root权限  
输入`exit`回到普通用户  
**如果操作不慎很可能会让你的手机变成板砖只能盖房子，谨慎使用**
## 备份和恢复
有些low炮搞termux怕自己一不小心搞坏了是吧，也是直接出个备份教程    
确保获取了外部存储权限，没有就
```bash
termux-setup-storage
```
### 备份
```bash
cd /data/data/com.termux/files # 转到termux根目录
tar -zcf /sdcard/termux-backup.tar.gz home usr # 压缩成 tar.gz 文件做备份
```
备份就完成了  

#### 千万不要
**千万不要将备份文件放置在 termux 的私有目录里！当通过设置清除数据输入或者卸载 termux 时，这些私有目录内的文件也会删掉（等同于你把备份文件放C盘但你要重装一个道理）**  
这些私有目录看上去类似如下的目录：
```bash
/data/data/com.termux 
/sdcard/Android/data/com.termux
/storage/XXXX-XXXX/Android/data/com.termux
${HOME}/storage/external-1
```
请不要把备份文件放在这些地方，**远离它们**！

### 恢复
这里假设您已将 Termux 之前备份的 home 和 usr 目录备份到同一个备份文件中。请注意，在此过程中所有文件都将被覆盖现有的配置：  
首先确保获取了外部存储权限，没有就`termux-setup-storage`
```bash
cd /data/data/com.termux/files # 转到termux根目录
tar -zxf /sdcard/termux-backup.tar.gz --recursive-unlink --preserve-permissions # 解压备份文件并覆盖之前的文件，同时删除备份
```
这样就恢复完成了
## pkg 仓库源
termux开发者提供了三个仓库源，可通过 `pkg` 添加
### x11-repo
如果你想要在termux上面安装桌面环境`(例如xfce)`，则执行下面代码添加x11仓库源
```bash
pkg install x11-repo
```
### root-repo
如果你想在termux上面搞点root才能做到的东西，可以执行下面代码添加root仓库源
```bash
pkg install root-repo
```
### tur-repo
全称 `Termux User Repository`，都是别人封装上传的东西，`code-server`也在该源里面  
如果你想在termux上面搞点其他的东西（例如安装`code-server`），可以执行下面代码添加tur仓库源
```bash
pkg install tur-repo
```
## 自启动
### etc目录
进入`$PREFIX/etc`目录，输入
```bash
vim termux-login.sh
```
这个文件是每次 Termux 启动时自动执行的
### home目录
来到`$HOME`目录，输入
```bash
vim .bashrc
```
这个也是termux会使用的自启动文件，每次登陆时都会执行它
## 短命令
如果发现某些情况下容易掉服务，可以参考本节  
这里使用短命令形式`alias`，可做到挂掉时快速通过短命令启动
```bash
alias <短命令名字>=<具体执行的命令>
```
定义短命令后，之后便可输入该短命令名字就可以运行其对应的长命令  
可以与上面的自启动一起使用
## 挂载
termux 可通过自带文件夹进行挂载并允许其他应用访问 `$HOME` 目录  
以mt管理器为例：
 1. 打开mt管理器
 2. 点击菜单 -> 右上角三个点 -> 添加本地存储
 3. 在弹出的文件夹管理器中，点击右上角菜单 -> Termux -> 选择
 4. termux 的文件夹便挂载在了mt管理器里，mt管理器可随意访问termux的`$HOME`目录
**注意：由于 Android 限制，在设置挂载存储前和访问挂载存储时，必须在后台启动termux并挂在后台**
## 配置完成
我们的termux配置完成了，是不是非常不错？  
接下来就可以开始我们的其他配置了！  
是不是特别激动！  
你可以从右边的目录栏中选择一项去导航到你需要的！或者继续深入配置！
## 参考
[Termux 高级终端安装使用配置教程 | 国光](https://www.sqlsec.com/2018/05/termux.html)