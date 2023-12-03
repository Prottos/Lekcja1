def myfunc(a, b, c):
    return a + b + c

def argfunction(*argv):                                                     # dowolna ilość argumentów w funkcji
    for arg in argv:
        print(arg)
    print(f"Koniec funkcji, przetworzono {len(argv)}")

# argfunction(1, 2, 3, "mama", 16, "ok", "103")

def message_to_employee(*ids, profit):                                      # dowolna ilość argumentów w funkcji, argument zdefiniowany (tu ostatni) dodawany za pomocą nazwy "profit="
    for id in ids:
        print("Szykuję wiadomość")
        print("Tworzę plik id.txt")
        print(f"Witaj {id}. Zysk w firmie za rok 2023 wynosi {profit}")

# message_to_employee(65564, 74944, 46541, 49845, 11561, profit=2300000)      # przykład zastosowania

def create_member(**kwargs):                                                # kwargsy to to kiedy definiujesz konkretne nazwy argumentów np name=, wiek=, itd.
    for key, value in kwargs.items():
        print(key, value)

# create_member(name = "Kamil", surname = "Kowalski")

def draw_lines(start: list, *points: list):
    begin = start
    for point in points:
        print(f"Narysuj kreskę od {start} do {point}")
        begin = point

def send_email(**member):
    print(f"Witaj {member['name']}, masz {member['wiek']} lat")
    if "urlop" in member.keys():
        print(f"Masz obecnie {member['urlop']} dni urlopu")
        if member["urlop"] > 10:
            print("Wysyłam na przymusowy urlop")

send_email(name="Kamil", wiek=26, urlop=12)

def total_function(pierwszy, drugi, *args, **kwargs,):   # można łączyć 1. zwykłe argumenty, 2. argumenty z nazwą, 3. argsy i 4. kwargsy; w jednej funkcji, ale pamiętamy o kolejności
    pass
total_function(3, 4, 5, 6, imie="kamil", wiek = 33)
