sample_list = [1,5,7,12,53,32,84,10]
cars = ["audi","fiat","citroen","toyota"]

for i in range(len(sample_list)):
    print(sample_list[i], end=' ')
print()

for i in sample_list:                   # teraz elementem od razu będą elementy listy - pętla przeleci po wszystkich elementach listy, robi dokładnie to samo co pętla wyżej
    print(i, end=' ')
print()

for car in cars:                                                # 'car' zastępuje po prost zmienną 'i'
    print(car, end=' ')
print()

for name in ["Marysia", "Kasia", "Kamil", "Natalia"]:           # możemy bezpośredio wpisać listę do komendy
    if len(name) > 5:
        print(f"{name} to długie imię.")
    if name[-1] == "a":
        print(f"{name} to żeńskie imię.")
print()

