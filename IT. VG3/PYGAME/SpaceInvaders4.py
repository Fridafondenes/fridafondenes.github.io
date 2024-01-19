# Oppgave: Lag et enkelt "Skyt spillet" med Pygame

# Lag et vindu med dimensjoner 800x600 piksler.
# Lag en spillerfigur som kan beveges horisontalt ved hjelp av piltastene.
# Legg til fiender som faller nedover skjermen fra toppen.
# Spilleren skal kunne skyte prosjektiler oppover ved å trykke på mellomromstasten.
# Hvis spillerens prosjektil treffer en fiende, får spilleren poeng.
# Hvis en fiende når bunnen av skjermen uten å bli truffet, mister spilleren et liv.
# Legg til en poengteller og en livsteller i spillet.
# Spillet skal avslutte når spilleren ikke har flere liv igjen.

import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m
from random import randint
import sys
from pygame.sprite import Sprite, Group



# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1100
VINDU_HOYDE  = 750
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
livsteller = 3


class Karakter(Sprite):
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fart = fart
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt

  
  def tegn(self, vindu):
    """Metode for å tegne ballen"""
    #pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 
    img = pg.image.load("spaeship.png")
    img = pg.transform.scale(img,(125,125))
    vindu.blit(img, (self.x,self.y))

  def flytt(self, taster):
    """Metode for å flytte ballen"""
    if taster[K_LEFT]:
      self.x -= self.fart
    if taster[K_RIGHT]:
      self.x += self.fart




class Romvesen(Sprite):
    def __init__(self, x, y, fart, radius, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.fart = fart
        self.radius = radius
        self.vindusobjekt = vindusobjekt
  
    def tegn(self, vindu):
        #pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 
        img = pg.image.load("Romvesen.png")
        img = pg.transform.scale(img,(70,70))
        vindu.blit(img, (self.x,self.y))

    def flytt(self):
      global livsteller  # Legg til denne linjen for å referere til den globale variabelen
      self.y += self.fart

      # Sjekk om romvesenet har nådd bunnen av vinduet
      


        # Gjenoppstiller romvesenet øverst hvis det går utenfor bunnen
        
   
    # def flytt(self):
    #   self.y += self.fart
    #   if self.y > VINDU_HOYDE:
    #     self.KarakterLiv - 1
    #     # Gjenoppstiller romvesenet øverst hvis det går utenfor bunnen
    #     self.y = -10
    #     self.x = randint(0, VINDU_BREDDE)

def vis_game_over(vindu):
    img = pg.image.load("gameover.png")
    img = pg.transform.scale(img, (VINDU_BREDDE, VINDU_HOYDE))
    vindu.blit(img, (0, 0))

# def restart_spill():
#     # Gjenopprett livsteller og posisjonene til spiller og romvesen
#     global livsteller
#     livsteller = 3
#     karakter.x = 400
#     karakter.y = 600
#     romvesen.y = -10
#     romvesen.x = randint(0, VINDU_BREDDE)


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
karakter = Karakter(400, 600, 5, 20, (255, 69, 0), vindu)
romvesen = Romvesen(randint(0, VINDU_BREDDE),-10, 5, 20, vindu)

# for i in range(3):
#   romvesen[i] += 2
#   if romvesen[i] >= vindu.get_height():
#     star_y[i] = 0
#   pg.draw.rect(vindu,(255,255,255), pg.Rect(romvesen[i],romvesen[i], 5, 5,))
        

  


# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False


    for i in range(50):
        star_y[i] += 2
        star2_y[i] += 1
        if star_y[i] >= vindu.get_height():
            star_y[i] = 0
        if star2_y[i] >= vindu.get_height():
            star2_y[i] = 0
        pg.draw.rect(vindu,(255,255,255), pg.Rect(star_x[i],star_y[i], 5, 5,))
        pg.draw.rect(vindu,(255,255,255), pg.Rect(star2_x[i],star2_y[i], 2, 2,))

    # font = pg.font.Font(None, 36)
    # livstekst = font.render(f"Liv: {livsteller}", True, (255, 255, 255))
    # vindu.blit(livstekst, (10, 10))


    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()


    # Tegner og flytter ballene
    karakter.tegn(vindu)
    karakter.flytt(trykkede_taster)
    romvesen.tegn(vindu)
    romvesen.flytt()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

    if Romvesen > VINDU_HOYDE:
        livsteller -= 1
        self.y = -10
        self.x = randint(0, VINDU_BREDDE)
        if livsteller == 0:
          # pg. quit()
          img = pg.image.load("gameover.png")
          img = pg.transform.scale(img,(70,70))
          vindu.blit(img, (self.x,self.y))

    

# Avslutter pygame
pg.quit()

