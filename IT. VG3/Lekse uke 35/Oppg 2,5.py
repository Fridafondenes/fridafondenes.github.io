# 2.5
# Stein-saks-papir!

# v1
# Skriv et program som tar inn et tilfeldig tall mellom 1-3 (1 = stein, 2 = saks, 3 = papir) fra random-biblioteket, og 
# enten stein('st'), saks('sa') eller papir('p') fra bruker. Sammenlign valgene og sjekk hvem som vant ut fra følgende regler:
# Stein vs saks: stein vinner
# Stein vs papir: papir vinner
# Papir vs saks: saks vinner
# Ved samme valg er det uavgjort.
# Bruk if-elif-else for å skrive programmet. Skriv resultatet ut til konsoll.

# v2
# Utvid spelet over til å inkludere fylgjande moglegheit:
# Spelaren skal få spele stein-saks-papir heilt fram til ein av partane har vunne ved å få ein gitt poengsum, til dømes 10. Kvar gong ein av partane vinn så får ein 1 poeng.


brukerPoeng = 0
dataPoeng = 0

vunnet = False

import random

while vunnet == False:
    valgBruker = input("Skriv inn stein , saks eller papir: ")

    valgData = random.choice(["stein","saks","papir"])
    print(valgData)

    if valgBruker == valgData:
        print("Uavgjort")
    elif (valgBruker == 'stein' and valgData == 'saks') or \
        (valgBruker == 'saks' and valgData == 'papir') or \
        (valgBruker == 'papir' and valgData == 'stein'):
        
        print("Du vant")
        brukerPoeng += 1
    else:
        print("Du tapte")
        dataPoeng += 1

    if brukerPoeng > 2 or dataPoeng > 2:
        vunnet = True

print("Din poensum er " + str(brukerPoeng) + " og datamaskinen sin er " + str(dataPoeng))


