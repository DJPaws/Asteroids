import pygame
import random
import math
from circleshape import CircleShape

class Asteroid(CircleShape):                    # initialize Asteroid using parant class CircleShape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.points = self._generate_points()
    
    def _generate_points(self):                 # Adjust shape to have multiple points
        points = []
        num_points = 8
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            variation = self.radius * 0.3
            point_radius = self.radius + random.uniform(-variation, variation)
            x = point_radius * math.cos(angle)
            y = point_radius * math.sin(angle)
            points.append((x, y))
        return points

    def draw(self, surface):                    # Draw onto screen, using round to limit flicker
        transformed_points = [(round(self.position.x + x), round(self.position.y + y)) 
                              for x, y in self.points]
        pygame.draw.polygon(surface, (255, 255, 255), transformed_points, width=2)

    def update(self, dt):                       # set velocity of Asteroid
        self.position += self.velocity * dt