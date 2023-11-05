from Lekcja4 import define_password
from Lekcja4 import check_user

user_list = {"majki": "1234", "Kamil": "2345", "Rafcio": "3456", "Kamil001": "4567", "Betty": "5678"}

while True:
    q = input("Czy chcesz dodać nowego użytkownika? T/N ")
    if q.upper() == "T":
        username = input("Wprowadź nazwę użytkownika: ")
        if username not in user_list:
            define_password(username)
        else:
            check_user(username)
    else:
        break
print(user_list)