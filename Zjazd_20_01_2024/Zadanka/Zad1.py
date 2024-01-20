# zad 1: wyprintuj sumę największej i najmniejszej liczby w liście:
a = [2, 52, 5, 7, 12, 67, 22, 31]

print(int(max(a)) + int(min(a)))

# zad 2: wyprintuj ile razy w tekście poniżej występuje litera 'e'
b = "pip! dwudziestu uzurpatorow dusi padalcem dwa pudle"
count = 0
for e in b:
    if e.lower() == "e":
        count +=1
print(count)
# zad 3: wyprintuj która litera występuje najczęściej
c = {}
b = b.replace(" ","")
for letter in b:
    if letter in c.keys():
        c[letter] += 1
    else:
        c[letter] = 1
sorted_c = sorted(c.items(), key=lambda item: item[1], reverse=True)
print(sorted_c[0])
# zad 4: zamień pary elementów w liście 'a' miejscami, czyli powinno wyjść: [52, 2, 7, 5, 67, 12, 31, 22]

x = []
for i in a:
    x.append(i)
print(x)

# zad 5: zasymuluj dużego lotka - wylosuj 6 NIEPOWTARZAJĄCYCH SIĘ liczb od 1 do 49
import random

lotto = []
while len(lotto) < 6:
    number = random.randrange(1,49)
    if number not in lotto:
        lotto.append(number)


print(lotto)

# zad 6: wyprintuj 4 najczęściej występujące litery w zmiennej 'b' jako 4-literowe słowo

print(f"{sorted_c[0][0]+sorted_c[1][0]+sorted_c[2][0]+sorted_c[3][0]}")
