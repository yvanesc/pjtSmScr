import pygame
import os

os.environ["SDL_FBDEV"] = "/dev/fb1"
pygame.init()
screen = pygame.display.set_mode((200, 200))
done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30,60,60))
	pygame.display.flip()
