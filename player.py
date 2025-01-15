import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):   # create initial shape of player, this will be used as thier hitbox
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):         # create triangle polygon to represent player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):     # draw triangle onto screen and color it white
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):       # rotate sprite based on turn speed multiplied by delta time
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):       # update sprite in relation to input from player
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):         # rotate and move sprite in game window
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt