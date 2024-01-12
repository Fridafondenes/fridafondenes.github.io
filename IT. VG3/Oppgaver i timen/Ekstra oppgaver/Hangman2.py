import random
import time
import os

print("Velkommen til Hangman!")
navn = input("Hva er navnet ditt? ")

time.sleep(1)

start = input(f"Vill du spille hangman {navn}? ")
if start == "ja":
    print("Ok la os starte!!!")
else: 
    print("Det var leit, en annengang!")
    

def hangman(word):
    display = "_" * len(word)
    poeng = 0
    maxPoeng = 5
    letters = list(word)
    forslagene = []

    while poeng < maxPoeng:
        forslag = input(f"Ordet: {display} Skriv ditt forslag: ")
       
        while len(forslag) == 0 or len(forslag) > 1:
            print("Du kan bare skrive en bokstav om gangen!")
            forslag = input(f"Ordet: {display} Skriv ditt forslag: ")
    
        if forslag in forslagene:
            print("OOOOObbbbbssss!!!, Du har allerede prøvd den bokstaven, du må prøve noe nytt!")
    

        if forslag in letters:
            letters.remove(forslag)
            index = word.find(forslag)
            display = display[:index] + forslag + display[index]

        else:
          forslagene.append(forslag)
          poeng += 1
          if poeng == 1:
              time.sleep(1)
              print('   _____ \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f"Feil svar: du har bare {maxPoeng - poeng}\n")

          elif poeng == 2:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f"Feil svar: du har bare {maxPoeng - poeng}\n")

          elif poeng == 3:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f"Feil svar: du har bare {maxPoeng - poeng}\n")

          elif poeng == 4:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f"Feil svar: du har bare {maxPoeng - poeng}\n")

          elif poeng == 5:
              time.sleep(1)
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |    /|\ \n'
                    '  |    / \ \n'
                    '__|__\n')
              print("Feil svar. Du har blitt hengt!!!\n")
              print(f"Ordet var: {word}")
    if display == word:
          print(f"Grattulerer! Du har funnet det riktige ordet \'{word}\' correctly!")
          


words_to_guess = [
    'hello'
]

# words_to_guess = [
#     'january', 'border', 'image', 'film', 'promise', 'kids',
#     'lungs', 'doll', 'rhyme', 'damage', 'plants', 'hello', 'world'
# ]

play = True
while play:
    word = random.choice(words_to_guess)
    hangman(word)
    play = play_again()



