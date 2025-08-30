# a.Write a Python program to display details of an image (dimension of an image, shape of an image, min pixel value at channel B).

from PIL import Image
import numpy as np

# Load image
img = Image.open("D:\onedrive_storage\OneDrive\Pictures\MU.jpg")   
img_array = np.array(img)

print("Dimensions:", img.size)                
print("Shape:", img_array.shape)               
print("Min pixel value at channel B:", img_array[:,:,2].min())  

# b. Write a Python program to padding black spaces 

import matplotlib.pyplot as plt
from PIL import Image, ImageOps
img = Image.open("D:\onedrive_storage\OneDrive\Pictures\MU.jpg")
padded_img = ImageOps.expand(img, border=(50, 50, 100, 100), fill="black")

# Show images
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original")
plt.subplot(1,2,2)
plt.imshow(padded_img)
plt.title("Padded")
plt.show()


# c. Write a Python program to visualize RGB channels 

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
img = Image.open("D:\onedrive_storage\OneDrive\Pictures\MU.jpg")
img_array = np.array(img)

R = img_array[:,:,0]
G = img_array[:,:,1]
B = img_array[:,:,2]

plt.subplot(2,2,1), plt.imshow(img), plt.title("Original")
plt.subplot(2,2,2), plt.imshow(R, cmap="Reds"), plt.title("Red Channel")
plt.subplot(2,2,3), plt.imshow(G, cmap="Greens"), plt.title("Green Channel")
plt.subplot(2,2,4), plt.imshow(B, cmap="Blues"), plt.title("Blue Channel")
plt.show()
