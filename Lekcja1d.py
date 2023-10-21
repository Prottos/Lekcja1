# hasło do systemu 1234
# użytkownik podaje hasło
# program wpuszcza użytkownika bądź nie

system_password = "1234"
user_password = input("Podaj hasło do systemu: ")

if user_password == system_password:                # aby sprawdzić czy coś jest równe dajemy dwa razy znak równa się '==', aby sprawdzić czy jest różne '!='
    print("Witaj w systemie.")
else:
    print("Błędne hasło, odmowa dostępu.")