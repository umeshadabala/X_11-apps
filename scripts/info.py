import platform
import psutil
import GPUtil
import tkinter as tk
from tkinter import ttk

# Function to get and display system information
def get_system_info():
    system_info = platform.uname()

    # Clear any previous data in the text widget
    info_text.delete(1.0, tk.END)

    # System Information
    info_text.insert(tk.END, "System Information:\n")
    info_text.insert(tk.END, f"System: {system_info.system}\n")
    info_text.insert(tk.END, f"Node Name: {system_info.node}\n")
    info_text.insert(tk.END, f"Release: {system_info.release}\n")
    info_text.insert(tk.END, f"Version: {system_info.version}\n")
    info_text.insert(tk.END, f"Machine: {system_info.machine}\n")
    info_text.insert(tk.END, f"Processor: {system_info.processor}\n\n")

    # CPU Information
    cpu_info = platform.processor()
    cpu_count = psutil.cpu_count(logical=False)
    logical_cpu_count = psutil.cpu_count(logical=True)

    info_text.insert(tk.END, "CPU Information:\n")
    info_text.insert(tk.END, f"Processor: {cpu_info}\n")
    info_text.insert(tk.END, f"Physical Cores: {cpu_count}\n")
    info_text.insert(tk.END, f"Logical Cores: {logical_cpu_count}\n\n")

    # Memory Information
    memory_info = psutil.virtual_memory()
    info_text.insert(tk.END, "Memory Information:\n")
    info_text.insert(tk.END, f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB\n")
    info_text.insert(tk.END, f"Available Memory: {memory_info.available / (1024 ** 3):.2f} GB\n")
    info_text.insert(tk.END, f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB\n")
    info_text.insert(tk.END, f"Memory Utilization: {memory_info.percent}%\n\n")

    # Disk Information
    disk_info = psutil.disk_usage('/')
    info_text.insert(tk.END, "Disk Information:\n")
    info_text.insert(tk.END, f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB\n")
    info_text.insert(tk.END, f"Used Disk Space: {disk_info.used / (1024 ** 3):.2f} GB\n")
    info_text.insert(tk.END, f"Free Disk Space: {disk_info.free / (1024 ** 3):.2f} GB\n")
    info_text.insert(tk.END, f"Disk Space Utilization: {disk_info.percent}%\n\n")

    # GPU Information
    gpus = GPUtil.getGPUs()

    if not gpus:
        info_text.insert(tk.END, "No GPU detected.\n")
    else:
        for i, gpu in enumerate(gpus):
            info_text.insert(tk.END, f"\nGPU {i + 1} Information:\n")
            info_text.insert(tk.END, f"ID: {gpu.id}\n")
            info_text.insert(tk.END, f"Name: {gpu.name}\n")
            info_text.insert(tk.END, f"Driver: {gpu.driver}\n")
            info_text.insert(tk.END, f"GPU Memory Total: {gpu.memoryTotal} MB\n")
            info_text.insert(tk.END, f"GPU Memory Free: {gpu.memoryFree} MB\n")
            info_text.insert(tk.END, f"GPU Memory Used: {gpu.memoryUsed} MB\n")
            info_text.insert(tk.END, f"GPU Load: {gpu.load * 100}%\n")
            info_text.insert(tk.END, f"GPU Temperature: {gpu.temperature}°C\n")

# Create a Tkinter window
root = tk.Tk()
root.title("System Information")
root.geometry("600x600")
root.resizable(False, False)

# Set color scheme
root.config(bg='#282c34')  # Dark background
text_bg_color = "#21252b"  # Slightly lighter background for text
text_fg_color = "#ffffff"  # White text
button_color = "#61afef"  # Button color (blue-ish)

# Header label
header_label = tk.Label(root, text="System Information", font=("Helvetica", 16, "bold"), bg='#282c34', fg='#61afef')
header_label.pack(pady=10)

# Create a scrollable text box to display the system information
info_frame = tk.Frame(root)
info_frame.pack(pady=5)

# Add text box
info_text = tk.Text(info_frame, wrap=tk.WORD, font=("Helvetica", 10), bg=text_bg_color, fg=text_fg_color, height=25, width=70)
info_text.grid(row=0, column=0)

# Add scrollbar
scrollbar = ttk.Scrollbar(info_frame, command=info_text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
info_text['yscrollcommand'] = scrollbar.set

# Button to fetch system information
fetch_button = tk.Button(root, text="Fetch System Information", font=("Helvetica", 12), bg=button_color, fg='black', command=get_system_info)
fetch_button.pack(pady=20)

# Run the application
root.mainloop()
