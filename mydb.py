import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Roots1866'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database

cursorObject.execute("CREATE DATABASE kobiedevdb")

print("All Done!")
