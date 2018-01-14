import pygame
import time
import random


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


class things:
	def __init__(self, thingx, thingy, thingw, thingh, color):
		self.color = color
		self.thingx = thingx
		self.thingy = thingy
		self.thingw = thingw
		self.thingh = thingh 
		

	def draw(self):
		pygame.draw.rect(gameDisplay,self.color,[self.thingx, self.thingy, self.thingw, self.thingh])
		pygame.display.update()

moveB = things(450,350,20,20,red)
# moveB.draw()
# pygame.display.update()
	
def gameLoop():

	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP	:
					moveB.thingy = moveB.thingy - 10

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					moveB.thingy = moveB.thingy + 10
		
			moveB.draw()
			pygame.display.update()
		clock.tick(60)

	# moveB = things(450,350,20,20,red)
	# moveB.draw()

# pygame.display.update()

gameLoop()
pygame.quit()
quit()






