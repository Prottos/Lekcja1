#to jest komentarz - tego nie wykona program

#print("Dzień dobry") #funkcja print() wyświetla elemnt zawarty w (), jeśli chemy wyświetlić tekst dajemy w nawiasie ""
#print('Dzień dobry') #lub ''
a = 5       #zmienna liczbowa
b = 6.5     #ułamki liczb - dajemy . a nie ,           typ danych - integer (int)
c = "kotek" #zmienna tekstowa musi być w "" lub ''     typ danych - string (str)

#print("a")  #aby użyć zmiennej nie dajemy "" lub '', ponieważ odczyta to jako tekst

#print(a)    #jeśli nie ma zmiennej wywali błąd - name '' is not defined
#print(a+c) #nie można dodać liczby do napisu
#print(a*c)  #można mnożyć liczbę i napis, ale tylko liczbę całkowitą
#print(c*c)  #nie można mnożyć napisu z napisem
d = a + b + 4
print(d)
print(a * (c + ' ')) #można do siebie dodać napisy