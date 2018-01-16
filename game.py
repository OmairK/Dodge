import pygame
import time
import random
import sys


pygame.init()

display_width = 900
display_height = 700 

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Omair Name')
clock = pygame.time.Clock()
gameDisplay.fill(white)
pygame.display.update()

charImg = pygame.image.load('character_left.png') 	###Use the correct image


def character(x,y):
    gameDisplay.blit(charImg,(x,y))



# class things:




# 	def __init__(self, thingx, thingy, thingw, thingh, color):
# 		self.color = color
# 		self.thingx = thingx
# 		self.thingy = thingy
# 		self.thingw = thingw
# 		self.thingh = thingh 
		

# 	def draw(self):
# 		pygame.draw.rect(gameDisplay,self.color,[self.thingx, self.thingy, self.thingw, self.thingh])
# 		pygame.display.update()

# moveB = things(450,350,20,20,red)
# moveB.draw()
# pygame.display.update()
	
def gameLoop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)

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
					# moveB.thingy = moveB.thingy - 150
				if event.key == pygame.K_DOWN:
					y_change = 10
					# moveB.thingy = moveB.thingy + 150

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					y_change = 10

					# moveB.thingy = moveB.thingy + 150
				if event.key == pygame.K_DOWN:
					y_change = -10
					# moveB.thingy = moveB.thingy - 150 


		y += y_change
		character(x,y)
		# moveB.draw()
		pygame.display.update()
		clock.tick(60)

	# moveB = things(450,350,20,20,red)

# pygame.display.update()

gameLoop()
pygame.quit()
quit()






