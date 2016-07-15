# -*-coding: utf-8 -*-

import unittest
from .utils import timer


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


class SortTestCase(unittest.TestCase):
    array = [5, 1, 4, 7, 11, 54, 8, 2, 36, 47, 25, 69, 87, 15, 11, 26, 100, 9, 97, 12]

    def test_heap_sort(self):
        self.assertEqual(heap_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])


if __name__ == '__main__':
    unittest.main()