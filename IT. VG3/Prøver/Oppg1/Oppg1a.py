# #https://www.c-sharpcorner.com/article/how-to-add-frame-in-tkinter-in-python/

# from tkinter import * 
# a= Tk()
# a.geometry("400x400")
# frame2=Frame(a,bg = "black",width=input("Skriv in antall pixler i bredden: "),height=input("Skriv inn antall piler i høyden: "),
# cursor = "target",relief=FLAT).grid(padx = 100, pady = 100)
# a.mainloop()

bredde = int(input("Skriv inn bredden i pixler: "))
høyde = int(input("Skriv inn høyden i pixler: "))

if høyde > bredde:
    print("Portrait")
elif høyde < bredde:
    print("Landscape")
elif høyde == bredde:
    print("Kvadrat")
else:
    print("Den er verken Landscape eller Portrait")
    
    