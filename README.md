# Stock_price_analysis
Polish version


# 1.Wstęp
Głównym celem projektu jest zaprogramowanie wskaźnika giełdowego MACD w języku Python przy użyciu dodatkowych bibliotek:
1)	Pandas -> wczytywanie/modyfikowanie danych
2)	Numpy -> operacja na macieżach, pomoc przy wykresach
3)	Matlpotlib.pyplot -> przedstawienie danych na wykresie
Wskaźnik został wyliczony na podstawie 1000 historycznych wartości akcji Intela w przedziale czasowym od 2018-01-02 do 2021-12-20. Dane zostały pobrane ze strony stooq.pl.
# 2.Analiza zadania
 ![image](https://user-images.githubusercontent.com/43847131/225050628-0a59f8bf-9314-4d83-ac58-266cd8baeab8.png)

Wykres.1 : Wartości akcji Intela na przedziale 1000 dni.
Jako wartości akcji danego dnia przyjmuję średnią z minimalnej i maksymalnej wartości danego dnia. Na podstawie tych danych zostały wyliczone wskaźniki MACD i SIGNAL.
 ![image](https://user-images.githubusercontent.com/43847131/225050705-759b90b3-2b7d-418f-a622-40f6f89806fe.png)

Wykres.2 :Wykresy MACD oraz SIGNAL.
Jak możemy zauważyć wykres 2 reaguje na zmiany wartości na wykresie 1, lecz nie jest on jego odwrozowaniem.
# 3.Algorytm
Początek symulacja zaczynamy z kapitałem 1000 jednostek, oraz trwa ona 900 dni.
Algorytm automatycznego operowania akcjami polega na:
1)	Jeżeli MACD przecina SIGNAL od dołu to akcja zostaje zakupiona
2)	Jeżeli MACD przecina SIGNAL od góry to akcja zostaje sprzedana

Akcja jest kupowana ze względu na poniższy wzór:<br>
 ![image](https://user-images.githubusercontent.com/43847131/225050743-b09366c7-0fa2-4d6b-9111-7eb189b0984c.png)
 
Akcja jest sprzedawana w 100%:<br>
 ![image](https://user-images.githubusercontent.com/43847131/225050764-23a6b35d-bc5c-4633-baee-ae53f17881cb.png)

# 4.Wizualizacja kupna/sprzedaży
Zostały przeprowadzone 2 symulacje:
1)	Symulacja nie uwzględniająca prowizję sprzedaży
2)	Symulacja uwzględniająca prowizję sprzedaży






<h2>Symulacja 1.</h2><br>

 ![image](https://user-images.githubusercontent.com/43847131/225050799-35d99d85-959c-4c94-9c43-3a578fbb5569.png)
![image](https://user-images.githubusercontent.com/43847131/225050820-7d604898-e4e2-4632-a07b-da60ad126615.png)

 
Można zauważyć maksymalny zysk o ponad 10% kapitału początkowego, natomiast ostatecznie symulacja zwiększa swój kapitał tylko o 12 jednostek.<br>
<h2>Symulacja 2.</h2><br>

![image](https://user-images.githubusercontent.com/43847131/225050855-26ab2a5b-6ae9-418d-92f9-c7c97415c025.png)
![image](https://user-images.githubusercontent.com/43847131/225050877-7e9180ee-b573-479d-ac70-889ac46c924b.png)

Z drugiej symulacji można zauważyć, że dodanie prowizji od sprzedaży drastycznie zmniejsza nasz początkowy kapitał o ponad 30% co oznacza, że ten algorytm dla ww. danych działa bardzo źle i nie jest on zalecany do używania przy takich warunkach.
# 5.Opis plików
GitHub: https://github.com/mikitomi21/Stock_price_analysis
1)	[Main.ipynb](https://github.com/mikitomi21/Stock_price_analysis/blob/main/Main.ipynb) -> Plik Jupyter do wizualizacji danych, wykresów, oraz do testowania 
2)	[ecofunction.py](https://github.com/mikitomi21/Stock_price_analysis/blob/main/ecofunction.py) -> Plik zawierający funckje do obliczeń: EMA, SIGNAL, MACD
3)	[visualization.py](https://github.com/mikitomi21/Stock_price_analysis/blob/main/visualization.py) -> Plik automatycznej wirtualizacji algorytmu
4)	[chart.py](https://github.com/mikitomi21/Stock_price_analysis/blob/main/chart.py) -> Plik tworzący wykres symulacji
5)	[trader.py](https://github.com/mikitomi21/Stock_price_analysis/blob/main/trader.py) -> Plik zawierający klasy: Trader, Share, Tax
6)	[intc_us_d.csv](https://github.com/mikitomi21/Stock_price_analysis/blob/main/intc_us_d.csv) -> Historyczne dane wartości akcji Intela




# 6.Zakończenie
Wskaźnik MACD jest dobrą metodą do wizualizacji zachodzących zmian i dawania przewidań kupna/sprzedaży. Nie działa on niestety poprawnie w pełni, gdyż jest on w stanie wyliczyć średnie zmiany z ostatnich dni, natomiast nie potrafi on przewidzeń nadchodzących zmian w przyszłych dniach. 
Wskaźnik ten nadaje się dobrze na dłuższy okres czasu dla wartości, które nie zmieniają się drastycznie. W przeciwnym przypadku nie powinno się opierać w pełni na nim.
