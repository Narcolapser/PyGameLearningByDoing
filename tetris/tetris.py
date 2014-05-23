####################################################################################################
#	Name:		Pygame Tetris
#	Purpose:	Make a simple pygame game to get a handle on PyGame
#	Date:		2014/05/23
#	Programmer:	Toben "Littlefoot" "Narcolapser" Archer
#	Version:	0.1
####################################################################################################

import sys, pygame
from pygame.locals import *
from random import randint
import math

#local imports
from game import *

game = Game()
con = True
while con:
	con = game.update()

#~To the King~#
