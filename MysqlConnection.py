import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='',port='3306')

cursor= db.cursor()

cursor.execute('show databases')

for i in cursor:
    print(i)
