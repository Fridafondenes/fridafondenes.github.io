import pygame as pg
import random

pg.init()

Bredde, Høyde = 800, 600

Hvit = (255, 255, 255)
Rød = (255, 0 ,0)

class Spiller:
    def __init_(self, )


import pygame
import sys
import random

# Initialisere Pygame
pygame.init()

# Definere konstanter
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
ENEMY_SPEED = 3
PROJECTILE_SPEED = 7
ENEMY_SPAWN_INTERVAL = 50

# Farger
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Spillerklasse
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

# Fiende-klasse
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = 0

    def update(self):
        self.rect.y += ENEMY_SPEED

# Prosjetil-klasse
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= PROJECTILE_SPEED

# Initialisere vinduet
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Skyt spillet")

# Opprette sprite-grupper
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

# Opprette spiller
player = Player()
all_sprites.add(player)

# Spillvariabler
score = 0
lives = 3
font = pygame.font.Font(None, 36)

# Spill-løkke
clock = pygame.time.Clock()
running = True

while running and lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectile = Projectile(player.rect.centerx, player.rect.top)
                all_sprites.add(projectile)
                projectiles.add(projectile)

    # Legg til fiender med jevne mellomrom
    if random.randrange(ENEMY_SPAWN_INTERVAL) == 0:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Oppdater sprites
    all_sprites.update()

    # Sjekk kollisjoner mellom prosjektiler og fiender
    hits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
    for hit in hits:
        score += 1

    # Sjekk kollisjoner mellom spiller og fiender
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        lives -= 1

    # Tegn bakgrunnen
    screen.fill((0, 0, 0))

    # Tegn alle sprites
    all_sprites.draw(screen)

    # Tegn poengteller og livsteller
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 150, 10))

    # Oppdater vinduet
    pygame.display.flip()

    # Kontroller oppdateringshastighet
    clock.tick(60)

# Avslutt Pygame
pygame.quit()
sys.exit()