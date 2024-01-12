personer = {
 "Sophie": 18, "Noah": 18, "Olivia": 29, "Oscar": 21,
 "Oliver": 25, "Sofia": 27, "Ella": 23, "Leah": 21,
 "Lucas": 23, "Maya": 25, "Isaac": 29, "Axel": 27,
 "Frida": 23, "Emil": 26, "Emma": 23, "Ingrid": 18,
 "Phillip": 25, "Jacob": 24, "Nora": 21, "William": 22
} 

# a) Det er flere av personene i ordboka som har samme alder. Finn alle unike aldre i ordboka.

unike_alder = []

for alder in personer.values():
    if alder not in unike_alder:
        unike_alder.append(alder)

print(unike_alder)

# b) Lag en ny ordbok, unikealdre, som inneholder én av personene for 
# hver unike alder. Det har ingenting å si hvilke personer du velger, men 
# det skal skje automatisk.

unike_alder = {}

for navn, alder in personer.items():
    if alder not in unike_alder:
        unike_alder[alder] = navn

print(unike_alder)
