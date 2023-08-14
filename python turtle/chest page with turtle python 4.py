from turtle import *


colors1 =['white','black']
speed(0)
pensize(3)

for row in range(8):
   for col in range(8):
        penup()
        goto(-300+(60 * row) ,300 -(60 * col))
        pendown()
        fillcolor(colors1[(row+col) % 2])
        begin_fill()
        for i in range(4):
            fd(60)
            rt(90)
        end_fill()
   
       
        
        
        
    
hideturtle()    
done()    
