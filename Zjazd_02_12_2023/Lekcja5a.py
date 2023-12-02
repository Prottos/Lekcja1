# 1. Rozwinąć program tworzony na zajęciach. 
# Chcemy, aby system podpowiadał ładną, podobną nazwę użytkownika, jeśli dana nazwa jest zajęta.
# Chcemy, aby haśło nie mogło zawierać ciągu znaków '12345'   bądź, aby nie mogło zawierać całego zestawu takich słabych wzorów.



# 2. Dany jest słownik, wskazujący ile mamy produktów:
available = {'mleko' : 3, 'jajko' : 25, 'maka' : 7, 'cukier' : 4, 'maliny' : 3}

# Dany jest również słownik wskazując ile jakich produktów potrzebujemy, aby zrobić ciasto:
recipe = {'mleko' : 1, 'jajko' : 8, 'maka' : 0.5, 'cukier' : 0.3}

# Zadanie, napisać program liczący, ile ciast możemy upiec z posiadanych produktów.

# critical = ""
# how_many = list()
# for i in available:
#     if i not in recipe:
#         print(f"Brak {i} w przepisie.")
#         pass
#     else:
#         x = available[i] // recipe [i]
#         how_many.append(x)
#         critical = i
# critical = 
# print(f"Zrobisz maksymalnie {min(how_many)} ciast, najszybciej zabraknie {i}.")



minimum = 1000000
critical = ""
results = {}
for key in recipe.keys():
    # print (f"Bierzemy {key}")
    # print (f"zrobimy {available[key] // recipe[key]} ciast")
    if available[key] / recipe[key] < minimum:
        minimum = available[key] / recipe[key]
        critical = key
    results[key] = available[key] / recipe[key]
print(f"Zrobimy {minimum} ciast. Najszybciej zabraknie {critical}.")
print("\n", results, "\n")

sorted_available = sorted(results.items(), key = lambda x: x[1])
print(sorted_available)



# x = lambda a : a + 10 # w jednej linijce transformje argument "a" zgodnie z działaniem