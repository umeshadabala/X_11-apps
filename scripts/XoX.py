import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title('Tic-Tac-Toe')
root.resizable(0, 0)

# X starts so true
clicked = True
count = 0

# Disable all the buttons
def disable_all_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

# Check to see if someone won
def check_if_won():
    global winner
    winner = False

    # Check rows
    for i in range(3):
        if buttons[i*3]["text"] == buttons[i*3+1]["text"] == buttons[i*3+2]["text"] and buttons[i*3]["text"] != " ":
            buttons[i*3].config(bg="red")
            buttons[i*3+1].config(bg="red")
            buttons[i*3+2].config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {buttons[i*3]['text']} Wins!!")
            disable_all_buttons()
            return

    # Check columns
    for i in range(3):
        if buttons[i]["text"] == buttons[i+3]["text"] == buttons[i+6]["text"] and buttons[i]["text"] != " ":
            buttons[i].config(bg="red")
            buttons[i+3].config(bg="red")
            buttons[i+6].config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {buttons[i]['text']} Wins!!")
            disable_all_buttons()
            return

    # Check diagonals
    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] and buttons[0]["text"] != " ":
        buttons[0].config(bg="red")
        buttons[4].config(bg="red")
        buttons[8].config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {buttons[0]['text']} Wins!!")
        disable_all_buttons()
        return

    if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] and buttons[2]["text"] != " ":
        buttons[2].config(bg="red")
        buttons[4].config(bg="red")
        buttons[6].config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {buttons[2]['text']} Wins!!")
        disable_all_buttons()
        return

    # Check if tie
    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
        disable_all_buttons()

# Button clicked function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked:
        b["text"] = "X"
        clicked = False
        count += 1
        check_if_won()
    elif b["text"] == " " and not clicked:
        b["text"] = "O"
        clicked = True
        count += 1
        check_if_won()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box...")

# Start the game over!
def reset():
    global clicked, count
    clicked = True
    count = 0

    # Create buttons
    for i in range(9):
        buttons[i].config(text=" ", bg="light gray", state=tk.NORMAL)

# Create buttons and place them in the grid
buttons = [tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="light gray", command=lambda i=i: b_click(buttons[i])) for i in range(9)]

for i in range(3):
    for j in range(3):
        buttons[i*3+j].grid(row=i, column=j)

# Create menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()  # Initialize the buttons

root.mainloop()
