import pandas as pd
from matplotlib import pyplot as plt

class CityAnalizer:
    def __init__ (self, filename = "F:\WSB\Lekcja1\Zjazd_16_12_2023\dane.csv"):
        self.dataframe = pd.read_csv(filename, sep =",", encoding = "UTF8")                 # pandas poradzi sobie z plikiem csv, nadajemy separator, i pamiętamy o encoding UTF8
        self.dataframe.columns = ["id", "age", "height", "weight", "city"]
        self.city_avg = self.dataframe.groupby("city")[["height","age","weight"]].mean()    # działania matematyczne z użyciem grupowania rekordów (tu wyliczanie średniej z grupowaniem wg miast)
        print(self.city_avg)                                                                # można dać w liście wiele różnych danych (jak w przykładzie wyżej)

    def plot (self):
        self.city_avg.plot(kind = "bar", figsize = (10, 6))                                 # tworzenie wykresu słupkowego (kind = "bar"), można dodać więcej argumentów, np kolor, rozmiar
        plt.title("Średni wzrost w miastach")                                               # nadawanie tytułu wykresu
        plt.xlabel("Miasto")                                                                # opis kolumn
        plt.xticks(rotation = 0)                                                            # obrót opisu kolumn
        plt.ylabel("Średni wzrost")                                                         # opis wartości
        plt.show()                                                                          # wyświetlanie wykresu

city = CityAnalizer()
city.plot()