


# set up assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
class Player(pygame.sprite.Sprite):
	#sprite for the Player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
		self.image.set_colorkey(BLACK)    ##ignores the colour
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
	def update(self):
		self.rect.x += 5
		if self.rect.left > WIDTH:
			self.rect.right = 0


#initialize pygame and create window

player = Player()
all_sprites.add(player)
# Game loop
running = True
while running:
	# keep loop running at right speed
	# process input (events)
	
	# Update
	
	# Draw / render
	
	# *after* drawing everything flip the display


pygame.quit()