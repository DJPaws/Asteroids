import pygame
from player import Player
from constants import *

def main():
	pygame.init()													# open game window and print opening message to terminal
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # initiate game enviornment
	my_clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()								#create groups based on functionality
	drawable = pygame.sprite.Group()

	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:														# start main game loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		for sprite in updatable:									# update sprite positions on screen
			sprite.update(dt)

		screen.fill((0, 0, 0))										# create black screen
		
		for sprite in drawable:										# draw sprite onto screen
			sprite.draw(screen)

		pygame.display.flip()										# refresh screen during loop

		elapsed_ms = my_clock.tick(60) 								# limit to 60 FPS and returns milliseconds passed
		dt = elapsed_ms / 1000										# convert to seconds and stores as delta time

if __name__ == "__main__":
	main()
