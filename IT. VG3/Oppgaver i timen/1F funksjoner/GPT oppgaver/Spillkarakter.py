# Oppgave: Lag en "Spillkarakter Generator"

# Beskrivelse:
# Du skal lage en Python-applikasjon som genererer tilfeldige spillkarakterer ved hjelp av funksjoner. 
# Hver spillkarakter skal ha egenskaper som navn, rase, klasse og helsepoeng. 
# Du skal også kunne tilpasse antall karakterer som genereres.

# 1) Lag en funksjon generer_navn() som returnerer et tilfeldig navn for spillkarakteren. Du kan bruke lister med fornavn og etternavn for variasjon.
import random

def generer_navn():
    navn = ["Ola", "Kari", "Per", "Maja", "Erik"]
    etternavn = ["Hansen", "Olsen", "Andersen", "Larsen", "Pedersen"]

    tilfeldigNavn = random.choice(navn)
    tilfeldigEtternavn = random.choice(etternavn)

    fullNavn = tilfeldigNavn + " " + tilfeldigEtternavn
    return fullNavn

# 2) Lag en funksjon generer_rase() som returnerer en tilfeldig rase for spillkarakteren. Eksempler på raser kan være menneske, alv, dverg, ork, osv. Lag en liste med ulike raser.


def generer_rase():
    raser = ["Alv", "Troll", "Menneske", "Drage", "Fe", "Dverg"]
    tilfeladigRase = random.choice(raser)
    return tilfeladigRase

# # 3) Lag en funksjon generer_klasse() som returnerer en tilfeldig klasse for spillkarakteren. Eksempler på klasser kan være kriger, trollmann, tyv, bueskytter, osv. Lag en liste med ulike klasser.


def generer_klasse():
    klasse = ["Tyv", "Kriger", "Beskytter", "Trollmann", "hjelper"]
    tilfeldigKlasse = random.choice(klasse)
    return tilfeldigKlasse

# # 4) Lag en funksjon generer_helsepoeng() som returnerer et tilfeldig antall helsepoeng for spillkarakteren. Helsepoengene kan være en tilfeldig verdi innenfor et gitt område (for eksempel mellom 50 og 100).


import random

def generer_helsepoeng():
    helsepoeng = random.randint(1,100)
    return helsepoeng


print(generer_navn())
print(generer_rase())
print(generer_klasse())
print(generer_helsepoeng())
# # 5) Lag en hovedfunksjon som lar brukeren angi hvor mange spillkarakterer de ønsker å generere. Deretter skal programmet generere og vise informasjon om hver karakter ved hjelp av de tidligere definerte funksjonene.

# # Ekstra utfordring:
# # Legg til flere egenskaper for spillkarakterene, for eksempel styrke, intelligens, og magiske evner. Lag funksjoner som genererer verdier for disse egenskapene.
# # Dette prosjektet vil gi deg god trening i å bruke funksjoner, lister og tilfeldige tall i Python, samtidig som det lar deg utforske kreativiteten din ved å generere morsomme og varierte spillkarakterer.