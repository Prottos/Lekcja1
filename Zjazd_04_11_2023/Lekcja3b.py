# funkcje - zgrupowany program kodu odpowiadający za pewną funkcjonalność (mozna używać go wielokrotnie)
'''
def przywitanie():                                      # komenda def - służy do definiowania funkcji
    print("Witam.")                                     # działanie funkcji zapisujemy w kolejnych liniach, każda od tabulatora

def przywitanie_2(imie, wiek):                          # można wprowadzić doatkowe argumenty do definiowania funkcji, tzw zmienne lokalne
    print(f"Cześć {imie}, masz {wiek} lat.")

def dodawanie():
    pass

print("Start programu.")
przywitanie()
przywitanie_2("Patryk",26)                              # używając zdefiniowanej funkcji z argumentami wprowadzamy je podczas wykorzystania fukncji w nawias
# print(imie)                                           # zmienne są lokalne tylko w zdefiniowanej funkcji, nie zadziałają poza nią
'''
# funkcja rozpoznaje czy facet czy kobieta i jeśli pełnoletni to napisz: Dzień dobry pany/pani, jeśli młody napiszmy: Cześć "imię"


"""
def przywitanie_zaawansowane(imie,wiek):
    if wiek >= 18:
        if imie[-1] == "a":
            print(f"Witam panią {imie}.")
        else:
            print(f"Witam pana {imie}.")
    else:
        print(f"Cześć {imie}, masz {wiek} lat.")
a = input("Podaj imię: ")
b = int(input("Podaj wiek: "))
przywitanie_zaawansowane(a,b)
"""

import random

def dodawanie(a,b):
    return a + b                                        # funkcja zwraca wynik działania

for i in range(3, dodawanie(3,6),2):
    print(i)

tmp_list = [5, 6, 12, 26, 38]

for i in range(dodawanie(tmp_list[2], random.randint(3,30))):
    print(i)

print(dodawanie(tmp_list[3], 5) + 6)