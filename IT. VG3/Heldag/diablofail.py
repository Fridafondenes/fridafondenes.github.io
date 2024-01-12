
import random
import os
import time
import grafikk

class Character:
    def __init__(self, name, level, hp, mana, money, weapon):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.money = money
        self.weapon = weapon

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}, Money: {self.money}"

    def choose_weapon(self):
        print(f"Available weapons (Your Money: {self.hero.money}):")
        for index, weapon in enumerate(self.weapons, start=1):
            print(f"{index}. {weapon}")

        while True:
            choice = input("Choose a weapon (1/2/3): ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.weapons):
                weapon_index = int(choice) - 1
                weapon = self.weapons[weapon_index]

                if self.hero.buy_weapon(weapon):
                    print(f"You bought {weapon.name} for {weapon.cost} money.")
                    return weapon_index
                else:
                    print("Cannot afford this weapon. Choose another one.")
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

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

    def buy_weapon(self, weapon):
        if self.money >= weapon.cost:
            self.money -= weapon.cost
            return True
        else:
            print("Not enough money to buy this weapon.")
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

hero = Character("Jo Bjørnar den objektorienterte", 1, 100, 100, money=5000)  
thegnome = Character("The gnome", 1, 100, 100)
vampire = Character("The vampire", 1, 100, 100)
weapons = [Weapon("Gun", 95, 1999), Weapon("Mase", 80, 1674), Weapon("Laser", 67, 1588)]


class Game:
    

    def battle(self):
        
        print()

        #start logo
        print(grafikk.startLogo)
        time.sleep(1)
        os.system("clear")

        #helt logo
        print(f"\n All information about the hero: {self.hero}")
        print(gragikk.heltLogo)
        time.sleep(1)
        os.system("clear")

        #gnom logo
        print(f"\n All information about the the gnome: {self.thegnome}\n")
        print(grafikk.gnomLogo)
        time.sleep(1)
        os.system("clear")

        

        while self.hero.is_alive() and self.thegnome.is_alive():
            # Hero's turn
            print(f"\nYour Money: {self.hero.money}")
            attack_choice = input("Do you want to attack? (yes/no) ")
            if attack_choice.lower() == "yes":
                attack_method = input("Do you want to use a weapon? (yes/no) ")
                if attack_method.lower() == "yes":
                    weapon_choice = self.choose_weapon()
                    weapon = self.weapons[weapon_choice]
                    damage = weapon.attack()
                    self.thegnome.hit(damage)
                    print(f"The gnome took {damage} damage. The gnome's HP: {self.thegnome.hp}")
                else:
                    print("Invalid choice. Using default attack.")

            else:
                print("You choose not to attack and heal instead.")
                self.hero.heal(random.randint(1, 20))
            

            # thegnome's turn
            thegnome_attacks = random.choice([True, False])
            if thegnome_attacks:
                thegnome_damage = random.randint(5, 20)
                self.hero.hit(thegnome_damage)
                print(f"The gnome attacks and deals {thegnome_damage} damage. Hero's HP: {self.hero.hp}")
            else:
                print("The genome takes a break and does nothing.")

        # Battle result
        print("\nBattle is over!")
        print(f"Hero's HP: {self.hero.hp}, The genome's HP: {self.thegnome.hp}")
        if self.hero.is_alive():
            print("Hero wins!")
        else:
            print("The gnome wins!")

    while self.hero is alive(): 
        Continue = input("Do you want to continue")
        if Continue == "yes":


# Create the game and start the battle
game = Game()
game.battle()

