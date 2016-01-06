# Python 正则学习笔记&实战 (2015/10/9) 

> `Python`正则默认使用内置模块`re`，这个模块提供了与`Perl`相似的正则表达式匹配操作。`Unicode`字符串也同样适用。
>   
> `Python`正则默认使用反斜杠`"\"`来表示特殊形式或作用转义字符，但是这样写起来是相当的麻烦，所以`Python`特别设计了原始字符串。在字符串前面使用`'r'`前缀。如`r"\n"`表示两个字符`"\"`和`"n"`，而不是换行符了。`Python`中写正则也推荐使用这种形式。


----------

## re模块几种函数介绍

### re.search和re.match

> `re.search`和`re.match`是`Python`提供了两种的不同的原始操作。match是从字符串的起点开始做匹配，而search是从字符串做任意匹配。search和match在字符串中查找，是否能匹配正则表达式。返回`_sre.SRE_Match`对象，如果不能匹配返回`None`。
> 
> > *注意: 当正则表达式是`'^'`开头的时候，match和search机制是相同的。* 

> 案例：
>
	>>> import re
	>>> re.search(r"wwx", "super wwxiong")
	<_sre.SRE_Match object; span=(6, 9), match='wwx'>
	>>> re.match(r"wwx", "super wwxiong")
	>>> 
	

### re.complie(pattern, string, flags=0)

> 编译正则表达式，返回`RegexObject`对象，然后可以通过该对象直接调用match和search等方法操作。
>
	>>> import re
	>>> r = re.complie(r'wwx')
	>>> r.search('super wwxiong')
	<_sre.SRE_Match object; span=(6, 9), match='wwx'>

### re.split(pattern, string, maxsplit=0)

> 通过正则表达式将字符串分离。如果用括号将正则表达式括起来，那么匹配的字符串也会被列入到list中返回。`maxsplit`是分离的次数，`maxsplit=1`分离一次，默认为0，不限制次数。
>
	>>> re.split(r'\W+', 'wwxiong, wwxiong, wwxiong')
	['wwxiong', 'wwxiong', 'wwxiong']
> 如果字符串不能匹配， 将会返回整个字符串的list
>
	>>> re.split(r'\d+', 'wwxiong')
	['wwxiong']

### re.finditer(pattern, string, flags=0)

> 找到所有匹配的子串，并把他们作为一个迭代器`iterator`返回。这个匹配默认是从左到右有序的返回。如果无匹配，返回空列表。
>
	>>> item = re.finditer(r'\d+', "12w34w56x78i01ong")
	>>> for i in item:
			print match.group()
	12
	34
	56
	78
	01

### re.findall(pattern, string, flags=0)

> 找到所有匹配的子串，并把他们作为一个列表返回。这个匹配是从做到有匹配。如果无匹配，返回空列表。
> >*ps这个方法在爬虫中经常使用到。*  

>`re.findall`针对pattern带括号`()`匹配的内容为一组。
> >
	>>> a = 'http://www.wwxiong.com/#1a/#2b'
	>>> r = re.compile(r'#\d{1}\w{1}')  #不带括号
	>>> r.findall(a)
	['#1a', '#2d']
	>>> r = re.compile(r'#(\d{1})(\w{2})')  #带括号
	>>> r.findlal(a)
	[('1', 'a'), ('2', 'd')]
> 
> 下面是一个爬取[36氪](http://36kr.com/ "36kr")的首页文章列表`title`的简单案例。
>
    >>> res = requests.get('http://36kr.com/')
    >>> content = res.content
    >>> r = re.compile(r'.?<a.?class="title.*?target="_blank">(.*?)<\/a>.?<div.?class="author"', re.DOTALL)
    >>> title = r.findall(content)
    >>> print len(title)
    >>> for t in title:
        	print t	


---------

## 贪婪模式与非贪婪模式

> 正则表达式通常用于在文本中查找匹配的字符串。Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；非贪婪的则相反，总是尝试匹配尽可能少的字符。例如：正则表达式"ab*"*如果用于查找"abbbc"，将找到"abbb"。而如果使用非贪婪的数量词*"ab*?"，将找到"a"。
>
	>>> re.findall(r"a(\d+?)","a23b") # 非贪婪模式
	['2']
	>>> re.findall(r"a(\d+)","a23b")
	['23']

	>>> b = 'a123b12b'
	>>> r = re.compile(r'a(.*)b')
	>>> r.findall(b) # 贪婪模式
	['123b12']
	>>> r = re.compile(r'a(.*?)b')
	>>> r.findall(b)
	['123']

------

## re模块编译标志
> 编译标志让你可以修改正则表达式的一些运行方式。在`re`模块中标志可以使用两个名字，一个是全名如IGNORECASE，一个是缩写，一字母形式如`re.I`。

### re.I(IGNORECASE)
> 使匹配对大小写不敏感；字符类和字符串匹配字母时忽略大小写。举个例子，`[A-Z]`也可以匹配小写字母，Spam可以匹配 "Spam", "spam", 或 "spAM"。这个小写字母并不考虑当前位置。

### re.M(MULTILINE)
> 多行匹配。使用`"^"`只匹配字符串的开始，而`$`则只匹配字符串的结尾和直接在换行前（如果有的话）的字符串结尾。当本标志指定後，`"^"`匹配字符串的开始和字符串中每行的开始。同样的， `$`元字符匹配字符串结尾和字符串中每行的结尾（直接在每个换行之前）。

### re.DOTALL
> 使`"."`特殊字符完全匹配任何字符，包括换行`\n`没有这个标志，`"."`匹配除了换行外的任何字符。

### re.X 
>该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。当该标志被指定时，在`RE`字符串中的空白符被忽略，除非该空白符在字符类中或在反斜杠之後；这可以让你更清晰地组织和缩进`RE`。它也可以允许你将注释写入`RE`，这些注释会被引擎忽略；注释用`"#"`号 来标识，不过该符号不能在字符串或反斜杠之後。

-----
