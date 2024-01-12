# def siHei():
#   print("Hei")

# siHei()
# siHei()


import random

def tilfeldigHilsen():
    hilsener = ["Hei", "Hallo", "God dag"]
    tilfeldig_hilsen = random.choice(hilsener)
    return tilfeldig_hilsen

# Eksempel på bruk:
hilsen = tilfeldigHilsen()
print(hilsen)