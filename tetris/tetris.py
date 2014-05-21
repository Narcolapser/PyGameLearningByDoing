####################################################################################################
#	Name:		Pygame Pong Experiement
#	Purpose:	Make a simple pygame game to get a handle on PyGame
#	Date:		2014/02/26
#	Programmer:	Toben "Littlefoo" "Narcolapser" Archer
#	Version:	0.1
####################################################################################################

import sys, pygame
from pygame.locals import *
from random import randint
import math

class Paddle:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x-8,y-30,16,60)
	
	def draw(self,surface):
		white = pygame.Color(255,255,255)
		pygame.draw.rect(surface,white,self.rect,0)
	
	def move(self,direction):
		self.rect.move_ip(0,direction)

class Puck:
	def __init__(self,x,y,sx,sy):
		self.size = 5
		self.x = x
		self.y = y
		self.sx = sx
		self.sy = sy
	
	def draw(self,surface):
		white = pygame.Color(255,255,255)
		pygame.draw.circle(surface,white,(self.x,self.y),self.size,0)
	
	def move(self):
		pass

class Score:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.value = 0
	
	def draw(self):
		pass
	
	def inc(self):
		self.value += 1


pygame.init()

fps = pygame.time.Clock()
pygame.key.set_repeat(5,5)

window = pygame.display.set_mode((640,480))
pygame.display.set_caption('Beep boop use w and s and up arrow and down arrow')

leftPaddle = Paddle(10,240)
rightPaddle = Paddle(630,240)
speed = 60

quit = False
while not quit:
	events = pygame.event.get()
	window.fill((0,0,0))
	for event in events:
		if event.type == KEYDOWN:
			if event.key == K_q:
				quit = True
			if event.key == K_s:
				leftPaddle.move(5)
			if event.key == K_w:
				leftPaddle.move(-5)
			if event.key == K_DOWN:
				rightPaddle.move(5)
			if event.key == K_UP:
				rightPaddle.move(-5)
	
	leftPaddle.draw(window)
	rightPaddle.draw(window)
#	leftPaddle.move(5)
	
	pygame.display.update()
	fps.tick(speed)
#	quit = snakeBitten or snakeCrashed or quit

#print "you ate:",snakeLength-3,"apples!"
#if randint(0,100)>95:
#	print "big question here: do snakes eat apples?"
