-*- coding: utf-8 -*-_
!/bin/python


import csv
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


mysql_host = '127.0.0,1'
mysql_user = 'test'
mysql_passwd = 'yourpw'
dbname = 'db_table'

def main():
	# 连接数据库
	conn = MySQLdb.connect(
		host = mysql_host,
	    user = mysql_user,
		passwd = mysql_passwd,
		charset='utf8',
	)
	cur = conn.cursor()
 
	# 以写的方式打开 csv 文件并将内容写入到w
	f = open("./out.csv", 'w')
	write_file = csv.writer(f)
	
    #channel_list = [2009, 2011]
	#for channel in channel_list:
	#print("query channel: %d" % channel)
	# 从表里面读出数据，写入到 csv 文件里
	for i in range(10):
		for j in range(100):
			print "query collect: %d, tableNo: %d" % (i, j)
			
			#str(j).rjust(2,'0') 按照00~99格式
			dbstr = "select * from db_%d.t_table_%s where create_time between '2020-04-13 00:00:00' and '2020-04-20 00:00:00' and F_channel_id in ( 2007, 2009, 2011, 2023 ) order by create_time" % (i,  str(j).rjust(2,'0') )
			cur.execute( dbstr )
			while True:
				row = cur.fetchone()    #获取下一个查询结果集为一个对象
				if not row:
					break
				write_file.writerow(row)    #csv模块方法一行一行写入
	f.close()
 
	# 关闭连接
	if cur:
		cur.close()
	if conn:
		conn.close()
 
 
if __name__ == '__main__':
	main()
	print("Exec finish, please check\n")


