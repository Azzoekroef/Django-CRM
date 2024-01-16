import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = "Aspire.1234"
)

#siapkan objek kursor
cursorObject = dataBase.cursor()

#buat database
cursorObject.execute("CREATE DATABASE elderco")

print("selesai!")
