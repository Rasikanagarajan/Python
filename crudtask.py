import sqlite3

class Empl:
    def __init__(self, db="employee.db"):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS employees")
        self.cursor.execute('''CREATE TABLE employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                emailid TEXT NOT NULL,
                age INTEGER,
                designation TEXT NOT NULL,
                salary INTEGER 
        )''')
        self.con.commit()

    def insert(self, name, emailid, age, designation, salary):
        self.cursor.execute(
            "INSERT INTO employees (name, emailid, age, designation, salary) VALUES (?,?,?,?,?)",(name, emailid, age, designation, salary)
        )
        self.con.commit()
        print("Data inserted")

    def read(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        if rows:
            for i in rows:
                print(i)
        else:
            print("Table empty")

    def update(self, emailid, designation, salary):
        self.cursor.execute(
            "UPDATE employees SET designation=?, salary=? WHERE emailid=?",
            (designation, salary, emailid)
        )
        self.con.commit()
        print("Data updated")

    def delete(self, emailid):
        self.cursor.execute("DELETE FROM employees WHERE emailid=?", (emailid,))
        self.con.commit()
        print("Data deleted")

    def close(self):
        self.con.close()


def main():
    dbs = Empl()

    while True:
        print("1. Insert")
        print("2. View")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter the choice: ")

        if choice == "1":
            name = input("Enter your Name: ")
            emailid = input("Enter your Email ID: ")
            age = input("Enter your Age: ")
            designation = input("Enter your Designation: ")
            salary = input("Enter your Salary: ")
            dbs.insert(name, emailid, age, designation, salary)

        elif choice == "2":
            dbs.read()

        elif choice == "3":
            emailid = input("Enter your Email ID : ")
            designation = input("Enter your Designation: ")
            salary = input("Enter your Salary: ")
            dbs.update(emailid, designation, salary)

        elif choice == "4":
            emailid = input("Enter Email ID to delete: ")
            dbs.delete(emailid)

        elif choice == "5":
            dbs.close()
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
