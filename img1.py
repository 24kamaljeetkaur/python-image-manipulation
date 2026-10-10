
import numpy as np
from PIL import Image


class ImageProcessor:
    def __init__(self, image_path):
        self.image = Image.open(image_path).convert("RGB")
        self.array = np.array(self.image, dtype=np.uint8)

    def show_info(self):
        print("Image type:", type(self.image))
        print("Array type:", type(self.array))
        print("Array shape:", self.array.shape)
        print("Array size:", self.array.size)
        print("Array data type:", self.array.dtype)
        print("First pixel:", self.array[0, 0])
        print("Top-left pixel:", self.array[0, 0])
        print("Next pixel:", self.array[0, 1])
        print("Next row pixel:", self.array[1, 0])
        print("Pixel at 10, 10:", self.array[10, 10])

    def flip_horizontal(self):
        # Reverse columns
        self.array = self.array[:, ::-1, :].copy()
        return self

    def flip_vertical(self):
        # Reverse rows
        self.array = self.array[::-1, :, :].copy()
        return self

    def crop(self, x1, y1, x2, y2):
        height, width = self.array.shape[:2]

        if not (0 <= x1 < x2 <= width):
            raise ValueError("Invalid horizontal crop coordinates")

        if not (0 <= y1 < y2 <= height):
            raise ValueError("Invalid vertical crop coordinates")

        self.array = self.array[y1:y2, x1:x2, :].copy()
        return self

    def adjust_brightness(self, value):
        # Positive value = brighter; negative = darker
        adjusted = self.array.astype(np.int16) + value
        self.array = np.clip(adjusted, 0, 255).astype(np.uint8)
        return self

    def save(self, output_path):
        Image.fromarray(self.array).save(output_path)
        print("Image saved:", output_path)
        return self


processor = ImageProcessor("12.png")

processor.show_info()

processor.flip_horizontal()
processor.flip_vertical()
processor.crop(10, 10, 200, 200)
processor.adjust_brightness(30)
processor.save("output.png")
