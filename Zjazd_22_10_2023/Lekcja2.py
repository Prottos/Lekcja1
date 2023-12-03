# 14 // 4 = 3       # część całkowita z dzielenia
# 14 % 4 = 2        # reszta z dzielenia

# x = 5

# sprawdzamy czy liczba jest parzysta czy nie

# if x % 2 == 0:
#     print("Liczba jest parzysta.")
# else:
#     print("Liczba jest nieparzysta.")

# # druga metoda

# if x % 2 != 0:
#     print("Liczba jest nieparzysta.")
# else:
#     print("Liczba jest parzysta.")

# pomidory kosztują 3zł sztuka. Ale w 3-paku, 3 pomidory razem kosztują 80% ceny
# program pyta ile pomidorów chcemy kupić i zwraca najniższą cenę

price = 3
pack = 3
amount = int(input("Ile pomidorów chcesz kupić? "))

print(f"Zapłacisz razem {round((amount // 3 * 3 * 0.8 + amount % 3) * price, 2)}zł.")
print(f"Najlepiej kupić {amount // 3} paczek i {amount % 3} pojedynczych pomidorów.")

# polecenie round() zaokrągla liczbę - domyślnie do calości, ale możemy to zmienić poprzez dodanie po przecinku liczby miejsca po przecinku np. round(x, 2) - zaokrągli do 2 miejsca po przecinku
