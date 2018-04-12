#!/usr/bin/python
 
import pygame
import os
#display on TFT screen
os.environ["SDL_FBDEV"] = "/dev/fb1" 
pygame.init()
#pygame.mouse.set_visible(False) 
class GameMenu():
    def __init__(self, screen, bg_color=(0,0,0)):
 
        self.screen = screen
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
 
            # Redraw the background
            self.screen.fill(self.bg_color)
            pygame.display.flip()
 
if __name__ == "__main__":
    # Creating the screen 320x240
    screen = pygame.display.set_mode((300, 200), 0, 32)
    pygame.display.set_caption('Game Menu')
    pygame.mouse.set_visible(False)
    gm = GameMenu(screen)
    gm.run()
