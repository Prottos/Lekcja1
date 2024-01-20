class Animal:
    is_alive = True
    amount_of_heads = 1
    
    def __init__(self, species: str, name: str):
        self.species = species
        self.name = name
        self._calories_left = 4000

    def eat(self):
        self._calories_left += 1000

# dziedziczenie przekazuje do klasy atrybuty z wyższej klasy
class Crocodile(Animal):

    def __init__(self, name):                       # częstu uzywamy super(). w finkcji __init__
        super().__init__("crocodile", name)

    def eat(self):
        self._calories_left += 2000
        super().eat()                               # aktywujemy funkcję z klasy wyżej - Animal (tzw superklasę - stąd nazwa funkcji)

    def dive(self):
        ...

andrew = Crocodile("Andrzej")
andrew.eat()

print(andrew._calories_left)


"""
Public - można wszędzie
_protected - można w Animal i Crocodile
__private - można wyłącznie w Animal
"""