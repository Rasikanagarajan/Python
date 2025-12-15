import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
 
con = sqlite3.connect("emp.db")
cursor = con.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS emps(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
con.commit()
 
def insert():
    name, age = name_var.get().strip(), age_var.get().strip()
    if not name:
        messagebox.showwarning("Validation", "Name is required.")
        return
    try:
        age_int = int(age) if age != "" else None
    except ValueError:
        messagebox.showwarning("Validation", "Age must be a number.")
        return
 
    cursor.execute("INSERT INTO emps (name, age) VALUES (?, ?)", (name, age_int))
    con.commit()
    read()
    name_var.set("")
    age_var.set("")
 
def read():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM emps")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
 
def update():
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("Select row", "Please select a row to update.")
        return
 
    item = tree.item(selected[0])['values']  # item[0] is id
    if not item:
        messagebox.showerror("Error", "Selected item has no values.")
        return
 
    name, age = name_var.get().strip(), age_var.get().strip()
    if not name:
        messagebox.showwarning("Validation", "Name is required.")
        return
    try:
        age_int = int(age) if age != "" else None
    except ValueError:
        messagebox.showwarning("Validation", "Age must be a number.")
        return
 
    cursor.execute("UPDATE emps SET name = ?, age = ? WHERE id = ?", (name, age_int, item[0]))
    con.commit()
    read()
    # leave the entries mapped to the (now updated) values or clear them:
    name_var.set("")
    age_var.set("")
 
def delete():
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("Select row", "Please select a row to delete.")
        return
 
    item = tree.item(selected[0])['values']
    if not item:
        return
 
    if messagebox.askyesno("Confirm delete", f"Delete record ID {item[0]}?"):
        cursor.execute("DELETE FROM emps WHERE id = ?", (item[0],))
        con.commit()
        read()
        name_var.set("")
        age_var.set("")
 
def on_select(event):
    sel = tree.selection()
    if not sel:
        return
    item = tree.item(sel[0])['values']
    if not item:
        return
    # item format: (id, name, age)
    name_var.set(item[1])
    age_var.set("" if item[2] is None else str(item[2]))
 
def on_close():
    try:
        con.commit()
        con.close()
    except:
        pass
    root.destroy()
 
 
root = tk.Tk()
root.title("CRUD")
 
name_var = tk.StringVar()
age_var = tk.StringVar()
 
tk.Label(root, text="Name").pack()
tk.Entry(root, width=30, textvariable=name_var).pack()
 
tk.Label(root, text="Age").pack()
tk.Entry(root, width=30, textvariable=age_var).pack()
 
tk.Button(root, text="Add", command=insert).pack(pady=5)
tk.Button(root, text="Update", command=update).pack(pady=5)
tk.Button(root, text="Delete", command=delete).pack(pady=5)
 
columns = ["id", "name", "age"]
tree = ttk.Treeview(root, columns=columns, show="headings", selectmode="browse")
for col in columns:
    tree.heading(col, text=col)
    # optional: set column width
    tree.column(col, width=100, anchor="center")
tree.pack(fill=tk.BOTH, expand=True)
 
# Bind selection event so entries fill when a row is selected
tree.bind("<<TreeviewSelect>>", on_select)
 
read()
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()