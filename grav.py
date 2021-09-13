# importing modules
import pymunk
import pygame
import sys

# Create a physical body
def create_ball(space, pos):
	body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
	body.position = pos
	design = pymunk.Circle(body, 75)
	space.add(body,design)
	return design

# Drawing it in Pygame
def display_ball(balls):
	for ball in balls:
		position_x = int(ball.body.position.x)
		position_y = int(ball.body.position.y)
		ball_rect = ball_design.get_rect(center = (position_x,position_y))
		screen.blit(ball_design, ball_rect)

def static_obstacle(space, pos):
	body = pymunk.Body(body_type = pymunk.Body.STATIC)
	body.position = pos
	design = pymunk.Circle(body, 30)
	space.add(body, design)
	return design

def display_static_obstacle(balls):
	for ball in balls:
		position_x = int(ball.body.position.x)
		position_y = int(ball.body.position.y)
		pygame.draw.circle(screen,(255, 255, 255),(position_x,position_y), 30)


pygame.init() # initializing pygame
pygame.display.set_caption('Gravity Simulator')
screen = pygame.display.set_mode((750,750)) # creating the display surface
clock = pygame.time.Clock() # creating the game clock
space = pymunk.Space()

space.gravity = (0, 500) # controlling the direction and speed of gravity
ball_design = pygame.image.load('ball.png')
background = pygame.image.load('background.jpg')

balls = []
obstacles = []

obstacles.append(static_obstacle(space,(500, 500)))
obstacles.append(static_obstacle(space,(250, 600)))
obstacles.append(static_obstacle(space,(100, 400)))
obstacles.append(static_obstacle(space,(650, 300)))
obstacles.append(static_obstacle(space,(350, 300)))


# Game Loop
while True:
	for event in pygame.event.get(): # checking for user input
		if event.type == pygame.QUIT: # input to close the game
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			balls.append(create_ball(space, event.pos))

	screen.fill((217, 217, 217)) # background colour
	screen.blit(background, (0,0))

	display_ball(balls)
	display_static_obstacle(obstacles)
	space.step(1/50)
	pygame.display.update() # rendering the frame\
	clock.tick(120) # limiting the frames per second to 120

