聚合练习 books
1. 统计每位作家出版图书的平均价格
select author,avg(price) from books group by author;

2. 统计每个出版社出版图书数量
select press,count(*) from books group by press;

3. 统计同一时间出版图书的最高价格和最低价格
select publish_time,max(price),min(price) from books
group by publish_time;

4. 筛选出那些出版过超过50元图书的出版社，
并按照其出版图书的平均价格降序排序

select press,avg(price)
from books
group by press
having max(price) > 50
order by avg(price) desc;


表关系设计练习 exercise库：
根据所学 用户朋友圈表内容表，使其合理，假设现有如下内容需要存储：
姓名  密码  电话  图片 内容  地点 时间 点赞  评论
能够表达出 朋友圈谁发的都有谁点赞评论了
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(64),
tel char(16)
);

create table friends(
id int primary key auto_increment,
image char(50),
content varchar(1024),
time datetime ,
address varchar(50),
user_id int ,
foreign key(user_id) references user(id)
);

create table like_comment(
id int primary key auto_increment,
`like` bit,
comment text,
user_id int ,
friends_id int ,
foreign key(user_id) references user(id),
foreign key(friends_id) references friends(id)
);