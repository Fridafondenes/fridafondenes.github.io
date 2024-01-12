import pygame
from pygame.locals import *
from random import randint

VINDU_BREDDE = 800
VINDU_HOYDE = 600
ANTALL_STJERNER = 100

class Star:
    def __init__(self):
        self.x = randint(0, VINDU_BREDDE)
        self.y = randint(0, VINDU_HOYDE)
        self.speed = randint(1, 3)

    def move(self):
        self.x = (self.x + self.speed) % VINDU_BREDDE

def main():
    pygame.init()
    vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
    pygame.display.set_caption('Bevegelige stjerner')

    stjerner = [Star() for _ in range(ANTALL_STJERNER)]

    klokke = pygame.time.Clock()

    kjorer = True
    while kjorer:
        for event in pygame.event.get():
            if event.type == QUIT:
                kjorer = False

        for stjerne in stjerner:
            stjerne.move()

        vindu.fill((0, 0, 0))  # Fyller vinduet med svart bakgrunn

        for stjerne in stjerner:
            pygame.draw.circle(vindu, (255, 255, 255), (int(stjerne.x), int(stjerne.y)), 2)

        pygame.display.flip()
        klokke.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
