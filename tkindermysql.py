import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


def connect_db():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="test"     
        )
        return con

    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", f"Cannot connect to MySQL:\n{err}")


con = connect_db()
cursor = con.cursor()

# Create table inside test DB
cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        price FLOAT,
        stock INT
    )
""")
con.commit()


def insert():
    name = name_var.get()
    price = price_var.get()
    stock = stock_var.get()

    if name == "" or price == "" or stock == "":
        messagebox.showwarning("Warning", "Fill all fields")
        return

    cursor.execute(
        "INSERT INTO product(name, price, stock) VALUES (%s, %s, %s)",
        (name, price, stock)
    )
    con.commit()
    read()

    name_var.set("")
    price_var.set("")
    stock_var.set("")


def read():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM product")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


def update():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select an item to update")
        return

    item = tree.item(selected[0])["values"]

    cursor.execute(
        "UPDATE product SET name=%s, price=%s, stock=%s WHERE id=%s",
        (name_var.get(), price_var.get(), stock_var.get(), item[0])
    )

    con.commit()
    read()
    name_var.set("")
    price_var.set("")
    stock_var.set("")


def delete():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select an item to delete")
        return

    item = tree.item(selected[0])["values"]

    cursor.execute("DELETE FROM product WHERE id=%s", (item[0],))
    con.commit()
    read()


def on_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])["values"]
        name_var.set(item[1])
        price_var.set(item[2])
        stock_var.set(item[3])



root = tk.Tk()
root.title("MySQL CRUD App (test DB)")

name_var = tk.StringVar()
price_var = tk.StringVar()
stock_var = tk.StringVar()

tk.Label(root, text="NAME").pack()
tk.Entry(root, width=30, textvariable=name_var).pack()

tk.Label(root, text="PRICE").pack()
tk.Entry(root, width=30, textvariable=price_var).pack()

tk.Label(root, text="STOCK").pack()
tk.Entry(root, width=30, textvariable=stock_var).pack()

tk.Button(root, text="Add", command=insert).pack(pady=5)
tk.Button(root, text="Update", command=update).pack(pady=5)
tk.Button(root, text="Delete", command=delete).pack(pady=5)

columns = ["id", "name", "price", "stock"]
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack(fill=tk.BOTH, expand=True)

tree.bind("<<TreeviewSelect>>", on_select)

read()
root.mainloop()
