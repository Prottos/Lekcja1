

class Animal:
    is_alive = True                       # atrybut klasy jest czymś, co dotyczy obiektu, jest to zazwyczaj czymś stałym, występującym przy wszystkich obiekatch tej klasy
#     gender = "Male"                       # czegoś takiego nie dajemy
    amount_of_heads = 1                   # zmienna klasowa charakteryzuje się tym, że nie trzeba tworzyć obiektu
    
    def __init__(self, species: str, name: str):            # atrybut instancji/obiektu - to najleży do konkretnego obiektu, wartości są zmienne
        self.species = species
        self.name = name

    def public(self):
        ...

    def _protected(self):
        ...

    def __private(self):
        ...
    
# metoda prywatna - jeżeli tworzymy sobie obiekt

andrew = Animal("crocodile", "Andrzej")
miau = Animal("cat", "Cola")

print(andrew.amount_of_heads)           # przykład użycia zmiennej klasowej
print(miau.amount_of_heads)