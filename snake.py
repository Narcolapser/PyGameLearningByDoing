#################################3##################################################################
#	Name:		Pygame Snake Experiement
#	Purpose:	Make a simple pygame game to get a handle on PyGame
#	Date:		2013/12/22
#	Programmer:	Toben "Littlefoo" "Narcolapser" Archer
#	Version:	0.1
####################################################################################################

import sys, pygame
from pygame.locals import *

pygame.init()

fps = pygame.time.Clock()

window = pygame.display.set_mode((640,480))
pygame.display.set_caption('SNAAAAAAAAAAAAAAAAAAAAAAKE!!!!!!!!!!!!!!')

quit = False

while not quit:
	keys = pygame.key.get_pressed()
	print keys
	print pygame.key.get_focused()
	quit = keys[113]
#	quit = True
	pygame.display.update()
	fps.tick(30)
