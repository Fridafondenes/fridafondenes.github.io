#Oppgave 3: Lag et program som ber brukeren om å skrive inn navnet på en frukt, og så skriver ut om frukten er søt eller sur. Programmet skal ha en liste over søte frukter og en liste over sure frukter, og bruke valgsetninger til å sammenligne brukerens input med listene. Hvis frukten ikke finnes i noen av listene, skal programmet skrive ut at det ikke vet om frukten er søt eller sur. For eksempel, hvis brukeren skriver inn “eple”, skal programmet skrive ut “Eple er en søt frukt.” Hvis brukeren skriver inn “sitron”, skal programmet skrive ut “Sitron er en sur frukt.” Hvis brukeren skriver inn “banan”, skal programmet skrive ut “Jeg vet ikke om banan er søt eller sur.”


# Lister
sureFrukter = ["sitron", "lime", "apelsin", "druer"]
søteFruket = ["jordbær", "banan", "pære", "eple"]

valgAvFrukt = input("Skriv inn en type frukt:")

if valgAvFrukt in sureFrukter:
    print("Frukten du skrev er en sur frukt")
elif valgAvFrukt in søteFruket:
    print("Frukten du valgte er søt")
else:
    print("Jeg vet ikke om frukten er søt eller sur")
