import RPi.GPIO as GPIO
import pygame, sys, os

from pygame.locals import *
#os.putenv('SDL_FBDEV', '/dev/fb1')
os.environ["SDL_FBDEV"] = "/dev/fb1"
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

while True:
        DISPLAYSURF.fill(WHITE)
        if (not GPIO.input(5)):
                # croix pos ??
                pygame.draw.line(DISPLAYSURF, BLUE, (10, 200), (50, 240), 10)
                pygame.draw.line(DISPLAYSURF, BLUE, (50, 200), (10, 240), 10)
                pygame.display.update()
        if (not GPIO.input(22)):
                # rect pos. 40
                pygame.draw.line(DISPLAYSURF, BLUE, (130, 200), (170, 240), 10)
                pygame.draw.line(DISPLAYSURF, BLUE, (170, 200), (130, 240), 10)
                pygame.display.update()
        #if (not GPIO.input(23)):
                # cercle pos. 20
                # shutdown
                # pygame.display.update()
        if (not GPIO.input(24)):
                # triangle pos. ??
                pygame.draw.line(DISPLAYSURF, BLUE, (70, 200), (70, 240), 10)
                pygame.draw.line(DISPLAYSURF, BLUE, (110, 200), (110, 240), 10)
                pygame.display.update()
        if (not GPIO.input(4)):
                # vol high
                GPIO.output(27,GPIO.HIGH)
                pygame.draw.line(DISPLAYSURF, BLUE, (70, 200), (70, 240), 10)
                pygame.draw.line(DISPLAYSURF, BLUE, (110, 200), (110, 240), 10)
                pygame.display.update()
        if (not GPIO.input(17)):
                # vol low
                GPIO.output(27,GPIO.LOW)
                pygame.draw.line(DISPLAYSURF, BLUE, (10, 10), (50, 50), 10)
                pygame.draw.line(DISPLAYSURF, BLUE, (50, 10), (10, 50), 10)
                pygame.display.update()
        for event in pygame.event.get():
                 if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        time.sleep(0.1)
