Sphinx 构建文档
===============
Sphinx 是一个基于 Python 的文档写作程序，经过不断完善，目前成为了大家可信赖的文档写作工具。通过 reST 文件来自动将其转化成文档。其有：

1. 插件扩展
#. 允许为文档选择主题
#. 支持生成 pdf、epub 等格式，而不仅限于 html

.. tip:: 虽然 Sphinx 写作使用 reST 语法，但你可以通过安装其他插件让 Sphinx 支持 Markdown。

安装
---------
使用下方命令安装

.. code-block:: sh

    $ apt install python make
    $ pip install -U sphinx

.. tip:: 你也可以在 Termux 中运行 Sphinx

安装好 Sphinx 后，你还需要安装 Sphinx 的常用主题和一些插件包，以下你可以根据个人喜好安装。

.. code-block:: sh

    # 自动构建插件（十分建议）
    $ pip install sphinx-autobuild
    # Read The Docs 官方提供的经典主题（建议安装）
    $ pip install sphinx_rtd_theme
    # Markdown 渲染插件
    $ pip install recommonmark sphinx_markdown_table

快速构建
---------

.. warning:: 本章节仅适用于已安装 sphinx-autobuild 的设备，如果需要，请先确保已安装 sphinx-autobuild。

按下方操作来初始化 Sphinx 根目录

.. code-block:: sh

    # 创建一个新文件夹
    # 文件夹名随意
    # 这里使用 toads
    $ mkdir toads
    # 进入到该目录
    $ cd toads
    # 启动 Sphinx 快速配置工具
    $ sphinx-quickstart

.. code-block:: sh

    # 接下来将会询问一连串的问题：
     欢迎使用 Sphinx 3.2.1 快速配置工具。
 ​
     Please enter values for the following settings (just press Enter to
     accept a default value, if one is given in brackets).
 ​
     Selected root path: .
 ​
     You have two options for placing the build directory for Sphinx output.
     Either, you use a directory "_build" within the root path, or you separate
     "source" and "build" directories within the root path.
     > 独立的源文件和构建目录（y/n） [n]: 
    # 此处询问是否创立独立的源文件夹和构建文件夹，根据个人喜好选择
    # 按下y后将独立文件夹，如下：
    # 所有源文件将存于 source 文件夹里
    # 构建的文件将存于 build 里
    # 我这里就选y了

.. code-block:: sh

    # 接下来询问本文档名、作者和文档版本
     The project name will occur in several places in the built documentation.
     > 项目名称: toad
     > 作者名称: toad114
     > 项目发行版本 []: v1.145

    # 接着询问项目语种，此处选择 zh-CN
     If the documents are to be written in a language other than English,
     you can select a language here by its language code. Sphinx will then
     translate text that it generates into that language.
      ​
     For a list of supported codes, see
     https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
     > 项目语种 [en]: zh_CN

完成之后，你将会得到一个 Sphinx 的目录了。结构如下所示：

.. code-block:: sh

    $ tree .
    # 两者目录结构如下：
    # 独立目录结构
    .
    ├── build
    ├── source
    ├── Makefile
    └── make.bat
        ├── _static
        ├── _templates
        ├── conf.py
        └── index.rst
    # 非独立目录结构
    .
    ├── _build
    ├── _static
    ├── _templates
    ├── Makefile
    ├── conf.py
    ├── index.rst
    └── make.bat

1. **build 或 _build** *(文件夹)* - 存放生成文件的输出目录
#. **_static** *(文件夹)* - 存放静态文件的目录（如图片）
#. **_templates** *(文件夹)* - 模板目录
#. **Makefile** *(文件)* - 使用 make 时将使用该文件里的命令来构建
#. **make.bat** *(文件)* - 上同，Windows 系统构建文档时使用该文件
#. **conf.py** *(文件)* - Sphinx 的配置文件
#. **index.rst** *(文件)* - 文件项目起始文件（一般情况下会在此处表示 toctree）

基础配置
------------
使用任意的文本编辑器来编辑 ``conf.py``，接着根据表格操作进行进一步配置。

.. list-table:: Sphinx conf.py 配置详细说明
    :header-rows: 1
    
    * - 变量名
      - 类型
      - 说明
    * - project
      - ``str``
      - 文档项目名
    * - copyright
      - ``str``
      - 版权声明
    * - author
      - ``str``
      - 作者名
    * - release
      - ``str``
      - 文档版本
    * - extensions
      - ``list``
      - Sphinx 插件启用列表，将插件名以 ``str`` 类型放入该列表中便可启用该插件。
    * - templates_path
      - ``list``
      - 模板目录
    * - exclude_patterns
      - ``list``
      - *未知*
    * - source_parsers
      - ``dict``
      - 指定 Sphinx 渲染某个文件类型时所使用的渲染器。``key`` 值传入文件后缀名（如 .rst、.md），``value`` 值传入对应的渲染器名称（如Recommonmark的渲染器为 *recommonmark.parser.CommonMarkParser* ）
    * - source_suffix
      - ``dict``
      - 指定 Sphinx 哪个文件后缀名对应哪种文本类型
    * - language
      - ``str``
      - Sphinx 的语言设定。这个新手就不要改了
    * - html_theme
      - ``str``
      - 指定渲染时使用的文档主题（已经安装好了 sphinx_rtd_theme 的可以改成 ``sphinx_rtd_theme`` ）
    * - html_theme_option
      - ``dict``
      - 设定主题特供的设置，修改该字典需要查询使用主题的对应文档
    * - html_static_path
      - ``list``
      - 设定静态目录输出位置。默认为 ``_static``
    * - html_search_language
      - ``str``
      - 设定文档搜索使用的语言。建议使用 ``zh`` 值

.. note:: 上述配置表格可能部分变量原先不存在，意味着该变量可有可没有。不会影响到实际 Sphinx 的文档生成

生成与预览
-------------
在 Sphinx 的根目录输入如下命令来构建文档：

.. code-block:: sh

    $ make html

构建完成后，你将会在 **build 或 _build** 文件夹中发现已生成的文件。

在 Sphinx 根目录中启动预览服务器（ **需要提前安装 sphinx-autobuild！！** ）

.. code-block:: sh

    $ sphinx-autobuild source build/html

.. warning:: Termux 运行该命令会出错！

执行后，便可通过浏览器访问 ``http://127.0.0.1:8000`` 查看构建后的文档。

toctree
--------------
在 ``index.rst`` 文件中，包含有 toctree 的内容，如下：

.. code-block:: rst

    .. toctree::
        :maxdepth: 2
        
        hello
        hello/index

该 toctree 命令仅 Sphinx 可用。用于渲染目录树，同时也会添加到左边的目录栏以展示。一般情况下，要想访问文档内的文档，都需要在 ``index.rst`` 中设置超链接。

添加一个文件到 toctree，只需要在其命令 content 中输入其文件的名字，无需输入后缀名。如果存放于文件夹内，例如想要将 ``./hello/index.md`` 文件添加到 toctree，那么只需输入 hello/index 即可（相对目录，以 ``index.rst`` 为起始）。