from matplotlib import pyplot as plt

class CityAnalizer:
    def __init__(self, filename = "F:\WSB\Lekcja1\Zjazd_16_12_2023\dane.csv"):
        self.cities = {}
        self.load_data(filename)

    def load_data(self, filename = "F:\WSB\Lekcja1\Zjazd_16_12_2023\dane.csv"):
        with open(filename, "r", encoding="UTF8") as file:
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
        avg = {}
        for city, data in self.cities.items():
            avg_height = data["total_height"]/data["number"]
            avg_age = data["total_age"]/data["number"]
            avg_weight = data["total_weight"]/data["number"]
            avg[city] = [round(avg_height, 0), round(avg_height, 0), round(avg_age, 0)]
        return avg
    
    def plot(self, typ=""):
        show_avg = self.show_avg()
        cities = []
        height = []
        age = []
        weight = []

        for city, values in show_avg():
            cities.append(city)
            height.append(values[0])
            age.append(values[1])
            weight.append(values[2])
        
        plt.figure(figsize=(6,10))
        if typ == "wzrost":
            plt.bar(cities, height)
        elif typ == "wiek":
            plt.bar(cities, age)
        elif typ == "waga":
            plt.bar(cities, weight)
        else:
            print("Zły typ danych")
        plt.show()


city = CityAnalizer()
city.plot("wzrost")