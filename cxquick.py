import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file_path:
        entry1.delete(1.0, tk.END)
        entry1.insert(tk.END, file_path)
def get_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    if icon_path:
        entry5.delete(1.0, tk.END)
        entry5.insert(tk.END, icon_path)
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
    icon = entry5.get("1.0", tk.END).strip()
    base = box1.get()
    outputf = entry6.get("1.0", tk.END).strip()
    content = f"""from cx_Freeze import setup, Executable
build_exe_options = {{
    "packages": ["os"],
    "build_exe": "{outputf}"
}}
setup(
    name="{name}",
    version="{version}",
    description="{description}",
    options={{"build_exe": buid_exe_options}},
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
main.geometry("650x500")
main.resizable(False, False)

text1 = tk.Label (main, text = ".py file path")
text1.place (x = 10, y = 10)
entry1 = tk.Text (main, height = 1, width = 50)
entry1.place (x = 10, y = 30)
text2 = tk.Label (main, text = "Name")
text2.place (x = 10, y = 60)
entry2 = tk.Text (main, height = 1, width = 50)
entry2.place (x = 10, y = 80)
text3 = tk.Label (main, text = "Version")
text3.place (x = 10, y = 110)
entry3 = tk.Text (main, height = 1, width = 50)
entry3.place (x = 10, y = 130)
text4 = tk.Label (main, text = "Description")
text4.place (x = 10, y = 160)
entry4 = tk.Text (main, height = 1, width = 50)
entry4.place (x = 10, y = 180)
text5 = tk.Label (main, text = "Icon path")
text5.place (x = 10, y = 210)
entry5 = tk.Text (main, height = 1, width = 50)
entry5.place (x = 10, y = 230)
text6 = tk.Label (main, text = "Base")
text6.place (x = 10, y = 260)
box1 = ttk.Combobox(main, values=["Win32GUI", "Console"], width=63)
box1.place(x = 10, y = 280)
text7 = tk.Label (main, text = "Output directory")
text7.place (x = 10, y = 310)
entry6 = tk.Text (main, height = 1, width = 50)
entry6.place (x = 10, y = 330)
text8 = tk.Label (main, text = "Status")
text8.place (x = 10, y = 360)
text9 = tk.Label (main, text = "Waiting for input...", bg = "white")
text9.place (x = 10, y = 380)
text10 = tk.Label (main, text = "*Note : Please set the output directory to an empty directory")
text10.place (x = 10, y = 410)

button1 = tk.Button(main, text="Browse .py file", command=browse_file)
button1.place(x = 470, y = 30)
button2 = tk.Button(main, text="Build", command=start)
button2.place (x = 470, y = 120)
button3 = tk.Button (main, text = "Browse .ico file", command = get_icon)
button3.place (x = 470, y = 60)
button4 = tk.Button(main, text="Browse Output Directory", command=output)
button4.place (x = 470, y = 90)

main.mainloop()