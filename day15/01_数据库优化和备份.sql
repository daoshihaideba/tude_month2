查看引擎
show engines;

hobby 表引擎更改
alter table hobby engine=myisam;


--explain 检测  看type
explain  select * from class;
explain  select * from class where id=2;

--表数据复制 : 不会复制任何索引，新的数据表与原数据表没有任何关系
create table student
select id,name,age,score from class where score>80;


数据库备份恢复
终端 ： mysqldump -u root -p stu > stu.sql
删库 ： drop database stu;
创建新库： create database stu charset=utf8;
终端 : mysql -u root -p stu < stu.sql








