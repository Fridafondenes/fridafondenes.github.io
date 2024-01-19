import pygame as pg
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
import sys
from pygame.sprite import Sprite
from random import randint

# Konstanter
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 750
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SPACESHIP_IMAGE_PATH = "spaeship.png"
ENEMY_IMAGE_PATH = "Romvesen.png"

class Player(Sprite):
    def __init__(self, x, y, speed, radius, window):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.window = window

    def draw(self):
        img = pg.image.load(SPACESHIP_IMAGE_PATH)
        img = pg.transform.scale(img, (125, 125))
        self.window.blit(img, (self.x, self.y))

    def move(self, keys):
        if keys[K_LEFT]:
            self.x -= self.speed
        if keys[K_RIGHT]:
            self.x += self.speed

class Enemy(Sprite):
    def __init__(self, x, y, speed, radius, window):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.window = window

    def draw(self):
        img = pg.image.load(ENEMY_IMAGE_PATH)
        img = pg.transform.scale(img, (70, 70))
        self.window.blit(img, (self.x, self.y))

    def move(self):
        self.y += self.speed
        if self.y > WINDOW_HEIGHT:
            # Reduser liv eller gjør andre handlinger ved behov
            self.y = -10
            self.x = randint(0, WINDOW_WIDTH)

# Pygame initialisering
pg.init()
window = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# Objekter
player = Player(400, 600, 5, 20, window)
enemy = Enemy(randint(0, WINDOW_WIDTH), -10, 5, 20, window)

# Hovedløkke
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    window.fill(BLACK)

    keys = pg.key.get_pressed()

    player.draw()
    player.move(keys)

    enemy.draw()
    enemy.move()

    pg.display.flip()

pg.quit()
sys.exit()
