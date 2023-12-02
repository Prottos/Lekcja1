x = int(input("Podaj 1 liczbę: "))
y = int(input("Podaj 2 liczbę: "))

try:
    result = x/y
except ZeroDivisionError:
    result = x
    raise
else:
    print("Udało się")
finally:
    print("Zbieram logi")