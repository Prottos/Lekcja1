# czytanie pliku .txt

with open("Rolling_stones.txt", "r") as stones:                     # komenda otwiera zadany plik w zadanym trybie
    content = stones.read()                                         # komenda zapisuje treść pliku w zadanym kontenerze
    content = content.lower()
print("Koniec programu, plik zamknięty.")
print(content)                                                      # wyświetla treść z zadanego kontenera

# metoda 1

# liczba_wyrazów = len(content.split())                               # rozdziela tekst z kontenera na listę pojedynczych słów i oblicza długość listy
# print(liczba_wyrazów)

# rozpisane

for i in content:
    content = content.replace(",","")
    content = content.replace(".","")

content = content.split()
print(content)
print(f"Liczba słów: {len(content)}")

content = set(content)
print(f"W tekście jest {len(content)} unikalnych słów")