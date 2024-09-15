import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.font import Font
import pickle

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x500")

        # Define the font
        self.my_font = Font(family="Helvetica", size=18, weight="bold")

        # Create the listbox to display the to-do items
        self.my_listbox = tk.Listbox(root, font=self.my_font, width=25, height=8, bg="white", bd=0, fg="#464646",
                                     selectbackground="#a6a6a6", activestyle="none")
        self.my_listbox.pack(pady=20)

        # Create the entry box to add items
        self.my_entry = tk.Entry(root, font=("Helvetica", 24), width=26)
        self.my_entry.pack(pady=10)

        # Create the button frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Add buttons to the frame
        self.add_button = tk.Button(self.button_frame, text="Add Item", command=self.add_item)
        self.delete_button = tk.Button(self.button_frame, text="Delete Item", command=self.delete_item)
        self.clear_button = tk.Button(self.button_frame, text="Clear List", command=self.clear_list)
        self.save_button = tk.Button(self.button_frame, text="Save List", command=self.save_list)
        self.open_button = tk.Button(self.button_frame, text="Open List", command=self.open_list)

        self.add_button.grid(row=0, column=0)
        self.delete_button.grid(row=0, column=1)
        self.clear_button.grid(row=0, column=2)
        self.save_button.grid(row=1, column=0)
        self.open_button.grid(row=1, column=1)

    def add_item(self):
        """Add a new item to the listbox"""
        item = self.my_entry.get()
        if item != "":
            self.my_listbox.insert(tk.END, item)
            self.my_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter an item.")

    def delete_item(self):
        """Delete the selected item from the listbox"""
        try:
            self.my_listbox.delete(self.my_listbox.curselection())
        except:
            messagebox.showwarning("Warning", "You must select an item.")

    def clear_list(self):
        """Clear all items from the listbox"""
        self.my_listbox.delete(0, tk.END)

    def save_list(self):
        """Save the list to a file"""
        file_name = filedialog.asksaveasfilename(
            title="Save File", 
            filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
        )
        if file_name:
            if not file_name.endswith(".dat"):
                file_name += ".dat"
            items = self.my_listbox.get(0, tk.END)
            with open(file_name, 'wb') as output_file:
                pickle.dump(items, output_file)

    def open_list(self):
        """Open a list from a file"""
        file_name = filedialog.askopenfilename(
            title="Open File", 
            filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
        )
        if file_name:
            self.my_listbox.delete(0, tk.END)
            with open(file_name, 'rb') as input_file:
                items = pickle.load(input_file)
                for item in items:
                    self.my_listbox.insert(tk.END, item)

if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoListApp(root)
    root.resizable(0,0)
    root.mainloop()
