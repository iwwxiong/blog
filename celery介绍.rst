.. _Celery介绍:

Celery介绍
============

``Celery`` 是一个简单、灵活且可靠的，处理大量消息的分布式系统，它是一个专注于实时处理的任务队列， 同时也支持任务调度。``Celery`` 中有两个比较关键的概念：

1. Worker: 是一个独立的进程，它持续监视队列中是否有需要处理的任务；
2. Broker: 也被称为中间人或者协调者，``broker`` 负责协调客户端和 ``worker`` 的沟通。客户端向 队列添加消息，``broker`` 负责把消息派发给 ``worker``。

0x01 安装Celery
----------------

因``Celery`` 是python开发的，我们可以使用 ``pip`` 命令直接安装::

    pip install celery

0x02 安装Broker
-----------------

本文中案例使用 ``Broker`` 是基于 ``RabbitMQ`` 的，具体教程可以参考 `RabbitMQ教程 <RabbitMQ.rst>`_ 。

.. tip::

    可以做 ``Broker`` 有很多，比如：Redis，mongodb，其它数据库等。这里就不一一介绍了。