import random
tiles = 27
loop = True

spiller1Eiendom = []
spiller2Eiendom = []

class Spillbrett:
    def __init__(self, runde):
        self.runde = runde
    
    eiendommer = [
    #start
    {"navn": "Parkveien", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 0, "eier": "ingen"},
    #Prøv Lykken
    {"navn": "Kirkeveien", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 1, "eier": "ingen"},
    #Inntektsskatt
    {"navn": "Oslo S.", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 2, "eier": "ingen"},
    {"navn": "Kongens Gate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 3, "eier": "ingen"},
    #Sjanse
    {"navn": "Prinsens Gate", "pris": 1000 , "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 4, "eier": "ingen"},
    {"navn": "Øvre Slottsgate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 5, "eier": "ingen"},
    #Fengsel
    {"navn": "Nedre Slottsgate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 6, "eier": "ingen"},
    {"navn": "Oslo Lysverker", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 7, "eier": "ingen"},
    {"navn": "Trondheimsveien", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 8, "eier": "ingen"},
    {"navn": "Nobels Gate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 9, "eier": "ingen"},
    {"navn": "Skjøyen stasjon", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 10, "eier": "ingen"},
    {"navn": "Grensen", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 11, "eier": "ingen"},
    #Prøv Lykken
    {"navn": "Gabels Gate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 12, "eier": "ingen"},
    {"navn": "Ringgata", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 13, "eier": "ingen"},
    #Gratis Parkering
    {"navn": "Bygdøy Allé", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 14, "eier": "ingen"},
    #Sjanse
    {"navn": "Skarpsno", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 15, "eier": "ingen"},
    {"navn": "Slemdal", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 16, "eier": "ingen"},
    {"navn": "Grorud stasjon", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 17, "eier": "ingen"},
    {"navn": "Karl Johans gate", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 18, "eier": "ingen"},
    {"navn": "Stortorget", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 19, "eier": "ingen"},
    {"navn": "Vannverket", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 20, "eier": "ingen"},
    {"navn": "Torggata", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 21, "eier": "ingen"},
    #Gå i fengsel
    {"navn": "Trosterudveien", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 22, "eier": "ingen"},
    {"navn": "Pilestredet", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 23, "eier": "ingen"},
    #Prøv Lykken
    {"navn": "Sinsen", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 24, "eier": "ingen"},
    {"navn": "Bryn stasjon", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 25, "eier": "ingen"},
    #Sjanse
    {"navn": "Ullevål Hageby", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 26, "eier": "ingen"},
    #Luksusskatt
    {"navn": "Rådhusplassen", "pris": 1000, "grunnleie": 100, "hus": 0, "hotell": 0, "hus_hotellpris": 50, "plassering": 27, "eier": "ingen"},
]

    def rundeBestemmelse(self):
        if self.runde == 1:
            spiller1.spillerRunde()
            self.runde += 1 
        elif self.runde == 2:
            spiller2.spillerRunde()
            self.runde += -1
    
    def byttehandel(self):
        if self.runde == 1:
            spiller1.forslag()
            #spiller2.motForslag()
            #spiller1.aksept()
    
    def leiebetaling(self):
        if self.runde == 1:
            spiller2.penger += spillbrett.eiendommer[spiller1.posisjon]["grunnleie"]
            spiller1.penger = spiller1.penger - spillbrett.eiendommer[spiller1.posisjon]["grunnleie"]
        if self.runde == 2:
            spiller1.penger += spillbrett.eiendommer[spiller2.posisjon]["grunnleie"]
            spiller2.penger = spiller2.penger - spillbrett.eiendommer[spiller2.posisjon]["grunnleie"]


class Spiller:
    def __init__(self, nummer, penger, posisjon):
        self.nummer = nummer
        self.penger = penger
        self.posisjon = posisjon
        self.eiendom = []
    
    def eiendomBehandling(self):
        plass = spillbrett.eiendommer[self.posisjon]
        if plass["eier"] == "ingen":
            if self.penger > plass["pris"]:
                x = input(f'Vil du kjøpe eiendommen? Den koster {plass["pris"]} penger. Du har {self.penger} penger.\ny/n\n')
                if x == "y":
                    self.penger = self.penger - plass["pris"]
                    plass["eier"] = self.nummer
                    self.eiendom.append(self.posisjon)
                    print(self.eiendom)
            elif self.penger < plass["pris"]:
                print("Du har ikke råd til denne eiendommen")
        if plass["eier"] != self.nummer:
            spillbrett.leiebetaling()
            print(f'Du betalte leie til den andre spilleren! Du betalte {plass["grunnleie"]}')

    def terningkasting(self):
        terningkast = random.randint(1,6)
        self.posisjon += terningkast
        if self.posisjon > tiles:
            self.posisjon = self.posisjon - tiles
        plass = spillbrett.eiendommer[self.posisjon]
        print(f'Du har landet på {plass["navn"]}')  
        self.eiendomBehandling()
    
    def forslag(self):
        self.seEiendommer()

    def seEiendommer(self):
        print("Her er dine eiendommer: ")
        i = 0
        for i in range(len(self.eiendom)):
            print(spillbrett.eiendommer[self.eiendom[i]]["navn"])

    #def motForslag(self):

    #def aksept(self):


    def spillerRunde(self):
        #global mulighet3
        #global trilletTerning
        mulighet3 = "Trille terning"
        trilletTerning = False
        loop = True
        while loop == True:
            x = input(f"Spiller {self.nummer} sin tur. \nHva vil du gjøre? \nSe eiendommer[1] \nByttehandel[2] \n{mulighet3}[3]\n")
            if x == "1":
                self.seEiendommer()
                y = input("Hva vil du gjøre? \nGå tilbake [1]")
            if x == "2":
                spillbrett.byttehandel()
            if x == "3":
                if trilletTerning == False:
                    self.terningkasting()
                    trilletTerning = True
                    mulighet3 = "Avslutt runden"
                else:
                    loop = False

spiller1 = Spiller(1, 10000, -1)
spiller2 = Spiller(2, 10000, -1)
spillbrett = Spillbrett(1)

x = "1"
#trilletTerning = False
#mulighet3 = "Trille terning"

#mulighet3 = "Trille terning"

while True:
    spillbrett.rundeBestemmelse()
