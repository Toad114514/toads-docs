==========
Toads-docs
==========
一个初二佬的Read The Docs文档，主要写一些部分东西的文档完善与整合，作为个人/公共维护和查询的文档库来使用。本文档库目前会持续更新。

值得一提的是，本文档的 Sphinx 本地环境其实是在 `Termux 0.118.1` 的情况下实现的（宿环境为Oppo A5战神机，Android8.1(ColorOS 5.0)。这又给了Termux可折腾的空间

本文档提供了EPUB格式的下载（在右下角的Read The Docs图标）

从提交 ``7b332743`` 后，之后的文档书写将采用 reST 语法书写文档，且之前书写的 Markdown 文档也将逐渐使用 reST 语法

.. toctree::
   :maxdepth: 2
   :caption: toads-docs-main:
   
   welcome
   toad114
   xianbei

.. toctree::
   :maxdepth: 2  
   :caption: repos:
   
   repos/xianbei
   repos/staxle

.. toctree::
   :maxdepth: 2  
   :caption: myfriend:
   
   myfriend/index
   myfriend/zhanghao
   myfriend/lizheting

.. toctree::
   :maxdepth: 2
   :caption: rst:
   
   rst/index
   rst/basic
   rst/command
   rst/sphinx

.. toctree::
   :maxdepth: 2
   :caption: termux:
   
   termux/index
   termux/install
   termux/start
   termux/basic
   termux/command
   termux/config
   termux/oh-my-zsh
   termux/vim
   termux/emacs
   termux/c
   termux/python
   termux/node
   termux/proot-distro
   termux/x11

Toads-docs 索引页面
===============
上面为本文档的目录，可以点击其中一个查看。
刚访问的老野们，建议先访问Welcome页面再去查看其他文档
下面为本文档的索引

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`