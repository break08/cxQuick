import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess, os, threading, json

def runner(py, exe):
    try:
        command = f"python {py}"
        os.system(command)
    except:
        try:
            os.startfile(exe)
        except Exception as e:
            messagebox.showerror("Error", f"{e}")
def opener (jsonfilea, key, entry: tk.Text):
    entry.config (state = "normal")
    entry.delete (1.0, tk.END)
    with open(jsonfilea, "r", encoding="utf-8") as f:
        data = json.load(f)
        edata = data[key]
        for item in edata:
            entry.insert(tk.END, item)
    entry.config(state = "disabled")
def cleaner(jsonfilea, key):
    with open(jsonfilea, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(jsonfilea, "w", encoding="utf-8") as f:
        data[key] = []
        json.dump(data, f, indent=4)
def browse_file():
    def running ():
        runner("executable.py", "executable.exe")
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
    output_text = tk.Text(result, height=20, width=100, bg = "black", fg = "white", wrap = tk.NONE)
    output_text.pack()
    scrollx = tk.Scrollbar(result, orient=tk.HORIZONTAL, command=output_text.xview)
    output_text.config(xscrollcommand=scrollx.set)
    scrolly = tk.Scrollbar(result, orient=tk.VERTICAL, command=output_text.yview)
    output_text.config(yscrollcommand=scrolly.set)
    scrollx.place(x = 10, y = 320, width = 810)
    scrolly.place(x = 820, y = 0, height = 320)
    text1bc = tk.Label (result, text = "Error")
    text1bc.place (x = 10, y = 340)
    errorlb = tk.Text (result, height = 10, width = 100, bg = "black", fg = "white", wrap = tk.NONE)
    errorlb.place (x = 10, y = 360)
    scrollx2 = tk.Scrollbar(result, orient=tk.HORIZONTAL, command=errorlb.xview)
    errorlb.config(xscrollcommand=scrollx2.set)
    scrolly2 = tk.Scrollbar(result, orient=tk.VERTICAL, command=errorlb.yview)
    errorlb.config(yscrollcommand=scrolly2.set)
    scrollx2.place(x = 10, y = 530, width = 810)
    scrolly2.place(x = 820, y = 360, height = 190)
    name = entry2.get("1.0", tk.END).strip()
    version = entry3.get("1.0", tk.END).strip()
    description = entry4.get("1.0", tk.END).strip()
    outputf = os.path.abspath(entry6.get("1.0", tk.END).strip())
    outputf = outputf.replace ("/", "\\")
    executable_get = entry1.get("1.0", tk.END).strip()
    lib = entry12.get("1.0", tk.END).strip()
    lib_list = lib.split(",")
    force_lib  = entry14.get("1.0", tk.END).strip()
    force_lib_list = force_lib.split(",")
    exclude_lib = entry15.get("1.0", tk.END).strip()
    exclude_lib_list = exclude_lib.split(",")
    fileinclude = entry13.get("1.0", tk.END).strip()
    if lib_list == [""] or lib_list == ['']:
        lib_list = []
    if force_lib_list == [""] or force_lib_list == ['']:
        force_lib_list = []
    if exclude_lib_list == [""] or exclude_lib_list == ['']:
        exclude_lib_list = []

    content = f"""from cx_Freeze import setup, Executable
build_exe_options = {{
    "packages": {lib_list},
    "includes": {force_lib_list},
    "excludes": {exclude_lib_list},
    "build_exe": r"{outputf}",
    "include_files": [{fileinclude}],
    "optimize": {int(optimize.get())},
    "include_msvcr": {msvcr_var},
}}
setup(
    name="{name}",
    version="{version}",
    description="{description}",
    options={{"build_exe": build_exe_options}},
    executables=[{executable_get}],
)
"""
    outputf = os.path.normpath (outputf)
    if len(os.listdir(outputf)) == 0:
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
        errorlb.insert(tk.END, building.stderr)
        messagebox.showinfo("Complete", "Build completed!")
    else:
        messagebox.showerror("Error", "Output directory is not empty! Please choose an empty directory.")
    result.mainloop()

def build():
    threading.Thread(target=start_process).start()

def executables_clear():
    entry1.config(state="normal")
    entry1.delete(1.0, tk.END)
    cleaner("dataexecutables.json", "executables")
    entry1.config(state="disabled")
def includefile_clear():
    entry13.config (state = "normal")
    entry13.delete(1.0, tk.END)
    cleaner("include_file_data.json", "include")
    entry13.config (state = "disabled")
def include_file_finder():
    def running ():
        runner("include_file.py", "include_file.exe")
    threading.Thread(target=running).start()
def load_all():
    opener("dataexecutables.json", "executables", entry1)
    opener("include_file_data.json", "include", entry13)

main = tk.Tk()
main.title ("cxQuick")
main.geometry("700x650")
main.resizable(False, False)

msvcr_var = None
msvcr = tk.IntVar(value = 1)
if msvcr.get() == 1:
    msvcr_var = True
else:
    msvcr_var = False

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
text11 = tk.Label (main, text = 'Libraries (Example: os,tkinter)')
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
entry13 = tk.Text (main, height = 8, width = 50, wrap = tk.NONE)
entry13.place (x = 10, y = 470)
entry13.config (state = "disabled")

text14 = tk.Label (main, text = "Optimize")
text14.place (x = 450, y = 220)
optimize = ttk.Combobox (main, values=["0", "1", "2"], width=17)
optimize.place (x = 450, y = 240)
optimize.set("0")

text15 = tk.Label (main, text = 'Force Import (Example: os,tkinter)')
text15.place (x = 450, y = 260)
entry14 = tk.Text (main, width = 25, height = 1)
entry14.place (x = 450, y = 280)

text16 = tk.Label (main, text = 'Exclude Libraries (Example: os,tkinter)')
text16.place (x = 450, y = 300)
entry15 = tk.Text (main, width = 25, height = 1)
entry15.place (x = 450, y = 330)

checkbox1 = tk.Checkbutton (main, text = "Include msvcr", variable=msvcr)
checkbox1.place (x = 450, y = 350)

menubar = tk.Menu (main)
main.config(menu=menubar)
filemenu = tk.Menu (menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=main.quit)
filemenu.add_command (label = "Load Data", command = load_all)
tools = tk.Menu (menubar)
menubar.add_cascade(label = "Tools", menu=tools)
tools.add_command(label = "Install cx_Freeze", command=lambda: os.startfile("cxfreeze_install.bat"))
tools.add_command(label = "About cx_Freeze", command=lambda: os.startfile("about_cxfreeze.bat"))
about = tk.Menu (menubar)
menubar.add_cascade (label = "About", command=lambda: os.startfile ("about.html"))

button1 = tk.Button(main, text="Add Executables", command=browse_file, width = 19)
button1.place (x = 470, y = 30)
button2 = tk.Button(main, text="Build", command=build, width = 19)
button2.place (x = 470, y = 120)
button3 = tk.Button(main, text="Clear All Executables", command= executables_clear, width = 19)
button3.place (x = 470, y = 150)
button4 = tk.Button(main, text="Browse Output Directory", command=output, width = 19)
button4.place (x = 470, y = 90)
button5 = tk.Button (main, text = "Add Include Files/Folders", width = 19, command=include_file_finder)
button5.place (x = 470, y = 60)
button6 = tk.Button (main, text = "Clear All Included", command = includefile_clear, width = 19)
button6.place (x = 470, y = 180)

scrolly2 = tk.Scrollbar(main, orient = tk.VERTICAL, command=entry13.yview)
entry13.config(yscrollcommand=scrolly2.set)
scrolly2.place(x=400, y=470, height=135)
scrollx2 = tk.Scrollbar (main, orient = tk.HORIZONTAL, command = entry13.xview)
entry13.config(xscrollcommand=scrollx2.set)
scrollx2.place(x=10, y=600, width=390)

load_all()

def executables_checking():
    with open ("check.json", "r", encoding="utf-8") as f:
        keyjson=json.load(f)
    if keyjson["exe"] == 1:
        opener("dataexecutables.json", "executables", entry1)
        with open ("check.json", "w", encoding="utf-8") as f:
            keyjson["exe"] = 0
            json.dump(keyjson, f, indent = 4)
    if keyjson["include"] == 1:
        opener("include_file_data.json", "include", entry13)
        with open ("check.json", "w", encoding="utf-8") as f:
            keyjson["include"] = 0
            json.dump(keyjson, f, indent = 4)
    main.after(50, executables_checking)
executables_checking()

main.mainloop()