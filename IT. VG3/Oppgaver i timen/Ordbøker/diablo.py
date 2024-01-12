import random

class Character:
    def __init__(self, name, level, hp, mana, money):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.money = money

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}, Wepon :{self.money}"
    
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_hp(self):
        return self.hp
    
    def get_mana(self):
        return self.mana
    
    def set_name(self, new_name):
        self.name = new_name

    def set_level(self, new_level):
        self.level = new_level

    def set_hp(self, new_hp):
        self.hp = new_hp

    def set_mana(self, new_mana):
        self.mana = new_mana

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



    def choose_weapon():
        print(f"Pengene dine :{self.money}")

        for i in range(len(self.weapons)):
            weapon = self.weapons[i]

        choice = input("Velg et våpen (1/2/3): ")
        while True:
            if choice in {'1', '2', '3'}:
                weaponChoice = int(choice) - 1
                weapon = self.weapons[weaponChoice]

            if self.hero.buy_weapon(weapon):
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

    # def choose_weapon(self):
    #     print(f"Dine penger: {self.money}):")

    #     for index, weapon in enumerate(self.weapons, start=1):
    #     print(f"{index}. {weapon}")

    #     while True:
    #         choice = input("Choose a weapon (1/2/3): ")
    #         if choice.isdigit() and 1 <= int(choice) <= len(self.weapons):
    #             weapon_index = int(choice) - 1
    #             weapon = self.weapons[weapon_index]

    #             if self.hero.buy_weapon(weapon):
    #                 print(f"You bought {weapon.name} for {weapon.cost} money.")
    #                 return weapon_index
    #             else:
    #                 print("Cannot afford this weapon. Choose another one.")
    #         else:
    #             print("Invalid choice. Please select 1, 2, or 3.")

# Lagar helten
hero = Character("Lana narnda", 1, 100, 100, 5000)
print(f"All informasjon om helten: {hero}") # Skriv ut informasjon om helten, kallar __str__-metoden
# Lagar bossen
thegnome = Character("The Gnome", 1, 100, 100, 0)
print(f"All informasjon om The Gnome: {thegnome}") # Skriv ut informasjon om bossen, kallar __str__-metoden
vampire = Character("The vampire", 1, 100, 100, 0)
print(f"All informasjon om Vampire: {vampire}") # Skriv ut informasjon om bossen, kallar __str__-metoden
# Lager våpen
weapons = [Weapon("Gun", 95, 1999), Weapon("Mase", 80, 1674), Weapon("Laser", 67, 1588)]
print()

# Gjer gjerne meir ut av delen over, der du kan sette meir avanserte verdier for helten og bossen
# Kanskje du til og med kan la spelaren setje verdiane sjølv for helten (tenk "character creation")?

# Kampen
while hero.is_alive() and thegnome.is_alive():
    # Helten sin tur
    angrip = input("Vil du angripe? (ja/nei) ")
    if angrip == "ja":
        angrip_metode = input("Vil du bruke våpen? (ja/nei) ")
        if angrip_metode == "ja":
            weapon_choice = hero.choose_weapon()
            weapon = self.weapons[weapon_choice]
            damage = weapon.attack()
            thegnome.hit(damage)
            print(f"The gnome took {damage} damage. The gnome's HP: {self.thegnome.hp}")
        else:
            print("Invalid choice. Using default attack.")
            thegnome.hit(random.randint(2, 20)) 
        print()
        print(f"Bossen har {thegnome.get_hp()} HP igjen.")

    elif angrip == "nei":
        print("Du angriper ikkje, og healer derfor!")
        print()

        hero.heal(10) # Gjer gjerne denne delen random (tilfeldig heal)
    else:
        print("Du må skrive ja eller nei!")
        continue
    
    # Gjer det tilfeldig om bossen angrip, må ta seg ein pause, eller kanskje healer? Sistnemnte er ikkje implementert endå
    boss_angrip = random.choice([True, False])
    if boss_angrip:
        print("Bossen angriper!")
        hero.hit(10) # Gjer gjerne denne delen random (tilfeldig skade)
        print(f"Du har {hero.get_hp()} HP igjen.")

        print(f"Etter angrepet så har helten {hero.get_hp()} HP og bossen {boss.get_hp()} HP.")
    else:
        print(f"{boss.get_name()} klarar ikkje gjere noko. Han forstår ikkje OOP og må ta seg ein pause.")
    
    print()

# Skriv ut resultatet av kampen (sidan me er ferdige med while-løkka, dvs ein av dei er døde)
print()
print("Kampen er over!")
print(f"Etter kampen så har helten {hero.get_hp()} HP og bossen {boss.get_hp()} HP.")