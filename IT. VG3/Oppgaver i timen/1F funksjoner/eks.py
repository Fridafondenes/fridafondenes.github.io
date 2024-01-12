
# def arealRektangel(lengde, bredde):
#   areal = lengde * bredde
#   print(f"Arealet av rektanglet er {areal}.")


def arealRektangel(lengde, bredde):
  return lengde * bredde

lengde = int(input("Skriv inn lengde: "))
bredde = int(input("Skriv inn bredde: "))

print(f"Arealet av et rektangel med sidelengder {lengde} og {bredde}, er: {arealRektangel(lengde,bredde)}.")
