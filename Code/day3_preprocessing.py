from pathlib import Path
from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt

# path locate karna 
project_path=Path(__file__).resolve().parent.parent
dataset_path=project_path/"Dataset"
data_path=next(dataset_path.iterdir())
train_path=data_path/"train"
print("Train Path:",train_path)

# image load 
extensions={".jpg",".jpeg",".png",".bmp",".webp"}
class_folders=[
    folder for folder in train_path.iterdir()
    if folder.is_dir()
]
sample_class=class_folders[0]
image_files=[
    file for file in sample_class.rglob("*")
    if file.suffix.lower() in extensions
]
image_path =image_files[0]
img =Image .open (image_path).convert("RGB")
print("Image Path:",image_path)
print("Original Image Size:",img.size)

#image resize karna 
resized_img=img.resize((224,224))
print("Resize Image Size:",resized_img.size)

# conver image into numpy aray
image_array=np.array(resized_img)
print("Image Shape:",image_array.shape)
print("Pixel Values:",image_array[0][0])

#image normalize
normalized_image=image_array/255.0
print("Minimum Pixel Value",normalized_image.min())
print("Maximum Pixel Value",normalized_image.max())

# original vs processed img visulaised
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original Image ")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(normalized_image)
plt.title("Normalized Image ")
plt.axis("off")
plt.tight_layout()
plt.show()

#data augmentation
from PIL import ImageEnhance
flipped_img =img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
rotated_img=img.rotate(10)
enhancer=ImageEnhance.Brightness(img)
bright_img=enhancer.enhance(1.5)
zoom_img=img.resize((280,280)).crop((28,28,252,252))

#display augmented img
plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(flipped_img)
plt.title("Horizontal Flip")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(rotated_img)
plt.title("Rotation")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(bright_img)
plt.title("Brightness")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(zoom_img)
plt.title("Zoom")
plt.axis("off")
plt.tight_layout()
plt.show()