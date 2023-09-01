
navn = input("Hva heter du? ")
antallOrd = int(input("Hvor mange ord vil du ha? "))
skryteListe = []

for antallOrd in range(antallOrd):
    skryteOrd = input("ord: ")
    skryteListe.append(skryteOrd)

print("Kjære " + navn + " du er:")

for element in skryteListe:
    print(element, end=", ")