import numpy as np
from PIL import Image


image_path = "12.png"

image = Image.open(image_path).convert("RGB")
array = np.array(image, dtype=np.uint8)

print("image type:" , type(image))
print("Array type:", type(array))
print("Array shape:", array.shape)
print("Array size:", array.size)
print("Array data type:", array.dtype)
print("First pixel:", array[0, 0])
print("Top-left pixel:", array[0, 0])
print("Next pixel:", array[0, 1])
print("Next row pixel:", array[1, 0])
print("Pixel at 10, 10:", array[10, 10])
# image type: <class 'PIL.Image.Image'>
# Array type: <class 'numpy.ndarray'>
# Array shape: (204, 204, 3)
# Array data type: uint8
# First pixel: [0 0 0]