# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór winogrady – wszystkich ludzi mieszkających na winogradach
# stwórzmy zbiór wilda – wszystkich ludzi mieszkających na wildzie
 
# set1 | set2 <- suma
# set1 & set2 <- cześć wspólna
# set1 - set2 <- róznica
# set1 ^ set2 <- różnica symetryczna (wszystko poza częścią wspólną)


NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
winogrady = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
wilda = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# ile osób chorowało w ostatnim roku na bemowie

print(f"Na Winogradach chorowało w ostatnim roku {len(winogrady & chorzy_rok)} osób.")
print(f"Na Winogradach chorowało w ostatnim roku {len(winogrady.intersection(chorzy_rok))} osób.")

# ile osób chorowało w ostatnim miesiacu na wildzie

print(f"Na Wildzie chorowało w ostatnim miesiącu {len(wilda & chorzy_miesiac)} osób.")
print(f"Na Wildzie chorowało w ostatnim miesiącu {len(wilda.intersection(chorzy_miesiac))} osób.")

# sprawdzamy poprawność danych:
# każdy kto chorował w ostatnim miesiącu chorował też w ostatnim roku

print(f"Osoby które chorowały w ostatnim miesiącu ale NIE chorowały w ostatnim roku: {chorzy_miesiac - chorzy_rok}")

# czy nie dublują się mieszkańcy

print(f"Osoby zapisane jako mieszkające zarówno na Wildzie jak i na Winogadach {wilda & winogrady}")
x = input("Skąd usunąć? A - Wilda, B - Winogrady ")
if x == "A":
    winogrady = winogrady - (wilda & winogrady)
elif x == "B":
    wspolne = wilda & winogrady
# wykonuje pętlę i 
    for pesel in wspolne:
        wilda.remove(pesel)
else:
    print("Nie rozpoznano wyboru, usuwam z Winograd.")
    winogrady = winogrady - wilda

print(winogrady)
print(wilda)

# każdy chory powinien być w bazie

wszyscy = chorzy_rok | chorzy_miesiac | wilda | winogrady
print(f"W bazie NFZ nie ma osób: {wszyscy - NFZ}")
NFZ = NFZ | wszyscy

# pesele żeńskie mają ostatnią cyfrę parzystą, męskie nieparzystą, zrób osobne zbiory dla mężczyzn i kobiet

mezczyzni = set()
kobiety = set()
for pesel in NFZ:
    if pesel % 2 == 0:
        kobiety.add(pesel)
    else:
        mezczyzni.add(pesel)

print(kobiety)
print(mezczyzni)