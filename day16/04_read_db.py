"""
数据库读操作
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

# 数据库读 select
sql = "select name,age,score from class where score>%s;"
cur.execute(sql,[70])

# 获取查询结果
# one = cur.fetchone()
# print(one)
#
# many = cur.fetchmany(2)
# print(many)
#
# all = cur.fetchall()
# print(all)

# 迭代获取
for row in cur:
    print(row)

cur.close()  # 关闭数据操作
db.close()  #　断开与数据库连接

