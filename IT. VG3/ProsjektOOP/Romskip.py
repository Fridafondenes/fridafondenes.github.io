# # Spørr Chatt GPT om idee til prosjekt:

# # Et morsomt lite prosjekt som jeg tror kan være gjennomførbart 
# # på to uker og samtidig gi rom for bruk av objektorientert programmering (OOP), 
# # er å lage et enkelt spill. La oss kalle det "Dodge the Asteroids."

# # Prosjektbeskrivelse:
# # Målet med spillet er å styre en romskipfigur (representert som et objekt) ved 
# # hjelp av tastaturkontroller for å unngå asteroider som faller ned fra toppen av skjermen. 
# # Hver gang spilleren unngår en asteroide, tjener de poeng. Spillet vil også inkludere et enkelt poengsystem, 
# # kollisjonsdeteksjon, og muligheten til å starte på nytt.

# # Teknologier og konsepter som kan inkluderes:

# # OOP: Du kan lage klasser for romskip, asteroider, og spillmotoren. Dette gjør det enklere 
# # å organisere og vedlikeholde koden.

# # Grafikk: Bruk enkle grafikkbiblioteker som Pygame (Python) eller LibGDX (Java) for å lage 
# # en grunnleggende visuell representasjon av spillet.

# # Kollisjonsdeteksjon: Implementer et system for å oppdage kollisjoner mellom romskipet og asteroidene, 
# # og håndter hva som skjer når en kollisjon inntreffer (for eksempel avslutte spillet eller trekke fra poeng).

# # Tid og animasjon: Lag en enkel animasjon der asteroidene beveger seg nedover på skjermen med en viss hastighet, 
# # og oppdater spillet på jevne tidsintervaller.

# # Poengsystem: Hold styr på spillerens poengsum og oppdater den i sanntid. Gi spilleren muligheten til å 
# # restarte spillet når de ønsker.

# # Nivåprogresjon: Legg til en økende vanskelighetsgrad ved å la asteroidene falle raskere eller legge til 
# # flere asteroider etter hvert som spilleren oppnår en viss poengsum.

# # Dette prosjektet kan være en morsom måte å utforske OOP og grunnleggende spillutvikling. Det kan også danne 
# # grunnlaget for videreutvikling og forbedring dersom du ønsker å gjøre spillet mer komplekst 
# # eller legge til flere funksjoner.


import random

class Character:
    def __init__(self, name, level, hp, attack):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack

    def __str__(self):
        return f"Name: {self.name}\n Level: {self.level}\n hp: {self.hp}\n Attack: {self.attack}"

# Genererer et tilfeldig navn fra listen 'name'
romskipNames = ["Millennium Falcon", "Enterprise", "Discovery", "Serenity", "TARDIS", "Battlestar Galactica", "Normandy", "Galactica"]
romskipeName = random.choice(romskipNames)

metriorNames = ["metior1","metior2","metior3","metior4" ]
metriorName = random.choice(metriorNames)

def tilfeldigHp():
    tilfeldig = random.randint(1, 100)
    return tilfeldig

def tilfeldigAttack():
    tilfeldig = random.randint(1, 10)
    return tilfeldig

def get_name(self):
    return self.name
    
def get_level(self):
    return self.level
    
def get_hp(self):
    return self.hp
    
def get_attack(self):
    return self.attack
    
def set_name(self, new_name):
    self.name = new_name

def set_level(self, new_level):
    self.level = new_level

def set_hp(self, new_hp):
    self.hp = new_hp

def set_attack(self, new_attack):
    self.attack = new_attack

def hit(self, damage):
    self.hp -= damage
    if self.hp < 0:
        print("GAME OVER")
    
def fix(self, amount):
    self.hp += amount
    if self.hp < tilfeldigHp():
        print("Du har max hp angrip!")

def pistol(self, cost):
    self.attack -= cost
    if self.attack < 0:
        self.attack = 0


# Oppretter et romskipobjek
hero = Character(romskipeName, 1, tilfeldigHp(), tilfeldigAttack())
metior1 = Character(metriorName, 1 , tilfeldigHp(), tilfeldigAttack())

# Skriver ut informasjonen om romskipet og metioer
print(hero)
print(metior1)

while hero.is_alive() and boss.is_alive():
    angrip= input("")
