# data_list = []

# data_list.append(6)             # dodaje na koniec listy nowy element
# data_list.append("kot")
# print(data_list)

# program który weźmie listę 'sample_list' i zapisze liczby parzyste i nieparzyste osobno w nowych listach

sample_list = [5,10.5,20,30,32,45,12,54,56,87]
parzyste = []
nieparzyste = []
x = 0

while x < len(sample_list):
    if sample_list[x] % 2 == 0:
        parzyste.append(sample_list[x])
    else:
        nieparzyste.append(sample_list[x])
    x += 1

print(parzyste)
print(nieparzyste)