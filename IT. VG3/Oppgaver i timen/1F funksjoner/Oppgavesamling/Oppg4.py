# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# a) Lag en funksjon som trekker vinnertall (altså syv tall pluss ett tilleggstall). 
# Tallene er fra 1–34, og ingen tall brukes to ganger.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
import random

def trekke_vinnertall():
    # Opprett en liste med tallene fra 1 til 34
    tall = list(range(1, 35))

    # Trekker syv hovedtall uten duplikater
    hovedtall = random.sample(tall, 7)

    # Trekker ett tilleggstall uten å inkludere det i hovedtallene
    tilleggstall = random.choice([t for t in tall if t not in hovedtall])

    # Sorterer tallene i stigende rekkefølge
    vinnertall = sorted(hovedtall) + [tilleggstall]

    return vinnertall

# Kjør funksjonen for å generere vinnertall
vinnertall = trekke_vinnertall()
print("Vinnertall:", vinnertall)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# b) Lag en funksjon som tar inn en lottokupong (altså tallene en person har valgt 
# ut) og sjekker hvor mange riktige personen har fått (sammenlign med vinnertallene
#  du fant i a).
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def sjekk_lottokupong(kupong, vinnertall):
    # Sjekk hvor mange av hovedtallene på kupongen som er riktige
    antall_riktige_hovedtall = len(set(kupong).intersection(set(vinnertall[:-1])))

    # Sjekk om tilleggstallet på kupongen er riktig
    riktig_tilleggstall = kupong[-1] == vinnertall[-1]

    if antall_riktige_hovedtall == 7 and riktig_tilleggstall:
        return "Gratulerer! Du har alle riktige tall og tilleggstall."
    elif antall_riktige_hovedtall == 7:
        return "Gratulerer! Du har alle riktige hovedtall, men ikke tilleggstallet."
    else:
        return f"Du har {antall_riktige_hovedtall} riktige hovedtall og tilleggstall er {'riktig' if riktig_tilleggstall else 'feil'}."

kupong = [5, 10, 15, 20, 25, 30, 35, 7]  # Eksempel på lottokupong

resultat = sjekk_lottokupong(kupong, vinnertall)
print(resultat)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# c) Regn ut hvor mange mulige kuponger som kan lages. Her holder det å tenke på 7 
# rette.Hvor sannsynlig er det å få syv rette hvis du bare leverer én lottokupong?
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
import math

def antall_mulige_kuponger(totalt_antall_tall, antall_trekkes):
    # Beregn binomialkoeffisienten
    antall_kombinasjoner = math.comb(totalt_antall_tall, antall_trekkes)
    return antall_kombinasjoner

totalt_antall_tall = 34
antall_trekkes = 7

mulige_kuponger = antall_mulige_kuponger(totalt_antall_tall, antall_trekkes)
print(f"Antall mulige kuponger for 7 rette: {mulige_kuponger}")


