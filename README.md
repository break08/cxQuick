# cxQuick

**cxQuick** is a graphical tool that simplifies converting `.py` Python scripts into `.exe` executables using [`cx_Freeze`](https://github.com/marcelotduarte/cx_Freeze).

## 🖼 Features

- Simple and clean Tkinter-based GUI.
- Browse and select Python files and icon files.
- Set metadata: name, version, and description.
- Choose base: `Win32GUI` (no terminal) or `Console`.
- Choose a custom output directory.
- Auto-generates a `setup.py` and builds the executable.

## 📦 Requirements

- Python 3.7+
- `cx_Freeze` installed:
  ```bash
  pip install cx_Freeze

## 🚀 How to Use

1. Run `cxquick.py`.

2. Select your `.py` script using the **Browse .py file** button.

3. Fill in the following fields:
   - **Name**: The name of your application.
   - **Version**: The version number of your application.
   - **Description**: A short description of what your application does.
   - **Icon path**: Path to a `.ico` file (optional).
   - **Base**: Choose one of the following:
     - `Win32GUI`: for applications without a terminal window.
     - `Console`: for applications that require a terminal.

4. Set the **Output directory** using the **Browse Output Directory** button.
   - ⚠️ This must be an **empty folder**. If it is not empty, the build will be aborted.

5. Click the **Build** button to generate your `.exe` file.

Once done:
- A temporary `setup.py` will be created in the `temp/` folder.
- `cx_Freeze` will run using `os.system()` to build the `.exe`.
- A success message will be shown once the process completes.
