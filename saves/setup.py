from cx_Freeze import setup, Executable
build_exe_options = {
    "packages": [],
    "includes": [],
    "excludes": [],
    "build_exe": r"C:\Users\lmdun\a",
    "include_files": [(r"C:/Users/lmdun/.mcreator/recentworkspaces", "recentworkspaces"),],
}
setup(
    name="a",
    version="1.0",
    description="a",
    options={"build_exe": build_exe_options},
    executables=[Executable(script=r"C:/Users/lmdun/OneDrive/Hình ảnh/cxquick.py", base=None, target_name=None, icon=None),],
)
