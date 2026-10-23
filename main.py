
import tkinter as tk
from PIL import Image, ImageTk
import os

# Main Window
root = tk.Tk()
root.title("Photo Album Slideshow")
root.geometry("900x850")
root.configure(bg="#202020")

# Image folder path
image_folder = r"C:\Python\python project\album photos"

# Image paths
image_paths = [
    os.path.join(image_folder, "image1.jpeg"),
    os.path.join(image_folder, "image2.jpeg"),
    os.path.join(image_folder, "image3.jpeg"),
    os.path.join(image_folder, "image4.jpeg"),
    os.path.join(image_folder, "image5.jpeg")
]

# Load images
final_images = []

for path in image_paths:
    if os.path.exists(path):
        img = Image.open(path)
        img = img.resize((700, 600))
        photo = ImageTk.PhotoImage(img)
        final_images.append(photo)
    else:
        print("Image not found:", path)

# Current image index
current_index = 0
slideshow_running = False
after_id = None

# Heading
heading = tk.Label(
    root,
    text="My Photo Album",
    font=("Arial", 25, "bold"),
    bg="#202020",
    fg="white"
)
heading.pack(pady=15)

# Image display label
image_label = tk.Label(root, bg="#202020")
image_label.pack(pady=10)

# Image counter
counter_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#202020",
    fg="white"
)
counter_label.pack(pady=5)


# Display image
def show_image():
    global current_index

    if not final_images:
        image_label.config(
            image="",
            text="No images found!\nPlease check the image folder.",
            fg="white",
            font=("Arial", 16),
            bg="#202020"
        )
        counter_label.config(text="")
        return

    image_label.config(image=final_images[current_index])
    image_label.image = final_images[current_index]

    counter_label.config(
        text=f"Image {current_index + 1} of {len(final_images)}"
    )


# Automatically change image
def next_slide():
    global current_index, after_id

    if not slideshow_running:
        return

    current_index = (current_index + 1) % len(final_images)
    show_image()

    after_id = root.after(2000, next_slide)


# Start slideshow
def start_slideshow():
    global slideshow_running, after_id

    if not final_images:
        show_image()
        return

    if not slideshow_running:
        slideshow_running = True
        show_image()
        after_id = root.after(2000, next_slide)


# Stop slideshow
def stop_slideshow():
    global slideshow_running, after_id

    slideshow_running = False

    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None


# Manual next image
def next_image():
    global current_index

    if final_images:
        current_index = (current_index + 1) % len(final_images)
        show_image()


# Manual previous image
def previous_image():
    global current_index

    if final_images:
        current_index = (current_index - 1) % len(final_images)
        show_image()


# Buttons
button_frame = tk.Frame(root, bg="#202020")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Previous",
    font=("Arial", 12),
    command=previous_image,
    width=10
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Start Slideshow",
    font=("Arial", 12),
    command=start_slideshow,
    width=15
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Stop",
    font=("Arial", 12),
    command=stop_slideshow,
    width=10
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Next",
    font=("Arial", 12),
    command=next_image,
    width=10
).grid(row=0, column=3, padx=5)


# Show first image when application opens
show_image()

# Run application
root.mainloop()
