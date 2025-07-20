import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess, os, threading, json
from pathlib import Path

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
def start_process():
    result = tk.Tk()
    result.geometry ("840x630")
    result.title ("Output")
    result.resizable (False, False)
    output_text = tk.Text(result, height=37, width=100, bg = "black", fg = "white", wrap = tk.NONE)
    output_text.pack()
    scrollx = tk.Scrollbar(result, orient=tk.HORIZONTAL, command=output_text.xview)
    output_text.config(xscrollcommand=scrollx.set)
    scrolly = tk.Scrollbar(result, orient=tk.VERTICAL, command=output_text.yview)
    output_text.config(yscrollcommand=scrolly.set)
    scrollx.place(x = 10, y = 600, width = 810)
    scrolly.place(x = 820, y = 0, height = 600)
    name = entry2.get("1.0", tk.END).strip()
    version = entry3.get("1.0", tk.END).strip()
    description = entry4.get("1.0", tk.END).strip()
    outputf = os.path.abspath(entry6.get("1.0", tk.END).strip())
    outputf = outputf.replace ("/", "\\")
    executable_get = entry1.get("1.0", tk.END).strip()
    lib = entry12.get("1.0", tk.END).strip()
    content = f"""from cx_Freeze import setup, Executable
build_exe_options = {{
    "packages": [{lib}],
    "build_exe": r"{outputf}"
}}
setup(
    name="{name}",
    version="{version}",
    description="{description}",
    options={{"build_exe": build_exe_options}},
    executables=[{executable_get}],
)
"""
    if len(os.listdir(outputf)) == 0:
        try:
            with open ("saves/setup.py", "w", encoding="utf-8") as f:
                f.write(content)
            path = os.path.abspath ("saves/setup.py")
            path = path.replace ("/", "\\")
            runner = f'python "{path}" build'
            building = subprocess.run (
                f"chcp 65001 && {runner}",
                text=True,
                shell=True,
                capture_output=True)
            output_text.insert(tk.END, building.stdout)
            messagebox.showinfo("Success", "Build completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "Output directory is not empty! Please choose an empty directory.")
    result.mainloop()

def build():
    threading.Thread(target=start_process).start()

def executables_clear():
    entry1.config(state="normal")
    entry1.delete(1.0, tk.END)
    with open("dataexecutables.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    with open("dataexecutables.json", "w", encoding="utf-8") as f:
        data["executables"] = []
        json.dump(data, f, indent=4)
    entry1.config(state="disabled")
def includefile_clear():
    entry13.config (state = "normal")
    entry13.delete(1.0, tk.END)
    with open ("include_file_data.json", "r", encoding = "utf-8") as file:
        data = json.load (file)
    with open ("include_file_data.json", "w", encoding = "utf-8") as file:
        data["include"] = []
        json.dump (data, file, indent=4)
    entry13.config (state = "disabled")
def include_file_finder():
    def running ():
        parentfolder = Path(__file__).parent
        list_file = os.listdir(parentfolder)
        if "include_file.py" in list_file:
            command = f'python include_file.py'
            os.system(command)
        elif "include_file.exe" in list_file:
            os.startfile("include_file.exe")
    threading.Thread(target=running).start()    

main = tk.Tk()
main.title ("cxQuick")
main.geometry("700x650")
main.resizable(False, False)

def executables_checking():
    entry1.config (state="normal")
    entry13.config(state = "normal")
    with open ("dataexecutables.json", "r", encoding = "utf-8") as f:
        data = json.load(f)
        edata = data["executables"]
        for item in edata:
            entry1.insert(tk.END, item)
    with open ("include_file_data.json", "r", encoding = "utf-8") as file:
        datafile = json.load (file)
        edatafile= datafile["include"]
        for item in edatafile:
            entry13.insert(tk.END, item)
    entry1.config (state="disabled")
    entry13.config (state = "disabled")
main.after(100, executables_checking)

text1 = tk.Label (main, text = "Executables")
text1.place (x = 10, y = 10)
entry1 = tk.Text (main, height = 8, width = 50, wrap= tk.NONE)
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
text10 = tk.Label (main, text = "*Note : Please set the output directory to an empty directory because all data \n in output folder will be replaced with the output files of cx_freeze")
text10.place (x = 10, y = 360)
text11 = tk.Label (main, text = 'Libraries (Example: "os", "tkinter")')
text11.place (x = 10, y = 390)
entry12 = tk.Text (main, height = 1, width = 50)
entry12.place (x = 10, y = 420)
scroll = tk.Scrollbar(main, orient = tk.VERTICAL, command=entry1.yview)
entry1.config(yscrollcommand=scroll.set)
scroll.place(x=400, y=30, height=135)
scroll2 = tk.Scrollbar (main, orient = tk.HORIZONTAL, command = entry1.xview)
entry1.config(xscrollcommand=scroll2.set)
scroll2.place(x=10, y=145, width=390)
text13 = tk.Label (main, text = "Include Files")
text13.place (x = 10, y = 450)
entry13 = tk.Text (main, height = 8, width = 50)
entry13.place (x = 10, y = 470)
entry13.config (state = "disabled")

button1 = tk.Button(main, text="Add executables", command=browse_file, width = 19)
button1.place (x = 470, y = 30)
button2 = tk.Button(main, text="Build", command=build, width = 19)
button2.place (x = 470, y = 120)
button3 = tk.Button(main, text="Clear All Executables", command= executables_clear, width = 19)
button3.place (x = 470, y = 150)
button4 = tk.Button(main, text="Browse Output Directory", command=output, width = 19)
button4.place (x = 470, y = 90)
button5 = tk.Button (main, text = "Add Include Files", width = 19, command=include_file_finder)
button5.place (x = 470, y = 60)
button6 = tk.Button (main, text = "Clear All Include Files", command = includefile_clear, width = 19)
button6.place (x = 470, y = 180)
main.mainloop()