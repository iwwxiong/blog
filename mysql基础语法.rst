.. _Mysql基础语法实战:

Mysql基础语法
================

测试数据库结构
---------------

下面是本文章所使用例子的数据库结构::

    SET FOREIGN_KEY_CHECKS=0;

    -- ----------------------------
    -- Table structure for Exam
    -- ----------------------------
    DROP TABLE IF EXISTS `Exam`;
    CREATE TABLE `Exam` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(255) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

    -- ----------------------------
    -- Table structure for ExamUser
    -- ----------------------------
    DROP TABLE IF EXISTS `ExamUser`;
    CREATE TABLE `ExamUser` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `User_id` int(11) NOT NULL,
      `Exam_id` int(11) NOT NULL,
      `score` float(4,0) NOT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `U_User_id_Exam_id` (`User_id`,`Exam_id`) USING BTREE
    ) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

    -- ----------------------------
    -- Table structure for Profile
    -- ----------------------------
    DROP TABLE IF EXISTS `Profile`;
    CREATE TABLE `Profile` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(255) NOT NULL,
      `email` varchar(255) NOT NULL,
      `sex` varchar(10) NOT NULL,
      `wechat` varchar(255) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

    -- ----------------------------
    -- Table structure for User
    -- ----------------------------
    DROP TABLE IF EXISTS `User`;
    CREATE TABLE `User` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(255) NOT NULL,
      `age` int(11) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;


基础增、删、查、改
--------------------

导入基础数据::

    INSERT INTO `User`(`name`, `age`) VALUES('wwxiong', 25);
    INSERT INTO `User`(`name`, `age`) VALUES('dracarysX', 21);
    INSERT INTO `User`(`name`, `age`) VALUES('wwx', 15);
    INSERT INTO `User`(`name`, `age`) VALUES('xhq', 27);

增::

    INSERT INTO `User`(`name`, `age`) VALUES('tmp', 10);

删::

    DELETE FROM `User` WHERE `name` = 'wwx';

查::

    SELECT `name`, `age` FROM User WHERE `name` = 'wwx';

改::

    UPDATE `User` SET `age` = 100 WHERE `name` = 'wwx';

表连接
---------

INNER JOIN(连接)
>>>>>>>>>>>>>>>>>

``SQL JOIN`` 子句用于把来自两个或多个表的行结合起来， ``SQL INNER JOIN`` 从多个表中返回满足 ``JOIN`` 条件的所有行。

.. image:: _static/img/mysql/innerjoin.gif

.. code::

    SELECT U.`name`, U.age, P.email, P.sex, P.wechat
    FROM `User` AS U
    JOIN `Profile` AS P
    ON U.`name` = P.`name`
    WHERE U.`name` = 'wwx';

=======  =====  ===========  =====   ======
name      age   email        sex     wechat
=======  =====  ===========  =====   ======
wwx       15    wwx@example   F       wwx
=======  =====  ===========  =====   ======

LEFT JOIN(左连接)
>>>>>>>>>>>>>>>>>>>

``LEFT JOIN`` 关键字从左表（table1）返回所有的行，即使右表（table2）中没有匹配。如果右表中没有匹配，则结果为 ``NULL``。

.. image:: ./_static/img/mysql/leftjoin.gif

.. code::

    SELECT U.`name`, U.age, P.email, P.sex, P.wechat
    FROM `User` AS U
    LEFT JOIN `Profile` AS P
    ON U.`name` = P.`name`
    WHERE U.`name` LIKE 'wwx%';

=======  =====  ===========  =====   ======
name      age   email        sex     wechat
=======  =====  ===========  =====   ======
wwxiong  25     null          null    null
wwx      15     wwx@example   F       wwx
=======  =====  ===========  =====   ======

RIGHT JOIN(右连接)
>>>>>>>>>>>>>>>>>>>

``RIGHT JOIN`` 关键字从右表（table2）返回所有的行，即使左表（table1）中没有匹配。如果左表中没有匹配，则结果为 ``NULL``。

.. image:: ./_static/img/mysql/rightjoin.gif

