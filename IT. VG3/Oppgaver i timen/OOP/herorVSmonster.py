class Hero:
    def __init__(self,navn, helse, skade):
        self.navn = navn
        self.helse = navn
        self.skade = skade

    def __str__(self):
        return f"Navn: {self.navn}, Helse: {self.helse}, Skade: {self.skade}"



class Monster:
    def __init__(self,navn, helse, skade):
        self.navn = navn
        self.helse = navn
        self.skade = skade

    def __str__(self):
        return f"Navn: {self.navn}, Helse: {self.helse}, Skade: {self.skade}"
        