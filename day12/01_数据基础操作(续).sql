--where 子句
select * from class where age+1=18;

--真除法
select * from class where age/2=9;

--取整除法
select * from class where age div 2=9;

--比较运算符  = 表示逻辑相等
select * from class where sex='m';
select * from class where score>80;

--字符串不区分大小写
select * from class where name="lily";

--查询时区分字母大小写
select * from class where binary name="Lily";

--错误演示 ： 分数大于70小于80的  不支持连续小于 或者 大于写法
select * from class where 70 < score < 80;

--分数在 70到80 之间
select * from class where score between 70 and 80;
select * from class where score not between 70 and 80;

--数据在集合范围内的
select * from class where age in (16,18,20);
select * from class where age not in (16,18,20);

判断是否为null 必须使用is
select * from class where sex is null;
select * from class where sex is not null;

分数大于80的男生
select * from class where sex="m" and score > 80;

--修改操作
update class set score=86,age=19 where name="Abby";

所有人增长1岁
update class set age=age+1;

删除分数小于60的记录
delete from class where score < 60;







