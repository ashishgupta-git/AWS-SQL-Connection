import mysql.connector

myc = mysql.connector.connect(
    host = 'database-1.cu41lbmug8so.ap-south-1.rds.amazonaws.com',
    user = 'admin',
    password = '12345678'
)

mycursor = myc.cursor()
mycursor.execute('show databases')

for x in mycursor:print(x)