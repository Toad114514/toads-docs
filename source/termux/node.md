# Node.js in termux
本页面创建于 2024/10/23
## 简介
Node.js 是一个开源和跨平台基于Chrome V8引擎的JavaScript运行环境。因 V8 引擎速度快、性能好，现在已经成为了制作快速高效网络应用的第一首选。
## 安装
```bash
# 此处安装的是 nodejs 的长期支持版本，稳定性好
pkg install nodejs-lts
node -v
```
## 简单示例
在vim中打开一个文件`vim hello.js`
```javascript
console.log('HelloWorld');
```
这一行是JavaScript的一个打印输出的一个命令，上述代码是在终端输出`HelloWorld`  
退出保存后，用nodejs运行该脚本
```bash
node hello.js
```
如果操作正确且`nodejs`环境完整时，终端输出的便是`HelloWorld`
## npm
nodejs 环境所对应的包管理器，开发者可以通过他从npm快速获取对应的库并直接使用。它具有极强的可配置性，可以支持各种用例。最常见的是，您使用它来发布、发现、安装和开发 node 程序。
### 安装
```bash
pkg install npm
# 查看 npm 版本
npm -v
```
### 公共注册表
在npm中，为了能快速获取对应的包信息、包文件等东西，便制作了公共注册表。这东西你大致理解为apt的源，但公共注册表是需要服务器根据npm的命令返回一串数据。  
默认安装后的npm预配置的是 [https://registry.npmjs.org/](https://registry.npmjs.org/) 的公共注册表，由于该公共注册表的服务器建立于国外，所以需要换成镜像公共注册表（换源）  
### 镜像公共注册表
```bash
npm config set registry <镜像公共注册表Url>
```
上述配置了公共注册表的Url设置，修改成国内特有的镜像站可以加快npm的安装速度。下面为镜像公共注册表Url列表，在下方列表中寻找一个Url并替换上方的`<镜像公共注册表Url>`：
- 淘宝：http://registry.npmmirror.com
- 阿里云：https://npm.aliyun.com
- 腾讯云：https://mirrors.cloud.tencent.com/npm/
- 华为云：https://mirrors.huaweicloud.com/repository/npm/
- 网易：https://mirrors.163.com/npm/
- 中国科学技术大学开源镜像站：http://mirrors.ustc.edu.cn/
- 清华大学开源镜像站：https://mirrors.tuna.tsinghua.edu.cn/
推荐使用前三个，前三个的镜像公共注册表内容较全。
### 基础命令
| 命令 | 说明 | 示例 |
| --- | --- | --- |
| `npm install` | 安装对应的包 | `npm install hexo-cli` |
| `npm search` | 根据关键词查找包 | `npm search hexo` |
| `npm ls` | 列出所有已安装的包 | `npm ls` |
## 参考
- [npm - npm 中文文档](https://nodejs.cn/npm/cli/v8/commands/npm/)
- [国内npm源镜像（npm加速下载） 指定npm镜像](https://blog.csdn.net/qq_43940789/article/details/131449710)