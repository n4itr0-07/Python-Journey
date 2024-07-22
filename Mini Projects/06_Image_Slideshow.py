from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image Slideshow Viewer")

#List of Image Path
image_paths =[
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\1719805096357.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\anon2.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\CS.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\Linux Cheetsheet.jpg",
    r"C:\Users\Salik\OneDrive\Pictures\Screenshots\Saved Pictures\Salik Naik QR Code.png",

]
# Resize Images
image_size =(1080,1080)
images=[Image.open(path). resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

lable = tk.Label(root)
lable.pack()

def update_image():
    for photoImage in photo_images:
        lable.config(image=photo_images)
        lable.update()
        lable.sleep(3)


slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()