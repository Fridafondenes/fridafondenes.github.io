
# fødselsNummer = input("Hva er fødselsnummeret ditt? Bruk mellomrom mellom tallene: ")
# nummer = fødselsNummer.split()

# nummer.append(fødselsNummer)

# #henter forskjellige verdier fra listen og organiserer
# def fødeselDag():
#     dato = nummer[0] + nummer[1]
#     månde = nummer[2] + nummer[3]
#     årstall = nummer[4] + nummer[5]
#     print(f"{dato}. {månde}. {årstall}")

# print(fødeselDag()) 

def main():
    fødselsnummer = str(input("Skriv inn fødsellsnummert ditt:")) # input("Skriv inn fødselsnummer (11 siffer): ")

    # Sjekk om fødselsnummeret er korrekt
    if len(fødselsnummer) != 11:
        print("Feil format på fødselsnummer. Skal være 11 siffer.")
        return

    # Fjern 0 før dagen om nødvendig
    dag = fødselsnummer[:2].lstrip('0')
    måned = fødselsnummer[2:4]
    århundre = kull()
    individnummer = fødselsnummer[8:9]
    # Konverter måned til tekst
    månedsnavn = konverter_måned_til_tekst(måned)

    # Finn kjønn
    kjønn = "kvinne" if int(individnummer) % 2 == 0 else "mann"

    # Skriv ut informasjonen
    print(f"Fødselsdatoen er {dag}. {månedsnavn}. {år}, ({kjønn}) med utgangspunkt i {fødselsnummer} som inndata.")

def kull():
    if fødselsnummer[4:6]

def konverter_måned_til_tekst(måned):
    måneder = {
        "01": "januar",
        "02": "februar",
        "03": "mars",
        "04": "april",
        "05": "mai",
        "06": "juni",
        "07": "juli",
        "08": "august",
        "09": "september",
        "10": "oktober",
        "11": "november",
        "12": "desember"
    }
    return måneder.get(måned, "ukjent")

print(main())
