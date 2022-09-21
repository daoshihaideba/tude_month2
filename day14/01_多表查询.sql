多表查询在选择字段时如果字段名重复需要使用 表名.的方式引出字段名
select age,score,hobby,price from class,hobby;
select class.name,score,hobby,price from class,hobby;

表明重命名往往可以简化书写
select c.name,c.score,h.hobby,h.price
from class as c,hobby as h;

即使两张表没有建立外键约束，如果我们找到一个切入点也可以进行多表查询
select c.name,c.score,h.name,h.hobby,h.price
from class as c,hobby as h
where c.name = h.name;

但是如果两张表有明确的外键关联，那么表关系几乎是不需要思考,
就是使用外键关系
select  person.name,person.salary,dept.dname
from person,dept
where person.dept_id = dept.id;


--where功能冗杂，有些数据容易无法筛选出来
select  person.name,person.salary,dept.dname
from person,dept
where person.dept_id = dept.id and person.salary>=20000;

内连接
select  p.name,p.salary,d.dname
from person as p inner join dept as d
on p.dept_id = d.id
where p.salary>=20000;

左连接 获取person表全部数据和dept表具有匹配关系的数据进行查询
select  p.name,p.salary,d.dname
from person as p left join dept as d
on p.dept_id = d.id
where p.salary>=20000;

右连接  统计每个部门人数   部门名称  人数
select dept.dname,count(person.name)
from  person right join dept
on person.dept_id = dept.id
group by dept.dname;










