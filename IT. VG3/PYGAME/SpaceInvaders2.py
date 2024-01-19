import pygame as pg
import random

pg.init()


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
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

    def tegn(self, vindu):
        #pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 
        img = pg.image.load("spaeship.png")
        img = pg.transform.scale(img,(125,125))
        vindu.blit(img, (self.x,self.y))

# Fiende-klasse
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = 0

    def update(self):
        self.rect.y += ENEMY_SPEED

# Prosjetil-klasse
class Projectile(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= PROJECTILE_SPEED

# Initialisere vinduet
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Skyt spillet")

# Opprette sprite-grupper
all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
projectiles = pg.sprite.Group()

# Opprette spiller
player = Player()
all_sprites.add(player)

# Spillvariabler
score = 0
lives = 3
font = pg.font.Font(None, 36)

# Spill-løkke
clock = pg.time.Clock()
running = True

while running and lives > 0:
    for event in pg.event.get():
        if event.type == .QUIT:
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