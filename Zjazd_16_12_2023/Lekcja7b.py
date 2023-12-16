with open("F:\WSB\Lekcja1\Zjazd_16_12_2023\dane.csv", "r", encoding="UTF8") as file:
    first_line = file.readline()
    lines = file.readlines()

data = [line.strip().split(",") for line in lines]

cities = {}

for row in data:
    city = row[4]
    height = int(row[2])
    if city in cities:
        cities[city]["total"] += height
        cities[city]["number"] += 1
    else:
        cities[city] = {"total": height, "number": 1}

print(cities)

for city, data in cities.items():
    avg = data["total"]/data["number"]
    print(f"W {city} średni wzrost wynosi {round(avg, 2)}cm")