import tkinter as tk
import numpy as np
from tkinter import filedialog
from PIL import Image, ImageTk
from valuechange import cb_compatible
import os

#show the variations with the severities of color blindness
def color_to_cb(c_type,filename):
    a = 1
    #conversion matrices in RGB
    Neutral = (1, 0,0 , 0, 0, 1, 0, 0, 0, 0, 1, 0)
    Deuteranomaly0_5 = (0.547494, 0.607765, -0.155259, 0, 0.181692, 0.781742, 0.036566, 0, -0.010410, 0.027275, 0.983136, 0)
    Deuteranomaly1 = (.367322, .860646, -.227968 , 0, .280085, .672501, .047413, 0, -.01182, .04294, .968881, 0)
    Protanomaly0_5 = (0.458064, 0.679578, -0.137642, 0, 0.092785, 0.846313, 0.060902, 0, -0.007494, -0.016807, 1.024301, 0)
    Protanomaly1 = (.152286, 1.052583, -.204868 , 0, .114503, .786281, .099216, 0, -.003882, -.048116, 1.051998, 0)
    Tritanomaly0_5 = (1.017277, 0.027029, -0.044306, 0, -0.006113, 0.958479, 0.047634, 0, 0.006379, 0.248708, 0.744913, 0)
    Tritanomaly1 = (1.255528, -0.076749, -0.178779, 0, -0.078411, 0.930809, 0.147602, 0, 0.004733, 0.691367, 0.303900, 0)
    im = (Image.open(filename))
    #if statements for the type, create 3 images to preview
    if(c_type == "Deuteranomaly"):
        out = im.convert("RGB", Neutral, None, 0,256)
        out = out.save(str(a) + '.jpg')
        out = im.convert("RGB", Deuteranomaly0_5, None, 0,256)
        a += 1
        out = out.save(str(a) + '.jpg')
        out = im.convert("RGB", Deuteranomaly1, None, 0,256)
        a += 1
        out = out.save(str(a) + '.jpg')
    if(c_type == "Protanomaly"):
        out = im.convert("RGB", Neutral, None, 0,256)
        out = out.save(str(a) + '.jpg')
        out = im.convert("RGB", Protanomaly0_5, None, 0,256)
        a += 1
        out = out.save(str(a) + '.jpg')
        out = im.convert("RGB", Protanomaly1, None, 0,256)
        a += 1
        out = out.save(str(a) + '.jpg')
    if(c_type == "Tritanomaly"):
        out = im.convert("RGB", Neutral, None, 0,256)
        out = out.save(str(a) + '.jpg')
        out = im.convert("RGB", Tritanomaly0_5, None, 0,256)
        a += 1
        out = out.save(str(a) + '.jpg')
        out = im.convert("RGB", Tritanomaly1, None, 0,256)
        a += 1
        out = out.save(str(a) + '.jpg')

#called by inclusive modification button in interface, takes the hue shifted picture and converts with color matrix
def finalConversion(imgaging, c_type):
    Deuteranomaly0_5 = (0.547494, 0.607765, -0.155259, 0, 0.181692, 0.781742, 0.036566, 0, -0.010410, 0.027275, 0.983136, 0)
    Protanomaly0_5 = (0.458064, 0.679578, -0.137642, 0, 0.092785, 0.846313, 0.060902, 0, -0.007494, -0.016807, 1.024301, 0)
    Tritanomaly0_5 = (1.017277, 0.027029, -0.044306, 0, -0.006113, 0.958479, 0.047634, 0, 0.006379, 0.248708, 0.744913, 0)
    
    if c_type == "Deuteranomaly": 
        out = imgaging.convert("RGB", Deuteranomaly0_5, None, 0,256)
        out = out.save('inclusive.jpg')
    
    if c_type == "Protanomaly": 
        out = imgaging.convert("RGB", Protanomaly0_5, None, 0,256)
        out = out.save('inclusive.jpg')

    if c_type == "Tritanomaly": 
        out = imgaging.convert("RGB", Tritanomaly0_5, None, 0,256)
        out = out.save('inclusive.jpg')
    #gets rid of the preview pictures and exits
    os.remove("1.jpg")
    os.remove("2.jpg")
    os.remove("3.jpg")
    window.destroy()
    
    

#open directory
def browseFiles():
    
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          )
      
    # Change label contents
    # label_file_explorer.configure(text="File Opened: "+filename)

    #buttons to call for what type of color blindness
    buttonDeut = tk.Button(window, text="Deuteranomaly",command=lambda: open("Deuteranomaly", filename))
    
    buttonProt = tk.Button(window, text="Protanomaly",command=lambda: open("Protanomaly",filename))
   
    buttonTrit = tk.Button(window, text="Tritanomaly",command=lambda: open("Tritanomaly",filename))
    buttonDeut.place( x = 220 , y =300, height = 50, width = 200)
    buttonProt.place(x = 430 , y =300, height = 50, width = 200)
    buttonTrit.place(x = 640 , y =300, height = 50, width = 200)
    

