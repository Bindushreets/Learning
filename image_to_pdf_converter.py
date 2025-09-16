# # 

# from PIL import Image
# import os

# # Folder containing images
# folder_path = r"D:/Marriage_Photo_segrigation/Sindhu"
# output_path = os.path.join(folder_path, "Bindu&Manoj_Wedding_pics.pdf")

# # Get sorted list of image files
# image_files = sorted([
#     f for f in os.listdir(folder_path)
#     if f.lower().endswith((".jpg", ".jpeg", ".png"))
# ])

# first_image = None
# image_list = []

# for idx, file in enumerate(image_files):
#     img_path = os.path.join(folder_path, file)
#     try:
#         img = Image.open(img_path).convert("RGB")
#         if idx == 0:
#             first_image = img
#         else:
#             image_list.append(img)
#         #print(f"✔️ Added: {file}")
#     except Exception as e:
#         print(f"❌ Error loading {file}: {e}")

# # Save to PDF
# if first_image:
#     first_image.save(output_path, save_all=True, append_images=image_list)
#     print(f"\n✅ PDF created successfully: {output_path}")
# else:
#     print("\n⚠️ No valid images found to convert.")

from PIL import Image
import os
import img2pdf


# Folder containing images
folder_path = r"D:/Marriage_Photo_segrigation/Sindhu"
output_path = os.path.join(folder_path, "Bindu&Manoj_Wedding_pics.pdf")

# Get sorted list of image files
image_files = sorted([
    f for f in os.listdir(folder_path)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

first_image = None
image_list = []

for idx, file in enumerate(image_files):
    img_path = os.path.join(folder_path, file)
    try:
        with Image.open(img_path).convert("RGB") as img:
            if idx == 0:
                first_image = img.copy()
            else:
                image_list.append(img.copy())
            img.close()
        # Image is automatically closed after 'with' block
    except Exception as e:
        print(f"❌ Error loading {file}: {e}")

# Save to PDF
if first_image:
    first_image.save(output_path, save_all=True, append_images=image_list)
    print(f"\n✅ PDF created successfully: {output_path}")
else:
    print("\n⚠️ No valid images found to convert.")