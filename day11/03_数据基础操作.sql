--插入数据
insert into class values
(1,"Lily",18,'w',90),
(2,"Tom",17,'m',68),
(3,"James",17,'m',79);

--查看数据表信息
select * from class;

insert into class (name,age,sex) values
("Abby",16,'w'),
("Alex",18,'m');

insert into class (name,age,sex,score) values
("Emma",17,'w',72),
("Joy",18,'m',88);

insert into class (name,age,score) values
("Tonny",17,63),
("Baron",19,83);

insert into class (name,age,sex,score) values
("Eva",17,'w',85);

--hobby数据表插入数据

insert into hobby (name,hobby,level,price,remark) values
("Lily","sing,dance","B",53000.888,"骨骼惊奇练舞奇才"),
("Lucy","draw","A",22000,"少年达芬奇");

insert into hobby (name,hobby,level,price,remark) values
("Joy","draw,sing","C",49800,"还行吧"),
("Levi","dance","B",19800,"基础扎实");

insert into hobby (name,hobby,level,price) values
("Tom","dance,draw","B",50000),
("Sunny","sing","C",9900),
("Alex","sing,draw","A",54900);


--基础查询

select * from class;
select name,score from class;

