#Python排序算法

##定时器装饰器
> 简单定时器。
> PS：有时候装饰器碰到递归函数就尴尬了，此时我们简单在递归函数外面套一层函数然后再使用装饰器即可。可参考[网站](http://2hwp.com/2015/08/03/Python-decorator-recursion/)。
>
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
	        print (u'Function {} spend {} seconds.'.format(func.__name__, (end-start).seconds))
	        return f
	    return decorator

## 插入排序
>插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。  
>时间复杂度：![](http://7xrszf.com1.z0.glb.clouddn.com/QN2.gif)    
>算法步骤：  
1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。  
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）  
![插入排序](http://7xrszf.com1.z0.glb.clouddn.com/insert_into.gif)  
>代码如下：
>
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

## 选择排序 
>选择排序(Selection sort)也是一种简单直观的排序算法。  
>时间复杂度：![](http://7xrszf.com1.z0.glb.clouddn.com/QN2.gif)  
算法步骤：  
1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。  
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。  
3. 重复第二步，直到所有元素均排序完毕。  
![选择排序](http://7xrszf.com1.z0.glb.clouddn.com/selection_sort.gif)  
代码如下：
>
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

## 冒泡排序
> 冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。  
> 时间复杂度： ![](http://7xrszf.com1.z0.glb.clouddn.com/QN2.gif)  
算法步骤：  
1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。  
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。  
3. 针对所有的元素重复以上的步骤，除了最后一个。  
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。  
![冒泡排序](http://7xrszf.com1.z0.glb.clouddn.com/bubble_sort.gif)    
>代码如下：
>
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

## 归并排序
>归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。  
>时间复杂度： ![](http://7xrszf.com1.z0.glb.clouddn.com/QN.gif)  
>算法步骤：  
1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列。
2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置。
3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置。
4. 重复步骤3直到某一指针达到序列尾。
5. 将另一序列剩下的所有元素直接复制到合并序列尾。  
![归并排序](http://7xrszf.com1.z0.glb.clouddn.com/merge_sort.gif)  
>代码如下：  
>	
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
>	
	    def _merge_sort(array):
	        length = len(array)
	        if length <= 1:
	            return array
	        t = length / 2
	        left = _merge_sort(array[:t])
	        right = _merge_sort(array[t:])
	        return _merge(left, right)
>	
	    return _merge_sort(array)

## 快速排序
>快速排序是由东尼·霍尔所发展的一种排序算法。在平均状况下，排序 n 个项目要Ο(n log n)次比较。在最坏状况下则需要Ο(n2)次比较，但这种状况并不常见。事实上，快速排序通常明显比其他Ο(n log n) 算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。  
快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。   
>时间复杂度： ![](http://7xrszf.com1.z0.glb.clouddn.com/nlogn.gif)  
算法步骤：  
1. 从数列中挑出一个元素，称为 “基准”（pivot）（一般默认是第一个元素）。  
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。  
递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会退出，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。  
![快速排序](http://7xrszf.com1.z0.glb.clouddn.com/quick_sort.gif)  
>代码如下：
>
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
	    
## 希尔排序
>希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。  
希尔排序是基于插入排序的以下两点性质而提出改进方法的：插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率。但插入排序一般来说是低效的因为插入排序每次，只能将数据移动一位。希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。</br>	
>时间复杂度：![](http://7xrszf.com1.z0.glb.clouddn.com/nlog2n.gif)  
>算法步骤：  
1. 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1。  
2. 按增量序列个数k，对序列进行k 趟排序。  
3. 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。  
![希尔排序](http://7xrszf.com1.z0.glb.clouddn.com/shell_sort.png)  
>代码如下：  
>
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
>	
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

##堆排序
>堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。  
>时间复杂度：![](http://7xrszf.com1.z0.glb.clouddn.com/nlogn.gif)  
>算法步骤：
1. 创建一个堆H[0..n-1]。  
2. 把堆首（最大值）和堆尾互换。  
3. 把堆的尺寸缩小1，并调用shift_down(0),目的是把新的数组顶端数据调整到相应位置。  
4. 重复步骤2，直到堆的尺寸为1。  
![堆排序](http://7xrszf.com1.z0.glb.clouddn.com/heap_sort.gif)  
>代码如下：
>
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
>	
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
>	
	    length = len(array)
	    if length <= 1:
	        return array
	    t = []
	    while len(array) > 0:
	        array = _max_heap(array)
	        t.insert(0, array[0])
	        array = array[1:]
	    return t

## 基数排序
>基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。  
>时间复杂度：![](http://7xrszf.com1.z0.glb.clouddn.com/kn.gif)  
![基数排序](http://7xrszf.com1.z0.glb.clouddn.com/radix_sort.gif)  
>代码如下：
>
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
>	
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

## Summary
>###关于稳定性：  
稳定的排序算法：冒泡排序、插入排序、归并排序和基数排序  
不是稳定的排序算法：选择排序、快速排序、希尔排序、堆排序
>###单元测试
>下面是测试代码。
>
	import unittest
	class SortTestCase(unittest.TestCase):
	    array = [5, 1, 4, 7, 11, 54, 8, 2, 36, 47, 25, 69, 87, 15, 11, 26, 100, 9, 97, 12]
>	
	    def test_quick_sort(self):
	        self.assertEqual(quick_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])
>	
	    def test_bubble_sort(self):
	        self.assertEqual(bubble_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])
>	
	    def test_insert_sort(self):
	        self.assertEqual(insert_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])
>	
	    def test_select_sort(self):
	        self.assertEqual(select_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])
>	
	    def test_merge_sort(self):
	        self.assertEqual(merge_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])
>	
	    def test_shell_sort(self):
	        self.assertEqual(shell_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])
>	
	    def test_heap_sort(self):
	        self.assertEqual(heap_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])
>	
	    def test_radix_sort(self):
	        self.assertEqual(radix_sort(copy.copy(self.array)), [1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 15, 25, 26, 36, 47, 54, 69, 87, 97, 100])

>###运行时间
>下面截图是上面算法对10000随机整数进行排序所花费时间结果。
![](http://7xrszf.com1.z0.glb.clouddn.com/sort_timer.png)  
>总体来说还是快速排序效果最佳。（时间因素受作者代码质量影响。--！）