--修改结尾符号
delimiter $$

如果函数中有写操作语句那么函数调用只能是 select func01() 而不能
作为值提供者放在where中
create function func01() returns int
begin
    update class set score=99 where id=1;
    return (select score from class where id=1);
end $$

delimiter ;

定义局部变量定义和赋值
declare s1 int;
declare s1 int default 0;  -- 局部变量初始值
declare s1,s2 int;
set s1=(select score from class where name=uname);
select score from class where name=uname into s1;


delimiter $$

create function func02(uname varchar(20)) returns int
begin
    declare s1 int;
    select score from class where name=uname into s1;
    return s1;
end $$

delimiter ;

存储过程

delimiter $$
create procedure proc01()
begin
    delete from class where score < 60;
    delete from hobby where id > 10;
    select * from class order by score;
    update class set score=94 where id =1;
end $$
delimiter ;


delimiter $$
create procedure proc_in(IN a int)
begin
    select a;
    set a=10000;
    select a;
end $$
delimiter ;

set @n=1;
call proc_in(@n);


delimiter $$
create procedure proc_out(OUT a int)
begin
    select a;
    set a=10000;
    select a;
end $$
delimiter ;

set @n=1;
call proc_out(@n);


查看创建语句
show create function func01;
show create procedure proc01;

查看所有函数或者存储过程
show procedure status  where db="stu";
show function status  where db="stu";

删除函数或存储过程
drop function func01;
drop procedure proc01;






