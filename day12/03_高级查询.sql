模糊查询
--% 表示任意0个或者多个字符
select * from class where name like "J%";

--_表示一个字符
select * from class where name like "____";

--集合数据类型的查找
select * from hobby where hobby like "%draw%";


as 重命名

select name as 姓名 , score as 分数  from class as cls;

--as 可以省略但是不推荐
select name  姓名 , score  分数  from class  cls;


--排序 : 数字  时间
select * from class where sex='m' order by score desc;
select * from marathon order by performance;

多字段排序
select * from class order by age,score desc;

班级中分数最低的3位女生
select * from class where sex='w' order by score limit 3;

--分数最高的男生
select * from class where sex='m'
order by score desc
limit 1;

--分数第二的男生 offset 表示跳过1个
select * from class where sex='m'
order by score desc
limit 1 offset 1;

update class set score=93 where sex='m' limit 1;

union 联合查询

select name,age,sex from class where sex='m'
union
select name,age,score from class where score>80;

select name,age,score from class
union
select name,hobby,price from hobby;

--不会去除重复的查询记录
select * from class where sex='m'
union all
select * from class where score>80;



子查询语句
--子查询语句作为表，必须起名字
select * from  (select * from class where sex='m') as man
where score>80;

--子查询作为值提供
select * from class
where score > (select score from class where name="Joy");

--class 表中谁报了兴趣班 作为集合时可以查询一个字段的多个值
select * from class
where name in (select name from hobby);



