# # pętla 'while'

# x = 5

# while x > 0:                # dajemy dwukropek jak przy 'if'
#     print("Siema")          # wykonuje kod we wcięciu tak jak 'if'
# #    x = x - 1              # 'while' wykonuje działania, póki warunek jest spełniony. W kodzie trzeba umieścić warunek, który zatrzyma kod inaczej zapętli się w nieskończoność
#     x -= 1                  # znaczy to samo co linijka wyżej - odejmuje 1 od zmiennej

# przykład 2

# age = int(input("Ile masz lat? "))

# while age < 18:                                             # trzeba odpowiednio dobrać warunek aby nie zapętlił się nie w tę stronę co chcemy
#     print("Jesteś za młody, spróbuj jeszcze raz.")
#     age = int(input("Ile masz lat? "))                      # dzięki umieszczeniu w pętli powtarzamy pytanie i możemy zaktualizować zmienną 'age'
# print("Welcome to the jungle!")                             # koniec wcięcia, po skończeniu pętli wyświetla się dalsza część programu

# przykład 3

# zgadnij liczbę wylosowaną przez program 2 pkt za odgadnięcie 1 jeśli nie, trzeba zdobyć 5 pkt

import random

number = random.randrange(1,10)
points = 0
tried = 0

while points < 10:
    guess_number = int(input("Zgadnij liczbę od 1 do 10 "))
    if  guess_number - number == 0:
        points += 3
        tried += 1
        number = random.randrange(1,10)
        print(f"Zgadłeś, dostajesz 3 punkty, łącznie masz {points} punktów. To twoje {tried} podejście.")
    elif abs(guess_number - number) == 1:
        points += 2
        tried += 1
        number = random.randrange(1,10)
        print(f"Byłeś blisko, dostajesz 2 punkty, łącznie masz {points} punktów. To twoje {tried} podejście.")
    else:
        points += 1
        tried += 1
        print(f"Nie zgadłeś, dostajesz 1 punkt, łącznie masz {points} punktów. To twoje {tried} podejście.")