import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Calculator")
root.config(bg="lightblue")

tk.Label(root, text="Number 1:", bg="lightblue").pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

tk.Label(root, text="Number 2:", bg="lightblue").pack()
num2_entry = tk.Entry(root)
num2_entry.pack()

def calculate(sum):
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())

        if sum == "+":
            result = a + b
        elif sum == "-":
            result = a - b
        elif sum == "*":
            result = a * b
        elif sum == "/":
            result = a / b

        if result.is_integer():
            result = int(result)

        messagebox.showinfo("Result", f"Answer = {result}")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero...")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers...")

tk.Button(root, text="Add",  command=lambda: calculate("+")).pack(pady=10)
tk.Button(root, text="Sub",  command=lambda: calculate("-")).pack(pady=10)
tk.Button(root, text="Mul",  command=lambda: calculate("*")).pack(pady=10)
tk.Button(root, text="Div",  command=lambda: calculate("/")).pack(pady=10)

root.mainloop()
