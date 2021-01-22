from __future__ import division
from threading import Thread
import RPi.GPIO as GPIO
import time
import os
import drivers
import Ultrasonict 
import FaceCV 

display = drivers.Lcd()
command = "python FaceCV.py"
os.system(command)

print "Start ", FaceCV.distance 

Ultrasonict.Arm()
Ultrasonict.Camera()

display.lcd_display_string("Hello World!", 1)  
display.lcd_display_string("This is project", 2)  
print("Hello World!")
print("This is project")
time.sleep(1)                                           
#display.lcd_clear
command = "aplay Sound_EndDetect.wav"
os.system(command)






#print("run file Ultrasonict.py")
# command = "python Ultrasonict.py" #command run demo_lcd.py for show message LCD
# os.system(command)

    
