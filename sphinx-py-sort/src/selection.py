# -*-coding: utf-8 -*-

import unittest
from .utils import timer


@timer
def selection_sort(array):
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


class SortTestCase(unittest.TestCase):
    array = [5, 1, 4, 7, 11, 54, 8, 2, 36, 47, 25, 69, 87, 15, 11, 26, 100, 9, 97, 12]

    def test_selection_sort(self):
        self.assertEqual(selection_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])


if __name__ == '__main__':
    unittest.main()