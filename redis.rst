.. _Redis:

Redis简介
==========

REmote DIctionary Server(Redis) 是一个由Salvatore Sanfilippo写的key-value存储系统。
Redis是一个开源的使用ANSIC语言编写、遵守BSD协议、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。
它通常被称为数据结构服务器，因为值（value）可以是 字符串( ``String`` ), 哈希( ``Map`` ), 列表( ``list`` ), 集合( ``sets`` ) 和 有序集合( ``sorted sets`` )等类型。学习参考 `Redis设计与实现 <http://redisbook.readthedocs.io/>`_ 。

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

Redis发布和订阅
--------------

Redis 通过 PUBLISH 、 SUBSCRIBE 等命令实现了订阅与发布模式， 这个功能提供两种信息机制， 分别是订阅/发布到频道和订阅/发布到模式

Redis 的 SUBSCRIBE 命令可以让客户端订阅任意数量的频道， 每当有新信息发送到被订阅的频道时， 信息就会被发送给所有订阅指定频道的客户端::
.. image:: _static/img/subscribe.svg

当有新消息通过 PUBLISH 命令发送给频道 channel1 时， 这个消息就会被发送给订阅它的三个客户端::
.. image:: _static/img/publish.svg

订阅频道
^^^^^^^^^

每个 ``Redis`` 服务器进程都维持着一个表示服务器状态的 ``redis.h/redisServer`` 结构， 结构的 ``pubsub_channels`` 属性是一个字典， 这个字典就用于保存订阅频道的信息::

    {
        'pubsub_channels': {
            "channel1": ["client1", "client2", "client3"],
            "channel2": ["client4", "client5", "client6"],
            "channel3": ["client1", "client2", "client4", "client5"]
        }
    }

``pubsub_channels`` 示例中有 ``channel1`` , ``channel2`` , ``channel3`` 3个频道。然后 ``client1`` , ``client2`` , ``client3`` 同时订阅了 ``channel1`` 频道。同时一个客户端可以订阅多个频道，一个频道也可以被多个客户端订阅。

客户端调用 ``SUBSCRIBE`` 命令时， 程序就将客户端和要订阅的频道在 ``pubsub_channels`` 字典中关联起来。举例 ``clientX`` 订阅 ``channel1`` , ``channel2`` , ``channel3`` 频道::

    SUBSCRIBE channel1 channel2 channel3

发布信息到频道
^^^^^^^^^^^^^

``PUBLISH`` 命令的实现就非常简单了： 当调用 ``PUBLISH channel message`` 命令， 程序首先根据 ``channel`` 定位到字典的键， 然后将信息发送给字典值链表中的所有客户端。

比如说，对于以下这个 ``pubsub_channels`` 实例， 如果某个客户端执行命令::

    PUBLISH channel1 "hello world" 

那么 ``client1`` 、 ``client2`` 和 ``client3`` 三个客户端都将接收到 ``hello world`` 信息。

退订频道
^^^^^^^^^

``UNSUBSCRIBE`` 退订频道，例子如下::

    UNSUBSCRIBE channel1

订阅模式
^^^^^^^^

``redisServer.pubsub_patterns`` 属性是一个链表，链表中保存着所有和模式相关的信息。链表中的每个节点都包含一个 ``redis.h/pubsubPattern`` 结构::

    typedef struct pubsubPattern {
        redisClient *client;
        robj *pattern;
    } pubsubPattern;

``client`` 属性保存着订阅模式的客户端，而 ``pattern`` 属性则保存着被订阅的模式。模式订阅命令如下::

    PSUBSCRIBE shop.*  # 订阅shop.*模式

发布信息到模式
^^^^^^^^^^^^^

发送信息到模式的工作也是由 ``PUBLISH`` 命令进行的，``PUBLISH`` 除了将 ``message`` 发送到所有订阅 ``channel`` 的客户端之外， 它还会将 ``channel`` 和 ``pubsub_patterns`` 中的模式进行对比， 如果 ``channel`` 和某个模式匹配的话， 那么也将 ``message`` 发送到订阅那个模式的客户端。

举例说明，如果 ``PUBLISH`` 命令到 ``shop.ipad`` 频道同时，也会把消息发布到所有匹配 ``shop.*`` 模式频道的客户端中。

.. image:: _static/img/pattern.svg

退订模式
^^^^^^^^

    PUNSUBSCRIBE shop.*

Summary
^^^^^^^^^

* 订阅信息由服务器进程维持的 redisServer.pubsub_channels 字典保存，字典的键为被订阅的频道，字典的值为订阅频道的所有客户端。
* 当有新消息发送到频道时，程序遍历频道（键）所对应的（值）所有客户端，然后将消息发送到所有订阅频道的客户端上。
* 订阅模式的信息由服务器进程维持的 redisServer.pubsub_patterns 链表保存，链表的每个节点都保存着一个 pubsubPattern 结构，结构中保存着被订阅的模式，以及订阅该模式的客户端。程序通过遍历链表来查找某个频道是否和某个模式匹配。
* 当有新消息发送到频道时，除了订阅频道的客户端会收到消息之外，所有订阅了匹配频道的模式的客户端，也同样会收到消息。
* 退订频道和退订模式分别是订阅频道和订阅模式的反操作。

Redis事务
----------

事务提供了一种“将多个命令打包， 然后一次性、按顺序地执行”的机制， 并且事务在执行的期间不会主动中断 —— 服务器在执行完事务中的所有命令之后， 才会继续处理其他客户端的其他命令。事务已 ``MULTI`` 开始，已 ``EXEC`` 结束。

一个事务从开始到执行会经历以下三个阶段：

    1. 开始事务。
    2. 命令入队。
    3. 执行事务。

事务总结
^^^^^^^^

* 事务提供了一种将多个命令打包，然后一次性、有序地执行的机制。
* 事务在执行过程中不会被中断，所有事务命令执行完之后，事务才能结束。
* 多个命令会被入队到事务队列中，然后按先进先出（FIFO）的顺序执行。
* 带 WATCH 命令的事务会将客户端和被监视的键在数据库的 watched_keys 字典中进行关联，当键被修改时，程序会将所有监视被修改键的客户端的 REDIS_DIRTY_CAS 选项打开。
* 只有在客户端的 REDIS_DIRTY_CAS 选项未被打开时，才能执行事务，否则事务直接返回失败。
* Redis 的事务保证了 ACID 中的一致性（C）和隔离性（I），但并不保证原子性（A）和持久性（D）。