import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
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
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	game_over = False
	running = True
	while running:
		dt = my_clock.tick(60) / 1000.0														# start main game loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and game_over:
				if event.key == pygame.K_SPACE:
					game_over = False
					updatable.empty()
					drawable.empty()
					asteroids.empty()
					player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
					asteroid_field = AsteroidField()

		if not game_over:
			updatable.update(dt)

			for asteroid in asteroids:
				if player.collides_with_asteroid(asteroid):
					player.destroy()
					game_over = True
			
		for sprite in updatable:									# update sprite positions on screen
			sprite.update(dt)

		screen.fill((0, 0, 0))										# create black screen
		
		for sprite in drawable:										# draw sprite onto screen
			sprite.draw(screen)

		if game_over:
			font = pygame.font.Font(None, 74)
			text = font.render('Game Over', True, (255, 255, 255))
			text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
			screen.blit(text, text_rect)
			
			font = pygame.font.Font(None, 36)
			restart_text = font.render('Press SPACE to restart', True, (255, 255, 255))
			restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
			screen.blit(restart_text, restart_rect)

		pygame.display.flip()										# refresh screen during loop

if __name__ == "__main__":
	main()
