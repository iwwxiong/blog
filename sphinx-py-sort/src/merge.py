# -*-coding: utf-8 -*-

import unittest
from .utils import timer


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


class SortTestCase(unittest.TestCase):
    array = [5, 1, 4, 7, 11, 54, 8, 2, 36, 47, 25, 69, 87, 15, 11, 26, 100, 9, 97, 12]

    def test_merge_sort(self):
        self.assertEqual(merge_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])


if __name__ == '__main__':
    unittest.main()