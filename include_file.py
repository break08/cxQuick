import tkinter as tk
from tkinter import filedialog, messagebox
import json

file_include = tk.Tk()
file_include.geometry ("420x420")
file_include.title ("Add Include Files")
file_include.resizable(False, False)

def open_path():
    include = filedialog.askopenfilename()
    if include:
        entry1b.delete (0, tk.END)
        entry1b.insert (tk.END, include)
def new_file():
    if not entry1b.get() == "" :
        path = entry1b.get()
        output = entry2b.get()
        element=f'(r"{path}", r"{output}"),\n'
        text01b.insert(tk.END, element)
        with open ("include_file_data.json", "r", encoding = "utf-8") as file:
            data = json.load (file)
        with open ("include_file_data.json", "w", encoding = "utf-8") as file:
            data["include"].append(element)
            json.dump (data, file, indent=4)
    else:
        messagebox.showerror ("Error", "Fill the forced field")
def clear_all():
    text01b.delete(1.0, tk.END)

text0 = tk.Label (file_include, text="*Include Files")
text0.place (x=10, y=10)
text01b = tk.Text(file_include, width = 50, height = 11)
text01b.place (x=10, y=40)
text1b = tk.Label (file_include, text="*File Path:")
text1b.place (x=10, y=240)
entry1b = tk.Entry (file_include, width=50)
entry1b.place (x=10, y=270)
text2b = tk.Label (file_include, text="Output:")
text2b.place (x=10, y=300)
entry2b = tk.Entry (file_include, width=50)
entry2b.place (x=10, y=330)
direct = tk.Button (file_include, text = "Browse File", command = open_path)
direct.place (x=10, y=360)
new_rowb = tk.Button (file_include, text = "New Include File", command = new_file)
new_rowb.place (x = 90, y = 360)
clear = tk.Button (file_include, text = "Clear All", command = clear_all)
clear.place (x = 200, y = 360)
file_include.mainloop()