.. code::

    SELECT U.`name`, U.age, P.email, P.sex, P.wechat
    FROM `User` AS U
    RIGHT JOIn `Profile` AS P
    ON U.`name` = P.`name`
    WHERE P.`name` LIKE 'xxx';

=======  =====  ===========  =====   ======
name      age   email        sex     wechat
=======  =====  ===========  =====   ======
null      null  xxx@example  F       xxx
=======  =====  ===========  =====   ======

UNION(联合)
>>>>>>>>>>>>>

``UNION`` 操作符用于合并两个或多个 SELECT 语句的结果集

.. attention::

    ``UNION`` 内部的每个 ``SELECT`` 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每个 ``SELECT`` 语句中的列的顺序必须相同。

.. code::

    SELECT U.`name` FROM `User` AS U WHERE U.`name` LIKE 'wwx%'
    UNION
    SELECT P.`name` FROM `Profile` AS P;

.. list-table::

    * - wwxiong
    * - wwx
    * - dracarysX
    * - xxx

``UNION`` 不能用于列出两个表中所有的country。如果一些网站和APP来自同一个国家，每个国家只会列出一次。``UNION`` 只会选取不同的值。请使用 ``UNION ALL`` 来选取重复的值::

    SELECT U.`name` FROM `User` AS U WHERE U.`name` LIKE 'wwx%'
    UNION ALL
    SELECT P.`name` FROM `Profile` AS P;

.. list-table::

    * - wwxiong
    * - wwxiong
    * - wwx
    * - dracarysX
    * - xxx

函数
-------

GROUP BY(分组)
>>>>>>>>>>>>>>>>

``GROUP BY`` 语句用于结合聚合函数，根据一个或多个列对结果集进行分组。

查找相同姓名的用户数量::

    SELECT `name`, `age`, COUNT(1) AS nums FROM `User` GROUP BY `name`;

==========  === ====
name        age nums
==========  === ====
dracarysX   21  2
wwxiong     25  2
xhq         27  2
==========  === ====

HAVING

``HAVING`` 子句可以让我们筛选分组后的各组数据。

查找相同姓名数量大于1的用户::

    SELECT `name`, `age`FROM `User` GROUP BY `name` HAVING COUNT(1) > 1 ;

==========  ===
name        age
==========  ===
dracarysX   21
wwxiong     25
xhq         27
==========  ===

行列转换
------------

``Mysql`` 可以利用 ``SUM IF`` 或者 ``SUM CASE`` 语句来实现行列转换操作。

SUM IF::

    SELECT U.`name`,
        SUM(IF(EU.Exam_id=1, score, null)) AS '语文',
        SUM(IF(EU.Exam_id=2, score, null)) AS '数学',
        SUM(IF(EU.Exam_id=3, score, null)) AS '英语',
        SUM(IF(EU.Exam_id=4, score, null)) AS '综合'
    FROM ExamUser AS EU
    RIGHT JOIN User AS U
    ON EU.User_id = U.id
    GROUP BY EU.User_id;

SUM CASE::

    SELECT U.`name`,
        SUM(CASE EU.Exam_id WHEN 1 THEN score END) AS '语文',
        SUM(CASE EU.Exam_id WHEN 2 THEN score END) AS '数学',
        SUM(CASE EU.Exam_id WHEN 3 THEN score END) AS '英语',
        SUM(CASE EU.Exam_id WHEN 4 THEN score END) AS '综合'
    FROM ExamUser AS EU
    RIGHT JOIN User AS U
    ON EU.User_id = U.id
    GROUP BY EU.User_id;

==========  ======  ======  ======  ======
name         语文    数学    英语     综合
==========  ======  ======  ======  ======
wwxiong     null    null    null    null
dracarysX   20      30      40      60
xhq         70      80      90      100
==========  ======  ======  ======  ======

批量操作
-----------

批量操作可以参考 **<mysql批量操作.md>**

常见操作
-----------

查询数据库中所有表名::

    select table_name from information_schema.`tables` where table_schema = '数据库名';

查询表的所有schema::

    select column_name from information_schema.`COLUMNS` where TABLE_NAME = '表名';
