handlekurv = {
 "melk": 17.90,
 "smør": 38.90,
 "kokt skinke": 23.10,
 "sjokolade": 11.90,
 "oppvaskmiddel": 24.40,
 "frossenpizza": 29.90
}

# a) 
laveste_pris_produkt = min(handlekurv, key=handlekurv.get)
laveste_pris = handlekurv[laveste_pris_produkt]

# b) 
hoyeste_pris_produkt = max(handlekurv, key=handlekurv.get)
hoyeste_pris = handlekurv[hoyeste_pris_produkt]

# c) Finn 
totalpris = sum(handlekurv.values())

print(f"Laveste pris: {laveste_pris_produkt} ({laveste_pris} kr)")
print(f"Høyeste pris: {hoyeste_pris_produkt} ({hoyeste_pris} kr)")
print(f"Totalpris: {totalpris} kr")