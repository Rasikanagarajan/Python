import mysql.connector

class practice:
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
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS std")
        self.cursor.execute("USE std")

        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS stds(
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            name VARCHAR(50),
                            cls VARCHAR(50),
                            mark INT,
                            school VARCHAR(50)
                            )
    """)
    def insert(self,name,cls,mark,school):
        sql="INSERT INTO stds (name,cls,mark,school) VALUES (%s, %s, %s, %s)"
        v=(name,cls,mark,school)
        self.cursor.execute(sql,v)
        self.db.commit()
        print("data inserted")
    def view(self):
        self.cursor.execute("SELECT * FROM stds")
        r=self.cursor.fetchall()

        if len(r)==0:
            print("empty")
        else:
            for i in r:
                print("id  ",i[0],"name ",i[1],"cls ",i[2],"mark ",i[3],"school ",i[4])
    def update(self,id,name,cls,mark,school):
        sql="UPDATE stds  SET name=%s, cls=%s, mark=%s, school=%s WHERE id=%s"
        v=(name,cls,mark,school,id)
        self.cursor.execute(sql,v)
        self.db.commit()
        print("updated")
    def delete(self,id):
        sql="DELETE FROM stds WHERE id=%s"
        v=(id,)
        self.cursor.execute(sql,v)
        self.db.commit()
        print("deleted")
dbs=practice()
while True:
        print("1 insert\n")
        print("2. view\n")
        print("3.update\n")
        print("4.delete\n")
        print("5.exit\n")
 
        c=input("enter choice:")
 
        if c=="1":
            name=input("enter name:")
            cls=input("enter class")
            mark=input("Enter mark")
            school=input("Enter school")
            dbs.insert(name,cls,mark,school)
        elif c=="2":
            dbs.view()
 
        elif c =="3":
            id=input("Enter your id:")
            name=input("enter name:")
            cls=input("enter class")
            mark=input("Enter mark")
            school=input("Enter school")
            dbs.update(id,name,cls,mark,school)
        elif c=="4":
            id=input("Enter id:")
            dbs.delete(id)
        elif c=="5":
            break
        else:
            print("invalid choice")