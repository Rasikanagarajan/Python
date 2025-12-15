import tkinter as tk
from tkinter import messagebox
 
root=tk.Tk()
root.title("intro")
root.config(bg="pink")
label=tk.Label(root,text="hello")
label.pack()

entry=tk.Entry(root,width=30)
entry.pack()
 
def showmsg():
    messagebox.showinfo("message",f"hello {entry.get()} !")
 
btn=tk.Button(root,text="show" ,command=showmsg)
btn.pack()
 
cv=tk.BooleanVar()
check=tk.Checkbutton(root,text="i agree" ,variable=cv)
check.pack()
 
radio=tk.StringVar(value="male")
tk.Radiobutton(root,text="male",variable=radio, value="male").pack()
tk.Radiobutton(root,text="female",variable=radio, value="female").pack()
 
list=tk.Listbox(root)
for i in ["python","java","c"]:
    list.insert(tk.END,i)
# list.pack()

# grid
# label=tk.Label(root,text="hello")
# label.grid(row=0,column=0) 

root.mainloop()