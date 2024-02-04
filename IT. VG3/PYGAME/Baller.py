import pygame
import sys
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

class Ball:
    def __init__(self, x, y, vx, vy, radius, farge):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.farge = farge
        self.gravity = 0.1
        self.friction = 0.01
        self.bounce_loss = 0.9

    def draw(self, screen):
        pygame.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def update(self, screen_width, screen_height):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity

        if self.y + self.radius >= screen_height:  # Ball is touching the ground
            self.y = screen_height - self.radius  # Stop the ball from falling through the ground
            self.vy *= -1 * self.bounce_loss  # Multiply by bounce_loss
            if self.vx > 0:  # Slow down horizontal velocity to simulate friction
                self.vx -= self.friction
            elif self.vx < 0:
                self.vx += self.friction

        if self.x + self.radius >= screen_width:  # Ball is touching the right edge
            self.x = screen_width - self.radius
            self.vx *= -1
        elif self.x - self.radius <= 0:  # Ball is touching the left edge
            self.x = self.radius
            self.vx *= -1

    def handle_collision(self, other):
        distance = ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        if distance <= self.radius + other.radius:
            overlap = 0.5 * (distance - self.radius - other.radius)
            self.x -= overlap * (self.x - other.x) / distance
            self.y -= overlap * (self.y - other.y) / distance
            other.x += overlap * (self.x - other.x) / distance
            other.y += overlap * (self.y - other.y) / distance

            # One-dimensional elastic collision formula
            new_vx1 = (self.vx * (self.radius - other.radius) + 2 * other.radius * other.vx) / (self.radius + other.radius)
            new_vx2 = (other.vx * (other.radius - self.radius) + 2 * self.radius * self.vx) / (self.radius + other.radius)

            self.vx, other.vx = new_vx1, new_vx2

class BallType1(Ball):
    def __init__(self, x, y, vx, vy, radius, farge):
        super().__init__(x, y, vx, vy, radius, farge)

class BallType2(Ball):
    def __init__(self, x, y, vx, vy, radius, farge, fart):
        super().__init__(x, y, vx, vy, radius, fart, vindusobjekt)
        self.fart = fart
        self.vindusobjekt = vindusobjekt

    def flytt(self, taster):
        """Metode for å flytte spilleren"""
        if taster[K_LEFT]:
            self.x -= self.fart
        if taster[K_RIGHT]:
            self.x += self.fart

pygame.init()
screen = pygame.display.set_mode((800, 600))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball1.update(800, 600)  
    ball2.update(800, 600) 

    ball1.handle_collision(ball2)
    ball2.handle_collision(ball1)

    screen.fill((0, 0, 0))
    ball1.draw(screen)
    ball2.draw(screen)

    pygame.display.flip()
    pygame.time.delay(20)


main()


