import math as m

x = int(input("Skriv radiusen til sirkelen: "))

def arealSirkel():
    areal = m.pi * x**2
    return areal

areal = arealSirkel()
print(areal)