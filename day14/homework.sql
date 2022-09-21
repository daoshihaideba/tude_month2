将books表拆分为三张表（图书   作家   出版社）,
自行设计表之间的关系，然后写出创建语句

create table author(
id int primary key auto_increment,
name varchar(30),
gender char
);

create table press(
id int primary key auto_increment,
name varchar(256),
address varchar(256),
tel char(16)
);

create table book(
id int primary key auto_increment,
name varchar(256),
price float,
author_id int,
press_id int,
foreign key (author_id) references author(id),
foreign key (press_id) references press(id)
);

create table author_press(
id int primary key auto_increment,
author_id int,
press_id int,
foreign key (author_id) references author(id),
foreign key (press_id) references press(id)
);
