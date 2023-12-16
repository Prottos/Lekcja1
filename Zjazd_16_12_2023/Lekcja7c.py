class CityAnalizer:
    def __init__(self, filename = "F:\WSB\Lekcja1\Zjazd_16_12_2023\dane.csv"):
        self.cities = {}
        self.filename = filename
        
        with open(self.filename, "r", encoding="UTF8") as file:
            first_line = file.readline()
            lines = file.readlines()
        data = [line.strip().split(",") for line in lines]

        for row in data:
            city = row[4]
            age = int(row[1])
            height = int(row[2])
            weight = int(row[3])
            if city in self.cities:
                self.cities[city]["total_height"] += height
                self.cities[city]["total_age"] += age
                self.cities[city]["total_weight"] += weight
                self.cities[city]["number"] += 1
            else:
                self.cities[city] = {"total_height": height, "total_age": age, "total_weight": weight, "number": 1}
    
    def show_avg(self, city="", x=2):
        if city:
            if city in self.cities:
                data = self.cities[city]
                avg_height = data["total_height"]/data["number"]
                avg_age = data["total_age"]/data["number"]
                avg_weight = data["total_weight"]/data["number"]
                print(f"W {city:<2.2} średni wzrost wynosi: {avg_height:.{x}f}cm, wiek: {avg_age:.{x}f} lat, waga {avg_weight:.{x}f}kg")
            else:
                print(f"Nie ma takiego miasta jak {city} w bazie danych.")
                
        else:
            for city, data in self.cities.items():
                avg_height = data["total_height"]/data["number"]
                avg_age = data["total_age"]/data["number"]
                avg_weight = data["total_weight"]/data["number"]
                print(f"W {city:<2.2} średni wzrost wynosi: {avg_height:.{x}f}cm, wiek: {avg_age:.{x}f} lat, waga {avg_weight:.{x}f}kg")    # formatowanie graficzne city:<8.8 dociąganie do prawej/lewej i odcinanie znaków powyżej jakiejś wartości

city = CityAnalizer()
city.show_avg("Warszawa")