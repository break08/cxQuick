from cx_Freeze import setup, Executable
build_exe_options = {
    "packages": ["os"],
    "build_exe": r"C:\Users\Sieu Toc PC\Desktop\â"
}
setup(
    name="a",
    version="1.0",
    description="a",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="C:/Users/Sieu Toc PC/Desktop/my_project/filein2winsandbox/filein2winsandbox.py", base="Win32GUI", target_name="gi", icon="C:/Users/Sieu Toc PC/Desktop/my_project/filein2winsandbox/icon/icon.ico"),],
)
