word1 = "abrakadabra"
word2 = "file.txt"



print(word2[:4] + "_" + word1 + word2[4:])          # wyciąganie konkrtnych liter ze słowa

word1 = word1.replace("a","A",1)                    # zamiana liter/części słowa przy pomocy argumentu .replace, zawsze trzeba to robić przez nadpisanie zmiennej 'str'
print(word1)

word3 = "mama.tata.pies"
word3 = word3.split(".")                               # podział słowa za pomocą spacji i zapis jako lista. zamiast spacji można użyć innego separatora
print(word3)

people = input("Wprowadź imiona ludzi, oddziel spacją: ").split()
print(people)