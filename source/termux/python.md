# Python in termux
本文档创建于 2024/10/22  
## 简介
一个解释型，面向对象、动态数据类型的高级程序设计语言。目前主要多使用于AI、网络爬虫和网络安全领域（黑客常用）  
目前 Termux 所封装的 Python 最新版本为 `3.11.10`
## 注意
目前 Python 总共有两个版本，Python2 和 Python3。Python3 对于以前的 Python2 是一个很大的升级，为了防止带入过多的累赘，开发本版本时并未考虑向下兼容 Python2。且**Python2 已经在 2020/1/1 停止了更新！**所以在寻找教程时，请注意教程所使用的 Python 版本！默认执行下方的命令将安装`Python3`
## 安装
```bash
pkg install python
```
正常像这样子安装将安装 Python3、pip和clang！可以输入下方命令查看每一个包的版本号
```bash
python --version
clang -v
pip --version
```
## 示例
用vim新建一个hello.py`vim hello.py`，接着输入
```python
print("hello world!")
```
保存文件之后，输入
```bash
python hello.py
```
就可以看到一个`hello world!`显示在终端上
## pip
Python 可以自由扩展各种各样的库，例如`numpy`库可以在上面运算复杂的数学题，`bs4`+`requests`库可以进行网络爬虫，`PyQt5`库可以构建一个GUI应用。  
那么这些库从哪里搞呢，怎么去安装他们呢？于是便有了 **Python 标准包管理器 - pip**。他是一个用于安装以及管理 Python 所安装的库，使开发者可以快速获取并使用这些库。  
在上面的 Python 安装过程中，早已经安装好了`pip`。以下是`pip`常用的命令：
| 命令 | 说明 | 示例 | 可选参数 |
| --- | --- | --- | --- |
| `pip install` | 安装一个指定的包 | `pip install requests` | `--user`: 安装到用户目录 `--upgrade`: 升级包 `--no-cache-dir`: 不使用缓存 `--pre`: 安装预发行版本 `-U`: 升级包，一般情况下常用该参数升级包 `-r <文件名>`: 从文件中安装依赖，例如`pip install -r requirements.txt` |
| `pip uninstall` | 卸载一个指定的包 | `pip uninstall requests` | `-y`: 自动确认卸载。不带该参数时将询问你是否卸载该包 |
| `pip list` | 列出所有已安装的包 | `pip list` | `--outdated`: 列出已过时的包 |
| `pip search` | 从 pypi 搜索包 | `pip search requests` | `--index`: 指定索引Url |
## pip 换源
原先所使用的 pypi 官方仓库源因为是在国外，所以在中国大陆中安装速度会很慢。所以需要切换到国内的pypi镜像源安装速度就会快很多了。  
如下命令请选择其中一个去设置默认的 pypi 镜像源
```bash
# 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里云
pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
```
## 更新 pip
```bash
python -m pip install --upgrade pip
```
## 升级后无法执行pip
可能修改了原先的pip命令文件，可以执行下方命令查看 pip
```bash
ls /data/data/com.termux/files/usr/bin|grep pip
pip
pip3
pip3.11
```
这里上述的`pip`、`pip3`和`pip3.11`都是一个pip命令。可以执行如下代码查看他们的版本
```bash
pip --version
pip3 --version
pip3.11 --version
```
## IPython
python的增强交互式shell，支持自动补全变量、自动缩进和shell命令执行，同时内置各种功能和有用的函数
```bash
pip install ipython
# 查看版本
ipython -V
```
## jupyter notebook
与ipython共用一个内核的强大Web交互式程序，在浏览器上面就能操作
```bash
# 安装依赖
termux-chroot && pkg install clang && pip install jupyter && exit
# 安装 jupyterlab
pip install jupyterlab
# 查看版本
jupyter --version
# 启动
jupyter notebook
```
启动后将打印出来的日志中取Url并粘贴到浏览器访问便可以使用了  
按下`Ctrl+C`退出
## 参考
- [Termux 高级终端安装使用配置教程 | 国光](https://www.sqlsec.com/2018/05/termux.html)
- [Python 基础教程 | 菜鸟教程](https://www.runoob.com/python/python-tutorial.html)
- [【Pip】初识 Pip：Python 包管理的基本命令详解](https://blog.csdn.net/Stromboli/article/details/143116950)