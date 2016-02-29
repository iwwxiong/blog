## Python操作Excel模块xlrd，xlwt和xlutils
> `xlrd, xlwt, xlutils`可以工作在任何平台。这也就意味着你我们可以在Linux下读取，写入Excel文件。
### xlrd--Python读取Excel模块
> `xlrd`是Python读取Excel的第三方模块，`xlrd`打开Excel是只读操作，不能对其进行编辑（put_cell方法只是临时更改内容，不能写入到Excel中）。
> 打开Excel：
>
	import xlrd
	book = xlrd.open_workbook('/tmp/tmp.xls')  # 打开Excel
> Sheet操作：
>
	sheets = book.sheets() # 返回所有xlrd.sheet.Sheet对象列表
	# 获取单个sheet的两种方法
	sheet = book.sheet_by_name('Sheet1')  # 根据索引
	sheet = book.sheet_by_index(0)        # 根据名称
> 方法介绍：
>
	sheet.nrows # 返回行总数
	sheet.ncols # 返回列总数
	sheet.row_values(index)  # 以列表形式返回第几行数据
	sheet.col_values(index)  # 以列表形式返回第几列数据
>
	# 通过索引读取数据(第几行，第几列)：
	sheet.cell(row_index, col_index).value
>
	# 循环打印出所有数据：
	for index in range(sheet.nrows):
		print sheet.row_values(index)
> 以上都是一些常见操作，其它额外具体使用请参考[官网](http://www.python-excel.org/)

### xlwt--Python写入Excel模块
> `xlwt`是Python的写入Excel第三方模块。  
> 在写入Excel表格之前，你必须初始化workbook对象，然后添加一个workbook对象。比如：
>
	import xlwt
	book = xlwt.Workbook()
	sheet = book.add_sheet('Sheet1')
> 初始化后，我们就开始写入基础数据了。例如Excel第一行我们一般定义标题内容：
>
	sheet.write(0, 0, 'username')
	sheet.write(0, 1, 'age')
	sheet.write(0, 2, 'sex')
> 然后我们就可以批量写入数据了，比如:
>
	data = [('wwx', u'男', 27), ('Teddy', u'男', 20), ('Lucy', u'女', 23)]
	i = 1
	for d in data:
		sheet.write(i, 0, d[0])
		sheet.write(i, 1, d[1])
		sheet.write(i, 2, d[2])
		i += 1
> 当基础数据写完后我们就可以保存文件了：
>
	book.save('/tmp/tmp.xls')  # 注意Linux上权限问题
> 当然`xlwt`不止这些基础的功能，还提供设置字体，Excel表格样式等高级功能，这里就不一一介绍了。具体可参考[官网](http://www.python-excel.org/)

### xlutils--Python操作Excel增值功能
> 当我们存在如下需求的时候：针对已有的Excel进行部分内容修改，或者新增部分栏位。这样的话我们使用`xlrd`进行读取所有内容，更改后再次用`xlwt`模块写入新的Excel。操作起来比较麻烦。不过，还有一个xlutils（依赖于xlrd和xlwt）提供复制excel文件内容和修改文件的功能。其实际也只是在xlrd.Book和xlwt.Workbook之间建立了一个管道而已。使用起来也比较简单：
>
	import xlrd
	from xlutils.copy import copy
	rbook = xlrd.open_workbook('/home/1.xls')
>
	#通过sheet_by_index()获取的sheet没有write()方法
	rsheet = rbook.sheet_by_index(0)
>
	#拷贝读取的对象
	wbook = copy(rbook)
>
	#通过索引获取wbook sheet
	wsheet.get_sheet(0)
>
	#这样我们就可以仅仅更改其中部分内容
	wsheet.write(0, 1, 28)
	wbook.save('/home/1.xls')  # 注意Linux上权限问题
> 这样我们就算完成了一次部分栏位更改了。**参考以上的内容我们就可以实现基本的Excel的读写功能了，能满足大部分的需求。**