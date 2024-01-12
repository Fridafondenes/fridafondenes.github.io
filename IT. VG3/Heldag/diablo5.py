
import random
import os
import time
import grafikk

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Character:
    def __init__(self, name, level, hp, mana, money, weapons, color = "", grafikk = ""):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.money = money
        self.weapons = weapons
        self.color = color
        self.grafikk = grafikk

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}, Money: {self.money}"

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

    def level_up(self):
        self.level += 1
        if self.level > 10:
            print("Du runnet spillet!")

    def earn_money(self, amount):
        self.money + amount


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
hero = Character("Lana narnda", 1, 100, 100, 5000, weapons, bcolors.BOLD)

# Lagar bossen

thegnome = Character("The Gnome", 1, 100, 100, 0, weapons, bcolors.OKGREEN,grafikk.gnomLogo)
pedofilenissen = Character("Den pedofilenissen", 2, 200, 200,0, weapons, bcolors.FAIL)
greg_151 = Character("Greg 151", 101, 300, 300, 0, weapons, bcolors.OKBLUE)

# Lager liste til bosser
bosser = [thegnome, pedofilenissen, greg_151]


# Lager våpen
print()

# Gjer gjerne meir ut av delen over, der du kan sette meir avanserte verdier for helten og bossen
# Kanskje du til og med kan la spelaren setje verdiane sjølv for helten (tenk "character creation")?

# Kampen
for i in range(len(bosser)):
        print(f"All informasjon om helten: {hero}")
        print(grafikk.heltLogo)
        time.sleep(1.5)
        os.system("clear")

        print(f"{bosser[i].color}All informasjon om {bosser[i].name}: {bosser[i]} {bcolors.ENDC}")
        # print(grafikk.gnomLogo)
        # time.sleep(1.5)
        # os.system("clear")

        while hero.is_alive() and bosser[i].is_alive():
        # Helten sin tur
            angrip = input("Vil du angripe? (ja/nei) ")
            if angrip == "ja":
                angrip_metode = input("Vil du bruke våpen? (ja/nei) ")
                if angrip_metode == "ja":
                    weapon_choice = hero.choose_weapon()
                    weapon = weapons[weapon_choice]
                    damage = weapon.attack()
                    bosser[i].hit(damage)
                    print(f"{bosser[i].color}{bosser[i].name} took {damage} damage. {bosser[i].name}'s HP: {bosser[i].hp}{bcolors.ENDC}")
                else:
                    print("Du brukte mana")
                    bosser[i].hit(random.randint(2, 20))
                print()
                print(f"{bosser[i].color} {bosser[i].name} har {bosser[i].hp} HP igjen.{bcolors.ENDC}")

            elif angrip == "nei":
                print("Du angriper ikke, og healer derfor!")
                print()

                hero.heal(10)  # Gjer gjerne denne delen random (tilfeldig heal)
            else:
                print("Du må skrive ja eller nei!")
                continue

            # Gjer det tilfeldig om bossen angrip, må ta seg ein pause, eller kanskje healer? Sistnemnte er ikkje implementert endå
            boss_angrip = random.choice([True])
            if boss_angrip:
                print(f"{bosser[i].color} {bosser[i].name} angriper!{bcolors.ENDC}")
                hero.hit(random.randint(25,50 ))  # Gjer gjerne denne delen random (tilfeldig skade)
                print(f"Du har {hero.hp} HP igjen.")

                print(f"Etter angrepet så har helten {hero.hp} HP og bossen {bosser[i].hp} HP.")
                if hero.is_alive() == False:
                    print("Du tapete din dritt unge!")
                    print(grafikk.ferdigLogo)
                    break

            else:
                print(f"{bosser[i].color}{bosser[i].name} klarar ikkje gjere noko. Han forstår ikkje O OP og må ta seg ein pause.{bcolors.ENDC}")
        
        print()

        time.sleep(5)
        os.system("clear") 

        # Skriv ut resultatet av kampen (sidan me er ferdige med while-løkka, dvs ein av dei er døde)
        print(f"Runde {i+1} er over!") 

        contune = input("Vil du fortsette å spille?")

        if contune == "ja":
            hero.level_up()
            hero.earn_money(2000)

        else:
            print(f"Ok, dine stats: {hero}")
            print(grafikk.godtjobbetLogo)
            break


        







