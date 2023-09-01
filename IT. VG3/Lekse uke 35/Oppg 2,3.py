# 2.3

# Et busselskap ønsker å automatisk beregne pris på billetter ut fra aldersinformasjon og reiserute hentet inn fra kunden. Priser for standard billetter:
# Rute 1 (By - Sjø): 150,- Rute 2 (Sjø - Fjell): 250,- Rute 3 (Fjell - By): 50,-
# Aldersrabatter: 0-2: Gratis 2-16: -50 % 16-65: Standard pris 65+: -70 %

# Spør bruker om reisestrekning:
# 1 = By-Sjø
# 2 = Sjø - Fjell
# 3 = Fjell - By
# Initier variabel "pris" til 0
# Initier variabel "totalsum" til 0
# Spør bruker om alder
# Skriv oppgitt alder ut til bruker
# Oppdater "pris": beregn rabattert pris ut fra alder og rute
# Skriv ut standard pris, rabatt og sluttpris til bruker. Hvis brukeren ikke får rabatt skal dette også skrives ut.



rute1 = "by - sjø" 
rute2 = "sjø - fjell"
rute3 = "fjell - by"

print(rute1,rute2,rute3)
rute = input("Hvilken rute skal du i dag? ")
alder = input("Hvor gammel er du?")


def regnUtPris(age, route):
    rutePris = {
        "rute 1": 150,
        "rrute 2": 250,
        "rute 3": 50
    }
    
    if alder <= 2:
        alder = "0-2"
        avslag = 0.0
    elif age <= 16:
        aldere = "2-16"
        avslag = 0.5
    elif age <= 65:
        aldere = "16-65"
        avslag = 1.0
    else:
        aldere = "65+"
        avslag = 0.3
    
    avslagsFaktor = avslag[aldere]
    route_price = standard_prices[route]
    
    return avslagsFaktor * rutePris

def main():
    routes = {
        1: "Rute 1 (By - Sjø)",
        2: "Rute 2 (Sjø - Fjell)",
        3: "Rute 3 (Fjell - By)"
    }
    
    print("Velkommen til busselskapet!")
    route_choice = int(input("Velg reisestrekning:\n1 = By-Sjø\n2 = Sjø - Fjell\n3 = Fjell - By\n"))
    
    if route_choice not in routes:
        print("Ugyldig valg av reisestrekning.")
        return
    
    route = routes[route_choice]
    age = int(input("Oppgi din alder: "))
    
    print(f"\nValgt reisestrekning: {route}")
    print(f"Oppgitt alder: {age} år")
    
    ticket_price = calculate_ticket_price(age, route)
    
    print("\nPrisinformasjon:")
    print(f"Standard pris: {route_price} kr")
    print(f"Rabatt: {discount_factor*100}%")
    print(f"Sluttpris: {ticket_price} kr")

if __name__ == "__main__":
    main()
