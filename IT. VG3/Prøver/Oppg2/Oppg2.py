#A)

varer = {
    "Asus Zenbook GH215": 
    {
        "Varenavn":"Asus laptop",
        "Pris": "9999", 
        "Varelager": "10", 
        "Produktinfo": "En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD",
        "TekniskeEgenskaper":
        {
            "prossesor": "Intel Core i5-1135G7", 
            "grafikkort": "Intel Iris Xe Graphics", 
            "batterikapasitet": "Opptil 8 timer",
            "vekt": "1.8 kg"},
        "Farge":["grå", "svart", "blå"]
    },

    "Samsung Galaxy S22 GH67": 
    {
        "Varenavn":"Samgsun mobiltelefon",
        "Pris": 6999, 
        "Varelager": "20", 
        "Produktinfo": "En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera",
        "TekniskeEgenskaper":
        {
            "prossesor": "Qualcomm Snapdragon 888", 
            "grafikkort": "Adreno 660", 
            "batterikapasitet": "4500 mAh",
            "vekt": "200 g"},
        "Farge":["hvit", "svart", "grønn"]
    },

    "Apple Airpods Pro Gen 3 (2023)": 
    {
        "Varenavn":"Trådløse hodetelefoner",
        "Pris": 2599, 
        "Varelager": "30", 
        "Produktinfo": "Trådløse hodetelefoner med aktiv støydemping",
        "TekniskeEgenskaper":
        {
            "batterikapasitet": "Opptil 4.5 timer",
            "vekt": "5.4 g"},
        "Farge":["hvit", "gul", "spygrønn"]
    },
}


#B)

#Organiserer og printer
for vare, info in varer.items():
    print(f"Vare: {vare}")
    print(f"Vare navn: {info['Varenavn']}")
    print(f"Pris: {info['Pris']}")
    print(f"Varelager: {info['Varelager']}")
    print(f"Produktinfo: {info['Produktinfo']}")
    # print(f"Tekniske Egenskaper: {info['TekniskEgenskaper']}")
    print(f"Farge: {', '.join(info['Farge'])}")

    print()

#Infor vare id
def infoVare():
    vareID = input("Skriv inn en vareID: ")
    sjekkeVare = varer.get(vareID)

    if sjekkeVare is not None:
        print(f"Vi har vare :{vareID}, inne på lager!")
    else:
        print("Sorry vi har den varen inne på lager")

print(infoVare())

#Opptatere prisen
def opptaterPris():
    vare = input("Skriv inn en vare: ")
    varer.vare["pris"] = input("Skriv inn ny pris: ")

print(opptaterPris())