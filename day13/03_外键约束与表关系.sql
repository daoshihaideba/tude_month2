--部门表  主表
CREATE TABLE dept (
  id int PRIMARY KEY auto_increment,
  dname VARCHAR(50) not null
);

insert into dept values
(1,"技术部"),
(2,"销售部"),
(3,"市场部"),
(4,"行政部"),
(5,'财务部'),
(6,'总裁办公室');

--员工表
CREATE TABLE person (
  id int PRIMARY KEY AUTO_INCREMENT,
  name varchar(32) NOT NULL,
  age tinyint unsigned,
  salary decimal(8,2),
  dept_id int
);

insert into person values
(1,"Lily",29,20000,2),
(2,"Tom",27,16000,1),
(3,"Joy",30,28000,1),
(4,"Emma",24,8000,4),
(5,"Abby",28,17000,3),
(6,"Jame",32,22000,3);

insert into person values
(7,"Alex",26,15000,8);

从表增加外键约束 : 创建外键约束 同时会对关系字段自动创建一个普通索引
alter table person add
constraint dept_fk
foreign key (dept_id)
references dept(id);

删除外键约束 ：索引并不会随之删除
alter table person drop foreign key dept_fk;

级联动作
从表关联你你就不要动
alter table person add
constraint dept_fk
foreign key (dept_id)
references dept(id);

主表动从表跟着动
alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete cascade on update cascade;

主表动从表都成空
alter table person add
foreign key(dept_id)
references dept(id)
on delete set null on update set null;

多对多关系表达
CREATE TABLE athlete (
  id int primary key AUTO_INCREMENT,
  name varchar(30),
  age tinyint NOT NULL,
  country varchar(30) NOT NULL
);

CREATE TABLE sports (
  id int primary key AUTO_INCREMENT,
  sport varchar(30) NOT NULL
);

CREATE TABLE athlete_sports (
   id int primary key auto_increment,
   aid int NOT NULL,
   sid int NOT NULL,
   FOREIGN KEY (aid) REFERENCES athlete (id),
   FOREIGN KEY (sid) REFERENCES sports (id)
);

--关系表中也可以增加一定的数据信息
alter table athlete_sport add ranking int;
