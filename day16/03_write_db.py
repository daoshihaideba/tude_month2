"""
数据库写操作
* 数据库写操作时会自动开启事务
* 如果操作的数据表不支持事务 execute 执行语句会自动生效
* 如果操作的数据表支持事务 execute 执行后需要commit  rollback
"""
import pymysql

# 参数字典
kwargs = {
    "user": "root",
    "password": "123456",
    "database": "stu",
    "charset": "utf8"
}

# 连接数据库
db = pymysql.connect(**kwargs)

# 生成游标对象 : 用来使用SQL语句操作数据得到数据操作结果的对象
cur = db.cursor()

# 数据库写操作  insert  update  delete
# score = 80
# id = 2
# try:
#     sql = "update class set score=%s where id=%s;" #传值位置统一写%s
#     cur.execute(sql,[score,id]) # 给sql语句传值 不能传递表名字段名符号等
#     sql = "delet from class where score < 60;"
#     cur.execute(sql)
# except Exception as e:
#     print(e)
#     db.rollback() # 事务回滚
# else:
#     db.commit() # 提交事务

data = [
    ("zhang",17,'m',66),
    ("wang",18,'w',67),
    ("lisi",17,'w',68)
]
try:
    sql="insert into class (name,age,sex,score) " \
        "values (%s,%s,%s,%s);"
    cur.executemany(sql,data) # 执行次数取决于data
except Exception as e:
    print(e)
    db.rollback() # 事务回滚
else:
    db.commit() # 提交事务


cur.close()  # 关闭数据操作
db.close()  #　断开与数据库连接

