# import PIL
# from PIL import Image
# from tkinter.filedialog import *

# f1 = askopenfilename(title="Select an image file", 
#                     filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])

# if f1:
#     img = Image.open(f1)
#     print("Original size:", img.size)

#     # Compress the image
#     img = img.resize((img.width // 2, img.height // 2), Image.Resampling.LANCZOS)
#     print("Compressed size:", img.size)
#     img.show()
#     # Save the compressed image
#     f2 = asksaveasfilename(defaultextension=".jpg", 
#                            filetypes=[("JPEG files", "*.jpg"), 
#                                       ("PNG files", "*.png"), 
#                                       ("BMP files", "*.bmp")])
#     if f2:
#         img.save(f2)
#         img.show()
#         print("Image saved as:", f2)

#------------------------------------------------------------------------------------
# Step 2:

import PIL
from PIL import Image

from tkinter.filedialog import *

file_name = askopenfilename()
img = Image.open(file_name)
img.save("comp_png", "JPEG", optimize = True, quality=80)
Image.open("comp_png").show()

#------------------------------------------------------------------------------------
import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Hide the root Tkinter window
Tk().withdraw()

# Ask user to select a folder
folder_path = askdirectory(title="Select Folder Containing Images")

# Output folder for compressed images
output_folder = os.path.join(folder_path, "compressed")
os.makedirs(output_folder, exist_ok=True)

# Supported image formats
supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(supported_formats):
        file_path = os.path.join(folder_path, filename)
        try:
            img = Image.open(file_path)
            # Convert to RGB if image has alpha channel
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            # Save compressed image
            compressed_path = os.path.join(output_folder, f"compressed_{filename}.jpg")
            img.save(compressed_path, "JPEG", optimize=True, quality=80)
            print(f"Compressed: {filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")