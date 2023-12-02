# zbiory (set)
# zbiory tworzymy za pomocą {} w zbiorzy elementy nie mogą się powtarzać (wywala duplikaty), a kolejność nie ma znaczenia
zbior = {1,3,5,7,10}
zbior2 = {7,1,12,45,6}

print(zbior)
print(zbior2)

# częste zadanie rekrutacyjne, jak usunąć duplikaty z listy
lista1 = [2,3,6,6,6,2,1,65,3,5,14,16,35,7]
# zamieniamy listę za pomocą komendy set() na zbiór, a następnie ponownie na listę za pomocą list()
lista1 = list(set(lista1))

print(lista1)

# ziobry można dodawać do siebie, wyznaczać część wspólną itd.

print(f"Suma dwóch zbiorów: {zbior | zbior2}")
print(f"Część wspólna dwóch zbiorów: {zbior & zbior2}")
print(f"Różnica zbiorów: {zbior2 - zbior}")
print(f"Różnica zbiorów: {zbior - zbior2}")

spec_sign = [".",",","!","?"]
password = input("Podaj hasło: ")

spec_sign = set(spec_sign)
password = set(password)

# wersja 1

differ = spec_sign - password

if spec_sign != differ:
    print("Hasło zawiera znaki specjalne")
else:
    print("Hasło nie zawiera znaków specjalnych")