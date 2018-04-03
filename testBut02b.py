#UPDATE Program test_1.py  and save as test_1_1.py
#1.	at the beginning set the backlight on and add a text to the screen
#2.	cleanup the CPIO  at the end
import time
import RPi.GPIO as GPIO
import sys, os
#import pygame, sys, os

#from pygame.locals import *os.putenv('SDL_FBDEV', '/dev/fb1')
#pygame.init()
#pygame.mouse.set_visible(False)
#DISPLAYSURF = pygame.display.set_mode((320, 240))
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.OUT) 
 

#backlight on											#
#GPIO.output(27, GPIO.HIGH)								#
#******************************************************** 
try: 
	while True:
		#DISPLAYSURF.fill(WHITE)		
		if (not GPIO.input(5)):
			print "5  "
        	if (not GPIO.input(22)):
                	print "22 "
        	if (not GPIO.input(23)):
                	print "23 "
        	if (not GPIO.input(24)):
                	print "24 "
    		if (not GPIO.input(4)):
                	print "4 "
		if (not GPIO.input(17)):
                	print "24 "
                
		#for event in pygame.event.get():
				#if event.type == QUIT:
                        #pygame.quit()
                        #sys.exit()
	time.sleep(0.1)

finally: GPIO.cleanup()
