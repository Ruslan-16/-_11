import requests

API_KEY = "c923b3dc-cd07-4216-8edc-9d73beb665cc"
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'symbol': 'PEPE',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}
response = requests.get(url, headers=headers, params=parameters)
data = response.json()

if response.status_code == 200:
    price = data['data']['PEPE']['quote']['USD']['price']

    print(f"Цена PEPE: ${price:.6f}")
else:
    print(f"Ошибка: {response.status_code}")
    print(data['status']['error_message'])

#Библиотека requests упрощает работу с HTTP-запросами (GET, POST и другие).
# Она позволяет быстро интегрироваться с API, скачивать данные и обрабатывать их.

import pandas as pd

if response.status_code == 200:
    data = response.json()
    rows = []
    for symbol in data["data"]:
        quote = data["data"][symbol]["quote"]["USD"]
        rows.append({
            "Symbol": symbol,
            "Price (USD)": quote["price"],
            "Market Cap (USD)": quote["market_cap"],
            "Volume 24h (USD)": quote["volume_24h"],
        })
    df = pd.DataFrame(rows)

    print("Первые строки данных:")
    print(df.head())
    print("\nСредние значения:")
    print(df.mean(numeric_only=True))
else:
    print(f"Ошибка: {response.status_code}")
    print(response.json()["status"]["error_message"])
#pandas — мощная библиотека для работы с табличными данными.
# Она предоставляет инструменты для чтения данных из различных форматов (CSV, Excel, SQL), анализа, фильтрации,
# обработки и визуализации. В данном примере мы используем pandas для анализа таблицы, находя средние значения.

import matplotlib.pyplot as plt

if response.status_code == 200:
    data = response.json()

    price = data["data"]["PEPE"]["quote"]["USD"]["price"]
    percent_change_1h = data["data"]["PEPE"]["quote"]["USD"]["percent_change_1h"]
    percent_change_24h = data["data"]["PEPE"]["quote"]["USD"]["percent_change_24h"]
    percent_change_7d = data["data"]["PEPE"]["quote"]["USD"]["percent_change_7d"]

    time_intervals = ["1 Hour", "24 Hours", "7 Days"]
    price_changes = [percent_change_1h, percent_change_24h, percent_change_7d]

    plt.figure(figsize=(8, 5))
    plt.bar(time_intervals, price_changes, color=["blue", "orange", "green"])
    plt.title("Изменение цены Pepe (PEPE) в процентах", fontsize=20)
    plt.xlabel("Временной интервал", fontsize=24)
    plt.ylabel("Изменение цены (%)", fontsize=24)
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.ylim(-20, 20)
    plt.xlim(-1, len(time_intervals))
    plt.show()
else:
    print(f"Ошибка: {response.status_code}")
    print(response.json()["status"]["error_message"])

#matplotlib — популярная библиотека для создания визуализаций.
# Она позволяет строить графики, диаграммы, гистограммы и другие виды визуализаций.
# В данном случае мы построили простой линейный график.