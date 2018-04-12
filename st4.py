#!/usr/bin/python
 
import pygame
import os

#display on TFT screen
os.environ["SDL_FBDEV"] = "/dev/fb1" 

pygame.init()

class GameMenu():
    def __init__(self, screen, items, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
 
        self.items = []
        for index, item in enumerate(items):
            #item = item + str(self.scr_width)
            label = self.font.render(item, 1, font_color)

            #size text
            width = label.get_rect().width
            height = label.get_rect().height
            
	    #if index == 0:
                #posx = 0
            posx = (self.scr_width / 2) - (width / 2)
            #print(posx)
            #label = label + posx
            # t_h: total height of text block
            t_h = len(items) * height
            #if index == 0:
            #posy = 0
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height) #/ 2) - (t_h / 2) + (index * height)
                
            self.items.append([item, label, (width, height), (posx, posy)])
 
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
 
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
 
            pygame.display.flip()
 
if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((320, 240), 0, 32)
    pygame.mouse.set_visible(False) 

    menu_items = ('<- Shutdown',' ','Vol Up ->',' ','<- Rectangle',' ','<- Triangle',' ','<- Croix    Vol Down-> ')#, 'Others', "will see")
 
    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, menu_items)
    gm.run()
