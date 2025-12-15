import sqlite3
 
class person:
    def __init__(self,db="emp.db"):
        self.con=sqlite3.connect(db)
        self.cursor=self.con.cursor()
        self.create_table()
   
    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS emps")
        self.cursor.execute('''CREATE TABLE emps(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
                            )
        ''')
        self.con.commit()
    def insert(self,name,age):
        self.cursor.execute("INSERT INTO emps (name,age) VALUES (?,?)",(name,age))
        self.con.commit()
        print("data inserted")
    def read(self):
        self.cursor.execute("SELECT * FROM emps")
        rows=self.cursor.fetchall()
        if rows:
            for i in rows:
                print(i)
        else:
            print("table empty")
 
    def update(self,name,age):
        self.cursor.execute("UPDATE emps SET age=? WHERE name=?",(age,name))
        self.con.commit()
        print("data updated")
    def delete(self,name):
        self.cursor.execute("DELETE FROM emps WHERE name=?",(name,))
        self.con.commit()
        print("data deleted ")
    def colse(self):
        self.con.close()
       
 
def main():
    dbs=person()
 
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
            dbs.insert(name,age)
        elif c=="2":
            dbs.read()
 
        elif c =="3":
            name=input("enter name:")
            age=input("enter age")
            dbs.update(name,age)
        elif c=="4":
            name=input("Enter name:")
            dbs.delete(name)
        elif c=="5":
            dbs.colse()
            break
        else:
            print("invalid choice")
if __name__=="__main__":
    main()
           
   