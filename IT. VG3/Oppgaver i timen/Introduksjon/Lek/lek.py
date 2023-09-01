
#Leik deg først med koden over (= endre, legg til, utforsk), og forsøk deretter å løyse oppgåvene under. Kopier oppgåveteksten inn i eigne filer.


# Variablar, datatypar og utskrift
fornavn = "Frida"
etternavn = "Fondenes"

print(fornavn, etternavn)

print(type(fornavn))

tallNrEin = 1
tallNrTo = 2.3

print(tallNrEin, tallNrTo)
print(type(tallNrEin))
print(type(tallNrTo))

print(tallNrEin + tallNrTo)

#print(fornavn + tallNrEin) # Dette fungerer ikkje, kvifor?
print(fornavn + str(tallNrEin)) # Dette fungerer, kvifor?

# Input frå brukar
# NB: input() returnerer alltid ein tekststreng
fornavn = input("Skriv inn fornavnet ditt: ")
print("Hei, " + fornavn)
alder = input("Skriv inn alderen din: ")
print("Du er " + alder + " år gammel")

# Konvertering av datatypar
alder = int(alder)

# Valgsetningar
if alder < 18:
    print("Du er under 18")
elif alder < 67:
    print("Du er i arbeidsfør alder")
else:
    print("Du er pensjonist")

# Lister
frukter = ["eple", "banan", "appelsin", "sitron"]
print(frukter)
print(frukter[0])

# Løkker
for frukt in frukter:
    print(frukt)



