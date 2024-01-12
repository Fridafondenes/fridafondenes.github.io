import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
    """Klasse for å representere en ball"""
    def __init__(self, x, y, fart, radius, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.fart = fart
        self.radius = radius
        self.vindusobjekt = vindusobjekt
        self.farge = (255, 69, 0)
  
    def tegn(self):
        """Metode for å tegne ballen"""
        pg.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius) 

    def flytt(self):
        """Metode for å flytte ballen"""
        # Sjekker om ballen er utenfor høyre/venstre kant
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
            self.fart = -self.fart
            self.skift_farge()

        self.x += self.fart * retning_x
        
        # Sjekker om ballen er utenfor topp/bunn kant
        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.fart = -self.fart
            self.skift_farge()  # Skifter farge ved kollisjon med vegge
        
        self.y += self.fart * retning_y

    def skift_farge(self):
        """Metode for å skifte farge"""
        self.farge = (pg.time.get_ticks() % 255, pg.time.get_ticks() % 255, pg.time.get_ticks() % 255)

# Lager et Ball-objekt
ball1 = Ball(250, 250, 5, 20, vindu)
ball2 = Ball(250, 250, 5, 20, vindu)


# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    keys = pg.key.get_pressed()

    # Endrer retning basert på tastaturinngang
    retning_x = keys[K_RIGHT] - keys[K_LEFT]
    retning_y = keys[K_DOWN] - keys[K_UP]

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Flytter og tegner ballene
    ball1.flytt(retning_x, retning_y)
    ball2.flytt(retning_x, retning_y)
    ball1.tegn()
    ball2.tegn()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()







