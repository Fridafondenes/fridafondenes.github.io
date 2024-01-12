byer = {
    "Oslo": 1043168,
    "Bergen": 265470,
    "Stavanger/sandnes": 229911,
    "Trondheim": 191771,
    "Fredrikstad/Sarpsborg": 117663,
    "Drammen": 110236,
    "Porsgrunn/Skien": 94102,
    "Kristiansand": 64913,
    "Ålesund": 54399,
    "Tønsberg":53818
}

# Funksjon for å finne byer med innbyggertall innenfor en gitt grense
def finn_byer_mellom_grenser(min_grense, maks_grense):
    kvalifiserte_byer = []
    for by, innbyggertall in byer.items():
        if min_grense <= innbyggertall <= maks_grense:
            kvalifiserte_byer.append(by)
    return kvalifiserte_byer

# Spør brukeren om å angi en nedre og øvre grense
min_grense = int(input("Skriv inn nedre grense for innbyggertall: "))
maks_grense = int(input("Skriv inn øvre grense for innbyggertall: "))

# Finn og skriv ut byer som oppfyller kriteriene
kvalifiserte_byer = finn_byer_mellom_grenser(min_grense, maks_grense)

if len(kvalifiserte_byer) > 0:
    print("Byer med innbyggertall mellom", min_grense, "og", maks_grense, "er:")
    for by in kvalifiserte_byer:
        print(by)
else:
    print("Ingen byer oppfyller kriteriene.")




