import random

land = [{
    "Kina":{
        "hovedstad": "Beijing", 
        "antallInbyggere": 1500000000, 
        "naboland": ["mongolia", "Nord-Korea", "Nepal"]
        },
    "India":{
        "hovedstad": "New Delhi",
        "antallInbyggere": 1400000000,
        "naboland": ["Kina", "Pakistan", "Nepal"]
        },
    "USA":{
        "hovedstad": "Washington, D.C.", 
        "antallInbyggere": 330000000, 
        "naboland": ["Mexico", "Canada"] 
        },
    "Indonesia":{
        "hovedstad": "Jakarta", 
        "antallInbyggere": 240000000, 
        "naboland": ["Singapor", "Papua New-Guinea"] 
        },
    "Pakistan":{
        "hovedstad": "Islamabad", 
        "antallInbyggere": 230000000, 
        "naboland": ["India", "Afganistan", "Kina"]
        }
    }]

# Finn land med fleste innbyggjarar.
# Finn land med fleste naboland.
hoyestAntallInnbyggere = 0
landhHoyestInbyggertall = ""

for landInfo in land:
    antallInbyggere = landInfo["antallInbyggere"]
    if antallInbyggere > hoyestAntallInnbyggere:
        hoyestAntallInnbyggere = antallInbyggere
        landHoyestInbyggertall = landInfo["antallInbyggere"]

print(f"Landet med høyest antall innbyggere er {landHoyestInbyggertall} med {hoyestAntallInnbyggere} innbyggere.")


# Still tilfeldige spørsmål til brukaren. Form: "Kva er -- i --?" Eksempelvis, "Kva er hovudstaden i Norge?" eller "Kva er innbyggjartalet i Canada?" Korleis vil du handtere at det kan kome både tal og tekst som svar?
# def stille_tilfeldig_sporsmal(land):
#     tilfeldig_land = random.choice(land)
#     sporsmal_type = random.choice(["hovudstad", "antallInbyggere", "naboland"])
#     sporsmal = f"Kva er {sporsmal_type} i {tilfeldig_land['navn']}?"
#     svar = input(sporsmal)

#     if sporsmal_type == "antallInbyggere":
#         try:
#             svar = str(svar)
#             riktig_svar = tilfeldig_land["antallInbyggere"]
#         except ValueError:
#             print("Svaret må være et tall.")
#             return

#     elif sporsmal_type == "naboland":
#         riktig_svar = ", ".join(tilfeldig_land["naboland"])
#     else:
#         riktig_svar = tilfeldig_land["hovedstad"]

#     if svar.lower() == str(riktig_svar).lower():
#         print("Riktig svar!")
#     else:
#         print(f"Feil svar. Riktig svar er: {riktig_svar}")

# while True:
#     stille_tilfeldig_sporsmal(land)
#     fortsett = input("Vil du fortsette? (ja/nei): ")
#     if fortsett.lower() != "ja":
#         break