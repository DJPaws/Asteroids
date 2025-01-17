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
    
    def get_points(self):                       # Finds points for collision function
        return [pygame.Vector2(self.position.x + x, self.position.y + y) 
                for x, y in self.points]
    
    def point_in_polygon(self, point):          # adds detection inside of asteroid for collision
        local_point = pygame.Vector2(point.x - self.position.x, 
                               point.y - self.position.y)
    
        n = len(self.points)
        inside = False
        j = n - 1
        for i in range(n):
            pi = pygame.Vector2(self.points[i])
            pj = pygame.Vector2(self.points[j])
        
            if ((pi.y > local_point.y) != (pj.y > local_point.y) and
                local_point.x < (pj.x - pi.x) * 
                (local_point.y - pi.y) / 
                (pj.y - pi.y) + pi.x):
                inside = not inside
            j = i
    
        return inside

    def draw(self, surface):                    # Draw onto screen, using round to limit flicker
        transformed_points = [(round(self.position.x + x), round(self.position.y + y)) 
                              for x, y in self.points]
        pygame.draw.polygon(surface, (255, 255, 255), transformed_points, width=2)

    def update(self, dt):                       # set velocity of Asteroid
        self.position += self.velocity * dt