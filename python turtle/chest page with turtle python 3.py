from turtle import *


colors1 =['white','black']
speed(0)
pensize(3)

for row in range(1,9):
    penup()
    goto(-300 ,300 -(60 * row))
    a = 300 -(60 * row)
    pendown()
    for col in range(1,9):
        fillcolor(colors1[(row+col) % 2])
        begin_fill()
        for i in range(4):
            fd(60)
            rt(90)
        end_fill()
#         fd(60)
        penup()
        goto(-300 + (col * 60) ,a)
        pendown()
       
        
        
        
    
hideturtle()    
done()    
