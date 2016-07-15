# -*-coding: utf-8 -*-

import unittest
from .utils import timer


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


class SortTestCase(unittest.TestCase):
    array = [5, 1, 4, 7, 11, 54, 8, 2, 36, 47, 25, 69, 87, 15, 11, 26, 100, 9, 97, 12]

    def test_shell_sort(self):
        self.assertEqual(shell_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])


if __name__ == '__main__':
    unittest.main()