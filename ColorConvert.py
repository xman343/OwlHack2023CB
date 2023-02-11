import numpy as np
from PIL import Image 

im = Image.open("pencils.jpeg")

img = np.array(im)

Deuteranomaly0_5 = np.array([[0.547494, 0.607765, -0.155259],[0.181692, 0.781742, 0.036566],[-0.010410, 0.027275, 0.983136]])

cb_data = np.dot(img, Deuteranomaly0_5)

print(cb_data)

cb_data[cb_data<0] = 0
            
print(cb_data.size)

cb_img = Image.fromarray((cb_data).astype(np.uint8))

cb_img.show()

# red = np.transpose(np.array([255, 0, 0]))
# green = np.transpose(np.array([0,255,0]))
# magenta = np.transpose(np.array([255,0,255]))

# Deuteranomaly0_5 = np.array([[0.547494, 0.607765, -0.155259],[0.181692, 0.781742, 0.036566],[-0.010410, 0.027275, 0.983136]])


# print('red',np.dot(Deuteranomaly0_5,red))
# print('green',np.dot(Deuteranomaly0_5,green))
# print('magenta',np.dot(Deuteranomaly0_5,magenta))