# Mongodb语法基础

MongoDB 是由C++语言编写的，是一个基于分布式文件存储的开源数据库系统。在高负载的情况下，添加更多的节点，可以保证服务器性能。MongoDB 旨在为WEB应用提供可扩展的高性能数据存储解决方案。MongoDB 将数据存储为一个文档，数据结构由键值(key=>value)对组成。MongoDB 文档类似于`JSON`对象。字段值可以包含其他文档，数组及文档数组。

## Momgodb的基本概念是文档、集合、数据库。下面是mongodb与sql概念术语对照

<table>
<tr><td>SQL</td><td>Mongodb</td><td>说明</td></tr>
<tr><td>database</td><td>database</td><td>数据库</td></tr>
<tr><td>table</td><td>collection</td><td>数据库表/集合</td></tr>
<tr><td>row</td><td>document</td><td>数据记录行/文档</td></tr>
<tr><td>column</td><td>field</td><td>数据字段/域</td></tr>
<tr><td>index</td><td>index</td><td>索引</td></tr>
<tr><td>primary key</td><td>primary key</td><td>主键，sql默认ID字段， mongodb默认_id字段</td></tr>
</table>

### 数据库

一个mongodb中可以建立多个数据库。MongoDB的默认数据库为"db"，该数据库存储在data目录中。MongoDB的单个实例可以容纳多个独立的数据库，每一个都有自己的集合和权限，不同的数据库也放置在不同的文件中。`show dbs` 命令可以显示所有数据的列表。

```bash
    > show dbs
    cs_comments_service_development    0.203125GB
    edxapp    0.953125GB
    local    0.078125GB
```

有一些数据库名是保留的，可以直接访问这些有特殊作用的数据库。

1. admin： 从权限的角度来看，这是"root"数据库。要是将一个用户添加到这个数据库，这个用户自动继承所有数据库的权限。一些特定的服务器端命令也只能从这个数据库运行，比如列出所有的数据库或者关闭服务器。
2. local: 这个数据永远不会被复制，可以用来存储限于本地单台服务器的任意集合。
3. config: 当Mongo用于分片设置时，config数据库在内部使用，用于保存分片的相关信息。

### 文档

文档是mongodb中的最核心的概念，是其核心单元，我们可以将文档类比成关系型数据库中的每一行数据。多个键及其关联的值有序的放置在一起就是文档。MongoDB使用了BSON这种结构来存储数据和网络数据交换。BSON数据可以理解为在JSON的基础上添加了一些json中没有的数据类型。如果我们会JSON，那么BSON我们就已经掌握了一半了。

1. 文档中的键/值对是有序的。
2. 文档中的值不仅可以是在双引号里面的字符串，还可以是其他几种数据类型（甚至可以是整个嵌入的文档)。
3. MongoDB区分类型和大小写。
4. MongoDB的文档不能有重复的键。
5. 文档的键是字符串。除了少数例外情况，键可以使用任意UTF-8字符(不过建议最好英文)。

```json
{
    "_id" : ObjectId("5677933fb844cfbffd9307f3"),
    "name" : "wwx",
    "sex" : "男",
    "年龄" : 26
}
```

### 集合

集合就是一组文档的组合。如果将文档类比成数据库中的行，那么集合就可以类比成数据库的表。在mongodb中的集合是无模式的，也就是说集合中存储的文档的结构可以是不同的，比如下面的两个文档可以同时存入到一个集合中。（不需要想sql类数据库中每一张表中的字段都是固定的。集合中保存的文档是可以无模式的。不过建议尽量保存类似结构，方便业务开发。）

```json
/* 1 */
{
    "_id" : ObjectId("56779472b844cfbffd9307f4"),
    "name" : "wwx",
    "sex" : "男",
    "年龄" : 26
}
/* 2 */
{
    "_id" : ObjectId("56779472b844cfbffd9307f5"),
    "name" : "wwxiong",
    "sex" : "男",
    "年龄" : 27,
    "school" : "天津理工大学"
}
```

## Mongodb数据类型

