class Game:
	def __init__(self,x=640,y=480):
		self.x = x
		self.y = y
		pygame.init()

		self.fps = pygame.time.Clock()
		pygame.key.set_repeat(5,5)

		self.window = pygame.display.set_mode((self.x,self.y))
		pygame.display.set_caption('Russian game, Made in the UK, by an American.')
		
		self.speed = 60
		self.keys = pygame.key.get_pressed()
		self.piece = None
	
	def __call__(self):
		return self.update()
	
	def update(self):
		pygame.event.pump()
		self.keys = pygame.key.get_pressed()
		window.fill((0,0,0))
		
		board.update(self.score)
		self.score.update()
		
		if self.piece:
			self.piece.interact(self.keys)
		
		if self.piece:
			self.piece.update()
		else:
			self.piece = Piece()
			self.piece.update()
		
		pygame.display.update()
		fps.tick(speed)
#		if con:
#			return True
#		return False
		return True

