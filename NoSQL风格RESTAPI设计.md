# NoSQL风格RESTAPI设计

## 问题

随着前端工程化脚步越来越快，前后端分离的开发模式也越来越受到欢迎。但是前后端合作的时候进场也会带来问题，不知道各位有没有碰到下面的场景：
>
前端：后端后端，需求变了，能不能把那个分页参数调整下；
>
前端：后端后端，把那个XXX参数也给我返回下吧；
>
......

碰到这种情况，通常情况下后端就需要调整代码适应新的需求，也就导致后端在开发新功能的同时不停的去修改之前的代码，不胜其烦。

那么我们有没有一种比较好的API设计，可以适应这种快速变换的需求呢？（要是能像SQL语句那样查询API就完美了。）

## 方案

伴着上面的问题，这里推荐一种`NoSQL`（这里采用`NoSQL`是感觉`NoSQL`的语义更加清晰）查询语句那样的风格来设计`RESTAPI`。下面看一个案例：

```
# 查询前10个姓名大于等于25的用户，返回用户的id, age, name且按照id倒叙排列
GET /users?select=id,age,name&age=gte.25&order=id.desc&limit=10  HTTP / 1.1
```

返回：

```json
[
    {
        'id': 101,
        'name': 'xxx',
        'age': 25
    },
    {
        'id': 90,
        'name': 'xxx',
        'age': 50
    }
    ......
]
```

从上面的例子我们可以很轻松的定义查询API，且后端无需做任务代码的变更，是不是很完美。

## 设计细节

### 查询

我们可以通过自定义的查询条件来查询API，每个查询条件都是一个字符串参数，举例说明：

```
GET /users?age=lt.25 HTTP/1.1  # 年龄小于25的用户
```

多个条件组合：

```
GET /users?age=lte.25&name=like.xxx  # 年龄小于等于25且姓名like xxx的用户
```

>下面是可用的操作符：
|eq     |  等于           
|neq    |  不等于         
|gt     |  大于           
|gte    |  大于等于        
|lt     |  小于           
|lte    |  小于等于        
|like   |  %xxx%          
|in     |  在[x, x, x]之中 
|betwee |  在[x, y]之间    

### 排序

排序使用关键字order来指定，可实现多字段order。案例说明：

```
GET /users?select=*&order=id.desc,age.asc  # 按照id倒叙，且年龄正序排序
```

### 分页

分页使用关键字page（采用page不用skip是page语义更加清晰）和limit来指定。案例说明：

```
GET /users?page=2&limit=10  # 查询10-20的用户
```

### 嵌套查询

实际工作中我们可能需求多个相关资源一起返回，来减少API的调用。案例说明：

这里我们有两个资源User和School。User中间包含ID，NAME, 和School_id（关联School），School包含字段ID，NAME。

```
GET /users?select=id,name,school{*}&school.name=xxx
# 查询学校名称为xxx的用户，且返回用户的id,name和学校的所有字段
```

### 案列介绍

下面那个案列来具体介绍各种情况的设计。下图是实际资源的关联图：

![](http://7xrszf.com1.z0.glb.clouddn.com/er.jpeg)

#### 查询书籍

```json
GET /books?select=id,name,user{id,name,school{*}}&user.name=xxx&order=id.desc&limit=10
# 返回
[
    {
        'id': 1,
        'name': 'Python',
        'user': {
            'id': 2,
            'name': 'xxx',
            'school': {
                'id': 3,
                'name': 'xxx'
            }
        }
    },
    {
        'id': 2,
        'name': 'Javascript',
        'user': {
            'id': 3,
            'name': 'xxx',
            'school': {
                'id': 4,
                'name': 'xxx'
            }
        }
    }
    ......
]
```

#### 批量更新

```json
PUT /books?name='Python'
# data
{'author': 2}
# 批量更新名称为Python的书籍，变更作者id为2
```

#### 批量删除
 
```json
DELETE /books?user.name='xxx'
# 删除作者名称为xxx的所有书籍
```

## 注意

这种风格的RESTAPI可能会造成部分问题。比如恶意的分页数量，恶意的连表查询造成后端性能等问题。此时就需要后端也牺牲一些自由行，做部分字段管控等。

## 框架

这里介绍作者完成的一款适用[Django orm](https://github.com/dracarysX/django-rest-query)的框架。

### Add Model

```python
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'School'

    def __str__(self):
        return 'School: {}'.format(self.name)

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    school = models.ForeignKey(School)

    class Meta:
        db_table = 'Author'

    def __str__(self):
        return 'Author: {}'.format(self.name)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    publisher = models.ForeignKey(Publisher)

    class Meta:
        db_table = 'Book'

    def __str__(self):
        return 'Book: {}'.format(self.name)
```

### Usage

```python
python manage.py shell
> from django_rest_query import *
> from demo.models import Book, Author, School
> args = {
        'select': 'id,name,author{id,name,school{*}}',
        'id': 'gte.20',
        'author.id': 'in.10,20,30,40,50',
        'order': 'id.desc',
        'page': 1,
        'limit': 5
    }
> builder = DjangoQueryBuilder(Book, args)
> builder.select
['author__school__*', 'author__id', 'author__name', 'id', 'name']
> build.where
{'author__id__in': [10, 20, 30, 40, 50], 'id__gte': '20'}
> builder.order
['-id']
> builder.paginate
(1, 5)
{'start': 0, 'end': 5, 'limit': 5, 'page': 1}
> builder.build()
<QuerySet [Book: Python], [Book: Javascript]>
```

当然也有使用于[peewee orm](https://github.com/dracarysX/peewee-rest-query)框架。欢迎大家来提Issue。有兴趣的大家可以一起交流交流。Email: huiquanxiong@gmail.com。
