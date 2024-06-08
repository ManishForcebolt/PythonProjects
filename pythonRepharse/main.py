import csv
import tkinter
from tkinter import *
import pandas as pd

from tkinter import filedialog


# file_path = "/Users/ca/PycharmProjects/pythonRepharse/Test1.csv"

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            print("File Loaded")
            print(df)
        except Exception as e:
            print("Error:", e)


# Create the main window on screen
root = Tk()
root.title("CSV File Reader")

# Create button for file
browse_button = tk.Button(root, text="Browse CSV File", command=browse_file)
browse_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()