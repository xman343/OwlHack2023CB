# Changes the value of the original image to make it more accessible for colorblind viewers. 

# from PIL import Image
import cv2
import numpy as np
from PIL import Image
    
    
def cb_compatible(img):
    im_rgb = np.array(img)
    
    # Converts to BGR scale for CV2 compatibility
    im_bgr = im_rgb[:, :, ::-1].copy()
    
    # Converts to HSV for hue modification
    im_hsv = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2HSV)
    
    # Shifts hue to blue (more CB compatible)
    shift_n = 180 // 2
    im_hsv[:, :, 0] = (im_hsv[:, :, 0].astype(np.int) + shift_n) % 181
    
    # Converts file back to RGB 
    im_rgb_mod = cv2.cvtColor(im_hsv, cv2.COLOR_HSV2RGB)
    im_rgb_mod = Image.fromarray(im_rgb_mod, 'RGB')
    return im_rgb_mod

img = (Image.open("ishihara.jpg"))

new_img = cb_compatible(img)

new_img.show()

# # Import image
# im_rgb = cv2.imread('ishihara.jpg')

# # Convert from RGB to HSV
# im_hsv = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2HSV)

# # Shift hue
# shift_n = 180 // 2
# im_hsv[:, :, 0] = (im_hsv[:, :, 0].astype(np.int) + shift_n) % 181

# im_rgb_mod = cv2.cvtColor(im_hsv, cv2.COLOR_HSV2BGR)
# cv2.imwrite('ishihara_mod.jpg', im_rgb_mod)

# def rgb_to_hsv(img):
#     return img.convert('HSV')
    
# def hsv_to_rgb(img):
#     return img.convert('RGB')


    