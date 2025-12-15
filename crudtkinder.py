import tkinter as tk
from tkinter import ttk,messagebox
import sqlite3
 
 
con=sqlite3.connect("emp.db")
cursor=con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS emps(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
                            )
        ''')
con.commit()
def insert():
        name,age=name_var.get(),age_var.get()
        cursor.execute("INSERT INTO emps (name,age) VALUES (?,?)",(name,age))
        con.commit()
        read()
        name_var.set("")
        age_var.set("")
    
def read():
        for row in tree.get_children():
               tree.delete(row)
        cursor.execute("SELECT * FROM emps")
        for row in cursor.fetchall():
                tree.insert("",tk.END,values=row)
 
def update():
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])['values']   # (id, name, age)
 
        name = name_var.get()
        age = age_var.get()

        cursor.execute("UPDATE emps SET name=?, age=? WHERE id=?", (name, age, item[0]))
        con.commit()
        read()
 
        name_var.set("")
        age_var.set("")
    else:
          messagebox.showwarning("message",f"please select the item u want to update")
def on_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])['values']
        name_var.set(item[1])
        age_var.set(item[2])
 
def delete():
        seleted=tree.selection()
        if seleted:
            item=tree.item(seleted[0])['values']
            cursor.execute("DELETE FROM emps WHERE id=?",(item[0],))
            con.commit()
            read()
        else:
          messagebox.showwarning("message",f"please select the item u want to delete")
root=tk.Tk()
root.title("curd")
 
name_var=tk.StringVar()
age_var=tk.StringVar()
 
tk.Label(root,text="name").pack()
tk.Entry(root,width=30,textvariable=name_var).pack()
 
tk.Label(root,text="age").pack()
tk.Entry(root,width=30,textvariable=age_var).pack()  
 
tk.Button(root,text="add",command=insert).pack(pady=5)
tk.Button(root,text="update",command=update).pack(pady=5)
tk.Button(root,text="delete",command=delete).pack(pady=5)
 
 
column=["id ","name","age"]
tree=ttk.Treeview(root,columns=column,show="headings")
for col in column:
       tree.heading(col,text=col)
tree.pack(fill=tk.BOTH,expand=True)
read()
tree.bind("<<TreeviewSelect>>", on_select)
root.mainloop()