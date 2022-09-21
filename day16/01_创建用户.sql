
创建新用户
create user "aid"@"%" identified by "123";

使用新用户访问数据库
mysql -u aid -p

分配权限
--identified by "123" 8.0版本后就不要了
--with grant option表示该用户是否可以继续向下再分配自己的权限 写就是可以
grant select,update on stu.class to "aid"@"%"
identified by "123"
with grant option;

grant insert on stu.class to "aid"@"%"
identified by "123"
with grant option;

删除权限 (删除权限时候 stu.class的写法要和添加权限时一致)
revoke update on stu.class from "aid"@"%";

--删除用户
drop user "aid"@"%";


