# funkcja, zarobki, wiek, stan zdrowia
# zwraca informacje o max kredycie, jaki można dostać

def max_kredyt(zarobki,wiek,stan_zdrowia):
    if stan_zdrowia == "dobry" and wiek >= 18 and zarobki >= 1500:
        return (zarobki-1500)*12*((65-wiek)*1)
    elif stan_zdrowia == "średni" and wiek >= 18 and zarobki >= 1500:
        return (zarobki-1500)*12*((65-wiek)*0.5)
    else:
        return 0

kwota = max_kredyt(4500,26,"średni")
if kwota != 0:
    print(f"Maksymalna kwota kredytu wynosi {kwota} zł." )
else:
    print("Niestety nie możesz otrzymać kredytu.")