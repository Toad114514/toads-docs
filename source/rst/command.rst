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

表格
---------
reST 的表格包含有 **网格**/ **简单** 风格，这两个需要跟画字符画似的构建表格，但看的时候美观

另外还有 ``list-table`` 和 ``csv-table`` 风格，这两个则无需画字符画。一般情况下还是 ``list-table`` 用的比较多。本文档主要讲后两个风格。

``csv-table`` 使用 CSV 来构成表格。允许接受一个参数，用于作为表格的标题（可有可不有）。支持选项如下：

**widths**

    设置每一列的列宽，可以是 *auto* 或一整个数组。默认每列宽度一致
    
**width**

    设置一整个表格宽度

**header-rows**

    整数。表示接下来表格中的前几行作为表头。默认0

**header**

    一列 CSV 内容，用作表头，这会插入到 header-rows 所设定的行的前面

**stub-columns**

    整数。表示 CSV 数据中左几列为存根，默认0

**file**

    从本地读取CSV文件

**url**

    从网络读取CSV内容

**encoding**

    设置外部 csv 数据的字符编码，默认和当前文档相同

