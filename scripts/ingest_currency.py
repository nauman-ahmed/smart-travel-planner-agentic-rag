import requests
import pandas as pd

url = "https://api.frankfurter.app/latest?from=EUR"

data = requests.get(url).json()

rates = data["rates"]

currency_data = []

for currency, value in rates.items():
    currency_data.append({
        "currency": currency,
        "rate": value
    })

df = pd.DataFrame(currency_data)

df.to_csv("data/processed/currency.csv", index=False)

print(df.head())