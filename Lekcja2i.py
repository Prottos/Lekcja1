# program pyta, ile osób dodać do systemu
# program pozwala dodać tyle osób, zapisuje w liście
# program za każdym razem pyta, czy chcesz dodać kolejną osobę

lista = []
amount = int(input("Ile osób chcesz dodać do listy? "))

for i in range(amount):
    name = input("Podaj imię: ")
    lista.append(name)

print(lista)

while True:
    nast = input(print("Czy chcesz dodać kolejną osobę? T/N"))
    if nast != "T":
        break
    else:
        name = input("Podaj imię: ")
        lista.append(name)

print(lista)
