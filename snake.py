#Import pygame module
import pygame

#Import time module
import time

#Import random module
import random

#Initialize the pygame module
pygame.init()

#Colors
white=[255,255,255]
black=[0,0,0]
red=[255,0,0]
green = [0,255,0]
blue = [0,0,255]

#Display Title
gameTitle='Snake 2017'

#Variables
gameExit=False
displayMaxWidth= 800
displayMaxHeight = 600
snakeTopPos= displayMaxHeight/2
snakeLeftPos= displayMaxWidth/2
snakeHeight= 10
snakeWidth= 10
snakeColor= green
snakeHitObject = False
snakeEatableCount = 20
snakeEatables = list([int(i*round(random.random()*100,0)), int(i*round(random.random()/2*100,0)),snakeWidth,snakeHeight] for i in range(snakeEatableCount))
snakeEatableColor = red

font = pygame.font.SysFont(None,25)
gameDisplay = pygame.display.set_mode((displayMaxWidth,displayMaxHeight))
pygame.display.set_caption(gameTitle)

	

def show_game_text (msg,color):
	gameText = font.render(msg,True,color)
	gameDisplay.blit(gameText,[displayMaxWidth/2 - len(msg)/2*10,displayMaxHeight/2])
	
def detect_collision(l,t,w,h):
	_newWidth=w
	for eatable in snakeEatables:
		if eatable == [l,t,w,h]:
			_newWidth += h
			snakeEatables.remove(eatable)
			break
		
		elif eatable[0] <= l + w <= eatable[0] + h and eatable[1] <= t + h <= eatable[1] + h:
			_newWidth += h
			snakeEatables.remove(eatable)
			break
				
	
	return _newWidth
		
		

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit=True		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				snakeTopPos -= 10
				if snakeTopPos <= 0:
					snakeTopPos = displayMaxHeight - 10
			elif event.key == pygame.K_DOWN:
				snakeTopPos += 10
				if snakeTopPos >= displayMaxHeight:
					snakeTopPos = 10
			elif event.key == pygame.K_LEFT:
				snakeLeftPos -= 10
				if snakeLeftPos <= 0:
					snakeLeftPos = displayMaxWidth - 10
			elif event.key == pygame.K_RIGHT:
				snakeLeftPos += 10
				if snakeLeftPos >= 	displayMaxWidth:
					snakeLeftPos = 10
					
			
			newSnakeWidth = detect_collision(snakeLeftPos,snakeTopPos,snakeWidth,snakeHeight)
			if snakeWidth != newSnakeWidth:
				show_game_text("snake ate...",green)
				pygame.display.update()
				snakeWidth = newSnakeWidth
				time.sleep(1)
		
		
	
	
	
	
	snakeRect = [snakeLeftPos,snakeTopPos,snakeWidth,snakeHeight]
	gameDisplay.fill(black)
	
	snakeEatableCount = len(snakeEatables)
	for i in range(snakeEatableCount):
		gameDisplay.fill(snakeEatableColor,rect=snakeEatables[i])
		
	gameDisplay.fill(snakeColor,rect=snakeRect)	
	pygame.display.update()
		
show_game_text("The snake 2017 is shutting down...",blue)
pygame.display.update()

#Wait for seconds
time.sleep(1)
pygame.quit()
quit()