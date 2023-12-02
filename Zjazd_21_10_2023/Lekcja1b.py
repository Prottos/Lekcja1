# print("Hej")
# input()                     # poczekaj na enter
# print("Miłego dnia")

imie = input("Jak masz na imię? ")          # wypisz treść, zapisz zmienną i poczekaj na enter
wiek = input("Ile masz lat? ")              # python wszystko co jest wprowadzane przez input() zapisuje jako string, nawet jeśli jest to liczba
# wiek = int(input("Ile masz lat? "))       # można od razu wymusić zapisanie wprowadzonej liczby jako 'int'

nowy_wiek = int(wiek)                       # tworzymy nową zmienną zamieniając 'str' ze zmiennej na 'int'

print('Cześć',imie,'. Masz',wiek,'lat.')                # wyświetla tekst i zmienną
print('Cześć ' + imie + '. Masz ' + wiek + ' lat.')     # można użyć wporwadzonej liczby, ponieważ zapisana jest jako 'str' a nie 'int'
print(f'Cześć {imie}. Masz {wiek} lat.')                # f wprowadza funkcje, gdzie zmienne możemy zapisywać w tekście za pomocą {}

print(f'Przejdziesz na emeryturę za {65 - int(wiek)} lat.')     # aby dało się użyć liczby zapisanej jako 'str' do obliczenia należy użyć funkcji int() aby zamienić ją ze 'str' do 'int'
print(f'Przejdziesz na emeryturę za {65 - nowy_wiek} lat.')
# print(f'Przejdziesz na emeryturę za {65 - wiek} lat.')