<table>
<thead><td>数据类型</td><td>描述</td></thead>
<tr><td>String</td><td>字符串。存储数据常用的数据类型。在 MongoDB 中，UTF-8 编码的字符串才是合法的。</td></tr>
<tr><td>Integer</td><td>整型数值。用于存储数值。根据你所采用的服务器，可分为 32 位或 64 位。</td></tr>
<tr><td>Boolean</td><td>布尔值。用于存储布尔值（真/假）。</td></tr>
<tr><td>Double</td><td>双精度浮点值。用于存储浮点值。</td></tr>
<tr><td>Min/Max keys</td><td>将一个值与 BSON（二进制的 JSON）元素的最低值和最高值相对比。</td></tr>
<tr><td>Arrays</td><td>用于将数组或列表或多个值存储为一个键。</td></tr>
<tr><td>Timestamp</td><td>时间戳。记录文档修改或添加的具体时间。</td></tr>
<tr><td>Object</td><td>用于内嵌文档。</td></tr>
<tr><td>Null</td><td>用于创建空值。</td></tr>
<tr><td>Symbol</td><td>符号。该数据类型基本上等同于字符串类型，但不同的是，它一般用于采用特殊符号类型的语言。</td></tr>
<tr><td>Date</td><td>日期时间。用 UNIX 时间格式来存储当前日期或时间。你可以指定自己的日期时间：创建 Date 对象，传入年月日信息。</td></tr>
<tr><td>Object ID</td><td>对象 ID。用于创建文档的 ID。</td></tr>
<tr><td>Binary Data</td><td>二进制数据。用于存储二进制数据。</td></tr>
<tr><td>Code</td><td>代码类型。用于在文档中存储 JavaScript 代码。</td></tr>
<tr><td>Regular expression</td><td>正则表达式类型。用于存储正则表达式。</td></tr>
</table>

## Mongodb增删查改

mongodb 操作命令格式一般是`db.COLLECTION_NAME.KEY`的方式。COLLECTION_NAME表示集合名称，KEY是操作关键字。

### 插入文档

MongoDB 使用 insert() 或 save() 方法向集合中插入文档，语法如下：`db.COLLECTION_NAME.insert({})`， `db.COLLECTION_NAME.save({})`

* db.mycoll.insert({name:"wwx",sex:"男","年龄":26})
* db.mycoll.insert({name:"wwxiong",sex:"男","年龄":27,"school":"天津理工大学"})
* db.mycoll.save({name:"yb", school:"易班大学", author:"wwxiong", job:"web开发工程师"})

```json
/* 3 */
{
    "_id" : ObjectId("56779ec2b844cfbffd9307f6"),
    "name" : "wwx",
    "sex" : "男",
    "年龄" : 26
}
/* 4 */
{
    "_id" : ObjectId("56779ec2b844cfbffd9307f7"),
    "name" : "wwxiong",
    "sex" : "男",
    "年龄" : 27,
    "school" : "天津理工大学"
}
/* 5 */
{
    "_id" : ObjectId("56779ec2b844cfbffd9307f8"),
    "name" : "yb",
    "school" : "易班大学",
    "author" : "wwxiong",
    "job" : "web开发工程师"
}
```

### 更新文档

MongoDB 使用 `update()` 和 `save()` 方法来更新集合中的文档。区别是:update更新结果，save方法是直接替换原来文档。

ps: 使用update的时候如果update中没有`$`关键字KEY的时候，会使用update的内容替换掉原文档（新手坑）。

#### update语法

```bash
db.collection.update(
    <query>,
    <update>,
    {
        upsert: <boolean>, #
        multi: <boolean>,  # 更新多个结果
        writeConcern: <document>
    }
)
```

1. query : update的查询条件，类似sql update查询内where后面的。
2. update : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
3. upsert : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
4. multi : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。
5. writeConcern :可选，抛出异常的级别。

```json
/* 0 */
{
    "_id" : ObjectId("5677caabb844cfbffd930801"),
    "name" : "wwx",
    "sex" : "男",
    "age" : 27
}
/* 1 */
{
    "_id" : ObjectId("5677cacdb844cfbffd930802"),
    "name" : "wwx",
    "sex" : "男",
    "age" : 28
}
```

