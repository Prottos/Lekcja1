print(100 * 1.1)
print(10 * 1.1 * 10)

def mnozenie(a,b):
    return round(a*b,2)

my_list = [23.4, 100, 45, 2137, 54.5694]

print(mnozenie(100,my_list[-1]))

# funkcja, która wykonuje dzielenie - uwzględnia dzielenie przez 0

def dzielenie(c,d):
    if d == 0:
        return "Error, can't div by zero."
    return round(c/d,2)                         # nie trzeba dawać else, ale można

print(dzielenie(1,1))

def testowa(a,b,c):
    d = a + b
    e = b + c
    f = a + c
    return d,e,f                                # zwraca krotkę - listę niemodyfikowalnych elementów

print(testowa(1,2,3))