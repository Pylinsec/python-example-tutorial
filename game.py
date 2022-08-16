import re
from tkinter import *
import random
from itertools import product



win = Tk()
frame = Frame(win)
frame.pack()
# for i in range(1,9):
#     if i < 4 :
#         btn+str{i}=Button(frame,text=str(i),activebackground='lightgreen',font=5,bg='green',height=5,width=10).grid( row=1,column=i)
#     elif i < 7 :
#         Button(frame,text=str(i),activebackground='lightgreen',font=5,bg='green',height=5,width=10).grid( row=2,column=i-3)
#     else :
#         Button(frame,text=str(i),activebackground='lightgreen',font=5,bg='green',height=5,width=10).grid( row=3,column=i-6)

list_num=[3,1,2]
random.shuffle(list_num)
list1 = list(product(list_num,repeat=2))

#create btns 
free_btn = Button(frame,text="",activebackground='lightgreen',font=5,height=5,width=10)
free_btn.grid( row = list1[0][0],column=list1[0][1])
btn1 = Button(frame,text="1",activebackground='lightgreen',font=5,bg='green',height=5,width=10)
btn1.grid( row = list1[1][0],column=list1[1][1])
btn2 = Button(frame,text="2",activebackground='lightgreen',font=5,bg='green',height=5,width=10)
btn2.grid(row = list1[2][0],column=list1[2][1])
btn3 = Button(frame,text="3",activebackground='lightgreen',font=5,bg='green',height=5,width=10)
btn3.grid(row = list1[3][0],column=list1[3][1])
btn4 = Button(frame,text="4",activebackground='lightgreen',font=5,bg='green',height=5,width=10)
btn4.grid( row = list1[4][0],column=list1[4][1])
btn5 = Button(frame,text="5",activebackground='lightgreen',font=5,bg='green',height=5,width=10)
btn5.grid( row = list1[5][0],column=list1[5][1])
btn6 = Button(frame,text="6",activebackground='lightgreen',font=5,bg='green',height=5,width=10)
btn6.grid( row = list1[6][0],column=list1[6][1])
btn7 = Button(frame,text="7",activebackground='lightgreen',font=5,bg='green',height=5,width=10)
btn7.grid(row = list1[7][0],column=list1[7][1])
btn8 = Button(frame,text="8",activebackground='lightgreen',font=5,bg='green',height=5,width=10)
btn8.grid( row = list1[8][0],column=list1[8][1])



# check btn1
def swap1(): 
   if free_btn.grid_info()['row'] == btn1.grid_info()['row'] and  abs(free_btn.grid_info()['column'] - btn1.grid_info()['column']) == 1:
        s = free_btn.grid_info()['column']
        free_btn.grid(column=btn1.grid_info()['column'])
        btn1.grid(column=s)
        win.update()
        
   elif free_btn.grid_info()['column'] == btn1.grid_info()['column'] and  abs(free_btn.grid_info()['row'] - btn1.grid_info()['row'] )== 1:
        s = free_btn.grid_info()['row']
        free_btn.grid(row=btn1.grid_info()['row'])
        btn1.grid(row=s)
        win.update()

 # check btn2        
def swap2():
      
   if free_btn.grid_info()['row'] == btn2.grid_info()['row'] and abs(free_btn.grid_info()['column'] - btn2.grid_info()['column']) == 1:
        s = free_btn.grid_info()['column']
        free_btn.grid(column=btn2.grid_info()['column'])
        btn2.grid(column=s)
        
        
   elif free_btn.grid_info()['column'] == btn2.grid_info()['column'] and abs(free_btn.grid_info()['row'] - btn2.grid_info()['row']) == 1:
        s = free_btn.grid_info()['row']
        free_btn.grid(row=btn2.grid_info()['row'])
        btn2.grid(row=s)


        
 # check btn3
