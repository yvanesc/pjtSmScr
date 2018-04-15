import time
import RPi.GPIO as GPIO
import pygame, sys, os
import iniPi
import sqlPi

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

clkX = 0
clkRect = 0
clkTri = 0
clkUp = 0
clkDw = 0

fontSel=pygame.font.SysFont(iniPi.font, iniPi.font_size)
#menuTxt= fontSel.render("test one", True, font_color)
menuX = "<- X"
menuTri = "<- triangle"
menuRect = "<- rectangle"
menuO = "<- Cercle"
menuUp = "vol. up ->"
menuDw = "vol. down ->"
#marge = 5
DISPLAYSURF.fill(iniPi.WHITE)
pygame.display.update()
GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)
while True:
        DISPLAYSURF.fill(iniPi.WHITE)
        #default display
        #fontSel=pygame.font.SysFont(font, font_size)
        menuTxtRect = fontSel.render(sqlPi.reqMenu("name", "rect", str(clkRect), str(clkTri), str(clkX), str(clkUp), str(clkDw)), True, iniPi.font_color)

        menuTxtX= fontSel.render(menuX, True, iniPi.font_color)
        menuTxtTri= fontSel.render(menuTri, True, iniPi.font_color)
        #menuTxtRect= fontSel.render(menuRect, True, iniPi.font_color)
        menuTxtO= fontSel.render(menuO, True, iniPi.font_color)
        menuTxtUp= fontSel.render(menuUp, True, iniPi.font_color)
        menuTxtDw= fontSel.render(menuDw, True, iniPi.font_color)
        #screen
        DISPLAYSURF.blit(menuTxtX, (iniPi.marge, 220))
        DISPLAYSURF.blit(menuTxtTri, (iniPi.marge, 150))
        DISPLAYSURF.blit(menuTxtRect, (iniPi.marge, 75))
        DISPLAYSURF.blit(menuTxtO, (iniPi.marge, 2))
	# button on right side 
	width = menuTxtUp.get_rect().width
	widthScr = DISPLAYSURF.get_rect().width
	posXup = widthScr - width -  iniPi.marge
        DISPLAYSURF.blit(menuTxtUp, (posXup, 2))
	# length end for text at 212
        DISPLAYSURF.blit(menuTxtDw, (200, 220))
        #display red rect to be calculate
        pygame.draw.rect(DISPLAYSURF, iniPi.RED, (160, 25, 150, 190))
        pygame.display.flip()

        #pygame.display.update()
        if (not GPIO.input(5)):
                # X
                clkX+=1
		# pygame.display.update()
        if (not GPIO.input(22)):
                # rect
                clkRect+=1
                #pygame.display.update()
        if (not GPIO.input(23)):
                # O
		pygame.quit()
                sys.exit()
        if (not GPIO.input(24)):
                # triangle
                clkTri+=1
                #pygame.display.update()
        if (not GPIO.input(4)):
                #VOL LOW
                clkUp+=1
                #GPIO.output(27,GPIO.HIGH)
        if (not GPIO.input(17)):
                #VOL HIGH
                clkDw+=1
                #GPIO.output(27,GPIO.LOW)
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        time.sleep(0.1)
