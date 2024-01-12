# - - - - - -
# Oppgave 2
# - - - - - - 
# Lag en funksjon som tar inn navn og alder. Hvis alder er under 30, skal funksjonen skrive ut «Hei, navn, du er ung!». Hvis ikke alder er under 30, skal funksjonen skrive ut «Du er gammel, navn!». 
# Funksjonen skal testes med Lise på 78 og Janne på 28.

navn = input("Hva heter du? ")
alder = int(input("Hvor gammel er du? "))

def navnAlder(navn, alder):

    if alder < 30:
        print(f"Hei, {navn}, du er ung!")
    else:
        print(f"Du er gammel, {navn} !")

navnAlder(navn, alder)

# navnAlder("Lise", 78)
# navnAlder("Anne", 28)

