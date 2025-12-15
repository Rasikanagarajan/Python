import sqlite3
 
try:
    con=sqlite3.connect("std.db")
    cursor=con.cursor()
    print("db connected")
except sqlite3.Error as e:
    print(e)
else:
    cursor.execute("SELECT sqlite_version();")
    print(cursor.fetchone()[0])
finally:
    con.close()
    print("connection end")
