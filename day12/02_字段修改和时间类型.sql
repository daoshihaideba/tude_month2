--增加新字段 也可以写约束
alter table hobby add phone char(10) after price;

--删除字段
alter table hobby  drop level;

修改字段数据类型或约束 ： 修改后的类型必须能够容纳现有的数据
alter table hobby modify  phone char(16);

--将原有字段替换
alter table hobby change  phone tel char(16) default 112;

--修改表名
alter table hobby rename hobby_class;


创建时间类型数据表
create table marathon(
id int primary key auto_increment,
athlete char(30) not null,
birthday date,
r_time datetime comment "报名时间",
performance time
);

insert into marathon values
(1,"尼古拉斯","1996-10-22","2022-4-1 10:26:55","2:45:33"),
(2,"托尼","2000/1/2","2022-4-3 19:6:35","2:25:19");

insert into marathon values
(3,"杰克","1998-2-28","2022-4-2 11:21:51","2:43:10");

时间比较大小
select * from marathon where  birthday>="2000-01-01";

成绩在两个半小时以内的运动员
select * from marathon where performance <= "2:30:00";


--now() 函数
select * from marathon where r_time < now();

--作为字段默认值
alter table marathon modify r_time datetime default now();

insert into marathon (athlete,birthday) values
("夸父","1999-1-1");

--date()函数 : 提取日期
select athlete, date(r_time) from marathon;

select athlete, date(r_time) from marathon
where date(r_time) < "2022-04-05";

--datediff() : 获取日期差
select datediff("2022-04-05","2022-04-01");

