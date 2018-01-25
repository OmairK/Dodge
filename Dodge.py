import pygame
import time
import random
import os


WIDTH =  600
HEIGHT = 600
FPS = 50

# Colours
BLACK = (0,0,0) 
WHITE =(255, 255, 255)
GREEN = (0 ,255 ,0)
BLUE = (0 ,0 ,255)
RED = (255 ,0 ,0)

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
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DODGE")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Game loop
running = True
while running:
	# keep loop running at right speed
	clock.tick(FPS)
	# process input (events)
	for event in pygame.event.get():
		#check for closing window
		if event.type == pygame.QUIT:
			running = False
	# Update
	all_sprites.update()
	# Draw / render
	screen.fill(WHITE)
	all_sprites.draw(screen)
	# *after* drawing everything flip the display
	pygame.display.flip()


pygame.quit()