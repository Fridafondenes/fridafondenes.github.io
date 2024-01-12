heltall = list(range(1,101))

antallVerdier = len(heltall)
print(f"Listen har {antallVerdier} verdier")

# delbar = int(input("Skriv et tall: "))

def deriverbar(listein, tallsjekk):
    for tall in listein:
        if tall % tallsjekk == 0:
            print(tall)

deriverbar(heltall,6)





