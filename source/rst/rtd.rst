Read The Docs 托管
=====================
当然了，Sphinx 帮助你构建了文档。但大家怎么去访问你的文档呢？是将生成的文件发到网盘上然后给大家访问？还是直接通过浏览器访问？当然是浏览器了，你只需要输地址就可以访问了。

Read The Docs 是一个网页托管项目，免费托管 Sphinx 的文档。将文档托管到 Read The Docs 后，所有人都可以便捷的通过浏览器访问你的文档。

- 2010年，Read The Docs项目由Eric Holscher、Bobby Grace 和Charles Leifer共同发起
- 2011年3月，Python 基金会给 Read The Docs 项目提供940块美金作为一年服务器费用，此后 Read The Docs 项目受到越来越多的开源社区和开发者关注
- 2017年11月，Linux Mint 宣布将所有文档转移到 Read the Docs

现在 Read The Docs 已经是一个成熟的 Sphinx 文档托管项目，被众多开源社区和开发者关注。这也是为什么要使用该开源项目来托管你的 Sphinx 文档了（免费+老牌，你要不要吧）

Read The Docs 网站：https://readthedocs.org

准备
-----------

1. 一个完整的 Sphinx 工作目录，没有的参考上一篇
#. 一个 GitHub 账号，不知道注册的百度，登不上就开魔法
#. Git 仓库管理程序，没有的终端输入

    .. code-block:: sh

        $ apt install git

仓库部分
----------------
登录已有的 GitHub 账号，并进入 https://github.com/new 创建新仓库。仓库名随意，但要记住后面要考。此处文档事例以 toads 为仓库名。

回到终端：

.. code-block:: sh

    # 切换到 Sphinx 根目录
    $ cd toad
    # 设置 .gitignore 不跟踪构建目录
    # 独立目录的输：
    $ echo "build/" > .gitignore
    # 非独立目录的输：
    $ echo "_build/" > .gitignore
    
    # 初始化 git 仓库
    $ git init
    # 提交第一份提交
    $ git add .
    $ git commit -m "commit"
    # 新建分支
    $ git branch -M main
    # 设置远程仓库
    # 远程仓库地址格式为 git@github.com:<Github账号名>/<仓库名>.git
    # 使用时将对应字段修改成自己的
    # 例如远程仓库名叫 toad，那么添加
    $ git remote add origin git@github.com:toad114514/toad.git
    # 推送
    $ git push -u origin main

托管
-----------
登录 https://readthedocs.org 并使用 Github 账号注册。

进入到 Dashboard 后，点击 ``import a project`` 导入项目，在里面输入项目名和代码库地址。项目名根据个人喜好输入，代码库填上面创建的代码库地址。（格式https://github.com/<Github名称>/<仓库名>。例如上面新建了 toad 仓库，那么就是输https://github.com/toad114514/toad）

之后每次你所创建的仓库只要有一个新提交，就会 **自动构建新版本**