`db.mycoll.update({"name":"wwx"}, {$set: {"sex":"女"}, $inc: {"age": 1}}, {'upsert': true, 'multi' : true})`

```json
/* 0 */
{
    "_id" : ObjectId("5677caabb844cfbffd930801"),
    "name" : "wwx",
    "sex" : "女",
    "age" : 28
}
/* 1 */
{
    "_id" : ObjectId("5677cacdb844cfbffd930802"),
    "name" : "wwx",
    "sex" : "女",
    "age" : 29
}
```

#### save语法

```
db.collection.save(
    <document>,
    {
        writeConcern: <document>
    }
)
```

参数说明：

1. document : 文档数据。
2. writeConcern :可选，抛出异常的级别。

```
db.mycoll.save({
    "_id" : ObjectId("5677caabb844cfbffd930801"),
    "name" : "wwx-save",
    "sex" : "女",
    "age" : 21
})
```

```json
/* 1 */
{
    "_id" : ObjectId("5677caabb844cfbffd930801"),
    "name" : "wwx-save",
    "sex" : "女",
    "age" : 21
}
```

### 删除文档

MongoDB remove()函数是用来移除集合中的数据。MongoDB数据更新可以使用update()函数。在执行remove()函数前先执行find()命令来判断执行的条件是否正确，这是一个比较好的习惯。

remove格式如下：

```
db.collection.remove(
    <query>,
    <justOne>,
    <writeConcern>
)
```

参数说明：

1. query :（可选）删除的文档的条件`{"key": "value"}`。
2. justOne : （可选）如果设为 true 或 1，则只删除一个文档。
3. writeConcern :（可选）抛出异常的级别。

```
/* 0 */
{
    "_id" : ObjectId("5677a2f0b844cfbffd9307fc"),
    "name" : "wwx",
    "sex" : "男",
    "年龄" : 26
}
/* 1 */
{
    "_id" : ObjectId("5677b020b844cfbffd9307ff"),
    "name" : "wwx",
    "sex" : "男",
    "年龄" : 26,
    "hobbit" : "DOTA2"
}
```

db.mycoll.remove({"name":"wwx"}, {justOne: 1})

```json
    /* 0 */
    {
        "_id" : ObjectId("5677b020b844cfbffd9307ff"),
        "name" : "wwx",
        "sex" : "男",
        "年龄" : 26,
        "hobbit" : "DOTA2"
    }
```

### 简单查询

MongoDB 查询数据的语法格式如下：`>db.COLLECTION_NAME.find()`，同时还提供`findOne()`，它只返回一个文档。

案例：`db.mycoll.find({'age':{'$gte': 25}})  # 查询年龄大于等于25岁的`

```json
>/* 0 */
{
    "_id" : ObjectId("5677cacdb844cfbffd930802"),
    "name" : "wwx",
    "sex" : "女",
    "age" : 29
}
/* 1 */
{
    "_id" : ObjectId("5678b4e862d9c2605253063f"),
    "name" : "def",
    "age" : 25,
    "values" : [
        {
            "a" : 6,
            "b" : 15
        }
    ]
}
/* 2 */
{
    "_id" : ObjectId("5678b4e862d9c26052530640"),
    "name" : "zbc",
    "age" : 26,
    "values" : [
        {
            "a" : 7,
            "b" : 16
        }
    ]
}
```

#### AND

mongodb find()可以传入多个键(key)，每个键(key)以逗号隔开，类似SQL `AND` 的用法：`db.mycoll.find({key1:value1, key2:value2,...})`。

#### $or

使用$or关键字可以实现SQL `OR` 的用法：`db.mycoll.find({$or: [{'key1': 'value1'}, {'key2': 'value2'}, {...}]})`。

#### $in&$nin

使用 `$in&$nin` 关键字实现sql `in&not in` 的用法。
用法：

