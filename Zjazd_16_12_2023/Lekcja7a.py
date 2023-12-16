with open("F:\WSB\Lekcja1\Zjazd_16_12_2023\dane.csv", "r", encoding="UTF8") as file:
    first_line = file.readline()
    lines = file.readlines()

print(first_line)
print(lines)