
from PyMysql import DoMysql
mysql = DoMysql()#实例化对象
sql = 'SELECT username FROM app_user WHERE id = 1;'
result = mysql.fetchAll(sql)
print(result)

sql = 'insert into `app_user`(`username`,`age`,`phone`,`email`,`info`) values("testname6","21","1361361623","243111511@qq.com","这个家伙很懒!!!")'
insert = mysql.insert_one(sql)
print(insert)
# 关闭连接
mysql.close()

# #插入一条数据
#     sql = 'insert into `user`(`mobile`,`passwd`) values("13100010000","123456")'
#     result = mysql.insert_one(sql)
#     print(result) #返回插入数据的条数(1)
#
#     #插入多条数据
#     datas = [
#         ("13100010001","111111"),
#         ("13100010002","666666")
#     ]
#     sql = 'insert into `user`(`mobile`,`passwd`) values(%s,%s)'
#     result = mysql.insert_many(sql,datas)
#     print(result) #返回插入数据的条数(2)
#
#     #查询数据
#     sql = 'select * from user'
#     result = mysql.fetchAll(sql) #返回列表,如果多条数据，列表中嵌套字典
#     for item in result:
#         print(item.get('mobile')) #循环列表，输出mobile值
#
#     #关闭连接
#     mysql.close()