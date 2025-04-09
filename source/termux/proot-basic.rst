Termux proot 初始化
=======================
帮助你初始化一个正常的 proot

选择发行版
-------------------
目前本文档提供了下方发行版的初始教程

.. list-table::
    :header-rows: 1
    
    * - 发行版名
      - Alias
      - 安装命令
      - 特性
    * - Ubuntu 24.04
      - ``ubuntu``
      - ``pd i ubuntu``
      - Debian 系发行版，适合小白，apt包管理器
    * - Debian 12 Bookworm
      - ``debian``
      - ``pd i debian``
      - 也算是比较大众的发行版，同上
    * - ArchLinux Arm
      - ``archlinux``
      - ``pd i archlinux``
      - 上手难但软件包更新快、安全的发行版，pacman包管理器

以后会添加更多发行版的初始教程

安装
-------------
从头开始安装我们的发行版

.. code-block:: sh
    
    pkg install proot-distro

安装 Proot-distro 后便开始安装 发行版

Debian 12 Bookworm
~~~~~~~~~~~
输入如下命令将在Termux中安装Debian 12

.. code-block:: sh

    pd i debian

等待初始完成即可

Ubuntu 24.04
~~~~~~~~~~~
输入如下命令将在Termux中安装Ubuntu 24.04

.. code-block:: sh

    pd i ubuntu

等待初始完成即可

ArchLinux Arm
~~~~~~~~~~~
输入如下命令将在Termux中安装ArchLinux Arm

.. code-block:: sh

    pd i archlinux

等待初始完成即可

登录发行版
-----------------------
以后登录也是用这些命令

Debian 12 Bookworm
~~~~~~~~~~~~~~~~
.. code-block:: sh
    
    pd sh debian

Ubuntu 24.04
~~~~~~~~~~~~~~~~
.. code-block:: sh
    
    pd sh ubuntu

ArchLinux Arm
~~~~~~~~~~~~~~~~
.. code-block:: sh
    
    pd sh archlinux
    
初始化语言
-------------------
初始化你的语言到 zh_CN

所有发行版通用
~~~~~~~~~~~~~~~~~

.. code-block:: sh
    
    vim /etc/locale.gen

在里面找到 ``zh_CN.UTF-8``，将注释去掉（去掉前面的``#``），完成后退出保存

接着生成 locale.gen

.. code-block:: sh
    
    locale.gen

最后打开 ``/etc/environment`` 文件，找到 ``en_US.UTF8`` 改成 ``zh_US.UTF8``，保存

语言部分设置完成，下次登录时将变成中文

时区设置
-------------------

Debian 12 Bookworm & Ubuntu 24.04
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh
    
    dpkg-configure tzdata
    
接着依次输入 ``Asia`` 对应序号和 ``Shanghai`` 对应序号，修改时区完成

ArchLinux Arm
~~~~~~~~~~~~~~~~~~~~~~~~~~~
一条命令

.. code-block:: sh
    
    sudo ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime

