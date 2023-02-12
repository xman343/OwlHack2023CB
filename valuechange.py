# Changes the value of the original image to make it more accessible for colorblind viewers. 

# from PIL import Image
import cv2
import numpy as np
from PIL import Image
    
    
def cb_compatible(img, val_shift):
    im_rgb = np.array(img)
    
    # Converts to BGR scale for CV2 compatibility
    im_bgr = im_rgb[:, :, ::-1].copy()
    
    # Converts to HSV for hue modification
    im_hsv = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2HSV)
    
    if val_shift == "b":
    
        # Shifts hue to blue 
        shift_n = 180 // 2
        im_hsv[:, :, 0] = (im_hsv[:, :, 0].astype(np.int) + shift_n) % 181
    
    if val_shift == "g":
    
        # Shifts hue to green 
        shift_n = 90 // 2
        im_hsv[:, :, 0] = (im_hsv[:, :, 0].astype(np.int) + shift_n) % 181
    
    if val_shift == "r":
    
    # Shifts hue to red
        shift_n = 45 // 2
        im_hsv[:, :, 0] = (im_hsv[:, :, 0].astype(np.int) + shift_n) % 181

    # Converts file back to RGB 
    im_rgb_mod = cv2.cvtColor(im_hsv, cv2.COLOR_HSV2RGB)
    im_rgb_mod = Image.fromarray(im_rgb_mod, 'RGB')
    return im_rgb_mod

# img = (Image.open("ishihara.jpg"))

# val_shift = "g"

# new_img = cb_compatible(img, val_shift)

# new_img.show()