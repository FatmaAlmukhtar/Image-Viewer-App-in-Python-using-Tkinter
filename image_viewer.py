import tkinter as tk
from PIL import ImageTk, Image

def next(img_num):
    global label
    global button_next
    global button_previous

    label.grid_forget()
    label = tk.Label(image=list[img_num-1])
    button_next = tk.Button(root, text='>>', command=lambda: next(img_num+1))
    button_previous = tk.Button(root, text='<<', command=lambda: previous(img_num-1))

    if img_num == len(list):
        button_next = tk.Button(root, text='>>', state='disabled')

    label.grid(row=0, column=0, columnspan=3)
    button_previous.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    status = tk.Label(root, text='Image ' + str(img_num) + ' of ' + str(len(list)), bd=1, relief='sunken', anchor=tk.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.EW)

def previous(img_num):
    global label
    global button_next
    global button_previous

    label.grid_forget()
    label = tk.Label(image=list[img_num-1])
    button_next = tk.Button(root, text='>>', command=lambda: next(img_num+1))
    button_previous = tk.Button(root, text='<<', command=lambda: previous(img_num-1))

    if img_num == 1:
        button_previous = tk.Button(root, text='<<', state='disabled')

    label.grid(row=0, column=0, columnspan=3)
    button_previous.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    status = tk.Label(root, text='Image ' + str(img_num) + ' of ' + str(len(list)), bd=1, relief='sunken', anchor=tk.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.EW)

root = tk.Tk()
root.title('Image Viewer')
root.resizable(0, 0)

img1 = ImageTk.PhotoImage(Image.open('/Users/fatmaalmukhtar/Desktop/red-blue.png'))
img2 = ImageTk.PhotoImage(Image.open('/Users/fatmaalmukhtar/Desktop/orange-green.png'))
img3 = ImageTk.PhotoImage(Image.open('/Users/fatmaalmukhtar/Desktop/yellow-black.png'))

list = [img1, img2, img3]

status = tk.Label(root, text='Image 1 of ' + str(len(list)), bd=1, relief='sunken', anchor=tk.E)

label = tk.Label(image=img1)
label.grid(row=0, column=0, columnspan=3)

button_previous = tk.Button(root, text='<<', command=previous, state='disabled')
button_next = tk.Button(root, text='>>', command=lambda: next(2))
button_exit = tk.Button(root, text='Exit Program', command=root.quit)

button_previous.grid(row=1, column=0)
button_next.grid(row=1, column=2, pady=10)
button_exit.grid(row=1, column=1)
status.grid(row=2, column=0, columnspan=3, sticky=tk.EW)

root.mainloop()
