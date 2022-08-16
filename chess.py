from tkinter import *


win = Tk()
win.geometry('800x800')
win.config(bd=10)
color=["red",'blue','yellow','black','white','orange','pink','green']
# for i in range(8):
#     frame1 = Frame(win,bg=color[i])
#     frame1.pack(side=LEFT)
#     colors=['black','white']
    # for j in range(8):
    #     if i % 2 == 0:
    #         colors=['black','white']
    #         lbl=Label(frame1,bg=colors[j % 2],width=12,height=6)
    #         lbl.pack(side='bottom')
           
    #     else:
    #         colors=['white','black']
    #         lbl=Label(frame1,bg=colors[j % 2],width=12,height=6)
    #         lbl.pack(side='bottom')
frame2 = Frame(win,bd=5,borderwidth=5)       
frame2.pack()          
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            colors=['black','white']
            lbl=Label(frame2,bg=colors[j % 2],width=12,height=6)
            lbl.grid(row=i,column=j)
        if i % 2 == 1:
            colors=['white','black']
            lbl=Label(frame2,bg=colors[j % 2],width=12,height=6)
            lbl.grid(row=i,column=j)

win.mainloop()