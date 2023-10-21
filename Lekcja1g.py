# program pyta o płeć i wiek
# pełnoletmo wchodzą na imprezę
# kobiety wchodzą za darmo
# mężczyźni płacą 10zł

age = int(input("Ile masz lat? "))
gender = input("Podaj swoją płeć K/M ")

# Sposób 1

# if age >= 18 and gender == 'K':                         # można łączyć warunki za pomocą operatora 'and'
#     print("Możesz wejść na imprezę za darmo.")
# elif age >= 18 and gender == 'M':
#     print("Możesz wejść na imprezę za 10zł.")
# else:
#     print("Nie możesz wejść na imprezę.")

# Sposób 2

# if age >= 18:
#     pass
# else:
#     print("Nie możesz wejść na imprezę.")

# if gender == 'K':
#     print("Możesz wejść na imprezę za darmo.")
# elif gender == 'M':
#     print("Możesz wejść na imprezę za 10zł.")
# else:
#     print("Podaj poprawną płeć.")

# Jest jeszcze więcej metod, np pytanie o płeć po sprawdzeniu wieku

print ("Wchodzisz za darmo" if age >= 18 and gender == 'K' else "Wchodzisz za 10zł" if age >= 18 and gender == 'M' else "Nie wchodzisz")