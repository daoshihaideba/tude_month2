创建一个视图
create view good_stu as
select name,age,sex,score from class where score>=80;

多表视图 : 通常只进行查询操作而不会进行写操作
create view dept_person as
select name,age,dname,salary from person left join dept
on dept.id = person.dept_id
where salary > 15000;

查看数据库下所有表信息
show full tables in stu;

可能替换同名的视图
create or replace view good_stu as
select name,age,sex,score from class where score>=85;

修改视图数据
alter view good_stu as
select name,age,sex,score from class where score>=85;

删除视图
drop view if exists dept_person;

