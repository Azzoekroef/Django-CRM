import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ""
)

#siapkan objek kursor
cursorObject = dataBase.cursor()

#buat database
cursorObject.execute("CREATE DATABASE elderco")

print("selesai!")
