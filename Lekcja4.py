user_list = {"majki": "1234", "Kamil": "2345", "Rafcio": "3456", "Kamil001": "4567", "Betty": "5678"}
set1 = set(".,/;!@#$%\'\"\\")
set2 = set(str("0123456789"))

import random


def define_password(username):
    password = input("Nadaj hasło: ")
    password2 = input("Potwierdź hasło: ")
    if password == password2 and is_pass_correct(password):
        user_list[username] = password
        add_user(username, password)
        return password
    else:
        print("Hasła nie są identyczne, lub nie spełniają wymagań, spróbuj ponownie.")


def add_user(username, password):
    user_list[username] = password
    print("Użytkownik został dodany.")


def check_user(username):
    while username in user_list:
        username = username + str(random.randrange(0,9))
    a = input(f"Nazwa użytkownika zajęta, czy chcesz wybrać {username}? T/N")
    if a.upper() == "T":
        define_password(username)
    else:
        print("Sróbuj ponownie.")

def up_down(password):
    if password.upper() != password and password.lower() != password:
        return True
    else:
        print("Nie znaleziono wielkiej lub małej litery")
        return False

def digit(password):
    if len(set(password) & set2) > 0:
        return True
    else:
        print("Nie znaleziono cyfry")
        return False
    
def sign(password):
    if len(set(password) & set1) > 0:
        return True
    else:
        print("Nie znaleziono znaku specjalnego")
        return False

def is_pass_correct(password):
    if up_down(password) and digit(password) and sign(password):
        return True
    return False
    

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