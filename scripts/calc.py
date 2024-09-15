import tkinter as tk

# Function to update the expression in the entry box
def click(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button)

# Function to calculate the result
def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.resizable(0, 0)

# Create the entry box for display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add the buttons to the window
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=calculate).grid(row=row_val, column=col_val, columnspan=2)
        col_val += 1
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=lambda b=button: click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add the clear button
tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear).grid(row=row_val, column=2, columnspan=2)

# Start the application
root.mainloop()
