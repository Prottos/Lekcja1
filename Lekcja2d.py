# program losuje 1-100
# uzytkownik zgaduje, a program mówi czy za wysoka, za niska liczba czy odgadnięta

import random

number = random.randrange(1,100)

while True:
    guess = int(input("Zgadnij liczbę od 1 do 100. "))
    if guess - number < -10:
        print("Liczba o wiele za niska, spróbuj ponownie.")
    elif 0 > guess - number > -10:
        print("Liczba nieco za niska, spróbuj ponownie.")
    elif 0 < guess - number < 10:
        print("Liczba nieco za wysoka, spróbuj ponownie.")
    elif guess - number > 10:
        print("Liczba o wiele za wysoka, spróbuj ponownie.")
    else:
        print("Brawo, zgadłeś!")
        break

print("Koniec zadania.")