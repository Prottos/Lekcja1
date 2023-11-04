# czytanie pliku .csv

# with open("rozliczenie.csv","r") as tabela:
# #    content = tabela.read(5)                               # odczytanie 5 pierwszych znaków
# #    content = tabela.read(5)                               # odczyta kolejnych 5 znaków (zapamiętuje gdzie skończyła poprzednia komenda)
# #    content = tabela.readline()                            # odczytuje linię
#     content = tabela.readlines()                            # odczytuje wszystkie linie, ale osobno jedna po drugiej, na końcu wstawia \n jako oznaczenie kolejnej linii

# print(content[3])                                         # odczyta teraz konkretną - 3 linię

with open("rozliczenie.csv","r") as tabela:
    content = tabela.readlines()
    for i in range(len(content)):
        content[i] = content[i].removesuffix("\n")
        content[i] = content[i].split(",")

# print(content)
# print(content[3])
# print(content[3][2])
# print(content[0][2][7:10])                                  # możemy wyciągać konkretne: 1. linie, 2. konkretne pole, 3. kawałek string'a

# średnia wypłata

lista_wyplat = []
salary = 0
for i in range(1,len(content)):                             # startujemy od drugiej linii, dzięku czemu nie ma problemu z tytułem kolumny
    salary += int(content[i][1])
    lista_wyplat.append(int(content[i][1]))

print(lista_wyplat)
print(f"Średnia wypłata wynosi {round(salary/(len(content)-1),2)} zł.")
print(f"Najwyższa wypłata wynosi: {max(lista_wyplat)} zł.")
print(f"Najniższa wypłata wynosi: {min(lista_wyplat)} zł.")

from statistics import mean
    
print(f"Średnia wypłata wynosi {round(mean(lista_wyplat), 2)} zł.")

# ile kobiet na macierzyńskim

parential = 0
for i in range(1, len(content)):
    if content[i][3] == "k" and content[i][4] == "t":
        parential += 1

print(f"Na urlopie macierzyńskim jest {parential} kobiet.")