```
db.mycoll.find({
    'key1': {$in: [v1, v2, v3]},
    'key2': {$nin: [v4, v5, v6]},
    'key3': {$not: {$in: [v7, v8, v9]}}
})
```

#### values

有时候我们只需要制定的返回键值，通过指定find的第二个参数来实现。这样可以节省传输的数据量，又能节省客户端解码文档的时间和内存消耗。类似SQL `select value1, value2... from table`。

`db.mycoll.find({'age':{'$gte': 25}}, {'name':1})`

```json
/* 0 */
{
    "_id" : ObjectId("5677cacdb844cfbffd930802"),
    "name" : "wwx"
}
/* 1 */
{
    "_id" : ObjectId("5678b4e862d9c2605253063f"),
    "name" : "def"
}
```

#### 简单条件< ,<= ,>= ,>, !=

mongodb的条件查询语句: `$lt, $lte, $gte, $gt, $ne`。

```
db.mycoll.find({
    'key1': {$lt: value1},
    'key2': {$lte: value2},
    'key3': {$gte: value3},
    'key4': {$gte: value4},
    'key5': {$ne: value5}
})
```

### 高级查询

#### $type

MongoDB中条件操作符 `$type` 是基于BSON类型来检索集合中匹配的数据类型，并返回结果。下面是type对照表：

<table>
<tr><td>类型</td><td>数字结果</td></tr>
<tr><td>Double</td><td>1</td></tr>
<tr><td>String</td><td>2</td></tr>
<tr><td>Object</td><td>3</td></tr>
<tr><td>Array</td><td>4</td></tr>
<tr><td>Binary data</td><td>5</td></tr>
<tr><td>Object id</td><td>7</td></tr>
<tr><td>Boolean</td><td>8</td></tr>
<tr><td>Date</td><td></td>9</tr>
<tr><td>Null</td><td></td>10</tr>
<tr><td>Regular Expression</td><td>11</td></tr>
<tr><td>JavaScript</td><td>13</td></tr>
<tr><td>Symbol</td><td>14</td></tr>
<tr><td>JavaScript (with scope)</td><td>15</td></tr>
<tr><td>32-bit integer</td><td>16</td></tr>
<tr><td>Timestamp</td><td>17</td></tr>
<tr><td>64-bit integer</td><td>18</td></tr>
<tr><td>Min key</td><td>255</td></tr>
<tr><td>Max key</td><td>127</td></tr>
</table>

案例

