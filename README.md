pip install pillow
pip install pyinstaller

pyinstaller --onefile --windowed --icon=logo.ico inf_tine_cal.py


To make your **Python script** a standalone executable file that can be run by double-clicking, you can use a tool like **`pyinstaller`**. Here's the step-by-step guide:

---

### Steps to Create an Executable File

#### 1. **Install PyInstaller**
Open a terminal or command prompt and install `pyinstaller` if it's not already installed:
```bash
pip install pyinstaller
```

---

#### 2. **Prepare Your Script**
Ensure your Python script (e.g., `inference_time_app.py`) is ready and that the logo image (e.g., `logo.png`) is in the same directory.

---

#### 3. **Run PyInstaller**
Open a terminal in the directory where your script is saved and execute the following command:

```bash
pyinstaller --onefile --windowed --icon=logo.ico inference_time_app.py
```

- **`--onefile`**: Packages everything into a single executable file.
- **`--windowed`**: Suppresses the terminal window (important for GUI apps).
- **`--icon=logo.ico`**: Adds a custom icon (replace `logo.ico` with your icon file).

---

#### 4. **Convert Logo (if necessary)**
If you don't already have a `.ico` file for the logo, convert your PNG logo using a free online tool or by running this Python snippet with Pillow installed:

```python
from PIL import Image

# Convert PNG to ICO
image = Image.open("logo.png")
image.save("logo.ico", format="ICO", sizes=[(64, 64)])
```

---

#### 5. **Locate the Executable**
After running PyInstaller, you will see a new **`dist`** folder created in your directory. Inside the `dist` folder, you’ll find your executable file (`inference_time_app.exe`).

---

#### 6. **Run the Executable**
Double-click the `inference_time_app.exe` file to launch the application. It should open without needing Python installed on the machine.

---

### Additional Notes
1. **Keep the Icon File Small**:
   - ICO files should be less than 256x256 pixels for optimal performance.
   
2. **Testing on Other Machines**:
   - Test the generated `.exe` file on a different machine without Python installed to ensure it works correctly.

3. **Distribute the Application**:
   - You can share the `.exe` file directly or bundle it into a ZIP archive for distribution.

---

### Example Command Recap:
```bash
pyinstaller --onefile --windowed --icon=logo.ico inference_time_app.py
```

---

Now you have a professional standalone application that can be run by double-clicking! If you encounter any issues during the process, feel free to ask for help. 😊
