import numpy as np
from PIL import Image
import matplotlib as plt
Deuteranomaly0_5 = (0.547494, 0.607765, -0.155259, 0, 0.181692, 0.781742, 0.036566, 0, -0.010410, 0.027275, 0.983136, 0)
im = (Image.open('pencils.jpg'))

out = im.convert("RGB", Deuteranomaly0_5, None, 0,256)
out.show()
# img = img.convert("RGB", Deuteranomaly0_5)
# img.show()

# for x in range(width) :
#     for y in range(height) :
#         img[x,y] = 160

