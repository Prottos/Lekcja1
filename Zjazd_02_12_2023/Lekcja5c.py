# 1. odczytać plik
# 2. wyczyścić dane
# 3. liczba słów
# 4. liczba różnych słów
# 5. zapisać ilość powtórzeń każdego słowa
# 6. zapisać to wszystko w funkcji

with open("F:\\WSB\\Lekcja1\\Zjazd_02_12_2023\\U2.txt" , "r") as U2:
    content = U2.read()
print("Krok zakończony.")

# 2
def clear(content):
    content = content.lower()
    for i in content:
        content_clear = content.replace(",","").replace(".","").replace("'s","").replace("(","").replace(")","")
    return content_clear
# 3
def split(content_clear):
    clear(content)
    content_split = content_clear.split()
    return content_split


# 4
def unique(content_split):
    unique = set(content_split)
    return unique

# 5
def amount(content_split):
    amount = {}
    for i in content_split:
        if i not in amount:
            amount[i] = 1
        elif i in amount:
            amount[i] += 1
    return amount

print(f"Liczba słów: {len(split(content))}")
print(f"W tekście jest {len(unique(split(clear(content))))} unikalnych słów")
print(amount(split(clear(content))))