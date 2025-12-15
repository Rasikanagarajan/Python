# print the output in terminal
# calculator

import tkinter as tk
from tkinter import messagebox


root=tk.Tk()
root.title("Rasika")
root.config(bg="lavender")

label=tk.Label(root,text="Hello Guys Welcome To My Tkinder")
label.pack()
print(label["text"])

# img = tk.PhotoImage(file="image.png")
# label = tk.Label(root, image=img,width=200,height=200)
# label.pack()

entry=tk.Entry(root,width=30)
entry.pack()

def showmsg():
    msg = f"Hello Dear's {entry.get()}!"  
    print(msg)                              
    messagebox.showinfo("message", msg)  
 
btn=tk.Button(root,text="show" ,command=showmsg)
btn.pack()

root.mainloop()

