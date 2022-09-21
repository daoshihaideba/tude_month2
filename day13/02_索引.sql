--创建表时直接添加索引
create table index_test(
id int auto_increment,
name varchar(30),
primary key (id),
unique nameIndex(name)
);

同

create table index_test(
id int primary key auto_increment,
name varchar(30) unique,
);

后添加一个普通索引
create index name on class(name);

查看索引
desc class;
show create table class;
show index from class;


删除索引
drop index nameIndex on index_test;


