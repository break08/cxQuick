def run_exe():
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox
    import json
    def check_exe():
        with open ("check.json", "r", encoding="utf-8") as file:
            keyjsona= json.load(file)
        with open ("check.json", "w", encoding="utf-8") as file:
            keyjsona["exe"] = 1
            json.dump (keyjsona, file, indent = 4)
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
        executables_name = f"""\nExecutable(script=r"{script}", base="{base}", target_name="{target_name}", icon="{icon}"),"""
        if script == "":
            messagebox.showerror("Error", "Please select a .py file.")
            return
        if icon == "":
            executables_name = f"""Executable(script=r"{script}", base="{base}", target_name="{target_name}", icon=None),"""
        if base == "":
            executables_name = f"""Executable(script=r"{script}", base=None, target_name="{target_name}", icon="{icon}"),\n"""
        if target_name == "":
            executables_name = f"""Executable(script=r"{script}", base=None, target_name=None, icon="{icon}"),\n"""
        if target_name == "" and base == "":
            executables_name = f"""Executable(script=r"{script}", base=None, target_name=None, icon=None),\n"""
        if icon == "" and base == "":
            executables_name = f"""Executable(script=r"{script}", base=None, target_name="{target_name}", icon=None),\n"""
        if icon == "" and target_name == "":
            executables_name = f"""Executable(script=r"{script}", base="{base}", target_name=None, icon=None),\n"""
        entry1a.insert (tk.END, executables_name)
    def clear():
        entry1a.delete(1.0, tk.END)
        with open("dataexecutables.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("dataexecutables.json", "w", encoding="utf-8") as f:
            data["executables"] = []
            json.dump(data, f, indent=4)
        check_exe()
    def save():
        if not entry1a.get("1.0", tk.END).strip() == "":
            with open("dataexecutables.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            datawrite = entry1a.get("1.0", tk.END).strip()
            with open ("dataexecutables.json", "w", encoding="utf-8") as f:
                data["executables"] = []
                for line in datawrite.splitlines():
                    with open ("dataexecutables.json", "w", encoding="utf-8") as f:
                        data["executables"].append(f"{line}"+ "\n")
                        json.dump(data, f, indent=4)
            messagebox.showinfo("Success", "Data saved successfully")
            check_exe()
        else:
            messagebox.showerror("Error", "No executable found")

    exe = tk.Tk()
    exe.title("Add Executables")
    exe.geometry("800x220")
    exe.resizable(False, False)

    text1a = tk.Label(exe, text="Executable Path:")
    text1a.place (x=10, y=10)

    entry1a = tk.Text(exe, height=10, width=50, wrap=tk.NONE)
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
    button5a = tk.Button (exe, text = "Save", command = save)
    button5a.place(x=670, y=150)

    scrolly2 = tk.Scrollbar(exe, orient = tk.VERTICAL, command=entry1a.yview)
    entry1a.config(yscrollcommand=scrolly2.set)
    scrolly2.place(x=420, y=32, height=160)
    scrollx2 = tk.Scrollbar (exe, orient = tk.HORIZONTAL, command = entry1a.xview)
    entry1a.config(xscrollcommand=scrollx2.set)
    scrollx2.place(x=15, y=195, width=390)

    with open("dataexecutables.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        edata = data["executables"]
        for item in edata:
            entry1a.insert(tk.END, item)

    exe.mainloop()