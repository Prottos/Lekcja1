# obsługa wyjątków
# komendami "try:" i "except:" możemy ustawić priorytet zadań, tak aby program się nie wysypał jeśli coś pójdzie nie tak

# x = int(input("Podaj 1 liczbę: "))
# y = int(input("Podaj 2 liczbę: "))

# try:
#     result = x/y
# except:
#     result = x

# print(f"Wynmik to: {result}")


# while True:
#     try:
#         x = int(input("Podaj liczbę: "))
#         break
#     except:
#         print("Źle, spróbuj jeszcze raz")

# print("Dalsza część kodu.")

# def can_be_int(data):
#     try:
#         data = int(data)
#         return True
#     except ValueError:
#         return False

# x= input("Podaj liczbę: ")
# if can_be_int(x):
#     print("Liczymy dalej")
# else:
#     print("PodałXś błędą liczbę")

def convert(data):
    try:
        data = int(data)
        print("Skonwertowano do int")
        return data
    except ValueError:
        try:
            data = float(data)
            print("Skonwertowano do float")
            return data
        except ValueError:
            print("Zostaje string")
            return data

x = input("Podaj dane: ")
print("Dalsza część kodu")