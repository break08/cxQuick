import tkinter as tk
from tkinter import ttk, filedialog, messagebox

exe = tk.Tk()
exe.title("Choose Executable")
exe.geometry("800x350")
exe.resizable(False, False)

text1a = tk.Label(exe, text="Executable Path:")
text1a.place (x=10, y=10)

entry1a = tk.Text(exe, height=10, width=50)
entry1a.place (x=10, y=30)

text2a = tk.Label (exe, text = ".py path file:")
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

checkbox1 = tk.Checkbutton(exe, text="Compress .exe")
checkbox1.place (x=10, y=210)

checkbox2 = tk.Checkbutton (exe, text = "copyDependentFiles")
checkbox2.place (x=10, y=240)

checkbox3 = tk.Checkbutton (exe, text = "appendScriptToExe")
checkbox3.place (x=10, y=270)

checkbox4 = tk.Checkbutton (exe, text = "appendScriptToLibrary (Compress script to .zip)")
checkbox4.place (x=10, y=300)

exe.mainloop()