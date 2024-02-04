import pygame as pg
import sys
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT)

#jeg tar utgangspungt i denne koden: https://github.com/hausnes/IT2-2023-2024/blob/main/pygame/sprettande_ballar/sprettande_ballar.py
#og deretter endret den til å bruke arv

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
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def update(self, screen_width, screen_height):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity

        if self.y + self.radius >= screen_height:
            self.y = screen_height - self.radius
            self.vy *= -1 * self.bounce_loss
            if self.vx > 0:
                self.vx -= self.friction
            elif self.vx < 0:
                self.vx += self.friction

        if self.x + self.radius >= screen_width:
            self.x = screen_width - self.radius
            self.vx *= -1
        elif self.x - self.radius <= 0:
            self.x = self.radius
            self.vx *= -1

    def handle_collision(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        if distance <= self.radius + other.radius:
            overlap = 0.5 * (distance - self.radius - other.radius)
            self.x -= overlap * (self.x - other.x) / distance
            self.y -= overlap * (self.y - other.y) / distance
            other.x += overlap * (self.x - other.x) / distance
            other.y += overlap * (self.y - other.y) / distance

            new_vx1 = (self.vx * (self.radius - other.radius) + 2 * other.radius * other.vx) / (
                        self.radius + other.radius)
            new_vx2 = (other.vx * (other.radius - self.radius) + 2 * self.radius * self.vx) / (
                        self.radius + other.radius)

            self.vx, other.vx = new_vx1, new_vx2

class BallType1(Ball):
    def __init__(self, x, y, vx, vy, radius, farge):
        super().__init__(x, y, vx, vy, radius, farge)


class BallType2(Ball):
    def __init__(self, x, y, vx, vy, radius, farge, fart):
        super().__init__(x, y, vx, vy, radius, farge)
        self.fart = fart

    def flytt(self, keys):
        if keys[K_LEFT]:
            self.x -= self.fart
        if keys[K_RIGHT]:
            self.x += self.fart
        if keys[K_UP]:
            self.y -= self.fart
        if keys[K_DOWN]:
            self.y += self.fart
        

pg.init()
VINDU_BREDDE = 800
VINDU_HOYDE = 600

vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

ball1 = BallType1(100, 100, 2, 0, 20, (255, 0, 0))
ball2 = BallType2(200, 200, -2, 0, 20, (0, 0, 255), 5)

clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()
    ball2.flytt(keys)

    ball1.update(800, 600)
    ball2.update(800, 600)

    ball1.handle_collision(ball2)
    ball2.handle_collision(ball1)

    vindu.fill((0, 0, 0))
    ball1.draw(vindu)
    ball2.draw(vindu)

    pg.display.flip()
    clock.tick(60)

pg.quit()