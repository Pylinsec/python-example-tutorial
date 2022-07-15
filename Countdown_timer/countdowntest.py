import time
import os
# hours,mins , secs = 0,0,0
def countdown(t):
    
    while t:
        if t >= 3600:
            hours, t1 = divmod(t,3600)
            print(hours)
            mins, secs = divmod(t1, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours,mins,secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
             
                 
        else:
            hours = 0
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours,mins,secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
      
            
        os.system('cls')

    print('Timer completed!')

t = input('Enter the time in seconds: ')

countdown(int(t))