# Tkinter Digital Clock

This Python script creates a digital clock using the Tkinter library, displaying the current time and date.

## Step-by-Step Explanation

1. **Import Required Libraries:**
   ```python
   import tkinter as tk
   from time import strftime
   ```
   - The `tkinter` library is imported as `tk` for creating the graphical user interface.
   - The `strftime` function from the `time` library is imported for formatting the current time and date.

2. **Initialize the Tkinter Window:**
   ```python
   root = tk.Tk()
   root.title("Digital Clock")
   ```
   - A Tkinter window object `root` is created.
   - The title of the window is set to "Digital Clock".

3. **Define the Time Function:**
   ```python
   def time():
       string = strftime("%H:%M:%S %p \n %D")
       label.config(text=string)
       label.after(1000, time)
   ```
   - The `time` function is defined to update the clock display.
   - `strftime` is used to format the current time and date as "Hours:Minutes:Seconds AM/PM \n Month/Day/Year".
   - The `label` widget's text is updated with the formatted time string.
   - `label.after(1000, time)` schedules the `time` function to be called again after 1000 milliseconds (1 second), ensuring the clock updates every second.

4. **Create and Configure the Label Widget:**
   ```python
   label = tk.Label(root, font=("calibri", 50, "bold"), bg="black", fg="white")
   ```
   - A `Label` widget is created and attached to the `root` window.
   - The font is set to "calibri", size 50, and bold.
   - The background color is set to black and the foreground (text) color is set to white.

5. **Pack the Label Widget:**
   ```python
   label.pack(anchor="center")
   ```
   - The `Label` widget is packed into the window with the anchor set to "center", centering the label within the window.

6. **Call the Time Function to Start the Clock:**
   ```python
   time()
   ```
   - The `time` function is called to initiate the clock update process.

7. **Run the Tkinter Main Loop:**
   ```python
   root.mainloop()
   ```
   - The `mainloop` method of the `root` window is called to start the Tkinter event loop, keeping the window open and responsive.

## Complete Code

```python
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=("calibri", 50, "bold"), bg="black", fg="white")

label.pack(anchor="center")

time()

root.mainloop()
```

---

**Follow Salik Seraj Naik On X**

---