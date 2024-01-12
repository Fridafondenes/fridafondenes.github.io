def tellTegn(tekst):
    antallTegn = 0
    for tegn in tekst:
        antallTegn += 1
    return antallTegn

def midtersteTegn(tekst):
    lengde = len(tekst)
    if lengde % 2 == 1:  # Oddetall antall tegn
        midten = lengde // 2
        return tekst[midten]
    else:  # Partall antall tegn
        midten_1 = lengde // 2 - 1
        midten_2 = lengde // 2
        return tekst[midten_1:midten_2 + 1]

def Palindrom(tekst):
    tekst = tekst.lower().replace(" ", "")  # Fjern mellomrom og gjør alt til små bokstaver
    return tekst == tekst[::-1]  # Sjekk om teksten er lik seg selv baklengs

tekst = "anna"
print(tellTegn(tekst))
print(midtersteTegn(tekst))
print(Palindrom(tekst))
