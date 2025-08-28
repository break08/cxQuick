# cxQuick

**cxQuick** is a graphical tool that simplifies converting `.py` Python scripts into `.exe` executables using [`cx_Freeze`](https://github.com/marcelotduarte/cx_Freeze).

## 📦 Requirements

- Python 3.7+
- `cx_Freeze` installed:
  ```bash
  pip install cx_Freeze

## How to Use

1. Run `cxquick.py`.

2. Select your `.py` script using the **Browse .py file** button.

3. Fill in the fields:
   
   **Main Window**:
   - **Name**: The name of your application.
   - **Version**: The version number of your application.
   - **Description**: A short description of what your application does.
   - Executables Field (Forced to be edit in Add Excutables Window)
     
   **Add Executables Window**(Forced):
   
   - **Path to your .py file** (Forced)
   - Icon, Base and Target name are not forced
   - **Remember to click add executables to create or save button to save your choices**

   **Add Included Window** (Not Forced):
   - **Direct the Files/Folders**(Forced if you want to add)
   - **Output** : Write the file's or folder's name for the copied (will be in output folder after build)
   **Don't fill the Output if you want the default name of files and folders**
   **With folder (changed name): add `/` at the end of the name to avoid errors**

5. Set the **Output directory** using the **Browse Output Directory** button.
   - ⚠️ This must be an **empty folder**. If it is not empty, the build will be aborted.

6. Click the **Build** button and wait while cx_Freeze generates your `.exe` file.

Once done:
- A `setup.py` will be created in the `saves/` folder.
- `cx_Freeze` will build the `.exe`.
- A success message will be shown once the process completes.