def swap3():
  
   if free_btn.grid_info()['row'] == btn3.grid_info()['row'] and abs(free_btn.grid_info()['column'] - btn3.grid_info()['column']) == 1:
        s = free_btn.grid_info()['column']
        free_btn.grid(column=btn3.grid_info()['column'])
        btn3.grid(column=s)          
   elif free_btn.grid_info()['column'] == btn3.grid_info()['column'] and abs(free_btn.grid_info()['row'] - btn3.grid_info()['row']) == 1:
        s = free_btn.grid_info()['row']
        free_btn.grid(row=btn3.grid_info()['row'])
        btn3.grid(row=s)

        
 # check btn4        
def swap4(): 
   if free_btn.grid_info()['row'] == btn4.grid_info()['row'] and abs(free_btn.grid_info()['column'] - btn4.grid_info()['column']) == 1:
        s = free_btn.grid_info()['column']
        free_btn.grid(column=btn4.grid_info()['column'])
        btn4.grid(column=s)          
   elif free_btn.grid_info()['column'] == btn4.grid_info()['column'] and abs(free_btn.grid_info()['row'] - btn4.grid_info()['row']) == 1:
        s = free_btn.grid_info()['row']
        free_btn.grid(row=btn4.grid_info()['row'])
        btn4.grid(row=s)


        
 # check btn5        
def swap5(): 
   if free_btn.grid_info()['row'] == btn5.grid_info()['row'] and abs(free_btn.grid_info()['column'] - btn5.grid_info()['column']) == 1:
        s = free_btn.grid_info()['column']
        free_btn.grid(column=btn5.grid_info()['column'])
        btn5.grid(column=s)          
   elif free_btn.grid_info()['column'] == btn5.grid_info()['column'] and abs(free_btn.grid_info()['row'] - btn5.grid_info()['row']) == 1:
        s = free_btn.grid_info()['row']
        free_btn.grid(row=btn5.grid_info()['row'])
        btn5.grid(row=s)

 # check btn6        
def swap6(): 
   if free_btn.grid_info()['row'] == btn6.grid_info()['row'] and abs(free_btn.grid_info()['column'] - btn6.grid_info()['column']) == 1:
        s = free_btn.grid_info()['column']
        free_btn.grid(column=btn6.grid_info()['column'])
        btn6.grid(column=s)          
   elif free_btn.grid_info()['column'] == btn6.grid_info()['column'] and abs(free_btn.grid_info()['row'] - btn6.grid_info()['row']) == 1:
        s = free_btn.grid_info()['row']
        free_btn.grid(row=btn6.grid_info()['row'])
        btn6.grid(row=s)

 # check btn7        
def swap7(): 
   if free_btn.grid_info()['row'] == btn7.grid_info()['row'] and abs(free_btn.grid_info()['column'] - btn7.grid_info()['column']) == 1:
        s = free_btn.grid_info()['column']
        free_btn.grid(column=btn7.grid_info()['column'])
        btn7.grid(column=s)          
   elif free_btn.grid_info()['column'] == btn7.grid_info()['column'] and abs(free_btn.grid_info()['row'] - btn7.grid_info()['row']) == 1:
        s = free_btn.grid_info()['row']
        free_btn.grid(row=btn7.grid_info()['row'])
        btn7.grid(row=s)

 # check btn8        
def swap8(): 
   if free_btn.grid_info()['row'] == btn8.grid_info()['row'] and abs(free_btn.grid_info()['column'] - btn8.grid_info()['column']) == 1:
        s = free_btn.grid_info()['column']
        free_btn.grid(column=btn8.grid_info()['column'])
        btn8.grid(column=s)          
   elif free_btn.grid_info()['column'] == btn8.grid_info()['column'] and abs(free_btn.grid_info()['row'] - btn8.grid_info()['row']) == 1:
        s = free_btn.grid_info()['row']
        free_btn.grid(row=btn8.grid_info()['row'])
        btn8.grid(row=s)


        
        
btn1.config(command=swap1)
btn2.config(command=swap2)
btn3.config(command=swap3)
btn4.config(command=swap4)
btn5.config(command=swap5)
btn6.config(command=swap6)
btn7.config(command=swap7)
btn8.config(command=swap8)

win.mainloop()