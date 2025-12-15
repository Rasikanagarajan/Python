import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",     
        database="test"   
    )

    print("Connected Successfully!")

except mysql.connector.Error as err:
    print("Error:", err)
