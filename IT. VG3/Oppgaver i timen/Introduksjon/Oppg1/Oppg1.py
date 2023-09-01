
#Oppgave 1: Lag et program som ber brukeren om å skrive inn navnet sitt og fødselsåret sitt, og så skriver ut en hilsen som sier “Hei, [navn]! Du er [alder] år gammel.” For eksempel, hvis brukeren skriver inn “Ola” og “1982”, skal programmet skrive ut “Hei, Ola! Du er 42 år gammel.”

fornavn = input("Skriv fornavnet ditt:")
print("Hei, " + fornavn)


årstall = input("Skriv in fødselsåret ditt:")
alder = 2023 - int(årstall)
print(" Du er " + str(alder) +  "år gammel")