print("hello world")

# code noe <- lager ny fil i vscode :()


import pygame



pygame.init()

# game window
screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))



rect = pygame.Rect(0, 0, 100, 100)
myRects = []

screen.fill((255,255,255))
pygame.draw.rect(screen,(0,0,0),rect)
pygame.draw.rect(screen,(5,150,5),rect)

# on doit creer des nouveaux rectangles parce que ils ne sont pas accesible quand ils sont cree dans un liste je crois

for p in range(8):
	if p%2 == 0:
		colors = [(0,0,0),(255,255,255)]
	else:
		colors = [(255,255,255),(0,0,0)]
	for i in range(8):
		color = (0,0,0)
		if i%2 == 0:
			color = colors[0]
		else:
			color = colors[1]
		print(color)
		rect = pygame.Rect(100*i,100*p,100,100)
		myRects.append(rect)
		pygame.draw.rect(screen,color,rect)


pygame.display.flip()


"""
print(myRects)

myRects[1].topleft(200,200)
"""


# game loop

run = True
while run:
	# event handler
	# samme som while run == True
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
pygame.quit()

