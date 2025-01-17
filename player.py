import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):                               # create initial shape of player, this will be used as thier hitbox
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):                                     # create triangle polygon to represent player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def point_in_triangle(self, point):
        triangle_points = self.triangle()
    
        def sign(p1, p2, p3):
            return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)
    
        d1 = sign(point, triangle_points[0], triangle_points[1])
        d2 = sign(point, triangle_points[1], triangle_points[2])
        d3 = sign(point, triangle_points[2], triangle_points[0])

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)
    
    def draw(self, screen):                                 # draw triangle onto screen and color it white
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def collides_with_asteroid(self, asteroid):             # Get's points of asteroid
        for point in asteroid.get_points():                 # Checks collision between asteroid and player
            if self.point_in_triangle(point):
                return True
            
        for point in self.triangle():
            if asteroid.point_in_polygon(point):
                return True
            
        return False

    def rotate(self, dt):                                   # rotate sprite based on turn speed multiplied by delta time
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):                                   # update sprite in relation to input from player
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):                                     # rotate and move sprite in game window
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def destroy(self):                                      # remove sprite from screen
        self.kill()