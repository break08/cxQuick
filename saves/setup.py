from cx_Freeze import setup, Executable
build_exe_options = {
    "packages": ['os', 'tkinter'],
    "includes": ['pygame'],
    "excludes": ['tempfile'],
    "build_exe": r"C:\Users\lmdun\OneDrive\Desktop\a12",
    "include_files": [(r"C:/Users/lmdun/OneDrive/Desktop/my_project/filein2winsandbox/user-change.json", "user-change.json"),
(r"C:/Users/lmdun/OneDrive/Desktop/my_project/filein2winsandbox/LICENSE", "LICENSE"),],
    "optimize": 0,
    "include_msvcr": True,
}
setup(
    name="ex",
    version="1.0",
    description="ex",
    options={"build_exe": build_exe_options},
    executables=[Executable(script=r"C:/Users/lmdun/OneDrive/Desktop/my_project/setup.py", base="Win32GUI", target_name=None, icon=None),
Executable(script=r"C:/Users/lmdun/OneDrive/Desktop/my_project/filein2winsandbox/filein2winsandbox.py", base=None, target_name=None, icon="C:/Users/lmdun/OneDrive/Desktop/my_project/filein2winsandbox/icon/icon.ico"),],
)
