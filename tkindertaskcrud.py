import tkinter as tk
from tkinter import ttk,messagebox
import sqlite3
 
con = sqlite3.connect("products.db")
cursor=con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        stock INTEGER
    )
''')

con.commit()

def insert():
        
        name,price,stock=name_var.get(),price_var.get(),stock_var.get()
        cursor.execute("INSERT INTO product (name,price,stock) VALUES (?,?,?)",
                   (name, price, stock))        
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
                tree.insert("",tk.END,values=row)

def update():
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])['values']  
 
        name = name_var.get()
        price = price_var.get()
        stock = stock_var.get()

        cursor.execute("UPDATE product SET name=?, price=?, stock=? WHERE id=?", (name, price, stock, item[0]))
        con.commit()
        read()
 
        name_var.set("")
        price_var.set("")
        stock_var.set("")
    
    else:
          messagebox.showwarning("message",f"please select the item u want to update")

def on_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])['values']
        name_var.set(item[1])
        price_var.set(item[2])
        stock_var.set(item[3])

 
def delete():
        seleted=tree.selection()
        if seleted:
            item=tree.item(seleted[0])['values']
            cursor.execute("DELETE FROM product WHERE id=?",(item[0],))
            con.commit()
            read()
        else:
          messagebox.showwarning("message",f"please select the item u want to delete")

root=tk.Tk()
root.title("crud")

name_var=tk.StringVar()
price_var=tk.StringVar()
stock_var=tk.StringVar()
 
tk.Label(root,text="NAME").pack()
tk.Entry(root,width=30,textvariable=name_var).pack()
 
tk.Label(root,text="PRICE").pack()
tk.Entry(root,width=30,textvariable=price_var).pack()  

tk.Label(root,text="STOCK").pack()
tk.Entry(root,width=30,textvariable=stock_var).pack()  
 
tk.Button(root,text="add",command=insert).pack(pady=5)
tk.Button(root,text="update",command=update).pack(pady=5)
tk.Button(root,text="delete",command=delete).pack(pady=5)
 
 
column=["id","name","price","stock"]
tree=ttk.Treeview(root,columns=column,show="headings")
for col in column:
       tree.heading(col,text=col)
tree.pack(fill=tk.BOTH,expand=True)
read()
tree.bind("<<TreeviewSelect>>", on_select)
root.mainloop()