# coding: utf-8


import copy
import random
import datetime
import functools


"""
装饰器碰到递归函数
http://2hwp.com/2015/08/03/Python-decorator-recursion/
"""

"""
斐波拉切
def fib(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b

print [fib(i) for i in 10]

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print [fib(i) for i in 10]

def fib(n):
    a, b = 1, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

print list(fib(10))
"""

def timer(func):
    """
    计时器
    @param {function} func
    """
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = datetime.datetime.now()
        f = func(*args, **kwargs)
        end = datetime.datetime.now()
        print (u'Function {} spend {} seconds.'.format(func.__name__, (end-start).total_seconds()))
        return f
    return decorator


@timer
def quick_sort(array):
    """
    快速排序
    @param {list} array
    @return {list}
    """
    def _quick_sort(array):
        length = len(array)
        if length <= 1:
            return array
        key = array[0]  # 默认选取第一个作为关键数
        return _quick_sort([i for i in array[1:] if i < key]) + [key] + _quick_sort([i for i in array[1:] if i >= key])
    return _quick_sort(array)


@timer
def bubble_sort(array):
    """
    冒泡排序
    @param {list} array
    @return {list}
    """
    length = len(array)
    if length <= 1:
        return array
    for i in range(1, length):
        j = i
        while array[j] < array[j-1] and j >= 1:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array

@timer
def insert_sort(array):
    """
    插入排序
    @param {list} array
    @return {list}
    """
    length = len(array)
    if length <= 1:
        return array
    for i in range(1, length):
        j = i
        t = array[i]
        while t < array[j-1] and j > 0:
            array[j] = array[j-1]
            j -= 1
        array[j] = t
    return array


@timer
def select_sort(array):
    """
    选择排序
    @param {list} array
    @return {list}
    """
    length = len(array)
    if length <= 1:
        return array
    for i in range(0, length):
        minimum = i
        for j in range(i+1, length):
            if array[j] < array[minimum]:
                minimum = j
        if minimum > i:
            array[i], array[minimum] = array[minimum], array[i]
    return array


@timer
def merge_sort(array):
    """
    归并排序
    @param {list} array
    @return {list}
    """
    def _merge(left, right):
        """
        归并
        """
        t = []
        for i in left:
            while len(right) > 0 and i > right[0]:
                t.append(right[0])
                del right[0]
            t.append(i)
        if len(right) > 0:
            t.extend(right)
        return t

    def _merge_sort(array):
        length = len(array)
        if length <= 1:
            return array
        t = length / 2
        left = _merge_sort(array[:t])
        right = _merge_sort(array[t:])
        return _merge(left, right)

    return _merge_sort(array)


@timer
def shell_sort(array):
    """
    希尔排序(分组插入排序)
    """
    def _selection_sort(_array):
        _length = len(_array)
        if _length <= 1:
            return _array
        for i in range(0, _length):
            minimum = i
            for j in range(i+1, _length):
                if _array[j] < _array[minimum]:
                    minimum = j
            if minimum > i:
                _array[i], _array[minimum] = _array[minimum], _array[i]
        return _array

    length = len(array)
    if length <= 1:
        return array
    gap = length / 2
    while gap >= 1:
        t = []
        for x in range(gap):
            t += _selection_sort([array[x] for x in range(x, length, gap)])
        array = t
        gap = gap / 2
    return array


@timer
def heap_sort(array):
    """
    堆排序
    """
    def _max_heap(array):
        """
        构造最大最大堆
        """
        def _parent_index(_index):
            """
            获取父节点位置索引
            """
            return (_index - 1) / 2

        max_heap = []
        for index, value in enumerate(array):
            max_heap.append(value)
            if index >= 1:
                i = index
                while i > 0:
                    parent_index = _parent_index(i)
                    if i > parent_index and max_heap[i] > max_heap[parent_index]:
                        max_heap[i], max_heap[parent_index] = max_heap[parent_index], max_heap[i]
                    i = parent_index
        return max_heap

    length = len(array)
    if length <= 1:
        return array
    t = []
    while len(array) > 0:
        array = _max_heap(array)
        t.insert(0, array[0])
        array = array[1:]
    return t


@timer
def radix_sort(array):
    """
    基数排序，默认桶[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    def _get_digit(num, digit):
        """
        获取整数的digit位数
        """
        return num % (10**digit) / (10**(digit-1))

    length = len(array)
    if length <= 1:
        return array
    max_length = len(str(max(array)))  # 获取最大数的位数
    bucket = [[] for i in range(10)]
    for digit in range(1, max_length+1):
        for value in array:
            bucket[_get_digit(value, digit)].append(value)
        t = []
        [t.extend(x) for x in bucket]
        array = t
        bucket = [[] for i in range(10)]
    return array


import unittest


class SortTestCase(unittest.TestCase):
    array = [5, 1, 4, 7, 11, 54, 8, 2, 36, 47, 25, 69, 87, 15, 11, 26, 100, 9, 97, 12]

    def test_quick_sort(self):
        self.assertEqual(quick_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])

    def test_insert_sort(self):
        self.assertEqual(insert_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])

    def test_select_sort(self):
        self.assertEqual(select_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])

    def test_merge_sort(self):
        self.assertEqual(merge_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])

    def test_shell_sort(self):
        self.assertEqual(shell_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])

    def test_heap_sort(self):
        self.assertEqual(heap_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])

    def test_radix_sort(self):
        self.assertEqual(radix_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])


if __name__ == '__main__':
    # array = [5, 1, 4, 7, 11, 54, 8, 2, 36, 47, 25, 69, 87, 15, 11, 26, 100, 9, 97, 12]
    # array = [random.randint(1, 100000) for i in range(10000)]
    # quick_sort(copy.copy(array))
    # bubble_sort(copy.copy(array))
    # insert_sort(copy.copy(array))
    # select_sort(copy.copy(array))
    # merge_sort(copy.copy(array))
    # shell_sort(copy.copy(array))
    # heap_sort(copy.copy(array))
    # radix_sort(copy.copy(array))
    unittest.main()
