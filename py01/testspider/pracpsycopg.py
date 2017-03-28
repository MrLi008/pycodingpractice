# coding=utf8





import psycopg2 as psy

try:

    conn = psy.connect(database='1',
                       user='1',
                       password='1',
                       host='11.2.8.70',
                       port=5432)

    if conn in (None, ):
        print 'faild'
    else:
        print 'successs'

except Exception,e:
    print e