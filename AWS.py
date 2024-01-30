import mysql.connector

myc = mysql.connector.connect(
    host = 'database-1.chnkmcdg0mlh.ap-south-1.rds.amazonaws.com',
    user = 'admin',
    password = '12345678'
)
print(myc)


