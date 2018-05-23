# Mysql批量操作

最近在工作中做一些`mysql sql`级别的性能优化的时候，把之前逻辑中的循环插入，更新的操作替换成了批量的插入，更新。测试性能确实带来不小的提升。执行效率高的主要原因是合并后日志量`mysql`的`binlog`和`innodb`的事务让日志）减少了，降低日志刷盘的数据量和频率，从而提高效率。通过合并`SQL`语句，同时也能减少`SQL`语句解析的次数，减少网络传输的IO。

下面是一些基本的批量更新的使用方法（部分是`mysql`特定语法。）。

## 批量插入

### 使用insert into批量插入数据

`mysql`允许我们在一条sql语句中批量插入数据。

```sql
INSERT INTO `Example`(`name`, `age`)
VALUES
('wwxiong', 25),
('teddy', 20),
('teddy bear', 11);
# 可以使用INSERT INTO IGNORE忽略掉中间可能因索引问题无法插入的问题（业务需要时使用。）
```

## 批量更新

### 使用mysql 自带的语句构建批量更新

`mysql`批量更新如果一条条去更新效率是相当的慢, 循环一条一条的更新记录,一条记录`update`一次，这样性能很差，也很容易造成阻塞。

PS：`where`部分不影响代码的执行，但是会提高`sql`执行的效率。确`保sql`语句仅执行需要修改的行数，这里只有3条数据进行更新，而`where`子句确保只有3行数据执行。

```sql
update `example`
set
    age = case id
        when 1 then 20
        when 2 then 21
        when 3 then 22
    name = case id
        when 1 then 'wwx'
        when 2 then 'dracarys'
        when 3 then 'teddy'
end
where id in (20, 21, 22)
# 根据ID更新age，name。例如：当id=1的时候，更新age=20，name='wwx'
```

在500W行数据中测试，`name`字段无索引。更新25条数据测试结果如下。

```sql
#批量更新
UPDATE `wwxiong`
SET `score` = CASE `name`
when 'wwx_59' then 100
when 'wwx_60' then 100
when 'wwx_61' then 100
when 'wwx_62' then 100
when 'wwx_63' then 100
when 'wwx_64' then 100
when 'wwx_65' then 100
when 'wwx_66' then 100
when 'wwx_67' then 100
when 'wwx_68' then 100
when 'wwx_69' then 100
when 'wwx_70' then 100
when 'wwx_71' then 100
when 'wwx_72' then 100
when 'wwx_73' then 100
when 'wwx_74' then 100
when 'wwx_75' then 100
when 'wwx_76' then 100
when 'wwx_77' then 100
when 'wwx_78' then 100
when 'wwx_79' then 100
when 'wwx_80' then 100
when 'wwx_81' then 100
when 'wwx_82' then 100
when 'wwx_83' then 100
end
where `name` in ('wwx_83','wwx_84','wwx_85','wwx_86','wwx_87','wwx_88','wwx_89','wwx_90','wwx_91','wwx_92','wwx_93','wwx_94','wwx_95','wwx_96','wwx_97','wwx_98','wwx_99','wwx_100','wwx_101','wwx_102','wwx_103','wwx_104','wwx_105','wwx_106','wwx_107')
[SQL]
update `wwxiong` set `score` = 100 where `name` = 'wwx_71';
受影响的行: 25
时间: 2.564s
#逐条更新
[SQL]
update `wwxiong` set `score` = 100 where `name` = 'wwx_78';
受影响的行: 1
时间: 2.365s
```

从结果来看，性能大大提示。如果`name`字段有索引的话，那么相对差距就没有那么大了。不过总体上来说批量更新效果更佳。

### 使用INSERT INTO方式更新

`INSERT` 中`ON DUPLICATE KEY UPDATE`的使用。如果您指定了`ON DUPLICATE KEY UPDATE`，并且插入行后会导致在一个`UNIQUE`索引或`PRIMARY KEY`中出现重复值，则执行旧行`UPDATE`。案例如下。

```sql
INSERT INTO `ExamUserAnswer`(
    `ExamUser_id`,
    `ExamSubject_id`,
    `answer`,
    `status`
)
VALUES
    (32, 348, '123', -1),
    (32, 351, '234', -1),
    (32, 1514, '123', -1)
ON DUPLICATE KEY UPDATE
`answer` = VALUES(`answer`),
`status` = IF(`status` = 0, VALUES(`status`), `status`);
#其中ExamUser_id和ExamSubject_id是联合唯一索引。更新的时候可以使用IF来处    理简单逻辑上操作。
```

如果行作为新记录被插入，则受影响行的值为1；如果原有的记录被更新，则受影响行的值为2。

PS：通常，您应该尽量避免对带有多个唯一关键字的表使用`ON DUPLICATE KEY UPDATE`语句操作。因为存在多个唯一索引的时候，联合的和操作会变成或操作，最终执行的效果可能不是我们希望的那样了。

### REPLACE INTO 批量更新

使用`REPLACE`插入一条记录时，如果不重复，`REPLACE`就和`INSERT`的功能一样，如果有重复记录，`REPLACE`就使用新记录的值来替换原来的记录值。 使用`REPLACE`的最大好处就是可以将`DELETE`和`INSERT`合二为一，形成一个原子操作。这样就可以不必考虑在同时使用`DELETE`和`INSERT`时添加事务等复杂操作了。 在使用`REPLACE`时，表中必须有唯一索引，而且这个索引所在的字段不能允许空值，否则`REPLACE`就和`INSERT`完全一样的。

```sql
REPLACE INT `Example`(`id`, `name`, `age`) VALUES(1, 'wwxiong', 25)
#执行结果，先查询是否存在唯一索引id=1的纪录，如果存在删除，然后插入纪录。
```

PS：`REPLACE INTO`的使用需谨慎，有可能会影响主从复制的纪录，因为是删除数据然后新增数据，那么数据的的自增字段就会＋1，然后此时从库的表中自增字段却没有增加，此时把从库提升为主库的时候`AUTO_INCREMENT`比数据库最新id小，那么就会发生`duplicate key error`。在正确理解`REPLACE INTO`行为和副作用的前提下，谨慎使用`REPLACE INTO`。目前暂未在正式环境中使用`REPLACE INTO`的用法。

## 批量删除

批量删除直接使用DELETE操作即可。

```sql
    DELETE FROM `Example` WHERE `name` = 'wwxiong';
    #删除表Example中所有姓名为wwxiong的纪录。
```
