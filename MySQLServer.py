import os
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database="alx_book_store"
    )
    if connection.is_connected():
        print("Connected to MySQL server successfully!")
except Error as e:
    print("Error while connecting to MySQL:", e)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()