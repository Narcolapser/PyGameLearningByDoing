from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

from random import randint
import random

class SnakeGame(Widget):
	apple = ObjectProperty(None)
	snake = ObjectProperty(None)

	def setup(self):
		width = Window.width / 10
		height = Window.height / 10
		self.apple.newSpot(width,height)
	
	def update(self, dt):
		width = int(Window.width / 10)
		height = int(Window.height / 10)

		self.snake.update()

class Snake(Widget):
        direction = 0
        speed = 60
        length = 5

        def update(self):
                self.move()

        def move(self):
                if self.direction == 0:
                        self.pos = self.x,self.y+10
                elif self.direction == 1:
                        self.pos = self.x+10,self.y
                elif self.direction == 2:
                        self.pos = self.x,self.y-10
                else:
                        self.pos = self.x-1,self.y

class SnakeSegment(Widget):
        pass

class Apple(Widget):

	def newSpot(self,x,y):
		self.pos = (randint(1,x-1)*10, randint(1,y-1)*10)

class SnakeApp(App):
	def build(self):
		game = SnakeGame()
		game.setup()
		Clock.schedule_interval(game.update, 1)
		return game

if __name__ == '__main__':
	SnakeApp().run()
	
