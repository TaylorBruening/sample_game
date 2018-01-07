import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carIMG = pygame.image.load('racecar.png')
carIMG = pygame.transform.scale(carIMG,(100,160))

def car(x,y):
	gameDisplay.blit(carIMG,(x,y))

def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)

	x_change = 0

	left = False
	right = False
	crashed = False


	while not crashed:
	    for event in pygame.event.get():

		if event.type == pygame.QUIT:
		    crashed = True

		if event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_LEFT:
			left = True

		    if event.key == pygame.K_RIGHT:
			right = True

		if event.type == pygame.KEYUP:
		    if left and event.key == pygame.K_LEFT:
			left = False
		    if right and event.key == pygame.K_RIGHT:
			right = False

	    if left and right:
		x_change *= 1 (stays the same)
	    elif left:
		x_change = -5
	    elif right:
		x_change = 5
	    else:
		x_change = 0

	    x += x_change

		gameDisplay.fill(white)
		car(x,y)

		pygame.display.update() #update what has been drawn to the screen
		clock.tick(60)

pygame.quit()
quit()
