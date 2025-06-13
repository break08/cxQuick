import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pathlib import Path
import threading
import json

def browse_file():
    def running ():
        parentfolder = Path(__file__).parent
        list_file = os.listdir(parentfolder)
        if "executable.py" in list_file:
            command = f'python executable.py'
            os.system(command)
        elif "executable.exe" in list_file:
            os.startfile("executable.exe")
    threading.Thread(target=running).start()

def output():
    output_path = filedialog.askdirectory()
    if output_path:
        entry6.delete(1.0, tk.END)
        entry6.insert(tk.END, output_path)
def start():
    text9.config (text = "Collecting Information...")
    filepath = entry1.get("1.0", tk.END).strip()
    name = entry2.get("1.0", tk.END).strip()
    version = entry3.get("1.0", tk.END).strip()
    description = entry4.get("1.0", tk.END).strip()
    outputf = entry6.get("1.0", tk.END).strip()
    base = ""
    icon = ""
    content = f"""from cx_Freeze import setup, Executable
build_exe_options = {{
    "packages": ["os"],
    "build_exe": "{outputf}"
}}
setup(
    name="{name}",
    version="{version}",
    description="{description}",
    options={{"build_exe": build_exe_options}},
    executables=[Executable("{filepath}", base="{base}", icon="{icon}")],
)
"""
    if len(os.listdir(outputf)) == 0:
        text9.config (text = "Building .exe file...")
        with open ("temp/setup.py", "w", encoding="utf-8") as f:
            f.write(content)
        path = os.path.abspath ("temp/setup.py")
        runner = f'python "{path}" build'
        text9.config (text = "Success")
        os.environ["PYTHONIOENCODING"] = "utf-8"
        os.system(runner)
        messagebox.showinfo("Success", "Build completed successfully!")
    else:
        text9.config (text = "Output directory is not empty!")
        messagebox.showerror("Error", "Output directory is not empty! Please choose an empty directory.")

main = tk.Tk()
main.title ("cxQuick")
main.geometry("700x500")
main.resizable(False, False)

def executables_checking():
    with open ("dataexecutables.json", "r") as f:
        data = json.load(f)
        edata = data["executables"]
        entry1.delete(1.0, tk.END)
        for item in edata:
            entry1.insert(tk.END, item + "\n")
main.after(100, executables_checking)

text1 = tk.Label (main, text = "Executables")
text1.place (x = 10, y = 10)
entry1 = tk.Text (main, height = 8, width = 50)
entry1.place (x = 10, y = 30)
text2 = tk.Label (main, text = "Name")
text2.place (x = 10, y = 180)
entry2 = tk.Text (main, height = 1, width = 50)
entry2.place (x = 10, y = 200)
text3 = tk.Label (main, text = "Version")
text3.place (x = 10, y = 220)
entry3 = tk.Text (main, height = 1, width = 50)
entry3.place (x = 10, y = 240)
text4 = tk.Label (main, text = "Description")
text4.place (x = 10, y = 260)
entry4 = tk.Text (main, height = 1, width = 50)
entry4.place (x = 10, y = 280)
text7 = tk.Label (main, text = "Output directory")
text7.place (x = 10, y = 300)
entry6 = tk.Text (main, height = 1, width = 50)
entry6.place (x = 10, y = 330)
text8 = tk.Label (main, text = "Status")
text8.place (x = 10, y = 360)
text9 = tk.Label (main, text = "Waiting for input...", bg = "white")
text9.place (x = 10, y = 380)
text10 = tk.Label (main, text = "*Note : Please set the output directory to an empty directory")
text10.place (x = 10, y = 410)
text11 = tk.Label (main, text = "Libraries")
text11.place (x = 10, y = 440)
entry12 = tk.Text (main, height = 1, width = 50)
entry12.place (x = 10, y = 460)

button1 = tk.Button(main, text="Add executables", command=browse_file)
button1.place (x = 470, y = 30)
button2 = tk.Button(main, text="Build", command=start)
button2.place (x = 470, y = 120)
button4 = tk.Button(main, text="Browse Output Directory", command=output)
button4.place (x = 470, y = 90)

main.mainloop()