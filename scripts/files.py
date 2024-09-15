# Python program to create 
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

# Function for opening the 
# file explorer window
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Text files",
														"*.txt*"),
													("all files",
														"*.*")))
	
		
	
																			
browseFiles()