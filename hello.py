import mysql.connector

print("hello ubuntu")
for i in range(10):
    print(i)

db = mysql.connector.connect(host='localhost',user='root',password='0000',port='3306')

cursor= db.cursor()

cursor.execute('show databases')

for i in cursor:
    print(i)