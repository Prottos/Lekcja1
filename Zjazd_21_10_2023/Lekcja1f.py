gender = input('Wprowadź płeć K/M... ')

if gender == 'K':                               # pamiętać, że jest to case sensitive - zadziała tylko z 'K', a z 'k' już nie
    print("Witam Panią")
    print("Uruchamiam pakiet spa dla Pań")
elif gender == 'M':
    print("Witam Pana")
else:
    print("Nie rozpoznałem - Witam.")