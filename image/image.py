
import numpy as np

# Represent an image using a matrix
image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Original Image:")
print(image)

# Reshape the image matrix
reshaped = image.reshape(2, 8)
print("\nReshaped Image:")
print(reshaped)

# Slice a specific region
region = image[0:2, 0:2]
print("\nSelected Region:")
print(region)

# Brightness adjustment using broadcasting
bright_image = np.clip(image + 20, 0, 255)
print("\nImage After Brightness Adjustment:")
print(bright_image)

# Matrix multiplication for transformation
transform = np.eye(4, dtype=int)
transformed = image @ transform

print("\nTransformed Image:")
print(transformed)
