# słowniki (dictionary)

# produkty = ["mleko","ser","olej","mleko"]
# ceny = [4, 30, 10, 24]

# lista_zakupow = [
#     ["mleko",4],
#     ["ser",28],
#     ["olej",10]
# ]



# słowniki tworzymy za pomocą {} i wpisujemy pary rozdzielone : pierwsza część to klucz, a druga to wartość
# jeśli dodaję potem coś do listy i to już tam istnieje, to zostanie to nadpisane, generalnie klucza nie powinno się powtarzać, klucz nie musi być stringiem
dict1 = {"mleko": 4, "ser": 20, "olej": 10}

print(type(dict1))
print(dict1)
# aby wywołać konkretny klucz ze słownika musimy wpisać jego nazwę
print(dict1["mleko"])

# dodawanie/nadpisywanie elementów do słownika
dict1["masło"] = 14
dict1["mleko"] = 1
print(dict1)

# możemy działać zgodznie z zasadami pythona, dodawać, odejmować itd
print(dict1["masło"] + dict1["mleko"])

# można zmieniać wartość za pomocą działań matematycznych
dict1["mleko"] += 1
dict1["masło"] = int(dict1["masło"] * 1.5)
print(dict1)

# jesli nie ma elementu to wywali błąd
# print(dict1["cola"])

while True:
    nazwa = input("Jaki produkt chcesz sprawdzić? ")
    if nazwa in dict1.keys():
        print(f"Cena produktu {nazwa} wynosi {dict1[nazwa]} zł.")
    else:
        q = input(f"Nie znaleziono produktu w bazie, czy chcesz go dodać? T/N")
        if q.upper() == "T":
            price = float(input("Wprowadź cenę produktu: "))
            dict1[nazwa] = price
        else:
            break

print(dict1)