.. _Selection Sort:

选择排序
========

选择排序(Selection sort)也是一种简单直观的排序算法。

**步骤**

    1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
    2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3. 重复第二步，直到所有元素均排序完毕。

**时间复杂度** ：:math:`O(N^{2})`

.. image:: ../_static/selection_sort.gif

.. literalinclude:: ../src/selection.py
    :language: python