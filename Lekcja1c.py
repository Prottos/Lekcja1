wyplata = int(input("Ile zarabiasz? "))

# print(f"Zarabiasz {wyplata}zł miesięcznie.")

# jeżeli zarabiasz więcej niż 15k, płacisz 20% podatku, jeśli mniej to 10%

# if wyplata > 15000:                     # warunek logiczny, pamiętać o dwukropku na koniec
#     print("Zarabiasz dużo.")            # robi się wcięcie pod if, tak gdzie jest wcięcie, tam będzie sprawdzało warunki od 'if', musi być przynajmniej jedno działanie po 'if'
# else:                                   # funkcja dodająca, co ma się działać jeżeli warunek nie został spełniony, również dwukropek na końcu i wcięcie w linijkach poniżej
#     print("Jesteś biedakiem, lol.")     
# print("Dalsza część programu.")         # koniec komendy 'if', kontynuacja programu
# print("Koniec programu.")

print(f"Zarabiasz {wyplata}zł miesięcznie.")
if wyplata > 15000:
    print(f"Zarabiasz {wyplata}zł brutto, podatek wynosi {wyplata * 0.2}, a wynagrodzenie netto {wyplata * 0.8}")
else:
    print(f"Zarabiasz {wyplata}zł brutto, podatek wynosi {wyplata * 0.1}, a wynagrodzenie netto {wyplata * 0.9}")