#################################3##################################################################
#	Name:		Pygame Snake Experiement
#	Purpose:	Make a simple pygame game to get a handle on PyGame
#	Date:		2013/12/22
#	Programmer:	Toben "Littlefoo" "Narcolapser" Archer
#	Version:	0.1
####################################################################################################

import sys, pygame
from pygame.locals import *
from random import randint
import math

def drawApple():
	red = pygame.Color(255,0,0)
	green = pygame.Color(0,255,0)
	pygame.draw.circle(window,red,apple,5,0)

def newApple():
	x = randint(5,635)
	y = randint(5,475)
	while abs(snakeBody[0][0]-x)<20:
		x = randint(1,63)
		x *= 10
		x += 5
	while abs(snakeBody[0][1]-y)<20:
		y = randint(1,47)
		y *= 10
		y += 5
	return (x,y)

def drawSnake():
	green = pygame.Color(0,255,0)
	for section in snakeBody:
		pygame.draw.circle(window,green,section,5,0)

def moveSnake(snakeBody):
	head = snakeBody[0]
	new = (head[0]+10*direction[0],head[1]+10*direction[1])
	snakeBody = [new] + snakeBody
	while len(snakeBody) > snakeLength:
		snakeBody.pop()
	return snakeBody

def snakeCollidesApple(snakeBody,apple):
	collide = False
	for s in snakeBody:
		x = s[0] - apple[0]
		y = s[1] - apple[1]
		if abs(x)<=7 and abs(y)<=7:
			collide = True
			break
	return collide

def snakeCollidesSelf(snakeBody):
	collide = False
	head = snakeBody[0]
	for s in snakeBody[1:]:
		x = s[0] - head[0]
		y = s[1] - head[1]
		if (x*x + y*y) < 25:
			collide = True
			break
	return collide

def snakeCollidesEdge(snakeBody):
	head = snakeBody[0]
	if head[0] < 0: return True
	if head[0] > 640: return True
	if head[1] < 0: return True
	if head[1] > 480: return True
	return False

pygame.init()

fps = pygame.time.Clock()

window = pygame.display.set_mode((640,480))
pygame.display.set_caption('SNAAAAAAAAAAAAAAAAAAAAAAKE!!!!!!!!!!!!!!')

snakeLength = 3
snakeBody = [(320,240),(320,250),(320,260)]
apple = newApple()
speed = 10
direction = (0,-1)
#(1, = left, (-1, = right, 1) = down, -1) = up

quit = False
while not quit:
	events = pygame.event.get()
	window.fill((0,0,128))
	for event in events:
		if event.type == KEYDOWN:
			if event.key == K_q:
				quit = True
			if event.key == K_a:
				direction = (-1,0)
			if event.key == K_d:
				direction = (1,0)
			if event.key == K_w:
				direction = (0,-1)
			if event.key == K_s:
				direction = (0,1)
	appleEaten = snakeCollidesApple(snakeBody,apple)
	snakeBitten = snakeCollidesSelf(snakeBody)
	snakeCrashed = snakeCollidesEdge(snakeBody)
	
	if appleEaten:
		apple = newApple()
		snakeLength += 1
		speed += 1
	
	snakeBody = moveSnake(snakeBody)
	
	drawApple()
	drawSnake()
	
	pygame.display.update()
	fps.tick(speed)
	quit = snakeBitten or snakeCrashed or quit

print "you ate:",snakeLength-3,"apples!"
if randint(0,100)>95:
	print "big question here: do snakes eat apples?"
