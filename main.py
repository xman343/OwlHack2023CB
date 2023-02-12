import numpy as np
from PIL import Image
import matplotlib as plt
from valuechange import cb_compatible

Deuteranomaly0_5 = (0.547494, 0.607765, -0.155259, 0, 0.181692, 0.781742, 0.036566, 0, -0.010410, 0.027275, 0.983136, 0)
Protanomaly0_5 = (0.458064, 0.679578, -0.137642, 0, 0.092785, 0.846313, 0.060902, 0, -0.007494, -0.016807, 1.024301, 0)
Tritanomaly0_5 = (1.017277, 0.027029, -0.044306, 0, -0.006113, 0.958479, 0.047634, 0, 0.006379, 0.248708, 0.744913, 0)
Tritanomaly0_8 = (1.257728, -0.139648, -0.118081, 0, -0.078003, 0.975409, 0.102594, 0, -0.003316, 0.501214, 0.502102, 0)

def color_to_cb(cb_type, im):
    # converts normal image to specified colorblind spectrum
    out = im.convert("RGB", cb_type, None, 0,256)
    out.show()

im = (Image.open('ishihara.jpg'))
im.show()

# Convert PNG to JPEG

program_run = True
    
while program_run == True: 
    print("Choose which type of color-blindness to simulate: \n")
    print("Protanomaly:        p")
    print("Deuteranomaly:      d")
    print("Tritanomaly:        t")
    print("Severe Tritanomaly: s")
    print("Exit:               e")

    try:
        user_input = str(input())  
    except TypeError:
        print("Not a valid input, try again!")
    
    if user_input == "p":
        cb_type = Protanomaly0_5
        color_to_cb(cb_type, im)
        
    if user_input == "d":
        cb_type = Deuteranomaly0_5
        color_to_cb(cb_type, im)
        
    if user_input == "t":
        cb_type = Tritanomaly0_5
        color_to_cb(cb_type, im)
    
    if user_input == "s":
        cb_type = Tritanomaly0_8
        color_to_cb(cb_type, im)
        
    if user_input == "e":
        print("Goodbye!")
        break
    
    try:
        convert_input = str(input("Make CB friendly? y/n"))
        if convert_input == "y":
            try: 
                shift_input = str(input("Enter the hue shift: \nBlue     b\nRed      r\nGreen    g"))
                if shift_input == "b" or "r" or "g":                    
                    mod_im = cb_compatible(im, shift_input)
                    mod_im.show()
                else:
                    print("Please enter a valid option.")
            except TypeError:
                print("Invalid input, try again!")
            try: 
                preview_input = str(input("CB Preview of modified image? y/n"))
                if preview_input == "y":
                    color_to_cb(cb_type, mod_im)
                if preview_input == "n":
                    continue
            except TypeError:
                print("Not a valid input!")
        if convert_input == "n":
            continue
    except TypeError:
        print("Not a valid input, try again!")
        
        
    try:
        again_input = str(input("Again? y/n"))
        if again_input == "y":
            program_run = True
        if again_input == "n":
            print("Goodbye!")
            program_run = False
    except TypeError:
        print("Not a valid input, try again!")