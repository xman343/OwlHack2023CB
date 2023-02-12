import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def convert(filename):
    a = 1
    Deuteranomaly0_5 = (0.547494, 0.607765, -0.155259, 0, 0.181692, 0.781742, 0.036566, 0, -0.010410, 0.027275, 0.983136, 0)
    Deuteranomaly0 = (1, 0,0 , 0, 0, 1, 0, 0, 0, 0, 1, 0)
    Deuteranomaly1 = (.367322, .860646, -.227968 , 0, .280085, .672501, .047413, 0, -.01182, .04294, .968881, 0)
    im = (Image.open('pencils.jpg'))
    out = im.convert("RGB", Deuteranomaly0, None, 0,256)
    out = out.save(str(a) + '.jpg')
    out = im.convert("RGB", Deuteranomaly0_5, None, 0,256)
    a += 1
    out = out.save(str(a) + '.jpg')
    out = im.convert("RGB", Deuteranomaly1, None, 0,256)
    a += 1
    out = out.save(str(a) + '.jpg')

def browseFiles():
    
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          )
      
    # Change label contents
    # label_file_explorer.configure(text="File Opened: "+filename)
    open(filename)


def open(filename):
    global my_label
    global img
    top = tk.Toplevel()
    top.title('output')
    # heading = tk.Label(top, text= " pics")
    # heading.grid(row = 0, column =0)
    img = ImageTk.PhotoImage(Image.open(filename))
    my_label = tk.Label(top, image=img)
    my_label.grid(row=0,column =0, columnspan=3)
    convert(filename)
    img1 = ImageTk.PhotoImage(Image.open('1.jpg'))
    img2 = ImageTk.PhotoImage(Image.open('2.jpg'))
    img3 = ImageTk.PhotoImage(Image.open('3.jpg'))

    image_list = [img1,img2,img3]
  

    def forward(num):
        global my_label
        global button_forward
        global button_back
        
        my_label.grid_forget()
        my_label = tk.Label(image=image_list[num-1])
        button_forward = tk.Button(top, text=">>", command = lambda: forward(num+1))
        button_back = tk.Button(top, text="<<", command=lambda: back(num - 1))
        heading = tk.Label(top, text= "Deutoronamaly: " + str((num - 1) * 0.5))
        heading.grid(row = 0, column =0)
        if num == 3: 
            button_forward = tk.Button(top, text=">>", state="disabled")

        my_label.grid(row=0,column =0, columnspan=3)
        button_back.grid(row = 1, column = 0)
        button_forward.grid(row = 1, column = 2)
        
    def back(num):
        global my_label
        global button_forward
        global button_back
        my_label.grid_forget()
        my_label = tk.Label(image=image_list[num-1])
        button_forward = tk.Button(top, text=">>", command = lambda: forward(num+1))
        button_back = tk.Button(top, text="<<", command=lambda: back(num - 1))
        heading = tk.Label(top, text= "Deutoronamaly: " + str((num - 1) * 0.5))
        heading.grid(row = 0, column =0)
        if num == 1: 
            button_back = tk.Button(top, text="<<", state="disabled")

        my_label.grid(row=0,column =0, columnspan=3)
        button_back.grid(row = 1, column = 0)
        button_forward.grid(row = 1, column = 2)

    button_back = tk.Button(top, text = "<<", command = back, state = "disabled")
    button_out = tk.Button(top, text = "exit", command = top.quit)
    button_forward = tk.Button(top, text = ">>", command = lambda: forward(2))

    button_back.grid(row = 1, column = 0)
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
