with open("F:\WSB\Lekcja1\Zjazd_16_12_2023\dane.csv", "r", encoding="UTF8") as file:
    first_line = file.readline()
    lines = file.readlines()

# print(first_line)
# print(lines)

data = [line.strip().split(",") for line in lines]                     # .strip() pozbywa się /n - znaku nowej linii, .split(",") rozdziela wartości rozdzielone znakiem 

# print(data[1:])
# average_height = sum(int(line[2]) for line in data) / len(data)
# print(average_height)

i = 0
total_height = 0
a = 0
total_height_poz = 0
for row in data:
    if row[4] == "Warszawa":
        total_height += int(row[2])
        i += 1
    elif row[4] == "Poznań":
        total_height_poz += int(row[2])
        a += 1

print(f"Średni wzrost w Warszawie to {total_height/i}cm")
print(f"Średni wzrost w Poznaniu to {total_height_poz/a}cm")

# def avg_height_list(data, city: str):
#     temp_list = []
#     for i in data:
#         if i[4] == city:
#             height = i[2]
#             temp_list.append(height)
#     return temp_list

# def avg_height(temp_list):
#     i = 0
#     for height in temp_list:
#         i += int(height)
#     return i/len(temp_list)

