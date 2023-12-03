# class (klasa) to zbiór informacji o obiekcie, i działania jakie możemy podjąć na obiekcie
# self - sprawia że wszystkie funkcje w danej klasie uwspólniają parametry

class Car:                                              # tworzenie obiektu
    def __init__(self, barwa, stan, wiek):              # tworzenie parametrów obiektu
        self.color = barwa
        self.fuel = 10
        self.condition = stan
        self.eco_mode = False
        self.fuel_consumption = 14
        self.year = 2023 - wiek
    
    def set_mode(self, mode):                           # nadpisywanie parametrów za pomocą komendy
        if mode == "eco":
            self.eco_mode = True
            self.fuel_consumption = 10
        elif mode == "normal":
            self.eco_mode = False
            self.fuel_consumption = 14
        else:
            print("Brak zmian.")

    def fuel_range(self):                               # operacje na parametrach obiektów
        fuel_range = self.fuel / self.fuel_consumption * 100
        return fuel_range

my_car = Car("silver", 5, 14)
neighbor_car = Car("white", 3, 24)

# print(my_car.color)
# my_car.color = "black"
# print(my_car.color)
# print(neighbor_car.color)
print(my_car.fuel_range())
my_car.set_mode("eco")
print(my_car.fuel_range())