def choose_weapon(self):
    print(f"Dine penger: {self.money}):")

    for weapon in self.weapons:
        print(f"{weapon}")

    while True:
        choice = input("Choose a weapon (1/2/3): ")

        if choice.isdigit() and 1 <= int(choice) <= len(self.weapons):
            weapon = self.weapons[int(choice) - 1]

            if self.hero.buy_weapon(weapon):
                print(f"You bought {weapon.name} for {weapon.cost} money.")
                return self.weapons.index(weapon)
            else:
                print("Cannot afford this weapon. Choose another one.")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

print(choose_weapon())