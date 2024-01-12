
from playsound import playsound
playsound("leva-in-the-dark-176514.mp3")

import random
import os
import time
import grafikk

class Character:
    def __init__(self, name, level, hp, mana, money, weapons):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.money = money
        self.weapons = weapons

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}, Weapon: {self.money}"

    def is_alive(self):
        return self.hp > 0

    def hit(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100

    def cast_spell(self, cost):
        self.mana -= cost
        if self.mana < 0:
            self.mana = 0

    def choose_weapon(self):
        print(f"Pengene dine: {self.money}")

        for i in range(len(self.weapons)):
            weapon = self.weapons[i]
            print(f"{i + 1}. {weapon}")

        while True:
            choice = input("Velg et våpen (1/2/3): ")
            if choice in {'1', '2', '3'}:
                weaponChoice = int(choice) - 1
                weapon = self.weapons[weaponChoice]

                if self.buy_weapon(weapon):
                    print(f"Du kjøpte {weapon.name} for {weapon.cost} mynter.")
                    return weaponChoice
                else:
                    print("Du har ikke råd til dette våpenet. Velg en annen.")
            else:
                print("Forstår ikke. Velg: 1, 2, or 3.")

    def buy_weapon(self, weapon):
        if self.money >= weapon.cost:
            self.money -= weapon.cost
            return True
        else:
            return False

class Weapon:
    def __init__(self, name, power, cost):
        self.name = name
        self.power = power
        self.cost = cost

    def __str__(self):
        return f"Name: {self.name}, Power: {self.power}, Cost: {self.cost}"

    def is_useful(self):
        return self.power > 0

    def attack(self):
        return self.power

#starter spille
print(grafikk.startLogo)
time.sleep(2)
os.system("clear")

# Lagar våpen
weapons = [Weapon("Gun", 95, 1999), Weapon("Mase", 80, 1674), Weapon("Laser", 67, 1588)]

#Lager helten
hero = Character("Lana narnda", 1, 100, 100, 5000, weapons)
print(f"All informasjon om helten: {hero}")
print(grafikk.heltLogo)
time.sleep(1.5)
os.system("clear")

# Lagar bossen
thegnome = Character("The Gnome", 1, 100, 100, 0, [])
print(f"All informasjon om The Gnome: {thegnome}")
print(grafikk.gnomLogo)
time.sleep(1.5)
os.system("clear")

# Lager våpen
print()

# Gjer gjerne meir ut av delen over, der du kan sette meir avanserte verdier for helten og bossen
# Kanskje du til og med kan la spelaren setje verdiane sjølv for helten (tenk "character creation")?

# Kampen
def rundeEN():
    while hero.is_alive() and thegnome.is_alive():
    # Helten sin tur
        angrip = input("Vil du angripe? (ja/nei) ")
        if angrip == "ja":
            angrip_metode = input("Vil du bruke våpen? (ja/nei) ")
            if angrip_metode == "ja":
                weapon_choice = hero.choose_weapon()
                weapon = weapons[weapon_choice]
                damage = weapon.attack()
                thegnome.hit(damage)
                print(f"The gnome took {damage} damage. The gnome's HP: {thegnome.hp}")
            else:
                print("Du brukte mana")
                thegnome.hit(random.randint(2, 20))
            print()
            print(f"Bossen har {thegnome.hp} HP igjen.")

        elif angrip == "nei":
            print("Du angriper ikke, og healer derfor!")
            print()

            hero.heal(10)  # Gjer gjerne denne delen random (tilfeldig heal)
        else:
            print("Du må skrive ja eller nei!")
            continue

        # Gjer det tilfeldig om bossen angrip, må ta seg ein pause, eller kanskje healer? Sistnemnte er ikkje implementert endå
    boss_angrip = random.choice([True, False])
    if boss_angrip:
        print("Bossen angriper!")
        hero.hit(10)  # Gjer gjerne denne delen random (tilfeldig skade)
        print(f"Du har {hero.hp} HP igjen.")

        print(f"Etter angrepet så har helten {hero.hp} HP og bossen {thegnome.hp} HP.")
    else:
        print(f"{thegnome.name} klarar ikkje gjere noko. Han forstår ikkje OOP og må ta seg ein pause.")

    print()
    
# Skriv ut resultatet av kampen (sidan me er ferdige med while-løkka, dvs ein av dei er døde)
print(rundeEN())
print("Runde 1 er over!")

def rundeTo():
    while hero.is_alive() and thegnome.is_alive():
    # Helten sin tur
        angrip = input("Vil du angripe? (ja/nei) ")
        if angrip == "ja":
            angrip_metode = input("Vil du bruke våpen? (ja/nei) ")
            if angrip_metode == "ja":
                weapon_choice = hero.choose_weapon()
                weapon = weapons[weapon_choice]
                damage = weapon.attack()
                thegnome.hit(damage)
                print(f"The gnome took {damage} damage. The gnome's HP: {thegnome.hp}")
            else:
                print("Du brukte mana")
                thegnome.hit(random.randint(2, 20))
            print()
            print(f"Bossen har {thegnome.hp} HP igjen.")

        elif angrip == "nei":
            print("Du angriper ikke, og healer derfor!")
            print()

            hero.heal(10)  # Gjer gjerne denne delen random (tilfeldig heal)
        else:
            print("Du må skrive ja eller nei!")
            continue

        # Gjer det tilfeldig om bossen angrip, må ta seg ein pause, eller kanskje healer? Sistnemnte er ikkje implementert endå
    boss_angrip = random.choice([True, False])
    if boss_angrip:
        print("Bossen angriper!")
        hero.hit(10)  # Gjer gjerne denne delen random (tilfeldig skade)
        print(f"Du har {hero.hp} HP igjen.")

        print(f"Etter angrepet så har helten {hero.hp} HP og bossen {thegnome.hp} HP.")
    else:
        print(f"{thegnome.name} klarar ikkje gjere noko. Han forstår ikkje OOP og må ta seg ein pause.")

    print()

    print(rundeTO())
    print("Runde 2 er over!")


Contune = input("Hvil du fortsette?(ja/nei)")
if Contune == "ja":
    hero.money = hero.money+ 1000
    hero.level = hero.level =+ 1
    print(rundeTo())
else: 
    print(f"Ok, dine stats: {self.hero}")




