# Image Slideshow Viewer

This guide will help you create an image slideshow viewer using Python with the Tkinter and PIL libraries.

## Prerequisites

1. **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **PIL (Pillow)**: Install the Pillow library using pip.

   ```sh
   pip install Pillow
   ```

3. **Tkinter**: Tkinter is included with standard Python installations. No separate installation is required.

## Steps

### 1. Set Up the Python Script

Create a new Python file (e.g., `slideshow_viewer.py`) and open it in your favorite code editor.

### 2. Import Required Libraries

Add the following import statements at the top of your Python script:

```python
from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk
```

### 3. Initialize the Tkinter Root Window

Create the root window and set the title:

```python
root = tk.Tk()
root.title("Image Slideshow Viewer")
```

### 4. Define the Image Paths

List the paths of the images you want to include in the slideshow:

```python
image_paths = [
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\1719805096357.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\anon2.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\CS.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\Linux Cheetsheet.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\Salik Naik QR Code.png",
]
```

### 5. Resize Images

Resize the images to the desired size and create `PhotoImage` objects:

```python
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]
```

### 6. Create a Label Widget

Create a label widget to display the images:

```python
label = tk.Label(root)
label.pack()
```

### 7. Update Image Function

Define a function to update the displayed image:

```python
def update_image():
    for photoImage in photo_images:
        label.config(image=photoImage)
        label.update()
        time.sleep(3)
```

### 8. Start Slideshow Function

Define a function to start the slideshow:

```python
slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()
```

### 9. Add Play Button

Add a button to start the slideshow:

```python
play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()
```

### 10. Run the Tkinter Main Loop

Run the Tkinter main loop:

```python
root.mainloop()
```

### 11. Full Script

Here is the complete script for reference:

```python
from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image Paths
image_paths = [
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\1719805096357.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\anon2.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\CS.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\Linux Cheetsheet.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\Salik Naik QR Code.png",
]

# Resize Images
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photoImage in photo_images:
        label.config(image=photoImage)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
```

## Follow Me

For more projects and updates, follow me [here](https://linktr.ee/SalikSerajNaik).
