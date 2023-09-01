# 3.3
# Du har følgende liste med navn: navn = ["Kari", "Arne", "Hanne", "Julie", "Maria", "Christine"]
# Iterer gjennom listen og finn og returner kun "Maria". For hvert navn som ikke er maria print "ikke Maria"

navn = ["Kari", "Arne", "Hanne", "Julie", "Maria", "Christine"]

# while navn[i] != "Maria":
#     print("ikke Maria")

for i in navn:
    if i !="Maria":
        print("ikke Maria")
    else:
        print("det er Maria")
