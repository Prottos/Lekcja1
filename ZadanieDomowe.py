# Zadanie domowe:
# dana jest lista użytkowników
# User_list = ['majki', 'Kamil001', 'Rafcio', 'Betty']
# - program pyta o wprowadzenie nowego użytkownika
# - jeśli nazwa użytkownika jest zajęta program prosi o ponowne wprowadzenie nazwy bądź proponuje swoją podobną nazwę
# - po wprowadzeniu uzytkownika, program 2 razy prosi o hasło
# - po dwukrotnie wprowadzonym takim samym haśle, uzytkownik zostaje dodany do listy użytkowników, a jego hasło jest zapisane w drugiej liście


User_list = ["majki","Kamil001","Rafcio","Betty"]
Password_list = ["1234","2345","5678","6789"]
User_password = [User_list,Password_list]

while True:
    nast = input(print("Czy chcesz dodać nową osobę? T/N "))
    if nast != "T":
        break
    else:
        name = input("Podaj imię: ")
        for i in User_list:
            if name in User_list:
                print("Użytkownik już istnieje, wybierz inny nick.")
                break
            else:
                password = input("Nadaj hasło: ")
                password2 = input("Potwierdź hasło: ")
                if password == password2:
                    User_list.append(name)
                    Password_list.append(password)
                    break
                else:
                    print("Błędne hasło, spróbuj jeszcze raz.")
print(User_password)