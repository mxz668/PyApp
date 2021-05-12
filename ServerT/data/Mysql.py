
import pymysql

# 打开数据库连接
db = pymysql.Connect(host='localhost', port=3306, user='root', passwd='root', db='test', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO input(name,age)  VALUES (%s, %s)"
val = ('Mohan', 20)
try:
   # 执行sql语句
   cursor.execute(sql, val)
   # 提交到数据库执行
   db.commit()
except Exception as e:
   print(e.args)
   print(str(e))
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()