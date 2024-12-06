=============
reST 常用命令
=============
接下来是一些 reST 的常用命令：

命令语法
-------------
任何满足：

.. code-block::

    .. <type>:: <block>

例如：

.. code-block:: rst

    .. image:: example.jpg

形式的都会尝试视为命令解析。

基本的命令语法为如下：

.. code-block:: rst

    .. {{ 指令名 }}:: {{ argument }}
        :{{ field name }}: {{ field value }}

        {{ content }}

紧跟着指令名之后的内容为指令的 argument， 在指令后一行，添加缩进并以字段列表的形式输入的为指令的 options， 在 options 后空一行，并相对指令缩进一次的输入，是指令的 content

图像
--------
图片可以使用 ``image`` 命令来插入图片。其接受一个参数：图像Url。如果使用相对路径，则起点为本文档。

image 可允许接受0或者多个选项，如下：

**height**

    图像高度，允许使用 reST 支持的长度单位。

**width**

    图像宽度，同上。

**scale**
    
    设置图像缩放，允许百分比

**align**

    设置对齐方式。可用 *top,middle,bottom,left,center,right*

**target**

     设置超链接靶标。需要传入一个超链接靶标，设置后会让图片可点击，并自动转到靶标链接

.. code-block:: rst
    
    .. image:: _img/example.jpeg
        :height: 149
        :width: 270
        :scale: 70%
        :align: left
        :target: https://www.bilibili.com

.. image:: ../_img/example.jpeg
    :height: 149
    :width: 270
    :scale: 70%
    :align: left
    :target: https://www.bilibili.com