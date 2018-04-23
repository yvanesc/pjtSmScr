import pygame
pygame.init()
picture=pygame.image.load("/home/pi/Pictures/coplandOS.jpg")
pygame.display.set_mode(picture.get_size())
main_surface = pygame.display.get_surface()
main_surface.blit(picture, (0,0))
while True:
   main_surface.blit(picture, (0,0))
   pygame.display.update()