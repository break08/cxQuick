import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import json

def browse_filepy():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file_path:
        entry2a.delete(1.0, tk.END)
        entry2a.insert(tk.END, file_path)
def browse_fileico():
    file_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    if file_path:
        entry4a.delete(1.0, tk.END)
        entry4a.insert(tk.END, file_path)
def executable_new():
    script = entry2a.get("1.0", tk.END).strip()
    icon = entry4a.get("1.0", tk.END).strip()
    base = box1.get()
    target_name = entry5a.get("1.0", tk.END).strip()
    if script == "":
        messagebox.showerror("Error", "Please select a .py file.")
        return
    if icon == "":
        icon = None
    if base == "":
        base = None
    if target_name == "":
        target_name = os.path.basename(script).replace(".py", ".exe")
    executables_name = f"""Executable(script={script}, base={base}, target_name="{target_name}", icon="{icon}"),\n"""
    entry1a.insert (tk.END, executables_name)
    with open("dataexecutables.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    with open ("dataexecutables.json", "w", encoding="utf-8") as f:
        data["executables"].append(f"{executables_name}")
        json.dump(data, f, indent=4)
def clear():
    entry1a.delete(1.0, tk.END)
    with open("dataexecutables.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    with open("dataexecutables.json", "w", encoding="utf-8") as f:
        data["executables"] = []
        json.dump(data, f, indent=4)

exe = tk.Tk()
exe.title("Choose Executable")
exe.geometry("800x210")
exe.resizable(False, False)

text1a = tk.Label(exe, text="Executable Path:")
text1a.place (x=10, y=10)

entry1a = tk.Text(exe, height=10, width=50)
entry1a.place (x=10, y=30)

text2a = tk.Label (exe, text = ".py file path:")
text2a.place (x=450, y=10)

entry2a = tk.Text(exe, height=1, width=20)
entry2a.place (x=450, y=30)

text3a = tk.Label(exe, text="Base:")
text3a.place (x=450, y=60)

box1 = ttk.Combobox(exe, values=["Console", "Win32GUI"], state="readonly")
box1.place (x=450, y=80)

text4a = tk.Label(exe, text="Icon:")
text4a.place (x=450, y=110)

entry4a = tk.Text(exe, height=1, width=20)
entry4a.place (x=450, y=130)

text5a = tk.Label(exe, text="targetName:")
text5a.place (x=450, y=160)

entry5a = tk.Text(exe, height=1, width=20)
entry5a.place (x=450, y=180)

button1a = tk.Button (exe, text = "Browse .py file path", command=browse_filepy)
button1a.place (x=670, y=30)
button2a = tk.Button (exe, text = "Browse Icon file path", command=browse_fileico)
button2a.place (x=670, y=60)
button3a = tk.Button(exe, text="New Executable", command = executable_new)
button3a.place (x=670, y=90)
button4a = tk.Button(exe, text="Clear All", command=clear)
button4a.place (x=670, y=120)
exe.mainloop()