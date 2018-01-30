import pygame
import time
import random
import sys


pygame.init()

WIDTH = 900
HEIGHT = 700 
FPS = 60



## COLOURS
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# Initialize pygame and create a window
pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.mixer.init()
pygame.display.set_caption('DODGE')
clock = pygame.time.Clock()

pygame.display.update()

charImg = pygame.image.load('character_left.png') 	

def character(x,y):
    gameDisplay.blit(charImg,(x,y))


all_sprites = pygame.sprite.Group()

# Game Loop
def gameLoop():
	# keep loop running at right speed
	
	x = (WIDTH * 0.45)
	y = (HEIGHT * 0.8)

	x_change = 0			#would have to make it equivalent to velocity
	y_change = 0			#will introduce gravity in the jump for a realistic movement

	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_UP	:
					y_change = -10	
				if event.key == pygame.K_DOWN:
					y_change = 10

				if event.key == pygame.K_LEFT:
					x_change = -10
				if event.key == pygame.K_RIGHT:
				    x_change = 10				
					

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0			
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				    x_change = 0	
		y += y_change
		x += x_change
		gameDisplay.fill(white)
		character(x,y)
		pygame.display.update()
		#Keep loop running at right speed
		clock.tick(FPS)



gameLoop()
pygame.quit()
quit()






