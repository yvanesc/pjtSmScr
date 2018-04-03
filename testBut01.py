#UPDATE Program test_1.py  and save as test_1_1.py
#1.	at the beginning set the backlight on and add a text to the screen
#2.	cleanup the CPIO  at the end
import time
import RPi.GPIO as GPIO
import pygame, sys, os

from pygame.locals import *
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
DISPLAYSURF = pygame.display.set_mode((320, 240))
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.OUT) 
 
# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#UPDATE Program test_1.py *******************************
DISPLAYSURF.fill(WHITE)									#
pygame.display.update()									#
#add a text to the screen.								#
myfont = pygame.font.SysFont("Consolas", 30)			#
label1 = myfont.render("Python Program",1,RED)			#
label2 = myfont.render("how to use",1,GREEN)			#
label3 = myfont.render("PiTFT + Button",1,BLACK)		#
														#
DISPLAYSURF.blit(label1, (80, 70))						#
DISPLAYSURF.blit(label2, (80, 100))						#
DISPLAYSURF.blit(label3, (80, 130))						#
pygame.display.flip()									#
#backlight on											#
GPIO.output(27, GPIO.HIGH)								#
#******************************************************** 
try: 
    while True:
		DISPLAYSURF.fill(WHITE)		
		if (not GPIO.input(5)):
				print "5  " + "X"
				pygame.draw.line(DISPLAYSURF, BLUE, (10, 200), (50, 240), 10)
				pygame.draw.line(DISPLAYSURF, BLUE, (50, 200), (10, 240), 10)
				pygame.display.update()

        if (not GPIO.input(22)):
                print "22 " + u"\u25A1"
                pygame.draw.rect(DISPLAYSURF, RED, (10, 70, 40, 40))
                pygame.display.update()
        if (not GPIO.input(23)):
                print "23 " + "O"
                pygame.draw.circle(DISPLAYSURF, BLACK, (30, 30), 20, 0)
                pygame.display.update()
        if (not GPIO.input(24)):
                print "24 " + u"\u1403"
                pygame.draw.polygon(DISPLAYSURF, GREEN, [[30, 140], [10, 180], [50, 180]], 10)
                pygame.display.update()
    	if (not GPIO.input(4)):
                print "4 " + u"\u140D"
                GPIO.output(27,GPIO.HIGH)
		if (not GPIO.input(17)):
                print "24 " + u"\u140E"
				GPIO.output(27,GPIO.LOW)
                
		for event in pygame.event.get():
				if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

    	time.sleep(0.1)

finally: GPIO.cleanup()
