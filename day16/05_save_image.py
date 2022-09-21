"""
二进制文件存取
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

# 存入图片
# with open("m.jpeg",'rb') as fr:
#     data = fr.read()
# sql = "update class set image=%s where id =1;"
# cur.execute(sql,[data])
# db.commit()

# 取出图片
sql = "select name,image from class where id=1;"
cur.execute(sql)
name,image = cur.fetchone()
with open(name+".jpeg",'wb') as fw:
    fw.write(image)


cur.close()  # 关闭数据操作
db.close()  #　断开与数据库连接

