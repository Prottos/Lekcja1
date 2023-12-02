# użytkownik wprowadza osoby, każda ma imię, nazwisko i mail. Program pyta, czy wprowadzić kolejną osobę. Po zakończeniu wprowadzania program wypisuje ile jest kobiet ile osób ma maila w domenie gmail

name = []
surname = []
mail = []

while True:
    nast = input(print("Czy chcesz dodać nową osobę? T/N"))
    if nast.upper() != "T":
        break
    else:
        imie = input(print("Podaj imię: "))
        name.append(imie)
        nazwisko = input(print("Podaj nazwisko: "))
        surname.append(nazwisko)
        email = input(print("Podaj adres mail: "))
        mail.append(email)

gmail = 0
woman = 0

for person in name:
    if person[-1] == 'a':
        woman += 1
for email in mail:
    if "gmail.com" in email[-9:]:
        gmail += 1

print(f" Liczba osób z gmailem: {gmail}")
print(f" Liczba kobiet: {woman}")

# do tego momentu działa spoko

names = ["Kasia","Basia","Kamil","Ola","Michał"]

for person in name:
    if person[0] not in name:
        name.remove(person)
        surname.remove(person)
        mail.remove(person)

print(name)
print(surname)
print(mail)