```json
/* 0 */
{
    "_id" : ObjectId("5678b4e862d9c26052530642"),
    "name" : "wxb",
    "age" : 28,
    "values" : [
        {
            "a" : 9,
            "b" : 212
        }
    ]
}
/* 1 */
{
    "_id" : ObjectId("5678c29e62d9c26052530643"),
    "name" : "wxb1",
    "age" : "28",
    "values" : [
        {
            "a" : 9,
            "b" : 212
        }
    ]
}

`db.mycoll.find({'age': {$type: 2}})`，查询年龄是String类型的结果

```json
/* 0 */
{
    "_id" : ObjectId("5678c29e62d9c26052530643"),
    "name" : "wxb1",
    "age" : "28",
    "values" : [
        {
            "a" : 9,
            "b" : 212
        }
    ]
}
```

#### limit&skip

有时候我们不需要查询所有的数据（分页需求）,只需要按照开始位置查询固定size的结果，此时我们就需要使用 `skip` 和 `limit` 配置了。语法：`db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)` (skip默认是0)。下面我们来看看它们的使用案例：

`db.mycoll.find().limit(2).skip(2)`

```json
/* 0 */
{
    "_id" : ObjectId("5678b4e862d9c2605253063a"),
    "name" : "ydb",
    "age" : 20,
    "values" : [
        {
            "a" : 1,
            "b" : 2
        }
    ]
}
/* 1 */
{
    "_id" : ObjectId("5678b4e862d9c2605253063b"),
    "name" : "ddd",
    "age" : 21,
    "values" : [
        {
            "a" : 2,
            "b" : 12
        }
    ]
}
```

#### 排序sort

在MongoDB中使用使用sort()方法对数据进行排序，sort()方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序排列，而-1是用于降序排列。其基本语法： `>db.COLLECTION_NAME.find().sort({KEY:1})`。

`db.mycoll.find().sort({'age': -1})`

```json
/* 0 */
{
    "_id" : ObjectId("5677cacdb844cfbffd930802"),
    "name" : "wwx",
    "sex" : "女",
    "age" : 29
}
/* 1 */
{
    "_id" : ObjectId("5678b4e862d9c26052530642"),
    "name" : "wxb",
    "age" : 28,
    "values" : [
        {
            "a" : 9,
            "b" : 212
        }
    ]
}
```

#### 正则查询

可以使用正则表达式来查询数据。db.collection.find({key: REGEX})。

`db.mycoll.find({'name': /^wwx/})`

```json
/* 0 */
{
    "_id" : ObjectId("5677cacdb844cfbffd930802"),
    "name" : "wwx",
    "sex" : "女",
    "age" : 29
}
/* 1 */
{
    "_id" : ObjectId("5677caabb844cfbffd930801"),
    "name" : "wwx-save",
    "sex" : "女",
    "age" : 21
}
```

#### 数组查询

#### $size查询

对数组的查询, 查询数组元素个数是size的记录，$size前面无法和其他的操作符复合使用。

`db.mycoll.find({'values':{$size: 4}})`

```json
/* 0 */
{
    "_id" : ObjectId("5678e2cd62d9c26052530645"),
    "name" : "fqy",
    "age" : 20,
    "date" : ISODate("2015-12-22T05:42:37.359Z"),
    "values" : [ 1, 2, 3, 4]
}
```

#### $all查询

关键字 `$all` 查询数组中同时包含的结果。`db.mycoll.find({'key': {$all: [v1, v2]}})` 表示查询结果key的内容同时包含v1， v2。

`db.mycoll.find({'values':{$all: [1,2]}})`

```json
/* 0 */
{
    "_id" : ObjectId("5678e2cd62d9c26052530645"),
    "name" : "fqy",
    "age" : 20,
    "date" : ISODate("2015-12-22T05:42:37.359Z"),
    "values" : [ 1, 2, 3, 4]
}
/* 1 */
{
    "_id" : ObjectId("5678e42062d9c26052530646"),
    "name" : "fqy",
    "age" : 20,
    "date" : ISODate("2015-12-22T05:48:16.014Z"),
    "values" : [ 1, 2, 5, 6]
}
```

#### $slice查询

对数组查询，查询后的结果按照 `$slice` 裁剪后返回。`db.collection.find( { field: value }, { array: {$slice: count } } )` ,$slice后面的value是一个数组,有点类似python的list切片。

`db.mycoll.find({}, {'values':{'$slice': 2}})`

```json
/* 3 */
{
    "_id" : ObjectId("5678e2cd62d9c26052530645"),
    "name" : "fqy",
    "age" : 20,
    "date" : ISODate("2015-12-22T05:42:37.359Z"),
    "values" : [ 1, 2]
}
/* 4 */
{
    "_id" : ObjectId("5678e42062d9c26052530646"),
    "name" : "fqy",
    "age" : 20,
    "date" : ISODate("2015-12-22T05:48:16.014Z"),
    "values" : [ 1, 2]
}
```

#### 数组index查询

`db.collection.find( {field.count: value } )` 查询field中的count位置等于value的结果。

`db.mycoll.find({'values.1': 2})`，查询values的第二个元素等于2

```json
/* 0 */
{
    "_id" : ObjectId("5678e2cd62d9c26052530645"),
    "name" : "fqy",
    "age" : 20,
    "date" : ISODate("2015-12-22T05:42:37.359Z"),
    "values" : [ 1, 2, 3, 4]
}
/* 1 */
{
    "_id" : ObjectId("5678e42062d9c26052530646"),
    "name" : "fqy",
    "age" : 20,
    "date" : ISODate("2015-12-22T05:48:16.014Z"),
    "values" : [ 1, 2, 5, 6]
}
```

#### 聚合，where使用

#### $where

`$where` 查询需要将每个文档从BSON转换为JavaScript对象，然后通过$where的表达式来运行，该过程不能利用索引，所以查询速度较常规查询慢很多。如果必须使用时，可以将常规查询作为前置过滤，能够利用索引的话可以使用索引根据非$where子句进行过滤。（不建议生产环境使用，玩玩还可以。如果实在有需求可以使用 `MapReduce` 替代。）。`db.collection.find({$where: function(){if return true else return false;}})`

`db.mycoll.find({$where: function(){if(this.name==='wwx'){return true;}}})`

```json
/* 0 */
{
    "_id" : ObjectId("5677cacdb844cfbffd930802"),
    "name" : "wwx",
    "sex" : "女",
    "age" : 29
}
```

#### $aggregate

MongoDB中聚合(aggregate)主要用于处理数据(诸如统计平均值,求和等)，并返回计算后的数据结果。有点类似sql语句中的 count(*)。基本语法：db.collection.aggregate(AGGREGATE_OPERATION)。

##### 求和$sum

`db.mycoll.aggregate([{$group: {_id: "$by_id", total: {$sum: 1}}}]) #select count(*) from table group by id;`

