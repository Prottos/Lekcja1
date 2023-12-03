# listy - zbiory wieloelementowe

my_list = [1,2,3.5,4,"kotek","piesek"]

print(my_list)
print(my_list[5])           # wyświetlanie konkretnego elementu z listy - WAŻNE - lista zaczyna się od elementu 0

print(my_list[2:4])         # wyświetlanie elementu od - do - WAŻNE - pokazuje elementy bez ostatniego (w tym przypadku wyświetli elementy 2 i 3 bez 4)
my_list[1] = 88             # nadpisanie elementu listy
my_list[2] += 4             # działania matematyczne na elementach listy
print(my_list)

print(len(my_list))         # komenda len() wyświetla długość listy

print(my_list[-2])          # wartość ujemna bierze wartość od końca listy

print(my_list[:4])          # wybór od początku do danego indeksu
print(my_list[2:])          # wybór od któregoś elementu do końca
print(my_list[::2])         # wybór od początku do końca, co 2 element
print(my_list[1:5:2])       # wybór co któregoś elementu, w przypadku ujemnego skoku będzie wybierał od końca

