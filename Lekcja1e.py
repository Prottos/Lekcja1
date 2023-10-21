wyplata = int(input("Ile zarabiasz? "))

if wyplata > 10000:                         # pierwszy warunek do sprawdzenia, jeśli nie jest spełniony, sprawdza kolejny - 'elif'
    print("2-gi próg podatkowy")
elif wyplata > 5000:                        # 'elif' dodaje dodatkowy warunek do sprawdzenia, jeśli zostanie spełniony wykonuje działanie, jeśli nie sprawdza dalej
    print("1-szy próg podatkowy")
elif wyplata > 3000:                        # generalnie nie ma limitu warunków 'elif', ale lepiej za dużo nie dawać, żeby kod był bardziej zoptymalizowany
    print("Mały podatek")
else:                                       # jeśli żaden warunek nie został spełniony wykonuje to działanie
    print("Wolny od podatku")

print("Dalsza cz. programu.")