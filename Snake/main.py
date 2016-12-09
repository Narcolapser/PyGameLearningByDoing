from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

import traceback

from random import randint
import random
import time

class MenuScreen(Screen):
	def update(self, dt):
		pass

	def load_game(self):
		#app.sm.current = 'snake'
		name = str(time.time())
		s = GameScreen(name=name)
		app.sm.add_widget(s)
		app.sm.current = name

class GameScreen(Screen):
	def update(self,dt):
		pass

	def pre(self):
		print("pre-enter")

	def start(self):
		print("starting...")
		try:
			game.setup()
		except:
			self.game = SnakeGame()
			game = self.game
			game.setup()
			self.game_update = Clock.schedule_interval(game.update, 1.0/60.0)
			self.add_widget(game)

	def end(self):
		print("I've exited")
		Clock.unschedule(self.game_update)
		

class SnakeGame(Widget):
	apple = ObjectProperty(None)
	snake = ObjectProperty(None)
	segs = []
	apple_count = NumericProperty(0)
	
	def setup(self):
##		self.snake = Snake(parent=self)
##		self.apple = Apple(parent=self)
		segs = []
		width = Window.width / 10
		height = Window.height / 10
		self.apple.newSpot(width,height)
		self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
		self._keyboard.bind(on_key_down=self.on_keyboard_down)

		self.snake.pos = ((height/2)*10,(width/2)*10)
	
	def update(self, dt):
		width = int(Window.width / 10)
		height = int(Window.height / 10)

		self.snake.update()
		if self.snake.eat_apple(self.apple):
			self.apple.newSpot(width,height)
			self.apple_count += 1
			

	def on_touch_down(self, touch):
		if self.snake.direction == 0 or self.snake.direction == 2:
			if touch.x > self.snake.x:
				self.snake.direction = 1
			else:
				self.snake.direction = 3
		else:
			if touch.y > self.snake.y:
				self.snake.direction = 0
			else:
				self.snake.direction = 2
		self.snake.move()
			
		

	def keyboard_closed(self):
		self._keyboard.unbind(on_key_down=self.on_keyboard_down)
		self._keyboard = None

	def on_keyboard_down(self, keyboard, keycode, text, modifiers):
		if keycode[1] == 'up':
			self.snake.direction = 0
		if keycode[1] == 'right':
			self.snake.direction = 1
		if keycode[1] == 'down':
			self.snake.direction = 2
		if keycode[1] == 'left':
			self.snake.direction = 3
		self.snake.move()

	def add_segment(self,segment):
		self.add_widget(segment)
		self.segs.append(segment)
		for s in self.segs:
			if s.life <= 0:
				self.remove_widget(s)
				self.segs.pop(self.segs.index(s))
			else:
				s.life -= 1
				if s != segment:
					if self.snake.bite(s):
						self.dead()
	def dead(self):
		#App.get_running_app().stop()
		for line in traceback.format_stack(): print(line.strip())
		app.sm.current = 'menu'

class Snake(Widget):
	direction = 0
	speed = 30
	advance = 0
	length = 5

	def update(self):
		if self.advance == 0:
			self.move()
		self.advance -= 1

	def move(self):
		if self.direction == 0:
			self.pos = self.x,self.y+10
		elif self.direction == 1:
			self.pos = self.x+10,self.y
		elif self.direction == 2:
			self.pos = self.x,self.y-10
		else:
			self.pos = self.x-10,self.y

		if self.x > Window.width or self.y > Window.height:
			self.parent.dead()
		if self.x < 0 or self.y < 0:
			self.parent.dead()		
		

		ss = SnakeSegment()
		ss.pos = self.pos
		ss.life = self.length
		self.parent.add_segment(ss)
		self.advance = self.speed

	def eat_apple(self,apple):
		if apple.x == self.x and apple.y == self.y:
			self.length += 3
			self.speed -= 1
			return True
		return False

	def bite(self,seg):
		if seg.x == self.x and seg.y == self.y:
			return True
		return False

class SnakeSegment(Widget):
	life = 5

class Apple(Widget):

	def newSpot(self,x,y):
		self.pos = (randint(1,x-1)*10, randint(1,y-1)*10)

class SnakeApp(App):
	sm = ScreenManager()
	def build(self):
		menu = MenuScreen(name='menu')
		self.sm.add_widget(menu)
		game = GameScreen(name='snake')
		self.sm.add_widget(game)
		self.sm.load_game = menu.load_game
		Clock.schedule_interval(menu.update, 1.0/60.0)
		return self.sm

app = None

if __name__ == '__main__':
	app = SnakeApp()
	app.run()
	
