import time
import RPi.GPIO as GPIO
import pygame, sys, os

from pygame.locals import *
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
#pygame.mouse.set_visible(False)
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

# ini font
font_color=(0, 0, 0)
font=None
font_size=30

fontSel=pygame.font.SysFont(font, font_size)
#menuTxt= fontSel.render("test one", True, font_color)
menuX = "<- X"
menuTri = "<- triangle"
menuRect = "<- rectangle"
menuO = "<- Cercle"
menuUp = "vol. up ->"
menuDw = "vol. down ->"
marge = 5
DISPLAYSURF.fill(WHITE)
pygame.display.update()
GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)
while True:
        DISPLAYSURF.fill(WHITE)
        #default display
        #fontSel=pygame.font.SysFont(font, font_size)
        menuTxtX= fontSel.render(menuX, True, font_color)
        menuTxtTri= fontSel.render(menuTri, True, font_color)
        menuTxtRect= fontSel.render(menuRect, True, font_color)
        menuTxtO= fontSel.render(menuO, True, font_color)
        menuTxtUp= fontSel.render(menuUp, True, font_color)
        menuTxtDw= fontSel.render(menuDw, True, font_color)
        #screen
        DISPLAYSURF.blit(menuTxtX, (marge, 220))
        DISPLAYSURF.blit(menuTxtTri, (marge, 150))
        DISPLAYSURF.blit(menuTxtRect, (marge, 75))
        DISPLAYSURF.blit(menuTxtO, (marge, 2))
	# button on right side 
	width = menuTxtUp.get_rect().width
	widthScr = DISPLAYSURF.get_rect().width
	posXup = widthScr - width -  marge
        DISPLAYSURF.blit(menuTxtUp, (posXup, 2))
	# length end for text at 212
        DISPLAYSURF.blit(menuTxtDw, (200, 220))
        pygame.display.flip()
        print "pass"
        #pygame.display.update()
        if (not GPIO.input(5)):
                #print "5" + "X"
                pygame.draw.line(DISPLAYSURF, BLUE, (10, 200), (50, 240), 10)
                pygame.draw.line(DISPLAYSURF, BLUE, (50, 200), (10, 240), 10)
		pygame.display.update()
        if (not GPIO.input(22)):
                #print "22 " + "rect"#+ u"\u25A1"
                pygame.draw.rect(DISPLAYSURF, RED, (10, 70, 40, 40))
                pygame.display.update()
        if (not GPIO.input(23)):
                #print "cercle"#"23 " + "O"
                pygame.draw.circle(DISPLAYSURF, BLUE, (30, 30), 20, 0)
                pygame.display.update()
		pygame.quit()
                sys.exit()
        if (not GPIO.input(24)):
                #print "24 " + "triangle" #u"\u1403"
                pygame.draw.polygon(DISPLAYSURF, BLACK, [[30, 140], [10, 180], [50, 180]], 10)
                pygame.display.update()
        if (not GPIO.input(4)):
                #VOL LOW
                #print "4 " +"vol high"#+ u"\u140D"
                GPIO.output(27,GPIO.HIGH)
        if (not GPIO.input(17)):
                #VOL HIGH
                print "24 " + "vol low"#u"\u140E"
                GPIO.output(27,GPIO.LOW)
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        time.sleep(0.1)
