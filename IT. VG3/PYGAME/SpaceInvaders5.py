
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m
from random import randint
import sys
from pygame.sprite import Sprite, Group

pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1100
VINDU_HOYDE  = 750
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
livsteller = 3
hit_objs = []
kills = 0
cash = 0
# Legg til dette før hovedloopen
font = pg.font.Font(None, 36)


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

    def shoot(self):
        x_midpoint = self.x + self.width/2 + 4
        Skudd.skudd.append(Skudd(self.surf, x_midpoint + 20, self.y, 0, -10, 1, 15, 50))
        Skudd.skudd.append(Skudd(self.surf, x_midpoint - 30, self.y, 0, -10, 1, 15,  50))


  
  def tegn(self, vindu):
    """Metode for å tegne ballen"""
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
        img = pg.image.load("Romvesen.png")
        img = pg.transform.scale(img,(70,70))
        vindu.blit(img, (self.x,self.y))

    def flytt(self):
      global livsteller  # Legg til denne linjen for å referere til den globale variabelen
      self.y += self.fart

      # Sjekk om romvesenet har nådd bunnen av vinduet
      if self.y > VINDU_HOYDE:
        livsteller -= 1
        if livsteller == 0:
          # pg. quit()
          img = pg.image.load("gameover.png")
          img = pg.transform.scale(img,(70,70))
          vindu.blit(img, (self.x,self.y))


        # Gjenoppstiller romvesenet øverst hvis det går utenfor bunnen
        self.y = -10
        self.x = randint(0, VINDU_BREDDE)

        # Sjekk om spilleren har mistet alle livene
        if livsteller == 0:
          fortsett = False  # Dette vil avslutte spillet

class Skudd:
    skudd = []  
    def __init__(self, surf, x, y, v_x, v_y, VINDU_BREDDE, VINDU_HOYDE, ):
        super().__init__(surf, x, y, VINDU_BREDDE, VINDU_HOYDE)
        self.v_x = v_x
        self.v_y = v_y
        

    def draw(self):
        py.draw.ellipse(self.surf, "red", py.Rect(self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

        if skudd.y <= 0:
            Skudd.skudd.remove(skudd)

    def check_target(self, targets):##
        dead_target = None
        hit = False
        for target in targets:##
            if target.y + target.height >= self.y:
                if target.x <= self.x <= target.x + target.width or target.x <= self.x + self.width<= target.x + target.width:
                    target.health -= shot.dmg
                    self.shots.remove(shot)
                    if target.health <= 0: 
                        hit = True
                        dead_target = target
                    elif target.dmgd_img != None: 
                        target.img = target.dmgd_img

        return hit, dead_target





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

# Gjenta helt til brukeren lukker vinduet
spill_avsluttet = False
while not spill_avsluttet:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            spill_avsluttet = True

    # Farger bakgrunnen lyseblå
    vindu.fill("black")

    for i in range(50):
        star_y[i] += 2
        star2_y[i] += 1
        if star_y[i] >= vindu.get_height():
            star_y[i] = 0
        if star2_y[i] >= vindu.get_height():
            star2_y[i] = 0
        pg.draw.rect(vindu,(255,255,255), pg.Rect(star_x[i],star_y[i], 5, 5,))
        pg.draw.rect(vindu,(255,255,255), pg.Rect(star2_x[i],star2_y[i], 2, 2,))

    livtekst = font.render(f'Liv: {livsteller}', True, (255, 255, 255))
    vindu.blit(livtekst, (10, 10))

    for skudd in Skudd.skudd:
        for objs in [romvesen]:
            hit, obj = skudd.check_target(objs)
            if hit:
                #explosion frame
                frame_nr = 0
                hit_objs.append([obj, frame_nr])
                objs.remove(obj)
        
        shot.draw()
        shot.move()

    if len(hit_objs) > 0:
        for obj in hit_objs:
            obj[0].move()
            frame_nr = obj[1]
            if frame_nr < 9:
                obj[0].explode(explosion_imgs[frame_nr])
                obj[1] += 1
            else:
                hit_objs.remove(obj)


    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Tegner og flytter ballene
    karakter.tegn(vindu)
    karakter.flytt(trykkede_taster)
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

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()


