# st5.py
# start apply
# button + display
import time
import RPi.GPIO as GPIO
import pygame
import sys
import os
import st4
#import clockPi

from pygame.locals import *
os.putenv('SDL_FBDEV', '/dev/fb1')
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.OUT) 
rectBut=0
triBut=0
xBut=0
while True:
    if (not GPIO.input(5)):
        print "5" + "X"
        xBut+=1
    if (not GPIO.input(22)):
        print "22 "+"rect" #+ u"\u25A1"
        rectBut+=1
    if (not GPIO.input(23)):
        #shutdown
        print "cercle"#"23 " + "O"
    if (not GPIO.input(24)):
        print "24 " + "triangle" #u"\u1403"
        triBut+=1
    if (not GPIO.input(4)):
        print "4 " +"vol high"#+ u"\u140D"
        GPIO.output(27,GPIO.HIGH)
    if (not GPIO.input(17)):
        print "24 " + "vol low"#u"\u140E"
        GPIO.output(27,GPIO.LOW)
    #run clockPi
    if (xBut == 0 and rectBut == 0 and triBut == 0):
        print "clockPi"
        __name__="__main__"
        st4.__name__
    else:
        print "menuPi"
    
    time.sleep(0.1)

