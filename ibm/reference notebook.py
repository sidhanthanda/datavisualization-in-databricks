# Databricks notebook source
import matplotlib.pyplot as plt

# COMMAND ----------

!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CV0101EN-SkillsNetwork/images%20/images_part_1/cat.png -O cat.png
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CV0101EN-SkillsNetwork/images%20/images_part_1/lenna.png -O lenna.png
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CV0101EN-SkillsNetwork/images%20/images_part_1/baboon.png -O baboon.png

#gets the images

# COMMAND ----------

from PIL import Image

def get_concat_h(im1, im2):
    # Create a new image with a width equal to the sum of im1 and im2's widths, and the height of im1
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    
    # Paste image im1 at the starting point (0, 0) on the new image 'dst'
    dst.paste(im1, (0, 0))
    
    # Paste image im2 right next to im1 by starting at (im1.width, 0) on the new image 'dst'
    dst.paste(im2, (im1.width, 0))
    
    # Return the new concatenated image
    return dst


# COMMAND ----------

image1 = "lenna.png"

# COMMAND ----------

import os
cwd = os.getcwd()
cwd 
#shows directory where the work is being done

# COMMAND ----------

image_path = os.path.join(cwd, image1)
image_path

#joins the cwd directory with image 1, so now the directory shows you the location of image 1


# COMMAND ----------

from PIL import Image
image = Image.open(image1)
#line above saves image1 to a variable, then shows the type of file the var is
type(image)
image
#shows the image

# COMMAND ----------

import matplotlib.pyplot as plt

# COMMAND ----------

plt.figure(figsize=(10,10))
#sets the size of the image that is displayed
plt.imshow(image)
plt.show()

# COMMAND ----------

image = Image.open(image_path)

# COMMAND ----------

# MAGIC %pip install opencv-python

# COMMAND ----------

from PIL import Image
import numpy as np

image = Image.open(image1)
import cv2

# COMMAND ----------

image.size

# COMMAND ----------

import matplotlib.pyplot as plt

import numpy as np

upper = 75
lower = 200
image_array = np.array(image)  
crop_top = image_array[upper:lower, :, :]

plt.imshow(crop_top)
plt.show()


# COMMAND ----------

image = Image.open("baboon.png")

# COMMAND ----------

from PIL import Image, ImageDraw
from IPython.display import display  # Import display from IPython.display

# Load an image
image = Image.open('baboon.png')
image_draw = image.copy()

# Create a drawing object
image_fn = ImageDraw.Draw(image_draw)

# Define coordinates for the rectangle
left = 50
upper = 200
right = 130
lower = 190
shape = [left, upper, right, lower]

# Draw the rectangle
image_fn.rectangle(xy=shape, fill="red")

# Display the image in the notebook
display(image_draw)



# COMMAND ----------

from PIL import Image, ImageDraw, ImageFont

# Load an image
image = Image.open('baboon.png')  # Replace with the correct path to your image

# Create a drawing object
image_draw = image.copy()
image_fn = ImageDraw.Draw(image_draw)

# Attempt to load Arial font, or fall back to the default font
try:
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 100)
except IOError:
    print("Font file not found, using default font.")
    fnt = ImageFont.load_default()

# Add text to the image
image_fn.text((10,10), "box", font=fnt, fill=(0,0,0))  # Adjust text position if needed

# Display the image
image_draw.show()


# COMMAND ----------

from PIL import Image

# Assuming crop_top is defined elsewhere and compatible
try:
    image_of_lady = Image.open("lenna.png")  # Ensure the file exists and is accessible
    left = 150
    upper = 120

    # Paste crop_top onto image_of_lady at the specified position
    image_of_lady.paste(crop_top, (left, upper))

    # Display the modified image to confirm changes
    image_of_lady.show()

except FileNotFoundError:
    print("Image file not found. Check the file name and path.")
except Exception as e:
    print(f"An error occurred: {e}")


# COMMAND ----------