#preview window of the variations of intensity
def open(c_type,filename):
    global my_label
    global img
    img = ImageTk.PhotoImage(Image.open(filename))
    # width, height = (Image.open(filename)).size
    top = tk.Toplevel()
    top.title('output')
    # top.geometry("%ix%i" % (width, height))
    # heading = tk.Label(top, text= " pics")
    # heading.grid(row = 0, column =0)
    
    my_label = tk.Label(top, image=img)
    my_label.grid(row=0,column =0, columnspan = 1)
    color_to_cb(c_type,filename)
    img1 = ImageTk.PhotoImage(Image.open('1.jpg'))
    img2 = ImageTk.PhotoImage(Image.open('2.jpg'))
    img3 = ImageTk.PhotoImage(Image.open('3.jpg'))

    image_list = [img1,img2,img3]
  
    #give functionallity to forwards button
    def forward(num):
        global my_label
        global button_forward
        global button_back
        
        my_label.grid_forget()
        my_label = tk.Label(image=image_list[num-1])
        button_forward = tk.Button(top, text=">>", command = lambda: forward(num+1))
        button_back = tk.Button(top, text="<<", command=lambda: back(num - 1))
        heading = tk.Label(top, text= c_type + str((num - 1) * 0.5))
        heading.grid(row = 0, column =0)
        if num == 3: 
            button_forward = tk.Button(top, text=">>", state="disabled")

        my_label.grid(row=0,column =0, columnspan=3)
        button_back.grid(row = 1, column = 0)
        button_forward.grid(row = 1, column = 2)
    
    #functionallity for back button
    def back(num):
        global my_label
        global button_forward
        global button_back
        my_label.grid_forget()
        my_label = tk.Label(image=image_list[num-1])
        button_forward = tk.Button(top, text=">>", command = lambda: forward(num+1))
        button_back = tk.Button(top, text="<<", command=lambda: back(num - 1))
        heading = tk.Label(top, text= c_type + str((num - 1) * 0.5))
        heading.grid(row = 0, column =0)
        if num == 1: 
            button_back = tk.Button(top, text="<<", state="disabled")

        my_label.grid(row=0,column =0, columnspan=3)
        button_back.grid(row = 1, column = 0)
        button_forward.grid(row = 1, column = 2)
    #calls cb_compatible function from valuechange.py. has algorithm for the conversion after previews, will be the hue shifted pics
    def call_cb_compatible(color):
        global im
        global show
        global converted_img
        im = Image.open(filename)
        show = cb_compatible(im, color)
        #save the hue shifted picture just in case
        show.save("color_adjusted.jpg")
        converted_img = ImageTk.PhotoImage(show)
        top2 = tk.Toplevel()
        top2.title('Converted:' + color)
        this_label = tk.Label(top2, image=converted_img)
        this_label.grid()
        button_save = tk.Button(top2, text="inclusive modification", command= lambda: finalConversion(show, c_type))
        button_nope = tk.Button(top2, text="no", command = lambda : top2.destroy())
        button_save.grid()
        button_nope.grid()

    button_back = tk.Button(top, text = "<<", command = back, state = "disabled")
    button_out = tk.Button(top, text = "exit", command = top.quit)
    button_convert_red = tk.Button(top, text="Hue Shift Red", command=lambda:call_cb_compatible("r"))
    button_convert_blue = tk.Button(top, text="Hue Shift Blue", command=lambda:call_cb_compatible("b"))
    button_convert_green = tk.Button(top, text="Hue Shift Green", command=lambda:call_cb_compatible("g"))
    button_forward = tk.Button(top, text = ">>", command = lambda: forward(2))

    button_back.grid(row = 1, column = 0)
    button_convert_red.grid(row = 2, column =1)
    button_convert_blue.grid(row = 2, column =2)
    button_convert_green.grid(row = 2, column =3)
    button_out.grid(row = 1, column = 1)
    button_forward.grid(row = 1, column = 2)


                                                                                    
# Create the root window
window = tk.Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("1024x1024")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = tk.Label(window,
    text = "File Explorer using Tkinter",
    width = 120, height = 4)

      
button_explore = tk.Button(window,
                        text = "Browse Files",width = 20,
                        command = browseFiles)
  
button_exit = tk.Button(window,
                     text = "Exit",
                     command = exit)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)
  

# Let the window wait for any events
window.mainloop()
