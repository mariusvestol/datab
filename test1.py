print("hello world")

# code noe <- lager ny fil i vscode :()


import pygame



pygame.init()

# game window
screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))



screen.fill((255,255,255))
pygame.display.flip()

# game loop

run = True
while run:
	# event handler
	# samme som while run == True
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
pygame.quit()

