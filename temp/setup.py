from cx_Freeze import setup, Executable
buid_exe_options = {
    "packages": ["os"],
    "build_exe": "C:/Users/Sieu Toc PC/Desktop/â"
}
setup(
    name="a",
    version="1.0",
    description="a",
    options={"build_exe": buid_exe_options},
    executables=[Executable("C:/Users/Sieu Toc PC/Desktop/my_project/filein2winsandbox/filein2winsandbox.py", base="Win32GUI", icon="C:/Users/Sieu Toc PC/Desktop/my_project/filein2winsandbox/icon/icon.ico")],
)
