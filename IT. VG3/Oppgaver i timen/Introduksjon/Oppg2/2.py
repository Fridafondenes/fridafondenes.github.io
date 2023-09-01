#Oppgave 2: Lag et program som ber brukeren om å skrive inn et tall mellom 1 og 10, og så sjekker om tallet er likt, større eller mindre enn et tilfeldig valgt tall. Programmet skal skrive ut om brukeren gjettet riktig, for  høyt eller for lavt, og hva det tilfeldige tallet var. For å velge et tilfeldig tall, kan du bruke funksjonen random.randint(a, b) fra modulen random, som gir et heltall mellom a og b (inkludert). For eksempel, hvis brukeren skriver inn “5” og det tilfeldige tallet er “7”, skal programmet skrive ut “Du gjettet for lavt. Det tilfeldige tallet var 7.”

brukerTall = int(input("Skriv in et tilfeldig tall mellom 1 0g ti:"))

from random import randint
tilfeldig = randint(1, 10)


if brukerTall == tilfeldig:
    print("Yay, du gjettet riktig")
else:
    print("Du tokk feil prøv igjen")