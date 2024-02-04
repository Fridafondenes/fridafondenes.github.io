import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m
from random import randint
import sys
from pygame.sprite import Sprite, Group

pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1100
VINDU_HOYDE = 750
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
livsteller = 3
hit_objs = []
kills = 0
cash = 0
# Legg til dette før hovedloopen
font = pg.font.Font(None, 36)


class Karakter(Sprite):
    """Generell karakterklasse"""

    def __init__(self, x, y, fart, radius, farge, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.fart = fart
        self.radius = radius
        self.farge = farge
        self.vindusobjekt = vindusobjekt

    def tegn(self, vindu):
        """Metode for å tegne karakteren"""
        img = pg.image.load("spaeship.png")
        img = pg.transform.scale(img, (125, 125))
        vindu.blit(img, (self.x, self.y))

    def flytt(self, taster):
        """Metode for å flytte karakteren"""
        if taster[K_LEFT]:
            self.x -= self.fart
        if taster[K_RIGHT]:
            self.x += self.fart


class Player(Karakter):
    """Klasse for å representere spilleren"""

    def __init__(self, x, y, fart, radius, farge, vindusobjekt):
        super().__init__(x, y, fart, radius, farge, vindusobjekt)

    def shoot(self):
        x_midpoint = self.x + 62  # Justert for midten av karakteren
        self.skudd.append(Skudd(x_midpoint, self.y, 0, -10, 5))


class Romvesen(Karakter):
    """Klasse for å representere romvesenet"""

    def __init__(self, x, y, fart, radius, vindusobjekt):
        super().__init__(x, y, fart, radius, (255, 255, 255), vindusobjekt)

    def flytt(self):
        global livsteller  # Legg til denne linjen for å referere til den globale variabelen
        self.y += self.fart

        # Sjekk om romvesenet har nådd bunnen av vinduet
        if self.y > VINDU_HOYDE:
            livsteller -= 1
            if livsteller == 0:
                img = pg.image.load("gameover.png")
                img = pg.transform.scale(img, (70, 70))
                vindu.blit(img, (self.x, self.y))

            # Gjenoppstiller romvesenet øverst hvis det går utenfor bunnen
            self.y = -10
            self.x = randint(0, VINDU_BREDDE)

            # Sjekk om spilleren har mistet alle livene
            if livsteller == 0:
                fortsett = False  # Dette vil avslutte spillet


class Skudd(Sprite):
    skudd = []

    def __init__(self, x, y, v_x, v_y, fart):
        super().__init__()
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.fart = fart

    def tegn(self, vindu):
        """Metode for å tegne skuddet"""
        pg.draw.rect(vindu, (255, 0, 0), pg.Rect(self.x, self.y, 5, 15))

    def flytt(self):
        """Metode for å bevege skuddet"""
        self.y += self.v_y

        # Fjern skuddet hvis det går utenfor vinduet
        if self.y < 0:
            Skudd.skudd.remove(self)

    def treffer_romvesen(self, romvesen):
        """Metode for å sjekke om skuddet treffer romvesenet"""
        return (
            self.x < romvesen.x + romvesen.radius
            and self.x + 5 > romvesen.x
            and self.y < romvesen.y + romvesen.radius
            and self.y + 15 > romvesen.y
        )


star_x = []
star_y = []

star2_x = []
star2_y = []
for i in range(50):
    star_x.append(randint(0,VINDU_BREDDE))
    star_y.append(randint(0,VINDU_HOYDE))
    
    star2_x.append(randint(0,VINDU_BREDDE))
    star2_y.append(randint(0,VINDU_HOYDE))
    
# Lager et Ball-objekt
spiller = Player(400, 600, 5, 20, (255, 69, 0), vindu)
romvesen = Romvesen(randint(0, VINDU_BREDDE), -10, 3, 20, vindu)

# Gjenta helt til brukeren lukker vinduet
spill_avsluttet = False
skudd_frekvens = 10  # Juster denne verdien for å endre hvor ofte karakteren kan skyte
skudd_teller = 0




while not spill_avsluttet:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            spill_avsluttet = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and skudd_teller == 0:
                spiller.shoot()
                skudd_teller = skudd_frekvens

    # Farger bakgrunnen lyseblå
    vindu.fill((0, 0, 0))

    for i in range(50):
        star_y[i] += 2
        star2_y[i] += 1
        if star_y[i] >= vindu.get_height():
            star_y[i] = 0
        if star2_y[i] >= vindu.get_height():
            star2_y[i] = 0
        pg.draw.rect(vindu,(255,255,255), pg.Rect(star_x[i],star_y[i], 5, 5,))
        pg.draw.rect(vindu,(255,255,255), pg.Rect(star2_x[i],star2_y[i], 2, 2,))

    # Tegn og oppdater skuddene
    for skudd in Skudd.skudd:
        skudd.tegn(vindu)
        skudd.flytt()
        # Sjekk om skuddet treffer romvesenet
        if skudd.treffer_romvesen(romvesen):
            romvesen.y = -10
            romvesen.x = randint(0, VINDU_BREDDE)
            Skudd.skudd.remove(skudd)
            kills += 1

    # Oppdater skuddtelleren
    if skudd_teller > 0:
        skudd_teller -= 1

    livtekst = font.render(f'Liv: {livsteller}', True, (255, 255, 255))
    vindu.blit(livtekst, (10, 10))

    # Tegn og oppdater karakteren
    spiller.tegn(vindu)
    spiller.flytt(pg.key.get_pressed())

    # Tegn og oppdater romvesenet
    romvesen.tegn(vindu)
    romvesen.flytt()

    # Sjekk om livstellingen er 0 og avslutt spillet
    if livsteller == 0:
        img = pg.image.load("gameover.png")
        scalar = 1500
        img = pg.transform.scale(img,(scalar,scalar))
        vindu.blit(img, ((VINDU_BREDDE - scalar)/2, (VINDU_HOYDE - scalar)/2))
        pg.display.flip()
        pg.time.delay(3000)  # Vent i 3 sekunder før du avslutter
        spill_avsluttet = True
    
    pg.display.flip()


# Avslutter pygame
pg.quit()