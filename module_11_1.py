import requests

url = "https://api.github.com/user"
response = requests.get(url)

if response.status_code == 200:
    print("Данные с API:")
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")
#Библиотека requests упрощает работу с HTTP-запросами (GET, POST и другие).
# Она позволяет быстро интегрироваться с API, скачивать данные и обрабатывать их.

import pandas as pd

data = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
print("Первые строки данных:")
print(data.head())
print("\nСредние значения:")
print(data.mean())
#pandas — мощная библиотека для работы с табличными данными.
# Она предоставляет инструменты для чтения данных из различных форматов (CSV, Excel, SQL), анализа, фильтрации,
# обработки и визуализации. В данном примере мы используем pandas для анализа таблицы, находя средние значения.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="o", label="y = 2x")
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.show()
#matplotlib — популярная библиотека для создания визуализаций.
# Она позволяет строить графики, диаграммы, гистограммы и другие виды визуализаций.
# В данном случае мы построили простой линейный график.