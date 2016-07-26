.. _Redis:

Redis简介
==========

REmote DIctionary Server(Redis) 是一个由Salvatore Sanfilippo写的key-value存储系统。
Redis是一个开源的使用ANSIC语言编写、遵守BSD协议、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。
它通常被称为数据结构服务器，因为值（value）可以是 字符串( ``String`` ), 哈希( ``Map`` ), 列表( ``list`` ), 集合( ``sets`` ) 和 有序集合( ``sorted sets`` )等类型。学习参考 `Redis教程 <http://www.runoob.com/redis/redis-tutorial.html>`_ 。

**特点**

    * Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。
    * Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
    * Redis支持数据的备份，即master-slave模式的数据备份。

**优势**

    * 性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
    * 丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
    * 原子 – Redis的所有操作都是原子性的，同时Redis还支持对几个操作全并后的原子性执行。
    * 丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。

Radis安装，配置
-----------------

unubtu安装
^^^^^^^^^^^

ubuntu下安装命令::
    sudo apt-get update
    sudo apt-get install redis-server
    # 测试连接
    redis-cli
    redis 127.0.0.1:6379>

redis配置
^^^^^^^^^^^

redis配置文件默认保存在 ``/etc/redis/redis.conf`` 。默认端口：6379
当然也可以使用命令来配置

    CONFIG SET NAME VALUE


Radis数据类型
-------------

String(字符串)
^^^^^^^^^^^^^^^

string是redis最基本的类型，一个键最大能存储512M。string类型是二进制安全的，可以包含任何数据。

**常用命令**

    - set：设置key的值
    - get：获取key的值
    - decr：将key值增1
    - incr：将key值减1
    - mget：获取多个key的值
    - 等

Hash(哈希)
^^^^^^^^^^^

Redis hash是一个string类型的field和value的映射表，hash特别适合用于存储对象。

    > HMSET user:1 wwx 20
    ok
    > HGETALL user:1
    "wwx"
    "20"
    # user:1 为键值

**常用命令**

    - hget：获取存储在哈希表中指定字段的值
    - hset：将哈希表 ``key`` 中的字段 ``field`` 的值设为 ``value``
    - hgetall：获取在哈希表中指定 ``key`` 的所有字段和值
    - 等

**使用场景**

    比如我们要存储一个用户信息对象数据，包含以下信息：用户ID为查找的key，存储的value用户对象包含姓名，年龄，生日等信息。

List(列表)
^^^^^^^^^^^^

Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素导列表的头部（左边）或者尾部（右边）。类似 ``Python`` 的list结构

**常用命令**

    - lpush：将一个或多个值插入到列表头部
    - rpush：在列表中追加一个或多个值
    - lpop：移出并获取列表的第一个元素
    - rpop：移出并获取列表的最后一个元素
    - lrange：获取列表指定范围内的元素
    - 等

Set(集合)
^^^^^^^^^^^

Redis的Set是string类型的无序集合。集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)。

**常用命令**

    - sadd：向集合添加一个或多个成员
    - spop：移除并返回集合中的一个随机元素
    - smembers：返回集合中的所有成员
    - sunion：返回所有给定集合的并集
    - 等

**应用场景**

    ``Set`` 提供的功能与 ``List`` 类似，特点是 ``Set`` 是去重的集合。

zset(sortet set有序集合)
^^^^^^^^^^^^^^^^^^^^^^^^

Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。zset的成员是唯一的,但分数(score)却可以重复。

**常用命令**

    - zadd：向有序集合添加一个或多个成员，或者更新已存在成员的分数
    - zrange：通过索引区间返回有序集合成指定区间内的成员
    - zrem：移除有序集合中的一个或多个成员
    - zcard：获取有序集合的成员数
    - 等

**使用场景**

    Redis sorted set的使用场景与set类似，区别是set不是自动有序的，而sorted set可以通过用户额外提供一个优先级(score)的参数来为成员排序，并且是插入有序的，即自动排序。当你需要一个有序的并且不重复的集合列表，那么 可以选择sorted set数据结构。
