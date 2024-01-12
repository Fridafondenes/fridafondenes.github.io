from IMDB import Cinemagoer

def fjernVerdier(filmdatabase, problematiske_verdier):
    renset_database = {}
    for film, runtime in filmdatabase.items():
        if runtime not in problematiske_verdier:
            renset_database[film] = runtime
    return renset_database

movie_runtimes = {
    "The Batman": 0,
    "No Time To Die": 163,
    "Dune": 155,
    "Avengers: Endgame": 181,
    "The Godfather": "x",
    "The Lord of the Rings: The Return of the King": 201,
    "Seven Samurai": 207,
    "Gone With The Wind": 238,
    "Lawrence of Arabia": 227,
    "The Clock": 1440
}

problematiske_verdier = [0, "x"]

renset_filmdatabase = fjernVerdier(movie_runtimes, problematiske_verdier)

for film, runtime in renset_filmdatabase.items():
    print(film, runtime)


def søk_på_film(film_tittel):
    # Send en HTTP-forespørsel til IMDBs søkeside
    url = f"https://www.imdb.com/find?q={film_tittel}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Analyser søkeresultatene og velg riktig film
    # Her kan du legge til logikk for å velge riktig film basert på tittel og årstall

    # Hent informasjon om den valgte filmen fra dens IMDB-side
    film_url = "URL for den valgte filmen"
    response = requests.get(film_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Analyser HTML-siden og hent nødvendig informasjon
    kjøretid = "Kjøretid fra HTML-siden"
    vurdering = "Vurdering fra HTML-siden"

    # Oppdater ordboken med den nye informasjonen
    movie_runtimes[film_tittel] = kjøretid
    # Du kan også oppdatere andre felt i ordboken, for eksempel vurdering

# Eksempel på bruk av søk_på_film-funksjonen
søk_på_film("The Batman")

# Skriv ut den oppdaterte ordboken
print(movie_runtimes)