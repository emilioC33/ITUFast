from PIL import Image
import numpy as np

arr = np.genfromtxt("image.csv", encoding="utf8")
arr = arr*255
arr = arr.reshape((64, 64))
im = Image.fromarray(arr)
im = im.convert("RGB")
im.save("input.png")
