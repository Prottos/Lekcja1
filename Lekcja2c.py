# pętla 'while' i 'while True'

# age = int(input("Ile masz lat? "))

# while True:                                             # rozpoczęcie pętli, będzie działa do czasu przerwania np. za pomocą polecenia 'break' lub spełnienia warunku
#     if age >= 18:
#         break                                           # zakończenie pętli za pomocą polecenia 'break' - zatrzymuje pętlę i przechodzi do dalszej części programu
#     else:
#         print("Zły wiek, wprowadź jeszcze raz.")
#         age = int(input("Ile masz lat? "))

# print("Witamy!")

# zadanie - program pyta o hasło
# jeśli hasło poprawne - wchodzimy
# jeśli wprowadzona hasło serwisoe, program pyta o wiek i jeśli pełnoletni to wchodzimy

password = "kotek"
servicepassword = "serwis"
userid = "1234"
proba = 0

while True:
    inputpassword = input(print("Wprowadź hasło. "))
    if inputpassword == password:
        print("Hasło poprawne, witamy.")
        break
    elif inputpassword == servicepassword:
        serviceid = input(print("Wprowadź ID serwisanta."))
        if serviceid == userid:
            print("Tryb serwisowy, witamy.")
        break
    else:
        if proba < 2:
            print(f"Dane niepoprawne, spróbuj jeszcze raz. Pozostało {2 - proba} prób.")
            proba += 1
        elif proba == 2:
            print("Ostatnia próba, dostęp zostanie zablokowany!")
        else:
            print("Dostęp zablokowany, skontaktuj się z administratorem systemu.")
            exit()

print("Koniec programu")