from turtle import *


colors1 =['white','black']
speed(0)
pensize(3)

x = -300
y = 300
penup()
goto(x,y)
pendown()

for row in range(8):
    for col in range(8):
        fillcolor(colors1[(row+col) % 2])
        begin_fill()
        for i in range(4):
            fd(60)
            rt(90)
        end_fill()
        penup()
        y =y -60
        goto(x,y)
        pendown()
    penup()
    y= 300
    x += 60
    goto(x,y)
    pendown()    
        
        
    
hideturtle()    
done()    
