--创建数据表
create table student (
name char(20),
age tinyint,
sex enum("男","女","其他"),
hight float(4,1)
);

--查看数据库的表
show tables;

--创建class数据表
create table class (
id int primary key auto_increment,
name varchar(30) not null,
age tinyint unsigned,
sex enum('m','w','o'),
score float default 0
);

CREATE TABLE `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  `sex` enum('m','w','o') DEFAULT NULL,
  `score` float DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--创建hobby数据表
create table hobby (
id int primary key auto_increment,
name varchar(30) not null,
hobby set("sing","dance","draw"),
level char(1) comment "评级",
price decimal(7,2),
remark text
);

--查看字段信息
desc class;
show full columns from hobby;

--查看数据表创建方法
show create table class;

--删除数据表
drop table student;
