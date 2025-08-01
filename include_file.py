import tkinter as tk
from tkinter import filedialog, messagebox
import json

file_include = tk.Tk()
file_include.geometry ("420x420")
file_include.title ("Add Include Files/Folders")
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
        element=f'(r"{path}", "{output}"),\n'
        text01b.insert(tk.END, element)
    else:
        messagebox.showerror ("Error", "Fill the forced field")
def clear_all():
    text01b.delete(1.0, tk.END)
    with open ("include_file_data.json", "r", encoding = "utf-8") as file:
        data = json.load (file)
    with open ("include_file_data.json", "w", encoding = "utf-8") as file:
        data["include"] = []
        json.dump (data, file, indent=4)
def include_saver():
    if not text01b.get("1.0", tk.END).strip() == "":
        try:
            with open("include_file_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            datawrite = text01b.get("1.0", tk.END).strip()
            with open ("include_file_data.json", "w", encoding="utf-8") as f:
                data["include"] = []
                for line in datawrite.splitlines():
                    with open ("include_file_data.json", "w", encoding="utf-8") as f:
                        data["include"].append(f"{line}"+ "\n")
                        json.dump(data, f, indent=4)
            messagebox.showinfo("Success", "Include files/folders saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "No include files/folders to save")
def include_file_finder():
    include_folder = filedialog.askdirectory()
    if include_folder:
        entry1b.delete(0, tk.END)
        entry1b.insert(tk.END, include_folder)

text0 = tk.Label (file_include, text="*Include Files/Folder")
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
new_rowb = tk.Button (file_include, text = "New Included", command = new_file)
new_rowb.place (x = 90, y = 360)
clear = tk.Button (file_include, text = "Clear All", command = clear_all)
clear.place (x = 200, y = 360)
save = tk.Button (file_include, text = "Save", command = include_saver)
save.place (x = 260, y = 360)
newfolder = tk.Button (file_include, text = "Browse Include Folder", command = include_file_finder)
newfolder.place (x = 10, y = 390)

with open ("include_file_data.json", "r", encoding = "utf-8") as f:
    data = json.load(f)
    edata = data["include"]
    for item in edata:
        text01b.insert(tk.END, item)

file_include.mainloop()