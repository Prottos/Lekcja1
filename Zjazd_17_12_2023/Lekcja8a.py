import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

class CityAnalizer:
    def __init__ (self, filename = "F:\WSB\Lekcja1\Zjazd_16_12_2023\dane.csv"):
        self.dataframe = pd.read_csv(filename, sep =",", encoding = "UTF8")                 # pandas poradzi sobie z plikiem csv, nadajemy separator, i pamiętamy o encoding UTF8
        self.dataframe.columns = ["id", "age", "height", "weight", "city"]
        self.city_avg = self.dataframe.groupby("city")[["height","age","weight"]].mean()    # działania matematyczne z użyciem grupowania rekordów (tu wyliczanie średniej z grupowaniem wg miast)
        print(self.city_avg)                                                                # można dać w liście wiele różnych danych (jak w przykładzie wyżej)

    def plot (self):
        ax = self.city_avg.plot(kind = "bar", figsize = (10, 6), color = ["cyan","magenta","yellow"])                                 # tworzenie wykresu słupkowego (kind = "bar"), można dodać więcej argumentów, np kolor, rozmiar, dodaję odwołanie do wykresu celem dalszego wprowadzenia opisu
        plt.title("Średni wzrost, wiek i waga w miastach")                                               # nadawanie tytułu wykresu
        # plt.xlabel("Miasto")                                                                # opis kolumn
        plt.xticks(rotation = 0)                                                            # obrót opisu kolumn
        plt.ylabel("Średni wzrost, wiek i waga")                                                         # opis wartości
        # for i, value in enumerate(self.city_avg):
        #     plt.annotate(f"{value:.2f}", (i, value), textcoords="offset points", xytext=(0, 5), ha="center")    # dodawanie opisu maksymalnej wartości do kolumn
        for i in ax.patches:                                                                # inna opcja dodwania opisów już na podstawie istniejącego wykresu
            height = i.get_height()                                                         # pobieramy z wykresu najwyższe wartości kolumn
            plt.annotate(f"{height:.2f}", 
                         (i.get_x() + i.get_width() / 2, height), 
                         textcoords = "offset points", 
                         xytext = (1, -35), 
                         ha = "center",
                         rotation = 90,
                         color = "black")      # teraz możemy dodać i opisać więcej danych w jednym wykresie
        plt.show()                                                                          # wyświetlanie wykresu
    def plot2 (self):
        fig, ax1 = plt.subplots(figsize = (10, 6))

        self.city_avg["height"].plot(kind = "bar", ax = ax1, color = "blue", position = 0, width = 0.5)
        ax1.set_ylabel("Średni wzrost (cm)", color = "blue")
        ax1.tick_params(axis="y", labelcolor = "blue")

        ax2 = ax1.twinx()
        self.city_avg["age"].plot(kind = "bar", ax = ax2, color = "red", position = 0.5, width = 0.5)
        ax2.set_ylabel("Średni wiek (lat)", color = "red")
        ax2.tick_params(axis="y", labelcolor = "red")
        
        plt.title("Średni wzrost i wiek w miastach")
        for i in ax1.patches and ax2.patches:                                                                # inna opcja dodwania opisów już na podstawie istniejącego wykresu
            height = i.get_height()                                                         # pobieramy z wykresu najwyższe wartości kolumn
            plt.annotate(f"{height:.2f}", 
                         (i.get_x() + i.get_width() / 2, height), 
                         textcoords = "offset points", 
                         xytext = (1, -35), 
                         ha = "center",
                         rotation = 90,
                         color = "black")
        plt.show()
    def plotcorr(self):
        corr_matrix = self.dataframe[["height","age","weight"]].corr()
        sns.heatmap(corr_matrix, annot=True)
        plt.show()
        print(corr_matrix)

city = CityAnalizer()

city.plotcorr()