10. #Currency Converter
import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching data from API.")
        return None

    data = response.json()

    if to_currency in data['rates']:
        conversion_rate = data['rates'][to_currency]
        conversion_amount = amount * conversion_rate
        return conversion_amount
    else:
        return None

try:
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., INR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount:
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency code or conversion not available.")
except ValueError:
    print("Please enter a valid numeric amount.")
    