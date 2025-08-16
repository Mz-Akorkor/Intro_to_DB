import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL1918",
    database="alx_book_store"
)
print("Connected to:", mydb.server_info)