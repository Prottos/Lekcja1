# zadanie palindrom - ukryta symetria słowa
# program który sprawdzi, czy słowo lub wyrażenie jest palindromem

# metoda 1

# while True:
#     test = input("Podaj wyrażenie do sprawdzenia: ")
#     test = test.lower()
#     test = "".join(test.split())
#     if test == test[::-1]:
#         print('To palindrom')
#         break
#     else:
#         print('To nie palindrom')

# metoda 2

sentence = input("Podaj wyrażenie do sprawdzenia: ")
sentence = sentence.replace(" ","")                         # zamienia część wyrażenia na coś innego
sentence = sentence.lower()                                 # zamienia wyrażenie na małe litery

if sentence == sentence[::-1]:                              # sprawdzamy czy wyrażenie od końca jest takie samo jak od początku
    print("Wyrażenie jest palinromem.")
else:
    print("Wyrażenie nie jest palindromem.")



print(sentence)