with open("F:\WSB\Lekcja1\Zjazd_16_12_2023\dane.csv", "r", encoding="UTF8") as file:
    first_line = file.readline()
    lines = file.readlines()

data = [line.strip().split(",") for line in lines]

# cities_height = {}
# cities_age = {}
# cities_weight = {}

# for row in data:
#     city = row[4]
#     height = int(row[2])
#     if city in cities_height:
#         cities_height[city]["total"] += height
#         cities_height[city]["number"] += 1
#     else:
#         cities_height[city] = {"total": height, "number": 1}

# for row in data:
#     city = row[4]
#     age = int(row[1])
#     if city in cities_age:
#         cities_age[city]["total"] += age
#         cities_age[city]["number"] += 1
#     else:
#         cities_age[city] = {"total": age, "number": 1}

# for row in data:
#     city = row[4]
#     weight = int(row[3])
#     if city in cities_weight:
#         cities_weight[city]["total"] += weight
#         cities_weight[city]["number"] += 1
#     else:
#         cities_weight[city] = {"total": weight, "number": 1}

# for city, data in cities_height.items():
#     avg = data["total"]/data["number"]
#     print(f"W {city} średni wzrost wynosi {round(avg, 2)}cm")
# for city, data in cities_age.items():
#     avg = data["total"]/data["number"]
#     print(f"W {city} średni wiek wynosi {round(avg, 2)} lat")
# for city, data in cities_weight.items():
#     avg = data["total"]/data["number"]
#     print(f"W {city} średnia waga wynosi {round(avg, 2)}kg")

cities_height = {}
cities_age = {}
cities_weight = {}

for row in data:
    city = row[4]
    height = int(row[2])
    age = int(row[1])
    weight = int(row[3])
    if city in cities_height:
        cities_height[city]["total"] += height
        cities_height[city]["number"] += 1
    else:
        cities_height[city] = {"total": height, "number": 1}
    if city in cities_age:
        cities_age[city]["total"] += age
        cities_age[city]["number"] += 1
    else:
        cities_age[city] = {"total": age, "number": 1}
    if city in cities_weight:
        cities_weight[city]["total"] += weight
        cities_weight[city]["number"] += 1
    else:
        cities_weight[city] = {"total": weight, "number": 1}

for city, data in cities_height.items():
    avg_height = data["total"]/data["number"]
    print(f"W {city} średni wzrost wynosi {round(avg_height, 2)}cm")            # zamiast round(avg_height, 2) możemy użyć avg_height:.2f
for city, data in cities_age.items():
    avg_age = data["total"]/data["number"]
    print(f"W {city} średni wiek wynosi {round(avg_age, 2)} lat")
for city, data in cities_weight.items():
    avg_weight = data["total"]/data["number"]
    print(f"W {city} średnia waga wynosi {round(avg_weight, 2)}kg")