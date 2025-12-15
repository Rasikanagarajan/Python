import mysql.connector

class mydb:
    def __init__(self):
        self.db=mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        print("connect")
        self.cursor=self.db.cursor()
        self.setup()
    def setup(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS emp")
        self.cursor.execute("USE emp")

        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS emps(
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            name VARCHAR(50),
                            age INT,
                            city VARCHAR(50)
                            )
    """)
    def insert(self,name,age,city):
        sql="INSERT INTO emps (name,age,city) VALUES (%s, %s, %s)"
        v=(name,age,city)
        self.cursor.execute(sql,v)
        self.db.commit()
        print("data inserted")
    def view(self):
        self.cursor.execute("SELECT * FROM emps")
        r=self.cursor.fetchall()

        if len(r)==0:
            print("empty")
        else:
            for i in r:
                print("id  ",i[0],"name ",i[1],"age ",i[2],"city ",i[3])
    def update(self,id,name,age,city):
        sql="UPDATE emps  SET name=%s, age=%s, city=%s WHERE id=%s"
        v=(name,age,city,id)
        self.cursor.execute(sql,v)
        self.db.commit()
        print("updated")
    def delete(self,id):
        sql="DELETE FROM emps WHERE id=%s"
        v=(id,)
        self.cursor.execute(sql,v)
        self.db.commit()
        print("deleted")
dbs=mydb()
while True:
        print("1 insert\n")
        print("2. view\n")
        print("3.update\n")
        print("4.delete\n")
        print("5.exit\n")
 
        c=input("enter choice:")
 
        if c=="1":
            name=input("enter name:")
            age=input("enter age")
            city=input("Enter the city")

            dbs.insert(name,age,city)
        elif c=="2":
            dbs.view()
 
        elif c =="3":
            id=input("Enter your id:")
            name=input("enter name:")
            age=input("enter age")
            city=input("Enter the city:")
            dbs.update(id,name,age,city)
        elif c=="4":
            id=input("Enter id:")
            dbs.delete(id)
        elif c=="5":
            break
        else:
            print("invalid choice")