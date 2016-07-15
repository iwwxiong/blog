.. _Radix Sort:

基数排序
========

基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。

**时间复杂度** ：:math:`O(k * n)`

.. image:: ../_static/radix_sort.gif

.. literalinclude:: ../src/radix.py
    :language: python