class Person:
    def __init__(self, fornavn, etternavn, fødselsår):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = fødselsår

    def __str__(self):
        return f"Fornavn: {self.fornavn}, Etternavn:{self.etternavn}, Fødselsår:{self.fødselsår}"


frida = Person("Frida","Fondenes", "2005")
print(frida)

# class Person:
#     def __init__(self, fornavn, etternavn, fødselsår):
#         self.fornavn = fornavn
#         self.etternavn = etternavn
#         self.fødselsår = fødselsår

#     def __str__(self):
#         return f"Fornavn: {self.fornavn}, Etternavn: {self.etternavn}, Fødselsår: {self.fødselsår}"

# frida = Person("Frida", "Fondenes", "2005")
# print(frida)



