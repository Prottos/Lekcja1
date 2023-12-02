# obsługa wyjątków
# komendami "try:" i "except:" możemy ustawić priorytet zadań, tak aby program się nie wysypał jeśli coś pójdzie nie tak

# x = int(input("Podaj 1 liczbę: "))
# y = int(input("Podaj 2 liczbę: "))

# try:
#     result = x/y
# except:
#     result = x

# print(f"Wynmik to: {result}")


while True:
    try:
        x = int(input("Podaj liczbę: "))
        break
    except:
        print("Źle, spróbuj jeszcze raz")

print("Dalsza część kodu.")