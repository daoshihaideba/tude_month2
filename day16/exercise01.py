"""
练习:
创建一个数据库 dict 使用utf8
在该数据库下创建一个数据表 words 字段如下
id int     word char(30)      mean varchar(512)

将dict.txt文本中的单词插入到该数据表

思路 :  从dict.txt里整理数据
       将整理好的数据写入数据库
create database dict charset=utf8;
create table words (id int primary key auto_increment,word char(30),mean varchar(512));
"""
import pymysql


class Dict:
    # 数据库链接 产生游标和连接对象
    def __init__(self):
        self.kwargs = {
            "user": "root",
            "password": "123456",
            "database": "dict",
            "charset": "utf8"
        }
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()  # 关闭数据操作
        self.db.close()  # 断开与数据库连接

    def get_data(self):
        # 整理出data  --> [(word,mean),()..........]
        data = []
        fr = open("dict.txt")
        for line in fr:
            word, mean = line.split(' ', 1)
            data.append((word, mean.strip()))
        fr.close()
        return data

    # 干事
    def insert_words(self):
        data = self.get_data()  # 获取数据
        try:
            sql = "insert into words (word,mean) values (%s,%s);"
            self.cur.executemany(sql, data)  # 执行次数取决于data
        except Exception as e:
            print(e)
            self.db.rollback()  # 事务回滚
        else:
            self.db.commit()  # 提交事务


if __name__ == '__main__':
    dict = Dict()
    dict.insert_words()
    dict.close()
