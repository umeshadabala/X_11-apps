import tkinter as tk
from tkinter import Menu, filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")

        # Initialize the text widget
        self.text_area = tk.Text(self.root, wrap='word', font=('Arial', 12))
        self.text_area.pack(fill='both', expand=True)

        # Create a menu bar
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Help menu
        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        # Store the current file name
        self.file_name = None

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_name = None
        self.root.title("New File - Notepad")

    def open_file(self):
        self.file_name = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("Text Files", "*.txt"),
                                                               ("All Files", "*.*")])
        if self.file_name:
            self.root.title(f"{self.file_name} - Notepad")
            with open(self.file_name, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if self.file_name:
            try:
                with open(self.file_name, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Save Error", f"Could not save file: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_name = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text Files", "*.txt"),
                                                                 ("All Files", "*.*")])
        if self.file_name:
            self.save_file()
            self.root.title(f"{self.file_name} - Notepad")

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def exit_app(self):
        self.root.quit()

    def show_about(self):
        messagebox.showinfo("About Notepad", "Simple Notepad application.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
