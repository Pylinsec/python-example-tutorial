from turtle import *
speed(0)
penup()
goto(-300,300)
pendown()
colors = ['white','black']
for k in range(1,9):
    for j in range(8):
        sum=(k+j)%2
        fillcolor(colors[(k+j)%2])
        begin_fill()
        for i in range(4):
            fd(60)
            lt(90)
        end_fill()    
        fd(60) 
    penup()
    goto(-300,300-(k*60)) 
    pendown()      
done()