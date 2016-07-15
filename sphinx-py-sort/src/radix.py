# -*-coding: utf-8 -*-

import unittest
from .utils import timer


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


class SortTestCase(unittest.TestCase):
    array = [5, 1, 4, 7, 11, 54, 8, 2, 36, 47, 25, 69, 87, 15, 11, 26, 100, 9, 97, 12]

    def test_radix_sort(self):
        self.assertEqual(radix_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])


if __name__ == '__main__':
    unittest.main()