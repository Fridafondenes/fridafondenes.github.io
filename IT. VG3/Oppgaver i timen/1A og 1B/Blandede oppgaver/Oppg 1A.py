# - - - - - - -
# Oppgave 1
# - - - - - - -
# Figuren nedenfor viser en bane og en syklist. Syklisten har gjennomsnittsfart 50 km/h. Lag et program som

# a beregner avstanden rundt banen, altså banens lengde
import math as m

lengde = 100 * 2
svingX2 = (2 * m.pi) * 31.83

strekning = int(lengde + svingX2 * 2)

print("Banens lengde er " + str(strekning) + " meter")


# b beregner syklistens gjennomsnittsfart i m/s
kmh = int(input("Skriv inn gjennomsnittsfarten i km/t: "))
ms = kmh / 3.6

print("Gjenomsnittsfarten i m/s er " + str(ms))


# c beregner tiden syklisten bruker på 10 runder
tid = (strekning * ms)/60
print("Han bruker " + str(tid) + " minutter på 1 runde")

tid10runder = (strekning * 10 * ms)/60
print("Han bruker " + str(tid10runder) + " minutter på ti runder rundt banaen!")
