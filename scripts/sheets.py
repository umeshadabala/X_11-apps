import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import csv

class ExcelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sheets")

        self.create_menu()
        self.create_sheet()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.load_csv)
        file_menu.add_command(label="Save", command=self.save_csv)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Bold", command=self.apply_bold)
        edit_menu.add_command(label="Italic", command=self.apply_italic)
        edit_menu.add_command(label="Formula", command=self.insert_formula)

    def create_sheet(self):
        self.entries = []
        self.sheet_frame = tk.Frame(self.root)
        self.sheet_frame.pack(fill=tk.BOTH, expand=True)

        for row in range(20):
            row_entries = []
            for col in range(10):
                entry = tk.Entry(self.sheet_frame, width=10)
                entry.grid(row=row, column=col, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def new_file(self):
        for row in self.entries:
            for cell in row:
                cell.delete(0, tk.END)

    def save_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            for row in self.entries:
                writer.writerow([cell.get() for cell in row])

        messagebox.showinfo("Saved", f"File saved as {file_path}")

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        with open(file_path, mode="r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i >= len(self.entries):
                    break
                for j, value in enumerate(row):
                    if j < len(self.entries[i]):
                        self.entries[i][j].delete(0, tk.END)
                        self.entries[i][j].insert(0, value)

    def apply_bold(self):
        selected_entry = self.get_selected_entry()
        if selected_entry:
            current_font = selected_entry.cget("font")
            if "bold" not in current_font:
                selected_entry.config(font=(current_font, 10, "bold"))

    def apply_italic(self):
        selected_entry = self.get_selected_entry()
        if selected_entry:
            current_font = selected_entry.cget("font")
            if "italic" not in current_font:
                selected_entry.config(font=(current_font, 10, "italic"))

    def insert_formula(self):
        selected_entry = self.get_selected_entry()
        if selected_entry:
            formula = simpledialog.askstring("Formula", "Enter a formula (e.g., A1+B1):")
            if formula:
                try:
                    result = self.evaluate_formula(formula)
                    selected_entry.delete(0, tk.END)
                    selected_entry.insert(0, str(result))
                except Exception as e:
                    messagebox.showerror("Error", str(e))

    def get_selected_entry(self):
        try:
            return self.root.focus_get()
        except Exception:
            return None

    def evaluate_formula(self, formula):
        # Example: A1+B1 (assuming A1 is at row 1, col 1)
        parts = formula.split('+')
        result = 0
        for part in parts:
            if len(part) == 2:
                col = ord(part[0].upper()) - ord('A')
                row = int(part[1]) - 1
                value = self.entries[row][col].get()
                result += float(value)
        return result

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0,0)
    app = ExcelApp(root)
    root.mainloop()
