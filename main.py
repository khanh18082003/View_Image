from tkinter import *
from PIL import ImageTk, Image

root = Tk()

image1 = ImageTk.PhotoImage(Image.open("img/clbptithcm.jpg").resize((500, 500)))
image2 = ImageTk.PhotoImage(Image.open("img/map.jpg").resize((500, 500)))
image3 = ImageTk.PhotoImage(Image.open("img/newyork.jpg").resize((500, 500)))
image4 = ImageTk.PhotoImage(Image.open("img/paris.jpg").resize((500, 500)))
image5 = ImageTk.PhotoImage(Image.open("img/sanfran.jpg").resize((500, 500)))

list_image = [(image1, "CLB VOLLEYBALL PTITHCM"), (image2, "MAP"), (image3, "NEWYORK"), (image4, "PARIS"), (image5, "SANFRANSICO")]

image_label = Label(root, image=list_image[0][0])
text_Label = Label(root, text=list_image[0][1], font=("Mordern", 16))
image_label.grid(row=0, column=0, columnspan=3)
text_Label.grid(row=1, column=0, columnspan=3)

def forward(imageNumber):
    global image_label
    global text_Label
    global button_forward
    global button_backward
    image_label.grid_forget() # hidden current image
    text_Label.grid_forget() # hidden current text
    # show new image
    image_label = Label(root, image=list_image[imageNumber - 1][0])
    text_Label = Label(root, text=list_image[imageNumber - 1][1], font=("Mordern", 16))
    image_label.grid(row=0, column=0, columnspan=3)
    text_Label.grid(row=1, column=0, columnspan=3)

    if imageNumber == len(list_image):
        button_forward = Button(root, text=">>", padx=10, pady=5, state=DISABLED)
    else:
        button_forward = Button(root, text=">>", padx=10, pady=5, command=lambda: forward(imageNumber + 1))
    button_forward.grid(row=2, column=2)
    button_backward = Button(root, text="<<", padx=10, pady=5, command=lambda: backward(imageNumber - 1))
    button_backward.grid(row=2, column=0)

    

def backward(imageNumber):
    global image_label
    global text_Label
    global button_backward
    
    image_label.grid_forget()
    text_Label.grid_forget()
    image_label = Label(root, image=list_image[imageNumber - 1][0])
    text_Label = Label(root, text=list_image[imageNumber - 1][1], font=("Mordern", 16))
    image_label.grid(row=0, column=0, columnspan=3)
    text_Label.grid(row=1, column=0, columnspan=3)

    if imageNumber == 1:
        button_backward = Button(root, text="<<", padx=10, pady=5, state=DISABLED)
    else:
        button_backward = Button(root, text="<<", padx=10, pady=5, command=lambda: backward(imageNumber - 1))
    button_backward.grid(row=2, column=0)
    button_forward = Button(root, text=">>", padx=10, pady=5, command=lambda: forward(imageNumber + 1))
    button_forward.grid(row=2, column=2)
    
# init button
button_backward = Button(root, text="<<", padx=10, pady=5, state=DISABLED)
button_exit = Button(root, text="Exit", padx=10, pady=5, command=root.quit)
button_forward = Button(root, text=">>", padx=10, pady=5, command=lambda: forward(2))

# show 
button_backward.grid(row=2, column=0)
button_exit.grid(row=2, column=1)
button_forward.grid(row=2, column=2)

root.mainloop()