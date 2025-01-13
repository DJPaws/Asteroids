# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	my_clock = pygame.time.Clock() 			# initialize clock to track FPS
	dt = 0 									# delta time

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))						# create black screen

		player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
		player.draw(screen)
		pygame.display.flip()						# refresh screen during loop

		elapsed_ms = my_clock.tick(60) 				# limit to 60 FPS and returns milliseconds passed
		dt = elapsed_ms / 1000						# convert to seconds and stores as delta time

if __name__ == "__main__":
	main()
