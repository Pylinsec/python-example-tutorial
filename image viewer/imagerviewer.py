
from tkinter import *
from tkinter import ttk
from PIL import  Image , ImageTk
import os

root = Tk()
root.geometry('700x700')
lbl = Label(root, text="imageviewer")
lbl.grid(row=0,column=0,columnspan=2)


image_list = []
files = os.listdir("../Pictures/test2")
print(files)
for file in files:
    image_list.append(ImageTk.PhotoImage(Image.open(os.path.join("../Pictures/test2",file))))

def forward(num):
    global btn_for
    global btn_pre
    global lbl
    print(num)
    if num == len(image_list):
        btn_for.config(state='disabled')
    else:

        lbl.config(image=image_list[num])
        btn_for.config(state=NORMAL,command=lambda:forward(num + 1))
        btn_pre.config(state=NORMAL,command=lambda:back(num-1))
        return root.update()

    
def back(num):
    global btn_for
    global btn_pre
    global lbl
    print(num)
    
    if num == -1:    
        btn_pre.config(state='disabled')
    else:


        lbl.config(image=image_list[num])
        btn_for.config(state=NORMAL,command=lambda:forward(num + 1))
        btn_pre.config(state=NORMAL,command=lambda:back(num - 1))
        return root.update()







btn_pre = Button(root,text = 'back',state=DISABLED)
btn_pre.grid(row=1,column=0)
btn_exit = Button(root,text = 'exit program',command=root.quit)
btn_exit.grid(row=1,column=1)
btn_for = Button(root,text = 'next',command=lambda:forward(0))
btn_for.grid(row=1,column=2)




root.mainloop()