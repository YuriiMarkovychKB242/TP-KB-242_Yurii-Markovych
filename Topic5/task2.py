import requests

def get_exchange_rate(currency_code):
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    data = response.json()
    for item in data:
        if item['cc'] == currency_code:
            return item['rate']
    return None

def convert():
    amount = float(input("Enter amount to convert: "))
    currency = input("Enter currency (USD, EUR, PLN): ").upper()
    
    rate = get_exchange_rate(currency)
    if rate:
        result = amount * rate
        print(f"{amount} {currency} = {result:.2f} UAH")
    else:
        print("Currency not found!")

convert()