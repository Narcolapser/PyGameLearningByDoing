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
		if self.y > 30 and direction < 0:
			self.rect.move_ip(0,direction)
			self.y += direction
		elif self.y < 450 and direction > 0:
			self.rect.move_ip(0,direction)
			self.y += direction

class Puck:
	def __init__(self,x,y,sx,sy):
		self.size = 5
		self.x = x
		self.y = y
		self.sx = sx
		self.sy = sy
	
	def draw(self,surface):
		white = pygame.Color(255,255,255)
		pygame.draw.circle(surface,white,(int(self.x),int(self.y)),self.size,0)
	
	def move(self):
		if self.y > 475:
			self.y = 475 - (self.y - 475)
			self.sy *= -1
		
		if self.y < 5:
			self.y = self.y + 5
			self.sy *= -1
		
		if self.x > 635:
			return 1
		
		if self.x < 5:
			return -1
		
		self.x += self.sx
		self.y += self.sy
		
		return 0
	
	def puckCollidesPaddle(self,paddle):
		if abs(self.x - paddle.x) < 5:
			if abs(self.y - paddle.y) < 55:
				self.sx *= -1.1
				self.sy += (self.y - paddle.y)/50.0
				self.x += self.sx

pygame.init()

fps = pygame.time.Clock()
pygame.key.set_repeat(5,5)

window = pygame.display.set_mode((640,480))
pygame.display.set_caption('Beep boop use w and s and up arrow and down arrow')

leftPaddle = Paddle(10,240)
rightPaddle = Paddle(630,240)
puck = Puck(320,240,2,2)
speed = 120

quit = False
while not quit:
#	events = pygame.event.get()
	pygame.event.pump()
	keys = pygame.key.get_pressed()
	window.fill((0,0,0))

	if keys[K_q]:
		quit = True
	if keys[K_s]:
		leftPaddle.move(5)
	if keys[K_w]:
		leftPaddle.move(-5)
	if keys[K_DOWN]:
		rightPaddle.move(5)
	if keys[K_UP]:
		rightPaddle.move(-5)
	
	scored = puck.move()
	if scored != 0:
		if scored == 1:
			print "Left wins."
		if scored == -1:
			print "AWH YEA RIGHT! YOU ARE AWESOME!"
		quit = True
	puck.puckCollidesPaddle(leftPaddle)
	puck.puckCollidesPaddle(rightPaddle)
	
	leftPaddle.draw(window)
	rightPaddle.draw(window)
	puck.draw(window)

	
	pygame.display.update()
	fps.tick(speed)
#	quit = snakeBitten or snakeCrashed or quit

#print "you ate:",snakeLength-3,"apples!"
#if randint(0,100)>95:
#	print "big question here: do snakes eat apples?"
