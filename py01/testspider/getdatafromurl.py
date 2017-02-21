# coding=utf8


import requests
import pymysql

url = 'http://www.baidu.com'

data = requests.get(url)

encoding = requests.utils.get_encodings_from_content(data.content)[0]

print 'coding: ', encoding
data.encoding = encoding

print data.text



# conn

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test')

print conn

# create table
sql = 'create table testdata(id int primary key, content varchar(255)); '

cur = conn.cursor()
try:
    print  cur.execute(sql)
except pymysql.err.InternalError, e:
    print 'wrong:', e

sql = 'insert into testdata(id, content) values('+str(123)+', '+data.text+' )'

cur.execute(sql)

cur.close()
conn.close()