```json
/* 0 */
{
    "result" : [
        {
            "_id" : null,
            "total" : 5
        }
    ],
    "ok" : 1
}
```

#### 平均值$avg

查询平均年龄，`db.mycoll.aggregate([{$group: {_id: "$by_id", average_age: {$avg: '$age'}}}])`

```json
/* 0 */
{
    "result" : [
        {
            "_id" : null,
            "average_age" : 22.5
        }
    ],
    "ok" : 1
}
```

下面是一些聚合的表达式（用法同上面的$sum和$avg）。

<table>
<tr><td>表达式</td><td>描述</td></tr>
<tr><td>$sum</td><td>求和</td></tr>
<tr><td>$avg</td><td>求平均值</td></tr>
<tr><td>$min</td><td>获取集合中所有文档对应值得最小值。</td></tr>
<tr><td>$max</td><td>获取集合中所有文档对应值得最大值。</td></tr>
<tr><td>$push</td><td>在结果文档中插入值到一个数组中。</td></tr>
<tr><td>$addToSet</td><td>在结果文档中插入值到一个数组中，但不创建副本。</td></tr>
<tr><td>$first</td><td>根据资源文档的排序获取第一个文档数据。</td></tr>
<tr><td>$last</td><td>根据资源文档的排序获取最后一个文档数据</td></tr>
</table>

#### 管道的使用

管道在Unix和Linux中一般用于将当前命令的输出结果作为下一个命令的参数。MongoDB的聚合管道将MongoDB文档在一个管道处理完毕后将结果传递给下一个管道处理。管道操作是可以重复的。表达式：处理输入文档并输出。表达式是无状态的，只能用于计算当前聚合管道的文档，不能处理其它的文档。下面是聚合框架中几个常见的操作：

1. $project：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。
2. $match：用于过滤数据，只输出符合条件的文档。$match使用MongoDB的标准查询操作。
3. $limit：用来限制MongoDB聚合管道返回的文档数。
4. $skip：在聚合管道中跳过指定数量的文档，并返回余下的文档。
5. $unwind：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
6. $group：将集合中的文档分组，可用于统计结果。
7. $sort：将输入文档排序后输出。
8. $geoNear：输出接近某一地理位置的有序文档

（下面是一个$match的使用案例）查询性别为女的平均年龄。

`db.mycoll.aggregate([{$match: {'sex': '女'}}, {$group: {_id: "$by_id", average_age: {$avg: '$age'}}}])`

```json
/* 0 */
{
    "result" : [
        {
            "_id" : null,
            "average_age" : 25
        }
    ],
    "ok" : 1
}
```

## 总结

当然Mongodb还有很多很好玩的查询，这里就不一一做介绍了。MapReduce 用法待下期介绍。总之一句话：mongo虽好玩，使用需谨慎。
