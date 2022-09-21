"""
pymysql  连接数据库
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

# 数据库读写


cur.close()  # 关闭数据操作
db.close()  #　断开与数据库连接

